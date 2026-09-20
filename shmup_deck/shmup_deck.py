#!/usr/bin/env python3
"""Shmup Deck service for the MiSTer.

Serves the deck web app and launches games itself, so nothing else (mrext
Remote, a PC, a hosted site) is needed. The page and the API share one origin,
which avoids the mixed-content and CORS problems of hosting the app elsewhere.

Games are matched by MAME setname, read from inside each .mra, never guessed
from filenames. That is what separates Gunbird from Gunbird 2 and DonPachi from
DoDonPachi.

Flyer art is not shipped. On first start the service downloads each flyer
from the sources pinned in app/art.json and keeps it on the SD card.

    python3 shmup_deck.py [--port 8190]

Python 3.9 standard library only, which is what the MiSTer image ships.
"""

import argparse
import io
import json
import os
import re
import socket
import struct
import subprocess
import sys
import threading
import time
import urllib.parse
import urllib.request
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from xml.sax.saxutils import quoteattr

HERE = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.environ.get("SHMUP_APP_DIR", os.path.join(HERE, "app"))
ART_DIR = os.environ.get("SHMUP_ART_DIR", os.path.join(HERE, "art"))
ARCADE = os.environ.get("SHMUP_ARCADE_DIR", "/media/fat/_Arcade")
# where to look for MRAs; by default every top-level "_" folder on the SD card
# and USB drives, since MRAs work from any of them, not just _Arcade
MRA_ROOTS = os.environ.get("SHMUP_MRA_ROOTS")
DRIVES = ["/media/fat"] + ["/media/usb%d" % i for i in range(6)]
CMD = os.environ.get("SHMUP_CMD", "/dev/MiSTer_cmd")
CACHE = os.environ.get("SHMUP_CACHE", os.path.join(HERE, "mra_index.json"))
SEEN = CACHE[:-5] + "_seen.json"     # size, date and setname of every MRA read
MGL_PATH = os.environ.get("SHMUP_MGL", "/tmp/shmup_deck.mgl")
CORENAME = os.environ.get("SHMUP_CORENAME", "/tmp/CORENAME")
PLAYS = os.environ.get("SHMUP_PLAYS", os.path.join(HERE, "plays.json"))
FAVS = os.environ.get("SHMUP_FAVS", os.path.join(HERE, "favourites.json"))
VERSIONS_FILE = os.environ.get("SHMUP_VERSIONS", os.path.join(HERE, "versions.json"))

VERSION = "1.8.0"
USER_AGENT = "ShmupDeck/%s (+https://github.com/searchsolved/shmup-deck)" % VERSION
PROGRAM = os.path.abspath(__file__)
REPO = os.environ.get("SHMUP_REPO", "searchsolved/shmup-deck")
GITHUB_API = os.environ.get("SHMUP_API", "https://api.github.com")
UPDATE_EVERY = int(os.environ.get("SHMUP_UPDATE_EVERY", 6 * 3600))
# the script in the Scripts menu, which is part of every release too
INSTALLER = os.environ.get("SHMUP_INSTALLER", os.path.normpath(os.path.join(HERE, "..", "..", "shmup_deck.sh")))
ART_DELAY = 2.0          # seconds between flyer downloads; be kind to the hosts
SETNAME = re.compile(rb"<setname>\s*(.*?)\s*</setname>", re.S)
HEAD_BYTES = 4096


def mra_roots():
    if MRA_ROOTS:
        return MRA_ROOTS.split(":")
    if "SHMUP_ARCADE_DIR" in os.environ:          # tests point at one folder
        return [ARCADE]
    roots = []
    for drive in DRIVES:
        try:
            roots += sorted(os.path.join(drive, d) for d in os.listdir(drive)
                            if d.startswith("_") and os.path.isdir(os.path.join(drive, d)))
        except OSError:
            pass
    return roots


def arcade_root(path):
    """The top-level "_" folder an MRA sits under. The MiSTer loads the MRA's
    core from that folder's cores/ subfolder (see Main_MiSTer mra_loader.cpp)."""
    i = path.find("/_")
    if i < 0:
        return os.path.dirname(path)
    j = path.find("/", i + 1)
    return path[:j] if j >= 0 else path


def path_cost(path):
    """Lower is better: the ordinary release beats variants and edits."""
    name = os.path.basename(path)
    low = path.lower()
    # organised sets file copies of each game into sorting folders (by letter,
    # region, rotation...); the copy nearest the top of _Arcade is the plain one
    n = 10 * os.path.relpath(path, arcade_root(path)).count(os.sep)
    if arcade_root(path) != ARCADE:
        n += 30                       # a quick-launch copy outside _Arcade
    if "/_alternatives/" in low:
        n += 100
    if "/_5 extra software/" in low:
        n += 100
    if "/_arcade offset/" in low:
        n += 80
    if "/_4 video & inputs/" in low:
        n += 60                       # rotation and control-scheme edits
    if name.startswith("}"):
        n += 50                       # year-prefixed duplicate
    if re.search(r"\[bl\]|bootleg", name, re.I):
        n += 40
    if re.search(r"free play|arrange|hack|prototype", name, re.I):
        n += 30
    return n + len(name)


