#!/usr/bin/env python3
"""Check that every art mirror pinned in art.json is live and complete.

The service downloads flyers from the mirror snapshot art.json pins, so a
release that pins a commit not yet pushed to shmup-deck-art ships with no
art. For each mirror: its manifest.json must load, list every game in
art.json, and one flyer must download. Two requests per mirror.

    tools/check_art_mirror.py
"""
import json
import os
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ART_JSON = os.path.join(HERE, "..", "shmup_deck", "app", "art.json")
UA = {"User-Agent": "shmup-deck-release-check"}


def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=20) as r:
        return r.read()


def main():
    with open(ART_JSON) as f:
        art = json.load(f)
    games = sorted(g for g in art if not g.startswith("_"))
    mirrors = art.get("_mirrors", [])
    if not mirrors:
        print("art.json has no _mirrors", file=sys.stderr)
        return 1
    bad = 0
    for m in mirrors:
        base = m.rstrip("/") + "/"
        try:
            manifest = json.loads(get(base + "manifest.json"))
        except Exception as e:
            print(f"{base}manifest.json: {e} (is the art commit pushed?)", file=sys.stderr)
            bad += 1
            continue
        missing = [g for g in games if g not in manifest]
        if missing:
            print(f"{base}: no flyer for {', '.join(missing)}", file=sys.stderr)
            bad += 1
            continue
        try:
            if not get(base + games[-1] + ".webp"):
                raise ValueError("empty file")
        except Exception as e:
            print(f"{base}{games[-1]}.webp: {e}", file=sys.stderr)
            bad += 1
            continue
        print(f"ok {base} ({len(games)} flyers)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
