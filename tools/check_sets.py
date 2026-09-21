#!/usr/bin/env python3
"""Check every card lists all of its game's MAME sets.

    python3 tools/check_sets.py [--fix]

A card matches MRAs by set name, so a Japanese version with its own title
(Area 88 under U.N. Squadron, U.S. Navy under Carrier Air Wing) is only
found if its set name is on the card. MAME's driver source is the reference:
every GAME line names a set and its parent. For each card this lists the
parent's clones that no card carries, leaving out hacks, bootlegs and
prototypes, sets that turn the monitor the other way from the card (a
horizontal Red Hawk under the tate Stagger I), and anything in SKIP. --fix
appends them to the card.

Shares the driver cache with check_orientation.py.
"""

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_orientation import GAMES, driver_map, expected, fetch  # noqa: E402

GAME_LINE = re.compile(
    r'^\s*GAME[A-Z_]*\(\s*\d{4}\??,\s*(\w+),\s*(\w*),\s*[\w<>]+,\s*[\w<>]+,\s*[\w<>]+,\s*[\w<>]+,\s*(ROT\d+|ORIENTATION_[A-Z_]+),\s*"([^"]*)",\s*"([^"]*)"',
    re.M)
LEAVE_OUT = ("hack", "bootleg", "prototype", "homebrew")
# sets of the same parent that are not versions of the card's game
SKIP = {
    "coh1000t", "sfchamp", "psyforce", "mgcldtex", "ftimpcta",  # other Taito FX-1 games, clones of the BIOS set
}


def game_lines(drivers, sets):
    """set -> (parent, description, manufacturer, screen) for every set in the drivers these sets live in."""
    out = {}
    for path in sorted({drivers[s] for s in sets if s in drivers}):
        for m in GAME_LINE.finditer(fetch(path)):
            s, p = m.group(1), m.group(2)
            out[s] = (s if p in ("0", "") else p, m.group(5), m.group(4), expected(m.group(3))[0])
    return out


def main(fix):
    games = json.loads(GAMES.read_text())
    drivers = driver_map()
    cards = [g for g in games if g.get("platform") != "neogeo"]
    table = game_lines(drivers, [s for g in cards for s in g.get("setnames", [g["id"]])])
    used = {s for g in games for s in g.get("setnames", [g["id"]])}
    missing = unchecked = 0
    for g in cards:
        sets = g.setdefault("setnames", [g["id"]])
        first = next((s for s in sets if s in table), None)
        if first is None:
            print(f"?  {g['id']:<10} no MAME set; nothing to compare")
            unchecked += 1
            continue
        parent = table[first][0]
        if "BIOS" in table.get(parent, ("", "", "", ""))[1]:
            parent = first                          # PGM and the like: every game is a clone of the BIOS set
        for s, (p, name, maker, screen) in table.items():
            if p != parent or s in used or s in SKIP or screen != g["orientation"]:
                continue
            if any(w in (name + " " + maker).lower() for w in LEAVE_OUT):
                continue
            print(f"!  {g['id']:<10} lacks {s:<12} {name}")
            missing += 1
            if fix:
                sets.append(s)
                used.add(s)
    if fix and missing:
        GAMES.write_text(json.dumps(games, indent=1, ensure_ascii=False) + "\n")
        print(f"added {missing}")
    print(f"{len(cards)} cards, {missing} sets missing, {unchecked} unchecked")
    sys.exit(1 if missing and not fix else 0)


if __name__ == "__main__":
    main("--fix" in sys.argv)