class Index:
    """setname -> best .mra path, built by reading every MRA once."""

    def __init__(self):
        self.lock = threading.Lock()
        self.best = {}
        self.roots = []                 # the folders the cached index covers
        self.stats = {"mras": 0, "broken_links": 0, "unreadable": 0, "seconds": 0, "built": None}
        self.scanning = False
        self._load_cache()

    def _load_cache(self):
        try:
            with open(CACHE) as f:
                data = json.load(f)
            self.best, self.stats = data["best"], data["stats"]
            self.roots = data.get("roots", [ARCADE])
        except (OSError, ValueError, KeyError):
            pass

    def scan(self, full=False):
        """Index every MRA. Only files that are new or have changed size or
        date since the last scan are actually read; the rest come from the
        cache, so a rescan costs a directory walk rather than 30,000 file
        reads. full=True reads everything again. That per-file cache is 30,000
        entries, so it lives in its own file and only in memory during a scan."""
        with self.lock:
            if self.scanning:
                return
            self.scanning = True
        try:
            t = time.time()
            roots = mra_roots()
            old = {}
            if not full:
                try:
                    with open(SEEN) as f:
                        old = json.load(f)
                except (OSError, ValueError):
                    pass
            seen, costs = {}, {}
            found, mras, broken, unreadable, read = {}, 0, 0, 0, 0
            for top in roots:
                for root, _dirs, files in os.walk(top):
                    for name in files:
                        if not name.lower().endswith(".mra"):
                            continue
                        mras += 1
                        path = os.path.join(root, name)
                        try:
                            st = os.stat(path)
                        except OSError:
                            # organised sets often carry shortcuts to files that
                            # have since moved; those are not worth reporting as errors
                            if os.path.islink(path):
                                broken += 1
                            else:
                                unreadable += 1
                            continue
                        prev = old.get(path)
                        if prev and prev[0] == st.st_size and prev[1] == st.st_mtime:
                            setname = prev[2]
                        else:
                            read += 1
                            try:
                                with open(path, "rb") as f:
                                    m = SETNAME.search(f.read(HEAD_BYTES))
                            except OSError:
                                unreadable += 1
                                continue
                            setname = m.group(1).decode("utf-8", "replace") if m else None
                        seen[path] = [st.st_size, st.st_mtime, setname]
                        if not setname:
                            continue
                        cost = costs[path] = path_cost(path)
                        if setname not in found or cost < costs[found[setname]]:
                            found[setname] = path
            stats = {"mras": mras, "read": read, "broken_links": broken, "unreadable": unreadable,
                     "seconds": round(time.time() - t, 1), "built": int(time.time())}
            with self.lock:
                self.best, self.stats, self.roots = found, stats, roots
            for path, data in ((CACHE, {"best": found, "stats": stats, "roots": roots}), (SEEN, seen)):
                with open(path + ".tmp", "w") as f:
                    json.dump(data, f)
                os.replace(path + ".tmp", path)
        finally:
            with self.lock:
                self.scanning = False

    def resolve(self, setnames):
        with self.lock:
            for s in setnames:
                if s in self.best:
                    return self.best[s]
        return None


def image_type(data):
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        return "image/png"
    if data[:3] == b"\xff\xd8\xff":
        return "image/jpeg"
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        return "image/webp"
    return None


def is_image(data):
    return image_type(data) is not None


class Art:
    """Downloads missing flyers once and keeps them on the SD card."""

    def __init__(self):
        self.fetching = False
        self.done = 0
        self.total = 0
        self.failed = []

    def fetch_missing(self):
        if self.fetching:
            return
        self.fetching = True
        try:
            os.makedirs(ART_DIR, exist_ok=True)
            with open(os.path.join(APP_DIR, "art.json")) as f:
                sources = json.load(f)
            # The mirrors hold a small, card-sized copy of every flyer; the
            # per-game source is the original scan, used if no mirror has it.
            mirrors = sources.get("_mirrors", [])
            # a flyer is fetched when it is missing, or when the preferred
            # place to get it has changed (a better scan, or a new mirror snapshot)
            todo = [(gid, s) for gid, s in sources.items()
                    if not gid.startswith("_") and self._stored_url(gid) != self._urls(gid, s, mirrors)[0]]
            self.total, self.done, self.failed = len(todo), 0, []
            for i, (gid, src) in enumerate(todo):
                if i:
                    time.sleep(ART_DELAY)
                if not any(self._get(gid, url, src.get("referer") if url == src["url"] else None)
                           for url in self._urls(gid, src, mirrors)):
                    self.failed.append(gid)
                self.done += 1
        finally:
            self.fetching = False

    @staticmethod
    def _urls(gid, src, mirrors):
        """Where to try, in order: each mirror, then the original scan."""
        return [m.rstrip("/") + "/" + gid + ".webp" for m in mirrors] + [src["url"]]

    @staticmethod
    def _stored_url(gid):
        if not os.path.exists(os.path.join(ART_DIR, gid + ".img")):
            return None
        try:
            with open(os.path.join(ART_DIR, gid + ".src")) as f:
                return f.read().strip()
        except OSError:
            return ""                   # fetched before sources were recorded

    def _get(self, gid, url, referer=None):
        headers = {"User-Agent": USER_AGENT}
        if referer:
            headers["Referer"] = referer
        dest = os.path.join(ART_DIR, gid + ".img")
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=40) as r:
                data = r.read()
        except Exception:
            return False
        # an error page or placeholder is small and not an image
        if len(data) < 5_000 or not is_image(data):
            return False
        tmp = dest + ".tmp"
        with open(tmp, "wb") as f:
            f.write(data)
        os.replace(tmp, dest)
        with open(os.path.join(ART_DIR, gid + ".src"), "w") as f:
            f.write(url)
        return True


