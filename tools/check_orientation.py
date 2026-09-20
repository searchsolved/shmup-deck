#!/usr/bin/env python3
"""Check every game's orientation and rotation against MAME.

    python3 tools/check_orientation.py [--fix]

MAME's driver source is the reference: each GAME line says ROT0 (a normal,
yoko monitor), ROT270 (a tate monitor turned anticlockwise; Cave, Raiden,
Psikyo, Toaplan) or ROT90 (turned clockwise; most Konami and Namco).
games.json must agree: "orientation" yoko or tate, and for tate games a
"rotation" of ccw or cw. Run it whenever games are added; --fix writes the
MAME answer into games.json.

mame.lst maps every set name to its driver file; the driver files are then
fetched from GitHub, a second apart, and kept in a cache under tools/.
"""

import json
import re
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GAMES = ROOT / "shmup_deck" / "app" / "games.json"
CACHE = ROOT / "tools" / ".mame_cache"
RAW = "https://raw.githubusercontent.com/mamedev/mame/master/src/mame/"
UA = {"User-Agent": "ShmupDeck-check (+https://github.com/searchsolved/shmup-deck)"}
GAME_LINE = r"^GAME\w*\(\s*\d+,\s*%s\s*,.*?(ROT0|ROT90|ROT180|ROT270|ORIENTATION_FLIP_[XY])"
# games with no MAME set, or whose MAME set is not the board they run on here
KNOWN = {"ddpsdoj": "ROT270", "akatana": "ROT0"}          # CV1000, not in MAME; Akai Katana is horizontal


def fetch(path):
    dest = CACHE / path.replace("/", "_")
    if not dest.exists():
        CACHE.mkdir(exist_ok=True)
        with urllib.request.urlopen(urllib.request.Request(RAW + path, headers=UA), timeout=60) as r:
            dest.write_bytes(r.read())
        time.sleep(1)
    return dest.read_text(encoding="utf-8", errors="replace")


def driver_map():
    """set name -> driver file, from MAME's own list of sets."""
    out, driver = {}, None
    for line in fetch("mame.lst").splitlines():
        line = line.strip()
        if line.startswith("@source:"):
            driver = line[8:].strip()
        elif line and not line.startswith("//") and driver:
            out[line.split()[0]] = driver
    return out


def mame_rotation(game, drivers):
    if game["id"] in KNOWN:
        return KNOWN[game["id"]]
    for s in game["setnames"]:
        if s not in drivers:
            continue
        m = re.search(GAME_LINE % re.escape(s), fetch(drivers[s]), re.M)
        if m:
            return m.group(1)
    return None


def expected(rot):
    if rot in ("ROT0", "ROT180", "ORIENTATION_FLIP_X", "ORIENTATION_FLIP_Y"):
        return "yoko", None
    return "tate", "cw" if rot == "ROT90" else "ccw"


def main(fix):
    games = json.loads(GAMES.read_text())
    drivers = driver_map()
    bad = unknown = 0
    for g in games:
        if g.get("platform") == "neogeo":
            continue
        rot = mame_rotation(g, drivers)
        if rot is None:
            print(f"?  {g['id']:<10} no MAME set found; checked by hand?")
            unknown += 1
            continue
        want = expected(rot)
        have = (g["orientation"], g.get("rotation"))
        if have != want:
            print(f"!  {g['id']:<10} games.json says {have}, MAME {rot} says {want}")
            bad += 1
            if fix:
                g["orientation"] = want[0]
                if want[1]:
                    g["rotation"] = want[1]
                else:
                    g.pop("rotation", None)
    if fix and bad:
        GAMES.write_text(json.dumps(games, indent=1) + "\n")
        print(f"fixed {bad}")
    print(f"{len(games)} games, {bad} wrong, {unknown} unchecked")
    sys.exit(1 if bad and not fix else 0)


if __name__ == "__main__":
    main("--fix" in sys.argv)
