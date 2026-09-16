#!/bin/bash
# Shmup Deck for MiSTer: run from the Scripts menu.
#
# First run downloads Shmup Deck, starts it, sets it to start at boot and
# shows the address to open on a phone. Run it again at any time to update
# to the latest release and restart.
#
#   shmup_deck.sh             install / update / restart
#   shmup_deck.sh uninstall   stop and remove the boot entry (files are kept)

REPO="searchsolved/shmup-deck"
PORT=8190
HOME_DIR=/media/fat/Scripts/.config/shmup_deck
PID_FILE=/tmp/shmup_deck.pid
SELF=$(readlink -f "$0")
LOG=/tmp/shmup_deck.log
STARTUP=/media/fat/linux/user-startup.sh
MARK="# shmup_deck"

stop_service() {
  # find the service by what it is running rather than trusting the pid
  # file, which can go stale; a stale pid would leave the old version up
  for p in /proc/[0-9]*; do
    c=$(tr "\0" " " 2>/dev/null <"$p/cmdline")   # a process can end mid-scan
    case "$c" in
      python3\ *shmup_deck.py*) kill "${p#/proc/}" 2>/dev/null ;;
    esac
  done
  rm -f "$PID_FILE"
}

start_service() {
  cd "$HOME_DIR" || exit 1
  nohup python3 "$HOME_DIR/shmup_deck.py" --port "$PORT" >"$LOG" 2>&1 &
  echo $! >"$PID_FILE"
}

if [ "$1" = "uninstall" ]; then
  stop_service
  [ -f "$STARTUP" ] && sed -i "/$MARK/d" "$STARTUP"
  echo "Shmup Deck stopped and removed from startup."
  echo "Files are still in $HOME_DIR"
  exit 0
fi

if ! command -v python3 >/dev/null; then
  echo "python3 is missing from this MiSTer Linux image."
  exit 1
fi

echo "Checking for the latest Shmup Deck release..."
# MiSTer's curl lacks a usable CA bundle for GitHub, Python's does not
python3 - "$REPO" "$HOME_DIR" "${SHMUP_API:-https://api.github.com}" "$SELF" <<'EOF'
import io, json, os, shutil, sys, urllib.request, zipfile
repo, home, api, self_path = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
ua = {"User-Agent": "ShmupDeck-installer"}
def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=ua), timeout=60) as r:
        return r.read()
installed = ""
try:
    installed = open(os.path.join(home, "VERSION")).read().strip()
except OSError:
    pass
try:
    rel = json.loads(get("%s/repos/%s/releases/latest" % (api, repo)))
    asset = next(a for a in rel["assets"] if a["name"] == "shmup_deck.zip")
except Exception as e:
    if installed:
        print("Could not check for updates (%s); keeping %s." % (e, installed))
        sys.exit(0)
    print("Download failed: %s" % e)
    sys.exit(1)
tag = rel["tag_name"]
# this script is part of the release too; a newer one is put beside this
# file for the shell to swap in and re-run, so fixes to the installer itself
# reach everyone who runs it
try:
    sh = next(a for a in rel["assets"] if a["name"] == "shmup_deck.sh")
    latest = get(sh["browser_download_url"])
    with open(self_path, "rb") as f:
        mine = f.read()
    if latest != mine and latest.startswith(b"#!/bin/bash") and len(latest) > 1000:
        with open(self_path + ".new", "wb") as f:
            f.write(latest)
except Exception:
    pass
if tag == installed:
    print("Already on the latest version, %s." % tag)
    sys.exit(0)
print("Installing %s..." % tag)
z = zipfile.ZipFile(io.BytesIO(get(asset["browser_download_url"])))
os.makedirs(home, exist_ok=True)
# replace the program and app, never the downloaded art or the game index
for sub in ("app",):
    shutil.rmtree(os.path.join(home, sub), ignore_errors=True)
for m in z.infolist():
    name = m.filename.split("/", 1)[-1] if m.filename.startswith("shmup_deck/") else m.filename
    if not name or name.endswith("/") or ".." in name:
        continue
    dest = os.path.join(home, name)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "wb") as f:
        f.write(z.read(m))
open(os.path.join(home, "VERSION"), "w").write(tag)
EOF
[ $? -ne 0 ] && { sleep 8; exit 1; }

# a newer copy of this script arrived: swap it in and let it finish the job
if [ -z "$SHMUP_REEXEC" ] && [ -f "$SELF.new" ]; then
  mv "$SELF.new" "$SELF" && chmod +x "$SELF"
  echo "Updated the installer itself."
  SHMUP_REEXEC=1 exec bash "$SELF" "$@"
fi
rm -f "$SELF.new"

# boot entry: one marked line, added once
if [ ! -f "$STARTUP" ]; then
  echo "#!/bin/sh" >"$STARTUP"
fi
if ! grep -q "$MARK" "$STARTUP"; then
  echo "[ -f $HOME_DIR/shmup_deck.py ] && (cd $HOME_DIR && nohup python3 shmup_deck.py --port $PORT >$LOG 2>&1 & echo \$! >$PID_FILE) $MARK" >>"$STARTUP"
fi

stop_service
sleep 1
start_service
sleep 2

if ! grep -q shmup_deck.py "/proc/$(cat $PID_FILE)/cmdline" 2>/dev/null; then
  echo "Shmup Deck failed to start. Log:"
  cat "$LOG"
  sleep 8
  exit 1
fi

IP=$(ip -4 addr show 2>/dev/null | awk '/inet / && $2 !~ /^127/ {sub(/\/.*/, "", $2); print $2; exit}')
echo
echo "Shmup Deck is running."
echo
echo "On your phone, open:"
echo "  http://shmupdeck.local"
echo
echo "If that doesn't load on your network, use:"
echo "  http://${IP:-<mister-ip>}:$PORT"
echo
echo "The first start scans your arcade folder and downloads"
echo "the flyer art, which takes a few minutes."
sleep 8
