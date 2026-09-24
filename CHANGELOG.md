# Changelog

Every release of Shmup Deck, newest first. The GitHub release for each version carries the same notes at greater length. `tools/release.sh` reads the notes for a release from this file, so a version cannot be published without an entry here.

## 1.11.0 (2026-09-24)

- New display font: the title, headings, deck names and Now playing use Press Start 2P, bundled with the app so it works offline and looks the same on every phone.
- Back to menu is now optional and off by default. Switch it on in Settings under Games; the choice is kept per device.

## 1.10.3 (2026-09-21)

- Five more games: Air Gallet, Darius, Darius II, Dogyuun and Grind Stormer, with their regional sets (Akuu Gallet, V-Five and the rest). From #8.
- Air Gallet runs on the CaveBanpresto core in the main distribution. Darius and Darius II use rmonic79's cores; Dogyuun and Grind Stormer use TheJesusFish's Slop-Core. Games on cores outside Update All appear once the core is installed.
- Batsugun's core link now points to Slop-Core, which has the core build.

## 1.10.2 (2026-09-21)

- Regional sets: 74 more set names on 39 cards, so a Japanese version with a different title is found and launched. Area 88 under U.N. Squadron, U.S. Navy under Carrier Air Wing, Lost Worlds under Forgotten Worlds, Sengoku Ace under Samurai Aces and so on. Fixes the rest of #7.
- Now playing names the set that loaded when it is not the card's first one, so Gradius II shows as such under the Vulcan Venture card.
- Region reads the short forms organised sets use, such as JP, W and EU.
- Back to menu: a button on the Now playing banner and the full-screen flyer loads the MiSTer's own menu, the same as the User button on the board.

## 1.10.1 (2026-09-20)

- The version picker has a Cancel button and a dimmed background, so closing it never launches the card underneath.
- The Layout choices in Settings share the control evenly.
- Standard app wording across Settings, the Decks page and the footers.

## 1.10.0 (2026-09-20)

- Region setting: Any, Japan, World, USA, Europe or Asia. The wall shows games with a set from that region and launches that set. Kept on the MiSTer, so every phone sees the same choice.
- Made for you: automatic decks on the Decks page. Most played, not played yet, tonight's ten, and games hidden by your screen filter.
- Share with everyone: a deck of yours can be offered to the community as a pull request on GitHub. A workflow checks each one.
- Twelve shared decks, reworded and in release order, including a Raizing deck.
- Favourites removed. An old favourites list becomes an ordinary deck called Favourites on first start.
- A game already running when the page opens no longer takes over the screen.
- 1944 The Loop Master is credited to Eighting.

## 1.9.0 (2026-09-20)

- Decks: named game lists kept on the MiSTer, built by tapping cards on the wall.
- A Decks page with an edit sheet for order, cover flyer and description.
- Share a deck as a link. Anyone opening it on their own MiSTer gets a Save button.
- Community decks from the decks folder in this repository.
- Kiosk mode can be limited to one deck.
- The wall can group by deck. The main tab is called Wall.

## 1.8.1 (2026-09-20)

- Kiosk: the running game's flyer stays on screen while it runs. The attract cycle only plays on the menu. A switch in Settings turns this off.
- Settings explains how to add the app to your phone's home screen.

## 1.8.0 (2026-09-20)

- Version picker: a card with several MRAs says how many sets it has. Tap the label or hold the card to choose which one launches. The choice is kept on the MiSTer.
- Cards for versions that play differently: Ketsui IKD 2007 Special, Ketsui Arrange, DoDonPachi Dai-Ou-Jou Black Label, Radiant Silvergun EX and Progear Red Label.
- About forty more regional and revision sets recognised.
- Kiosk intro explains how to leave. No iOS copy callout when holding a card. 200 games.

## 1.7.1 (2026-09-20)

- Every tate game records which way the monitor turns, clockwise or anticlockwise, from MAME. A filter can keep one direction.
- Mars Matrix, 1944, Raiga, Insector X and Tengai corrected to yoko.
- The release script refuses to ship an orientation that disagrees with MAME.

## 1.7.0 (2026-09-20)

- Ten games: Cyvern, Sengeki Striker (Super Kaneko Nova System), Twin Eagle, Arbalester, Meta Fox (Seta Downtown), Twin Hawk, Gigandes, U.N. Defense Force: Earth Joker, Galmedes and Asuka & Asuka (bazset cores).
- Sharper flyers for games still on small scans.
- Phones can no longer nudge the page sideways.

## 1.6.0 (2026-09-19)

- Phone layout: bottom navigation, filters behind one button with chips, the running game at the top of the wall, and a full-screen flyer while a game launches and runs.
- Kiosk mode: just the wall, full screen, kept awake, with a flyer slideshow when idle. Hold the top left corner for two seconds to leave.
- Large layout option. Controls in normal case.
- Seven Seibu Kaihatsu games: Raiden, Raiden II, Raiden DX, Viper Phase 1, Raiden Fighters, Raiden Fighters 2 and Raiden Fighters Jet.
- Sharper flyers for 29 games.

## 1.5.0 (2026-09-19)

- In-app updates: the service checks GitHub every six hours, a dot appears on the settings cog, and Update installs the release and restarts.
- The settings sheet on phones opens from the bottom of the screen.

## 1.4.4 (2026-09-18)

- Giga Wing and Progear corrected to yoko.
- DoDonPachi SaiDaiOuJou and Akai Katana point at the CV1K_Res MRA set.

## 1.4.3 (2026-09-16)

- Games on cores that Update All does not distribute are never reported as missing.

## 1.4.2 (2026-09-16)

- Core names match with or without the Arcade- prefix, fixing Psikyo, Jaleco MegaSystem 32 and SSV (#5).

## 1.4.1 (2026-09-16)

- Updating from a version before 1.3.0 no longer fails with "address already in use".
- The installer script updates itself.

## 1.4.0 (2026-09-16)

- Flyers come from the shmup-deck-art mirror, about 100 KB each, and load as cards scroll into view.
- Same logo size on every page.

## 1.3.1 (2026-09-16)

- Cleaner header, filters on one row, tate and yoko back on the main page, Group as a dropdown.
- The installer updates itself from the release.

## 1.3.0 (2026-09-16)

- Favourites, kept on the MiSTer, with a Copy link.
- Site navigation and a settings panel with a Compact layout.
- Sharper flyers for 112 games. Launch from the stats page.

## 1.2.0 (2026-09-16)

- Play history kept on the MiSTer: launches and time played, however a game was started.
- Played view, Stats page and a stats API.

## 1.1.2 (2026-09-16)

- Rescans only read new or changed MRAs. games.json parsed once. Lighter now playing updates.

## 1.1.1 (2026-09-16)

- shmupdeck.local answers after a reboot. Every game has art. The service runs at low priority.

## 1.1.0 (2026-09-16)

- 49 more games, 178 in total: NMK16, Taito F3, Taito FX-1B, Jaleco MegaSystem 32, Seta, Sega ST-V and Seta SSV.
- Group by developer or arcade system. ROM checklist page. Missing switch. MRAs found in any top-level folder. ROMS.md.

## 1.0.0 (2026-09-14)

- First release: 129 shooters, running on the MiSTer at shmupdeck.local, with flyer art downloaded on first start.