NEO_ROOTS = os.environ.get("SHMUP_NEO_ROOTS",
                           "/media/fat/games/NeoGeo:/media/usb0/games/NeoGeo:/media/usb1/games/NeoGeo").split(":")
NEO_SETNAME = re.compile(r"\(([a-z0-9_]+)\)$")
# files that mark a folder as an unzipped Darksoft set
DARKSOFT_PARTS = {"prom", "crom0", "vroma0", "m1rom", "fix"}


class NeoIndex:
    """setname -> Neo Geo game file, relative to the games/NeoGeo folder.

    The Neo Geo core loads .neo files, and Darksoft or MAME sets as zips or
    folders named by setname. Each is matched on that setname: the "(blazstar)"
    in "Blazing Star (blazstar).neo", or a zip or folder called "blazstar".
    """

    RANK = {".neo": 0, ".zip": 1, "dir": 2}   # prefer the self-contained format

    def __init__(self):
        self.lock = threading.Lock()
        self.best = {}                          # setname -> (root, relpath, kind)

    def scan(self):
        found = {}

        def offer(setname, root, path, kind):
            rel = os.path.relpath(path, root)
            key = (self.RANK[kind], rel.count(os.sep), len(rel))
            if setname not in found or key < found[setname][3]:
                found[setname] = (root, rel, kind, key)

        for root in NEO_ROOTS:
            if not os.path.isdir(root):
                continue
            for d, dirs, files in os.walk(root):
                if d != root and DARKSOFT_PARTS & {f.lower() for f in files}:
                    offer(os.path.basename(d).lower(), root, d, "dir")
                    dirs[:] = []
                    continue
                for f in files:
                    stem, ext = os.path.splitext(f)
                    ext = ext.lower()
                    if ext not in (".neo", ".zip"):
                        continue
                    m = NEO_SETNAME.search(stem.lower())
                    offer(m.group(1) if m else stem.lower(), root, os.path.join(d, f), ext)
        with self.lock:
            self.best = {s: v[:3] for s, v in found.items()}

    def resolve(self, setnames):
        with self.lock:
            for s in setnames:
                if s in self.best:
                    return self.best[s]
        return None


INDEX = Index()
NEO = NeoIndex()
ART = Art()
LAST_LAUNCH = {"id": None, "core": None}


_DECK = {"mtime": None, "games": []}
_DECK_LOCK = threading.Lock()


def load_deck():
    """games.json, parsed once and re-read only when the file changes."""
    path = os.path.join(APP_DIR, "games.json")
    mtime = os.stat(path).st_mtime
    with _DECK_LOCK:
        if mtime != _DECK["mtime"]:
            with open(path) as f:
                _DECK["games"], _DECK["mtime"] = json.load(f), mtime
        return _DECK["games"]


def now_playing():
    """The deck game currently running.

    Arcade cores report the game's setname. The Neo Geo core only reports
    "NEOGEO", so for those the best available answer is the last Neo Geo game
    launched from the deck.
    """
    try:
        with open(CORENAME) as f:
            name = f.read().strip()
    except OSError:
        return None
    if name.upper() == "NEOGEO":
        return LAST_LAUNCH["id"] if LAST_LAUNCH["core"] == "neogeo" else None
    for g in load_deck():
        if g.get("platform") != "neogeo" and name in g.get("setnames", [g["id"]]):
            return g["id"]
    return None


class Plays:
    """Launches and time played per game, kept on the MiSTer.

    Watches which core is running, so a game counts however it was started:
    from the deck, from the MiSTer menu or from anything else. Time played is
    written out every minute while a game runs, since a MiSTer is usually
    switched off mid-game rather than returned to the menu.
    """

    POLL, FLUSH = 5, 60

    def __init__(self):
        self.lock = threading.Lock()
        self.games = {}                 # id -> {"launches", "seconds", "last"}
        self.current = None             # id of the game being timed
        self.relaunch = None            # id the deck just launched again
        try:
            with open(PLAYS) as f:
                self.games = json.load(f)
        except (OSError, ValueError):
            pass

    def note_launch(self, gid):
        # the same game launched again does not change CORENAME, so the
        # watcher is told to close the session and start a new one
        with self.lock:
            if gid == self.current:
                self.relaunch = gid

    def watch(self):
        last, since_flush, dirty = time.time(), 0, False
        # a game already running when the service starts (after an update,
        # say) was launched before it was watching, so it is timed, not counted
        self.current = now_playing()
        if self.current:
            self.games.setdefault(self.current, {"launches": 0, "seconds": 0, "last": int(last)})
        while True:
            time.sleep(self.POLL)
            now = time.time()
            elapsed, last = now - last, now
            gid = now_playing()
            with self.lock:
                restart = self.relaunch is not None and gid == self.current
                self.relaunch = None
                if gid == self.current and not restart:
                    if gid:
                        self.games[gid]["seconds"] += elapsed
                        self.games[gid]["last"] = int(now)
                        dirty = True
                else:
                    if gid:
                        g = self.games.setdefault(gid, {"launches": 0, "seconds": 0, "last": 0})
                        g["launches"] += 1
                        g["last"] = int(now)
                        dirty = True
                    self.current = gid
                    since_flush = self.FLUSH      # a change is saved at once
                since_flush += elapsed
                if dirty and since_flush >= self.FLUSH:
                    self._save()
                    since_flush, dirty = 0, False

    def _save(self):
        tmp = PLAYS + ".tmp"
        with open(tmp, "w") as f:
            json.dump(self.games, f)
        os.replace(tmp, PLAYS)

    def snapshot(self):
        with self.lock:
            games = {k: dict(v) for k, v in self.games.items()}
            for g in games.values():
                g["seconds"] = int(g["seconds"])
            return {"games": games, "playing": self.current}


