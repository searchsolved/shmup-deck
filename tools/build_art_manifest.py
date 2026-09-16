#!/usr/bin/env python3
"""Build shmup_deck/app/art.json from downloaded flyer scans.

For each game this records where its flyer is downloaded from and which
rectangle of the scan to show on the card: the scan minus the blank paper the
scanner caught around it. Nothing printed is cropped. The recorded scan size
lets the app notice if a source ever serves a different image, and show that
one whole rather than applying a crop meant for another scan.

    python3 tools/build_art_manifest.py sources.json scans/

sources.json maps game id to {"url": ..., "referer": optional}. scans/ holds
<id>.img files downloaded from exactly those URLs. The scans themselves are
never committed; only the numbers derived from them are.
"""

import json
import sys
from pathlib import Path

import numpy as np
from PIL import Image

WHITE = 218         # a pixel this bright counts as bare paper
PAPER_ROW = 0.85    # a row or column this light is margin, not artwork
CARD_RATIO = 1.42   # height / width of a card
MAX_SHIFT = 0.08    # warn when a scan is stretched further than this


def trim_box(im):
    a = np.asarray(im.convert("RGB")).astype(int)
    h, w, _ = a.shape
    light = a.mean(axis=2) > WHITE
    rows, cols = light.mean(axis=1), light.mean(axis=0)
    top = 0
    while top < h and rows[top] > PAPER_ROW:
        top += 1
    bottom = h
    while bottom > top and rows[bottom - 1] > PAPER_ROW:
        bottom -= 1
    left = 0
    while left < w and cols[left] > PAPER_ROW:
        left += 1
    right = w
    while right > left and cols[right - 1] > PAPER_ROW:
        right -= 1
    return [left, top, right - left, bottom - top]


def main(sources_path, scans_dir, out_path):
    sources = json.loads(Path(sources_path).read_text())
    out, problems = {}, []
    # entries starting with "_" are settings (the mirror list), not games
    try:
        existing = json.loads(Path(out_path).read_text())
        out.update({k: v for k, v in existing.items() if k.startswith("_")})
    except (OSError, ValueError):
        pass
    for gid, src in sources.items():
        scan = Path(scans_dir) / f"{gid}.img"
        if not scan.exists():
            problems.append(f"{gid}: no scan")
            continue
        im = Image.open(scan)
        crop = trim_box(im)
        shift = CARD_RATIO / (crop[3] / crop[2]) - 1
        if abs(shift) > MAX_SHIFT:
            problems.append(f"{gid}: needs {shift:+.0%} to fit a card")
        entry = {"url": src["url"], "size": list(im.size), "crop": crop}
        if src.get("referer"):
            entry["referer"] = src["referer"]
        out[gid] = entry
    Path(out_path).write_text(json.dumps(out, indent=1) + "\n")
    print(f"{len(out)} entries written to {out_path}")
    for p in problems:
        print("  " + p)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2],
         Path(__file__).resolve().parent.parent / "shmup_deck" / "app" / "art.json")
