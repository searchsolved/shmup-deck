#!/bin/bash
# Release checklist: benchmark the running MiSTer, build the zip, publish.
#
#   tools/release.sh 1.5.0 [--skip-bench] [--minutes 30] < notes.md
#
# Steps, each of which stops the release if it fails:
#   1. VERSION in shmup_deck.py matches, no uncommitted changes
#   2. ROMS.md is current
#   3. tools/bench.py against the MiSTer (the new build must already be
#      running there, installed with shmup_deck.sh); --skip-bench for a
#      docs-only release
#   4. dist/shmup_deck.zip and dist/shmup_deck.sh
#   5. git push, then the GitHub release with the notes from stdin
set -euo pipefail
cd "$(dirname "$0")/.."

ver=${1:?version, like 1.5.0}; shift
bench=1; minutes=30
while [ $# -gt 0 ]; do
  case "$1" in
    --skip-bench) bench=0;;
    --minutes) minutes=$2; shift;;
    *) echo "unknown option $1" >&2; exit 2;;
  esac
  shift
done

grep -q "^VERSION = \"$ver\"" shmup_deck/shmup_deck.py || { echo "shmup_deck.py is not at VERSION $ver" >&2; exit 1; }
[ -z "$(git status --porcelain)" ] || { echo "commit first; the tree is not clean" >&2; git status --short; exit 1; }
python3 -m py_compile shmup_deck/shmup_deck.py

python3 tools/build_rom_list.py >/dev/null
[ -z "$(git status --porcelain)" ] || { echo "ROMS.md changed; commit it and run again" >&2; exit 1; }
# the shared decks list the app fetches must match the files
python3 tools/build_deck_index.py >/dev/null || { echo "a shared deck in decks/ is invalid; run tools/build_deck_index.py" >&2; exit 1; }
[ -z "$(git status --porcelain)" ] || { echo "decks/index.json changed; commit it and run again" >&2; exit 1; }
# orientation and rotation come from MAME, never by eye
python3 tools/check_orientation.py >/dev/null || { echo "a game's orientation disagrees with MAME; run tools/check_orientation.py" >&2; exit 1; }

if [ $bench = 1 ]; then
  echo "== benchmark"
  running=$(curl -s -m 5 "http://${SHMUP_HOST:-shmupdeck.local}:8190/api/status" | python3 -c 'import json,sys;print(json.load(sys.stdin)["version"])' || true)
  [ "$running" = "$ver" ] || { echo "the MiSTer is running ${running:-nothing}, not $ver; install this build there first" >&2; exit 1; }
  python3 tools/bench.py --minutes "$minutes"
fi

echo "== package"
rm -rf shmup_deck/__pycache__ tools/__pycache__
rm -f dist/shmup_deck.zip
zip -r -X dist/shmup_deck.zip shmup_deck -x "*/__pycache__/*" "*.DS_Store" "*/art/*" "*mra_index*.json" "*plays.json" "*favourites.json" "*versions.json" "*decks.json" "*.migrated" "*settings.json" >/dev/null
cp shmup_deck.sh dist/shmup_deck.sh
unzip -l dist/shmup_deck.zip | tail -1

echo "== publish v$ver"
git push -q origin main
gh release create "v$ver" -R searchsolved/shmup-deck --title "Shmup Deck $ver" --target main \
  dist/shmup_deck.zip dist/shmup_deck.sh --notes-file -