PLAYED = Plays()


class Favourites:
    """The cab's own deck: game ids starred by anyone using it, kept on the
    MiSTer so every phone and browser sees the same list."""

    def __init__(self):
        self.lock = threading.Lock()
        self.ids = []
        try:
            with open(FAVS) as f:
                self.ids = [i for i in json.load(f) if isinstance(i, str)]
        except (OSError, ValueError):
            pass

    def get(self):
        with self.lock:
            return list(self.ids)

    def set(self, gid, on):
        with self.lock:
            if on and gid not in self.ids:
                self.ids.append(gid)
            elif not on and gid in self.ids:
                self.ids.remove(gid)
            tmp = FAVS + ".tmp"
            with open(tmp, "w") as f:
                json.dump(self.ids, f)
            os.replace(tmp, FAVS)
            return list(self.ids)


FAVOURITES = Favourites()


class Versions:
    """Which version of a game the cab launches: game id -> MAME set name,
    chosen from the card's version list and kept on the MiSTer. A game with
    no choice launches the first set of its card that is on the SD card."""

    def __init__(self):
        self.lock = threading.Lock()
        self.chosen = {}
        try:
            with open(VERSIONS_FILE) as f:
                self.chosen = {k: v for k, v in json.load(f).items() if isinstance(v, str)}
        except (OSError, ValueError, AttributeError):
            pass

    def get(self, gid):
        with self.lock:
            return self.chosen.get(gid)

    def set(self, gid, setname):
        with self.lock:
            if setname:
                self.chosen[gid] = setname
            else:
                self.chosen.pop(gid, None)
            tmp = VERSIONS_FILE + ".tmp"
            with open(tmp, "w") as f:
                json.dump(self.chosen, f)
            os.replace(tmp, VERSIONS_FILE)
            return self.chosen.get(gid)


VERSIONS = Versions()


def versions_of(game):
    """Every version of a game on this MiSTer: one per set name of the card
    that has an MRA, in the card's order, named after the MRA file."""
    if game.get("platform") == "neogeo":
        return []
    out = []
    with INDEX.lock:
        for s in game.get("setnames", [game["id"]]):
            path = INDEX.best.get(s)
            if path:
                out.append({"set": s, "path": path, "name": os.path.splitext(os.path.basename(path))[0]})
    return out


