#!/usr/bin/env python3
"""Build decks/index.json, the list of shared decks the app shows.

    python3 tools/build_deck_index.py [--check]

--check validates without writing, for a pull request whose author has
not rebuilt the index.

Every decks/<slug>.json is a deck someone has shared by pull request:

    {"name": "Cave, in order", "note": "...", "ids": ["donpachi", ...],
     "cover": "ddonpach", "author": "Lee Foot"}

Game ids come from shmup_deck/app/games.json. The checks here are the
ones the service applies when a deck is saved, so a shared deck saves
whole: name up to 60 characters, note up to 300, up to 200 ids, every id
a deck game, no repeats, cover one of the ids, slug lower-case letters,
digits and dashes. Exit status 1 on any problem, so it can gate a merge.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DECKS = ROOT / "decks"
CAPS = {"name": 60, "note": 300, "ids": 200}
MIN_GAMES = 3
# words that fail a shared deck outright; the owner reads the rest
BLOCKED = ("fuck", "shit", "cunt", "nigg", "fag", "retard", "nazi", "hitler", "rape", "porn")


def main():
    known = {g["id"] for g in json.loads((ROOT / "shmup_deck" / "app" / "games.json").read_text())}
    out, names, bad = [], {}, 0
    for path in sorted(DECKS.glob("*.json")):
        if path.name == "index.json":
            continue
        slug = path.stem
        problems = []
        if not re.fullmatch(r"[a-z0-9-]+", slug):
            problems.append("file name must be lower-case letters, digits and dashes")
        try:
            d = json.loads(path.read_text())
        except ValueError as e:
            print(f"{path.name}: not JSON ({e})")
            bad += 1
            continue
        for key in ("name", "ids"):
            if key not in d:
                problems.append(f"missing {key}")
        name = str(d.get("name", ""))
        if not name.strip() or len(name) > CAPS["name"]:
            problems.append(f"name must be 1 to {CAPS['name']} characters")
        if len(str(d.get("note", ""))) > CAPS["note"]:
            problems.append(f"note over {CAPS['note']} characters")
        ids = d.get("ids", [])
        if not isinstance(ids, list) or not ids:
            problems.append("ids must be a non-empty list")
            ids = []
        if len(ids) < MIN_GAMES:
            problems.append(f"a shared deck needs at least {MIN_GAMES} games")
        text = (name + " " + str(d.get("note", "")) + " " + str(d.get("author", ""))).lower()
        if any(w in text for w in BLOCKED):
            problems.append("name, note or author contains a blocked word")
        unknown = [i for i in ids if i not in known]
        if unknown:
            problems.append("unknown ids: " + ", ".join(unknown))
        if len(ids) != len(set(ids)):
            problems.append("repeated ids")
        if len(ids) > CAPS["ids"]:
            problems.append(f"more than {CAPS['ids']} ids")
        if d.get("cover") and d["cover"] not in ids:
            problems.append("cover is not one of the ids")
        if name in names:
            print(f"{path.name}: warning, same name as {names[name]}")
        names[name] = path.name
        if problems:
            bad += 1
            for p in problems:
                print(f"{path.name}: {p}")
            continue
        out.append({"slug": slug, "name": name, "note": str(d.get("note", "")), "ids": ids,
                    "cover": d.get("cover") or None, "author": str(d.get("author", ""))})
    out.sort(key=lambda d: d["name"].lower())
    if "--check" in sys.argv:
        print(f"{len(out)} decks valid" + (f", {bad} rejected" if bad else ""))
    else:
        (DECKS / "index.json").write_text(json.dumps({"decks": out}, indent=1) + "\n")
        print(f"decks/index.json: {len(out)} decks" + (f", {bad} rejected" if bad else ""))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
