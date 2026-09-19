#!/usr/bin/env python3
"""Write ROMS.md, the list of every game the deck supports and what it needs.

    python3 tools/build_rom_list.py

Reads shmup_deck/app/games.json and shmup_deck/app/cores.json, so run it
again whenever a game is added. The zip names in games.json come from each
game's MRA and MAME's parent and clone lists.
"""

import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
APP = ROOT / "shmup_deck" / "app"


def zip_list(names):
    return ", ".join(f"`{n}.zip`" for n in names) if names else ""


def main():
    games = json.loads((APP / "games.json").read_text())
    cores = json.loads((APP / "cores.json").read_text())
    sources, by_rbf = cores["sources"], cores["cores"]

    def source_of(g):
        c = by_rbf.get(g["rbf"], {})
        if c.get("url"):
            return f"[GitHub]({c['url']})"
        return sources.get(c.get("source"), {}).get("name", "")

    arcade = [g for g in games if g.get("platform") != "neogeo"]
    neo = [g for g in games if g.get("platform") == "neogeo"]
    by_core = defaultdict(list)
    for g in arcade:
        by_core[g["core"]].append(g)

    out = []
    w = out.append
    w("# Supported games and ROMs")
    w("")
    w(f"Shmup Deck supports {len(games)} games: {len(arcade)} arcade games that run from MRA files "
      f"and {len(neo)} Neo Geo games. This page lists the core and ROM files each one needs.")
    w("")
    w("To see what your own MiSTer is missing, open **http://shmupdeck.local/check.html** once "
      "Shmup Deck is installed. It checks every game for its MRA, core and ROM zips and can copy "
      "the missing zip names.")
    w("")
    w("Shmup Deck contains no ROMs, MRAs or cores.")
    w("")
    w("## Reading the tables")
    w("")
    w("- ROM zips go in `games/mame` on the SD card or a USB drive.")
    w("- **Zip** is the file from a non-merged or split MAME set.")
    w("- **Merged set zip** is where a merged set keeps the same game. Clones live inside their "
      "parent's zip, so it differs only for clones. A split set needs both.")
    w("- **Also needs** lists BIOS and chip ROM zips shared between games. These are needed "
      "whichever kind of set you use.")
    w("- Each MRA is written against a particular MAME version, stated in its `<mameversion>` tag. "
      "A recent MAME set suits most games; if one won't start, compare your set's version with that tag.")
    w("")
    w("## Cores")
    w("")
    w("| Source | How to get it |")
    w("| --- | --- |")
    for key in ("official", "jotego", "coinop", "meatcores"):
        w(f"| {sources[key]['name']} | {sources[key]['note'][0].upper() + sources[key]['note'][1:]} |")
    w("")
    w("These cores are not in update_all. Install the core and its MRAs from each repository:")
    w("")
    w("| Core | Games | Repository | Notes |")
    w("| --- | --- | --- | --- |")
    manual = defaultdict(list)
    for g in arcade:
        c = by_rbf.get(g["rbf"], {})
        if c.get("url"):
            manual[(g["core"], c["url"], c.get("note", ""))].append(g["title"])
    for (core, url, note), titles in sorted(manual.items()):
        # a core can live outside GitHub, on the author's Patreon say
        label = url.split("github.com/")[1] if "github.com/" in url else url.split("//")[-1].split("/posts/")[0]
        w(f"| {core} | {len(titles)} | [{label}]({url}) | {note} |")
    w("")
    w("## Arcade games")
    w("")
    for core in sorted(by_core, key=str.lower):
        w(f"### {core}")
        w("")
        w("| Game | Year | Core source | Zip | Merged set zip | Also needs |")
        w("| --- | --- | --- | --- | --- | --- |")
        for g in sorted(by_core[core], key=lambda g: g["title"].lower()):
            r = g["roms"]
            merged = f"`{r['merged']}.zip`" if r["merged"] != r["zip"] else "same"
            title = g["title"] + (" *" if r.get("note") else "")
            w(f"| {title} | {g['year']} | {source_of(g)} | `{r['zip']}.zip` | {merged} | {zip_list(r['shared'])} |")
        notes = [g for g in by_core[core] if g["roms"].get("note")]
        if notes:
            w("")
            for g in notes:
                w(f"\\* {g['title']}: {g['roms']['note']}.")
        w("")
    w("## Neo Geo games")
    w("")
    w("Neo Geo games run on the Neo Geo core from the MiSTer main distribution and go in "
      "`games/NeoGeo`, on the SD card or a USB drive. Subfolders are fine. The Neo Geo core also "
      "needs its BIOS files in that folder; see the core's own documentation.")
    w("")
    w("| Game | Year | Setname | Accepted files |")
    w("| --- | --- | --- | --- |")
    for g in sorted(neo, key=lambda g: g["title"].lower()):
        s = g["roms"]["zip"]
        w(f"| {g['title']} | {g['year']} | `{s}` | `{s}.neo`, `Title ({s}).neo`, or a `{s}` Darksoft or MAME zip or folder |")
    w("")
    w("## All arcade zip names")
    w("")
    w("One per line, for filtering a download. Non-merged or split set:")
    w("")
    w("```")
    # jtbeta is JOTEGO's beta key, not part of any MAME set
    shared = {z for g in arcade for z in g["roms"]["shared"] if z != "jtbeta"}
    nonmerged = sorted({g["roms"]["zip"] for g in arcade} | shared)
    w("\n".join(f"{z}.zip" for z in nonmerged))
    w("```")
    w("")
    w("Merged set:")
    w("")
    w("```")
    merged = sorted({g["roms"]["merged"] for g in arcade} | shared)
    w("\n".join(f"{z}.zip" for z in merged))
    w("```")
    w("")
    (ROOT / "ROMS.md").write_text("\n".join(out))

    # flyers shown whole rather than card shaped, or not confirmed as flyers
    art = json.loads((APP / "art.json").read_text())
    titles = {g["id"]: g["title"] for g in games}
    wanted = [(titles[gid], a["upgrade"]) for gid, a in art.items()
              if not gid.startswith("_") and a.get("upgrade") and gid in titles]
    lines = ["# Flyers wanted", "",
             "These games use the best art found so far, shown whole on the card. A portrait scan of the "
             "front of the original arcade flyer would be an upgrade. If you have one, or know where one "
             "is, please open an issue with a link.", "",
             "| Game | Current art |", "| --- | --- |"]
    lines += [f"| {t} | {why} |" for t, why in sorted(wanted, key=lambda x: x[0].lower())]
    (ROOT / "FLYERS_WANTED.md").write_text("\n".join(lines) + "\n")
    print(f"FLYERS_WANTED.md: {len(wanted)} games")
    print(f"ROMS.md: {len(games)} games, {len(nonmerged)} non-merged zips, {len(merged)} merged zips")


if __name__ == "__main__":
    main()