def fetch(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


FETCH_CHILD = """
import sys, urllib.request
req = urllib.request.Request(sys.argv[1], headers={"User-Agent": sys.argv[2]})
with urllib.request.urlopen(req, timeout=30) as r:
    sys.stdout.buffer.write(r.read())
"""


def fetch_apart(url):
    """Fetch in a child process. Python's TLS stack keeps about 2 MB resident
    from its first HTTPS request onwards, measured on the MiSTer, and this
    service's memory budget is tight, so the routine check runs where that
    cost is thrown away. The install itself fetches in-process: it ends in
    exec, which throws away everything anyway."""
    r = subprocess.run([sys.executable, "-c", FETCH_CHILD, url, USER_AGENT],
                       capture_output=True, timeout=90)
    if r.returncode != 0:
        lines = r.stderr.decode("utf-8", "replace").strip().splitlines()
        raise RuntimeError(lines[-1] if lines else "fetch failed")
    return r.stdout


def version_key(tag):
    """'v1.4.10' -> (1, 4, 10). Anything else sorts below every real version."""
    m = re.fullmatch(r"v?(\d+(?:\.\d+)*)", (tag or "").strip())
    return tuple(int(x) for x in m.group(1).split(".")) if m else ()


class Updater:
    """Looks for a newer release on GitHub and installs it when asked.

    The check runs a minute and a half after start and every six hours after
    that, so a MiSTer left on all evening asks GitHub once or twice, well
    inside the limit for anonymous requests. Installing does what
    shmup_deck.sh does: replace the program and the app, keep the art, the
    index, favourites and play history, refresh the script in the Scripts
    menu, then start the new program in place of this one.
    """

    def __init__(self):
        self.latest = None      # tag, version, zip, sh, notes, published
        self.checked = 0
        self.error = ""
        self.state = ""         # "", downloading, installing, restarting
        self.lock = threading.Lock()

    @property
    def available(self):
        return bool(self.latest) and version_key(self.latest["tag"]) > version_key(VERSION)

    def snapshot(self):
        return {"current": VERSION, "available": self.available,
                "latest": self.latest["version"] if self.latest else None,
                "notes": self.latest["notes"] if self.latest else "",
                "checked": int(self.checked), "state": self.state, "error": self.error}

    def check(self):
        # a tap on "check" straight after the last look gets the same answer
        if time.time() - self.checked < 30:
            return self.available
        try:
            rel = json.loads(fetch_apart("%s/repos/%s/releases/latest" % (GITHUB_API, REPO)))
            assets = {a["name"]: a["browser_download_url"] for a in rel.get("assets", [])}
            if "shmup_deck.zip" not in assets:
                raise ValueError("release %s has no shmup_deck.zip" % rel.get("tag_name"))
            tag = rel["tag_name"]
            self.latest = {"tag": tag, "version": tag.lstrip("v"), "zip": assets["shmup_deck.zip"],
                           "sh": assets.get("shmup_deck.sh"), "published": rel.get("published_at") or "",
                           "notes": (rel.get("body") or "").strip()[:1500]}
            self.error = ""
        except Exception as e:
            self.error = "could not check GitHub: %s" % e
        self.checked = time.time()
        return self.available

    def watch(self):
        time.sleep(90)
        while True:
            self.check()
            time.sleep(UPDATE_EVERY)

    def start_install(self):
        """Begins the install on its own thread; progress is read from /api/status."""
        if not self.available or not self.lock.acquire(blocking=False):
            return False
        threading.Thread(target=self._install, daemon=True).start()
        return True

    def _install(self):
        import shutil
        import zipfile
        rel = self.latest
        try:
            self.error = ""
            self.state = "downloading"
            z = zipfile.ZipFile(io.BytesIO(fetch(rel["zip"], timeout=180)))
            self.state = "installing"
            files = {}
            for m in z.infolist():
                name = m.filename.split("/", 1)[-1] if m.filename.startswith("shmup_deck/") else m.filename
                if not name or name.endswith("/") or ".." in name or name.startswith("/"):
                    continue
                files[name] = z.read(m)
            program = files.pop("shmup_deck.py", None)
            if not program or not any(n.startswith("app/") for n in files):
                raise ValueError("the download is not a Shmup Deck release")
            # a release that does not even parse must not take the service down
            compile(program, "shmup_deck.py", "exec")
            # the app is swapped whole so a half-written one is never served
            new_app = APP_DIR + ".new"
            old_app = APP_DIR + ".old"
            shutil.rmtree(new_app, ignore_errors=True)
            shutil.rmtree(old_app, ignore_errors=True)
            for name, data in files.items():
                dest = os.path.join(new_app, name[4:]) if name.startswith("app/") else os.path.join(HERE, name)
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                with open(dest, "wb") as f:
                    f.write(data)
            if os.path.isdir(APP_DIR):
                os.rename(APP_DIR, old_app)
            os.rename(new_app, APP_DIR)
            shutil.rmtree(old_app, ignore_errors=True)
            with open(PROGRAM + ".new", "wb") as f:
                f.write(program)
            os.replace(PROGRAM + ".new", PROGRAM)
            # the installer reads this to know what is on the card
            with open(os.path.join(HERE, "VERSION"), "w") as f:
                f.write(rel["tag"])
            self._refresh_installer(rel.get("sh"))
            self.state = "restarting"
            # a scan writing its index should not be cut off mid-file
            for _ in range(120):
                if not INDEX.scanning:
                    break
                time.sleep(1)
            restart()
            # only reached when exec failed: the new files are in place and
            # start on the next boot, but this process is still the old one
            self.error = "installed %s, but the service could not restart; it will start on the next boot" % rel["version"]
        except Exception as e:
            self.error = "update failed: %s" % e
        finally:
            self.state = ""
            self.lock.release()

    def _refresh_installer(self, url):
        if not url or not os.path.isfile(INSTALLER):
            return
        try:
            latest = fetch(url)
            with open(INSTALLER, "rb") as f:
                mine = f.read()
            if latest != mine and latest.startswith(b"#!/bin/bash") and len(latest) > 1000:
                with open(INSTALLER + ".new", "wb") as f:
                    f.write(latest)
                os.replace(INSTALLER + ".new", INSTALLER)
                os.chmod(INSTALLER, 0o755)
        except Exception:
            pass                # the script updates itself the next time it runs


def restart():
    """Start the program on disk in place of this process. The pid, the pid
    file and the boot entry all stay valid; the listening sockets close on
    exec, so the new copy can bind the same ports. argv[0] stays "python3"
    because that is what shmup_deck.sh and other_instances() look for."""
    sys.stdout.flush()
    sys.stderr.flush()
    try:
        os.execvp("python3", ["python3"] + sys.argv)
    except OSError:
        pass


UPDATER = Updater()


def resolve_game(game):
    """Where a deck game lives on this MiSTer, or None if it isn't installed."""
    sets = game.get("setnames", [game["id"]])
    if game.get("platform") == "neogeo":
        hit = NEO.resolve(sets)
        return os.path.join(hit[0], hit[1]) if hit else None
    return INDEX.resolve(sets)


MAME_DIRS = os.environ.get("SHMUP_MAME_DIRS", ":".join(
    ["/media/fat/games/mame", "/media/fat/_Arcade/mame"] +
    ["/media/usb%d/games/mame" % i for i in range(6)])).split(":")


def listing(dirs, ext):
    """Lower-cased file stems with this extension across folders that exist."""
    found = set()
    for d in dirs:
        try:
            found.update(f[:-len(ext)].lower() for f in os.listdir(d) if f.lower().endswith(ext))
        except OSError:
            pass
    return found


def core_present(rbf, cores):
    # The MiSTer takes the newest <rbf>_<date>.rbf, with or without an
    # "Arcade-" prefix: cores in the main distribution drop it, cores from a
    # developer's own repo usually keep it. Match either way.
    want = rbf.lower()
    if want.startswith("arcade-"):
        want = want[7:]
    return any(c == want or c.startswith(want + "_") or
               c == "arcade-" + want or c.startswith("arcade-" + want + "_") for c in cores)


def needed_zips(game):
    """ROM zips a game needs, as groups where any one zip will do.

    The game's own zip comes from a non-merged or split set; a merged set keeps
    clones inside the parent's zip instead. BIOS and sound chip zips are shared
    between games and always needed. Taken from games.json, which records them
    from each game's MRA and MAME's parent and clone lists.
    """
    roms = game.get("roms", {})
    groups = []
    if roms.get("zip"):
        groups.append(list(dict.fromkeys([roms["zip"], roms.get("merged", roms["zip"])])))
    groups += [[z] for z in roms.get("shared", [])]
    return groups


def core_is_standard(rbf):
    """Whether a core is distributed through Update All (MiSTer-devel, JOTEGO
    or Coin-Op Collection). Games on other cores are never reported as
    missing: they show only once the user has installed the core themselves,
    so the deck never points people at cores Update All can't provide."""
    try:
        with open(os.path.join(APP_DIR, "cores.json")) as f:
            cores = json.load(f)
    except (OSError, ValueError):
        return True
    name = rbf[7:] if rbf.lower().startswith("arcade-") else rbf
    src = cores["cores"].get(name, cores["cores"].get(rbf, {})).get("source")
    return bool(cores["sources"].get(src, {}).get("standard"))


def checklist():
    """For every deck game: is it ready, and if not, what is missing.

    Checks the three things an arcade game needs: an MRA, the core it names
    and the ROM zips it reads. Neo Geo games only need their game file.
    "listed" is false for a game that is not ready and whose core is not
    distributed through Update All; the app hides those entirely.
    """
    zips = listing(MAME_DIRS, ".zip")
    cores = {}                              # arcade root -> core file names there
    out = []
    for g in load_deck():
        entry = {"id": g["id"], "mra": None, "core": True, "missing": []}
        if g.get("platform") == "neogeo":
            entry["mra"] = resolve_game(g)
            if not entry["mra"]:
                entry["missing"] = [g.get("roms", {}).get("zip", g["id"])]
            entry["state"] = "ready" if entry["mra"] else "roms"
            entry["listed"] = True
            out.append(entry)
            continue
        path = INDEX.resolve(g.get("setnames", [g["id"]]))
        entry["mra"] = path
        if path:
            home = arcade_root(path)
            if home not in cores:
                cores[home] = listing([os.path.join(home, "cores")], ".rbf")
            entry["core"] = core_present(g.get("rbf", ""), cores[home])
        else:
            if ARCADE not in cores:
                cores[ARCADE] = listing([os.path.join(ARCADE, "cores")], ".rbf")
            entry["core"] = core_present(g.get("rbf", ""), cores[ARCADE])
        entry["missing"] = [" or ".join(grp) for grp in needed_zips(g)
                            if not any(z.lower() in zips for z in grp)]
        entry["state"] = ("mra" if not path else "core" if not entry["core"]
                          else "roms" if entry["missing"] else "ready")
        entry["listed"] = entry["state"] == "ready" or core_is_standard(g.get("rbf", ""))
        entry["versions"] = len(versions_of(g))
        out.append(entry)
    return out


def send_command(cmd):
    # paths come from our own indexes, but the command pipe is line based, so
    # refuse anything that could smuggle a second command
    if "\n" in cmd or "\r" in cmd:
        raise ValueError("bad path")
    with open(CMD, "w") as f:
        f.write(cmd + "\n")


def launch(game, setname=None):
    if game.get("platform") == "neogeo":
        hit = NEO.resolve(game.get("setnames", [game["id"]]))
        if not hit:
            return None
        root, rel, _kind = hit
        # An MGL names the core and the file to hand it; the path is relative
        # to the core's games folder. Settings verified on a MiSTer.
        mgl = ('<mistergamedescription>\n'
               '    <rbf>_Console/NeoGeo</rbf>\n'
               '    <file delay="1" type="f" index="1" path=%s/>\n'
               '</mistergamedescription>\n') % quoteattr(rel)
        with open(MGL_PATH, "w") as f:
            f.write(mgl)
        send_command("load_core %s" % MGL_PATH)
        LAST_LAUNCH.update(id=game["id"], core="neogeo")
        PLAYED.note_launch(game["id"])
        return os.path.join(root, rel)
    # a version picked for this launch, else the one remembered for the game,
    # else the first set on the card
    found = {v["set"]: v["path"] for v in versions_of(game)}
    path = found.get(setname) or found.get(VERSIONS.get(game["id"])) or INDEX.resolve(game.get("setnames", [game["id"]]))
    if not path:
        return None
    send_command("load_core %s" % path)
    LAST_LAUNCH.update(id=game["id"], core="arcade")
    PLAYED.note_launch(game["id"])
    return path


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=APP_DIR, **kw)

    def log_message(self, fmt, *args):
        pass

    def end_headers(self):
        # the app changes between versions; the art never does
        if not self.path.startswith("/art/"):
            self.send_header("Cache-Control", "no-cache")
        super().end_headers()

    def send_json(self, obj, code=200):
        body = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def read_json(self):
        n = int(self.headers.get("Content-Length") or 0)
        if n > 10_000:
            raise ValueError("too large")
        return json.loads(self.rfile.read(n) or b"{}")

    def send_art(self, gid):
        path = os.path.join(ART_DIR, gid + ".img")
        if not re.fullmatch(r"[a-z0-9_]+", gid) or not os.path.exists(path):
            return self.send_json({"error": "no art"}, 404)
        with open(path, "rb") as f:
            data = f.read()
        self.send_response(200)
        self.send_header("Content-Type", image_type(data) or "application/octet-stream")
        self.send_header("Cache-Control", "max-age=31536000")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path == "/api/status":
            return self.send_json({
                "service": "shmup-deck", "version": VERSION, "scanning": INDEX.scanning,
                **INDEX.stats,
                "art": {"fetching": ART.fetching, "done": ART.done, "total": ART.total,
                        "failed": ART.failed},
                "now_playing": now_playing(),
                "update": UPDATER.snapshot()})
        if self.path == "/api/available":
            return self.send_json({g["id"]: resolve_game(g) for g in load_deck()})
        if self.path == "/api/checklist":
            return self.send_json(checklist())
        if self.path == "/api/stats":
            return self.send_json(PLAYED.snapshot())
        if self.path == "/api/favourites":
            return self.send_json({"ids": FAVOURITES.get()})
        if self.path.startswith("/api/versions?"):
            gid = urllib.parse.parse_qs(self.path.split("?", 1)[1]).get("id", [""])[0]
            game = next((g for g in load_deck() if g["id"] == gid), None)
            if not game:
                return self.send_json({"error": "unknown game"}, 404)
            return self.send_json({"id": gid, "versions": versions_of(game), "chosen": VERSIONS.get(gid)})
        if self.path.startswith("/art/"):
            return self.send_art(self.path[5:].split("?")[0])
        return super().do_GET()

    def do_POST(self):
        try:
            if self.path == "/api/launch":
                body = self.read_json()
                gid = body.get("id")
                game = next((g for g in load_deck() if g["id"] == gid), None)
                if not game:
                    return self.send_json({"error": "unknown game"}, 404)
                path = launch(game, body.get("set"))
                if not path:
                    return self.send_json({"error": "not installed"}, 404)
                return self.send_json({"ok": True, "path": path})
            if self.path == "/api/version":
                # {"id", "set"}: remember a version for the game; a null set forgets it
                body = self.read_json()
                gid, setname = body.get("id"), body.get("set")
                game = next((g for g in load_deck() if g["id"] == gid), None)
                if not game:
                    return self.send_json({"error": "unknown game"}, 404)
                if setname and setname not in game.get("setnames", []):
                    return self.send_json({"error": "not a version of this game"}, 400)
                return self.send_json({"id": gid, "chosen": VERSIONS.set(gid, setname)})
            if self.path == "/api/favourites":
                body = self.read_json()
                gid = body.get("id")
                if not any(g["id"] == gid for g in load_deck()):
                    return self.send_json({"error": "unknown game"}, 404)
                return self.send_json({"ids": FAVOURITES.set(gid, bool(body.get("on")))})
            if self.path == "/api/update/check":
                UPDATER.check()
                return self.send_json(UPDATER.snapshot())
            if self.path == "/api/update":
                if not UPDATER.available:
                    return self.send_json({"error": "nothing newer than %s" % VERSION}, 409)
                if not UPDATER.start_install():
                    return self.send_json({"error": "already updating"}, 409)
                return self.send_json({"ok": True, "installing": UPDATER.latest["version"]})
            if self.path == "/api/rescan":
                # {"full": true} re-reads every MRA instead of only changed ones
                full = bool(self.read_json().get("full"))
                threading.Thread(target=INDEX.scan, kwargs={"full": full}, daemon=True).start()
                threading.Thread(target=NEO.scan, daemon=True).start()
                return self.send_json({"ok": True})
        except (ValueError, OSError) as e:
            return self.send_json({"error": str(e)}, 400)
        self.send_json({"error": "not found"}, 404)


