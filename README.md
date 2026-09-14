# Shmup Deck

A flyer-wall launcher for shoot 'em ups on the MiSTer FPGA. Open it on your
phone, tap a flyer, and the MiSTer loads the game.

It runs on the MiSTer itself. There is nothing to host, no PC involved and no
other service to install.

![Shmup Deck showing the now playing banner and a search for Cave games](docs/screenshot.jpg)

- 129 auto-scrolling shooters from 1985 onwards, across Toaplan, Cave,
  CV1000, Capcom CPS1/CPS2, PGM, Psikyo, Raizing, Konami, Irem, Neo Geo and more
- Only games actually installed on your SD card are shown
- Sort by name, year or most played; filter by tate or yoko; search by title,
  developer or core
- Shows what is playing right now

## Install

1. Download [`shmup_deck.sh`](https://github.com/searchsolved/shmup-deck/releases/latest/download/shmup_deck.sh)
   and copy it to the `Scripts` folder on your SD card.
2. On the MiSTer, open the Scripts menu and run `shmup_deck`.
3. On your phone, open **http://shmupdeck.local** and add it to your home
   screen if you like.

The address stays the same even when your router gives the MiSTer a new IP.
If `shmupdeck.local` doesn't load on your network, the script also shows the
numbered address, like `http://192.168.1.50:8190`, which always works.

The first start scans your `_Arcade` folder and downloads the flyer art, which
takes a few minutes. Games appear as soon as the scan finishes and flyers fill
in as they arrive.

Run `shmup_deck` from the Scripts menu again at any time to update.

To remove it from startup, run `shmup_deck.sh uninstall` over SSH. Files live
in `/media/fat/Scripts/.config/shmup_deck/`.

## Requirements

- A MiSTer with network access
- Arcade MRAs and ROMs for the games you want, in `_Arcade` (any folder layout
  works, including organised sets)
- For Neo Geo games: the Neo Geo core and games in `games/NeoGeo` (on the SD
  card or a USB drive, subfolders are fine)
- The cores for those games

### Neo Geo formats

| Format | Status |
| --- | --- |
| `.neo` files, e.g. `Blazing Star (blazstar).neo` or `blazstar.neo` | Tested |
| Darksoft sets as a folder or zip named by setname, e.g. `blazstar/` | Detected, not yet tested; reports welcome |
| MAME zips with your own `romsets.xml` | Detected, not yet tested; reports welcome |

Neo Geo games are launched through a generated MGL file. The MiSTer reports
only "NEOGEO" while one is running, so "Now playing" shows the last Neo Geo
game launched from the deck.

Shmup Deck contains no ROMs, MRAs or cores.

## How it works

`shmup_deck.py` is a small Python service using only the standard library that
ships with the MiSTer. It:

- reads the MAME setname inside every `.mra` under `/media/fat/_Arcade`, so
  games are matched exactly (Gunbird is never confused with Gunbird 2) and
  your folder names don't matter
- prefers the plain release over alternatives, bootlegs, free play edits and
  duplicates in sorting folders
- launches by writing `load_core <path>` to `/dev/MiSTer_cmd`, the MiSTer's own
  command interface
- serves the web app on port 80 (if free) and port 8190
- answers mDNS lookups for `shmupdeck.local` itself, since the MiSTer image
  has no Avahi (start it with `--name` to use a different name)

## Flyer art

Flyer art is not included in this repository. On first start each flyer is
downloaded once, a couple of seconds apart, from a pinned snapshot of the
[libretro thumbnails](https://github.com/libretro-thumbnails/MAME) archive
(plus a few from arcadeartwork.org and Wikipedia), and stored on your SD card.
All flyer artwork belongs to its respective copyright holders.

If a flyer can't be downloaded, its card shows the game title instead.

## Adding games

Games are listed in `shmup_deck/app/games.json`:

```json
{
 "id": "gunbird",
 "title": "Gunbird",
 "dev": "Psikyo",
 "year": 1994,
 "core": "Psikyo",
 "orientation": "tate",
 "setnames": ["gunbird"]
}
```

`setnames` lists the MAME sets that count as this game, preferred first.
`orientation` is which way the monitor is fitted for it. Flyer sources go in
`shmup_deck/app/art.json`; `tools/build_art_manifest.py` works out each
flyer's crop from a downloaded scan.

## API

| Method | Path | |
| --- | --- | --- |
| GET | `/api/status` | scan and art progress, version, now playing |
| GET | `/api/available` | game id to installed MRA path (null if missing) |
| POST | `/api/launch` | `{"id": "gunbird"}` |
| POST | `/api/rescan` | rescan `_Arcade` after adding games |

## License

MIT. See [LICENSE](LICENSE).
