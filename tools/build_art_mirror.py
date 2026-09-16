#!/usr/bin/env python3
"""Build the flyer mirror: one small WebP per game, cropped and sized for a card.

    python3 tools/build_art_mirror.py <mirror repo dir> [cache dir]

Reads shmup_deck/app/art.json. For each game it downloads the source scan
(once; kept in the cache dir), cuts it to the recorded crop box, scales it to
at most MAX_W wide (or MAX_H tall for flyers shown whole) and writes
<id>.webp into the mirror repo, plus a manifest.json of sizes and sources.
Sources are fetched a couple of seconds apart, with the Referer some hosts
need. Scans whose size no longer matches art.json are skipped and reported,
since the crop box would then be wrong.
"""

import hashlib
import io
import json
import sys
import time
import urllib.request
from pathlib import Path

from PIL import Image

MAX_W, MAX_H = 640, 900
QUALITY = 80
UA = "ShmupDeck-mirror/1.0 (+https://github.com/searchsolved/shmup-deck)"
ROOT = Path(__file__).resolve().parent.parent


def fetch(url, referer, cache):
    key = cache / (hashlib.sha1(url.encode()).hexdigest() + ".img")
    if key.exists():
        return key.read_bytes()
    headers = {"User-Agent": UA}
    if referer:
        headers["Referer"] = referer
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=60) as r:
        data = r.read()
    key.write_bytes(data)
    time.sleep(2)
    return data


def main(out_dir, cache_dir):
    out, cache = Path(out_dir), Path(cache_dir)
    out.mkdir(parents=True, exist_ok=True)
    cache.mkdir(parents=True, exist_ok=True)
    art = json.loads((ROOT / "shmup_deck" / "app" / "art.json").read_text())
    manifest, problems = {}, []
    for gid, a in art.items():
        if gid.startswith("_"):
            continue
        try:
            im = Image.open(io.BytesIO(fetch(a["url"], a.get("referer"), cache)))
        except Exception as e:
            problems.append(f"{gid}: download failed ({e})")
            continue
        if list(im.size) != a["size"]:
            problems.append(f"{gid}: scan is {im.size}, art.json says {a['size']}")
            continue
        l, t, w, h = a["crop"]
        im = im.convert("RGB").crop((l, t, l + w, t + h))
        scale = min(MAX_W / im.width, MAX_H / im.height, 1)
        if scale < 1:
            im = im.resize((round(im.width * scale), round(im.height * scale)), Image.LANCZOS)
        dest = out / f"{gid}.webp"
        im.save(dest, "WEBP", quality=QUALITY, method=6)
        manifest[gid] = {"size": list(im.size), "bytes": dest.stat().st_size, "source": a["url"]}
        print(f"{gid:10} {im.width}x{im.height} {dest.stat().st_size // 1024} KB")
    (out / "manifest.json").write_text(json.dumps(manifest, indent=1) + "\n")
    total = sum(m["bytes"] for m in manifest.values())
    print(f"{len(manifest)} flyers, {total / 1e6:.1f} MB")
    for p in problems:
        print("  " + p)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else ROOT.parent / "shmup-deck-artcache")