MDNS_GROUP, MDNS_PORT = "224.0.0.251", 5353


def lan_ip():
    """This machine's LAN address. Connecting a UDP socket sends nothing."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect((MDNS_GROUP, MDNS_PORT))
        return s.getsockname()[0]
    finally:
        s.close()


def mdns_name(data, off):
    labels = []
    while True:
        n = data[off]
        if n & 0xC0 == 0xC0:                       # compressed pointer
            ptr = struct.unpack("!H", data[off:off + 2])[0] & 0x3FFF
            return labels + mdns_name(data, ptr)[0], off + 2
        off += 1
        if n == 0:
            return labels, off
        labels.append(data[off:off + n].decode("ascii", "replace").lower())
        off += n


def mdns_responder(hostname):
    """Answer mDNS lookups for <hostname>.local with this MiSTer's address.

    The MiSTer image has no Avahi, so without this the deck is only reachable
    by IP, which changes whenever the router hands out a new one. Phones,
    Macs and Windows all resolve .local names over mDNS.
    """
    want = [hostname.lower(), "local"]
    qname = b"".join(bytes([len(p)]) + p.encode() for p in want) + b"\0"

    def open_socket():
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        try:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            if hasattr(socket, "SO_REUSEPORT"):
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
            sock.bind(("", MDNS_PORT))
            sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP,
                            struct.pack("4s4s", socket.inet_aton(MDNS_GROUP), socket.inet_aton("0.0.0.0")))
            sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 255)
            lan_ip()                               # fails until there is a route
            return sock
        except OSError:
            sock.close()
            raise

    def answer(ipv6_asked=False):
        ip = lan_ip()
        # The address record, cache-flush class, two minute TTL. Its name is
        # written out in full at offset 12, so later records point back to it.
        a = qname + struct.pack("!HHIH", 1, 0x8001, 120, 4) + socket.inet_aton(ip)
        # NSEC saying "A is the only address type this name has". Without it a
        # client that also asks for IPv6 waits about five seconds for an answer
        # that never comes before falling back to IPv4.
        nsec = b"\xc0\x0c" + struct.pack("!HHIH", 47, 0x8001, 120, 5) + b"\xc0\x0c\x00\x01\x40"
        if ipv6_asked:
            # no IPv6 answer; the IPv4 address and the NSEC ride as extras
            return struct.pack("!HHHHHH", 0, 0x8400, 0, 0, 0, 2) + a + nsec
        return struct.pack("!HHHHHH", 0, 0x8400, 0, 1, 0, 1) + a + nsec

    # At boot the service usually starts before the network is up, and joining
    # the multicast group fails with "No such device" until it is. Keep trying
    # rather than giving up, or the .local name never answers after a reboot.
    while True:
        try:
            sock = open_socket()
            break
        except OSError:
            time.sleep(5)
    sock.sendto(answer(), (MDNS_GROUP, MDNS_PORT))    # announce on start
    while True:
        try:
            data, addr = sock.recvfrom(9000)
            flags, qd = struct.unpack("!2xHH", data[:6])
            if flags & 0x8000:                         # a response, not a query
                continue
            off = 12
            for _ in range(qd):
                labels, off = mdns_name(data, off)
                qtype, qclass = struct.unpack("!HH", data[off:off + 4])
                off += 4
                if labels == want and qtype in (1, 28, 255):
                    # a one-shot resolver asks from a random port and wants a
                    # direct reply; everyone else listens on the group
                    dest = addr if addr[1] != MDNS_PORT or qclass & 0x8000 else (MDNS_GROUP, MDNS_PORT)
                    sock.sendto(answer(ipv6_asked=qtype == 28), dest)
                    break
        except Exception:
            time.sleep(1)


def other_instances():
    """Pids of any other copy of this service."""
    me = os.getpid()
    found = []
    try:
        pids = os.listdir("/proc")
    except OSError:
        return found
    for pid in pids:
        if not pid.isdigit() or int(pid) == me:
            continue
        try:
            with open("/proc/%s/cmdline" % pid, "rb") as f:
                cmd = f.read().replace(b"\0", b" ")
        except OSError:
            continue
        if cmd.startswith(b"python3 ") and b"shmup_deck.py" in cmd:
            found.append(int(pid))
    return found


def bind(port):
    """The HTTP server on a port, taking it over from an older copy of this
    service if one still holds it.

    An update starts the new service while the old one may be running (an
    installer from before 1.3.0 cannot stop it). Rather than die with
    "address already in use", stop the older copy and try again.
    """
    for attempt in range(6):
        try:
            return ThreadingHTTPServer(("0.0.0.0", port), Handler)
        except OSError as e:
            if e.errno not in (98, 48) or attempt == 5:     # EADDRINUSE on Linux, macOS
                raise
            for pid in other_instances():
                try:
                    os.kill(pid, 15)
                except OSError:
                    pass
            time.sleep(1)


def rescan_if_folders_changed():
    """Rescan when the cached index covers different folders, e.g. a USB drive
    was plugged in, or the cache predates scanning outside _Arcade. USB drives
    can mount after the service starts at boot, so wait before comparing."""
    time.sleep(60)
    if INDEX.roots != mra_roots():
        INDEX.scan()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8190)
    ap.add_argument("--name", default="shmupdeck", help="answers at http://<name>.local")
    args = ap.parse_args()
    # Stay out of the way of the MiSTer's own software: the cores run in the
    # FPGA, but loading games, the menu and CD-based cores use the same ARM CPU.
    try:
        os.nice(10)
    except OSError:
        pass
    if not INDEX.best:
        threading.Thread(target=INDEX.scan, daemon=True).start()
    else:
        threading.Thread(target=rescan_if_folders_changed, daemon=True).start()
    # the Neo Geo folder is small, so it is simply rescanned on every start
    threading.Thread(target=NEO.scan, daemon=True).start()
    threading.Thread(target=ART.fetch_missing, daemon=True).start()
    threading.Thread(target=PLAYED.watch, daemon=True).start()
    threading.Thread(target=UPDATER.watch, daemon=True).start()
    try:
        threading.Thread(target=mdns_responder, args=(args.name,), daemon=True).start()
    except OSError:
        pass
    main_server = bind(args.port)
    # port 80 lets the address be just http://shmupdeck.local; if something
    # else already has it, the numbered port still works
    try:
        http80 = bind(80)
        threading.Thread(target=http80.serve_forever, daemon=True).start()
    except OSError:
        pass
    main_server.serve_forever()


if __name__ == "__main__":
    main()
