# Supported games and ROMs

Shmup Deck supports 294 games: 280 arcade games that run from MRA files and 14 Neo Geo games. This page lists the core and ROM files each one needs.

To see what your own MiSTer is missing, open **http://shmupdeck.local/check.html** once Shmup Deck is installed. It checks every game for its MRA, core and ROM zips and can copy the missing zip names.

Shmup Deck contains no ROMs, MRAs or cores.

## Reading the tables

- ROM zips go in `games/mame` on the SD card or a USB drive.
- **Zip** is the file from a non-merged or split MAME set.
- **Merged set zip** is where a merged set keeps the same game. Clones live inside their parent's zip, so it differs only for clones. A split set needs both.
- **Also needs** lists BIOS and chip ROM zips shared between games. These are needed whichever kind of set you use.
- Each MRA is written against a particular MAME version, stated in its `<mameversion>` tag. A recent MAME set suits most games; if one won't start, compare your set's version with that tag.

## Cores

| Source | How to get it |
| --- | --- |
| MiSTer main distribution | Installed by update_all by default |
| JOTEGO cores | Optional database; switch it on in update_all's settings |
| Coin-Op Collection | Optional database; switch it on in update_all's settings |
| MeatCores | Not distributed through Update All; the deck lists these games only when the core is already installed |

These cores are not in update_all. Install the core and its MRAs from each repository:

| Core | Games | Repository | Notes |
| --- | --- | --- | --- |
| Asuka | 1 | [www.patreon.com/bazset](https://www.patreon.com/bazset/posts/asuka-asuka-1988-169899343) | Core and MRA from the author's Patreon post; no repository |
| CV1000 | 14 | [ika-musume/ikacore_CV1k](https://github.com/ika-musume/ikacore_CV1k) | The repository has no core build or MRAs; builds come from the developer. MRAs for all games, including DoDonPachi SaiDaiOuJou and Akai Katana, are in [funkycochise/CV1K_Res](https://github.com/funkycochise/CV1K_Res) |
| Capcom | 1 | [OngoGablogian/MiSTer_Ongo](https://github.com/OngoGablogian/MiSTer_Ongo) |  |
| Darius | 1 | [rmonic79/Arcade-Darius_MiSTer](https://github.com/rmonic79/Arcade-Darius_MiSTer) | Core and MRAs in the repository's releases folder |
| Darius II | 1 | [rmonic79/Arcade-Darius2NinjaWarriors_MiSTer](https://github.com/rmonic79/Arcade-Darius2NinjaWarriors_MiSTer) | Core and MRAs in the repository's releases folder; The Ninja Warriors shares it |
| Dooyong | 7 | [searchsolved/Arcade-Dooyong_MiSTer](https://github.com/searchsolved/Arcade-Dooyong_MiSTer) | Core and MRAs in the repository's releases folder; one core runs all the Dooyong games |
| EarthJoker | 1 | [www.patreon.com/bazset](https://www.patreon.com/bazset/posts/u-n-defense-1993-169900198) | Core and MRA from the author's Patreon post; no repository |
| Galmedes | 1 | [www.patreon.com/bazset](https://www.patreon.com/bazset/posts/galmedes-visco-169900687) | Core and MRA from the author's Patreon post; no repository |
| Gigandes | 1 | [bazset/Gigandes-FPGA](https://github.com/bazset/Gigandes-FPGA) | Source only; the core build and MRA are on the author's Patreon |
| Kaneko | 1 | [kuzearcade/Arcade-SandScrp_MiSTer](https://github.com/kuzearcade/Arcade-SandScrp_MiSTer) | Core and MRAs in the repository's releases folder |
| Kaneko16 | 3 | [alphanu1/kaneko16-mister](https://github.com/alphanu1/kaneko16-mister) | Core and MRAs in the repository's releases folder |
| Konami | 1 | [jlrh/konami-fpga](https://github.com/jlrh/konami-fpga) | Core and MRA in the repository's releases and cores/blswhstl folders |
| Konami | 1 | [jlrh/konami-fpga](https://github.com/jlrh/konami-fpga) | Core and MRA in the repository's releases and cores/xexex folders |
| Konami | 4 | [ppriest/Arcade-KonamiGX_MiSTer](https://github.com/ppriest/Arcade-KonamiGX_MiSTer) | Core and MRAs in the repository's releases folder; a work-in-progress beta. Every game also needs konamigx.zip |
| Mega System 1 | 3 | [kuzearcade/Arcade-JalecoMS1BCD_MiSTer](https://github.com/kuzearcade/Arcade-JalecoMS1BCD_MiSTer) | Core and MRAs in the repository's releases folder |
| MegaSystem 32 | 4 | [ppriest/Arcade-JalecoMS32_MiSTer](https://github.com/ppriest/Arcade-JalecoMS32_MiSTer) |  |
| NMK | 1 | [kuzearcade/Arcade-NMKBP964_MiSTer](https://github.com/kuzearcade/Arcade-NMKBP964_MiSTer) | Core and MRAs in the repository's releases folder |
| NMK16 | 19 | [kuzearcade/Arcade-NMK16_MiSTer](https://github.com/kuzearcade/Arcade-NMK16_MiSTer) |  |
| Namco | 3 | [kuzearcade/Arcade-NamcoSystem2_MiSTer](https://github.com/kuzearcade/Arcade-NamcoSystem2_MiSTer) | Core and MRAs in the repository's releases folder; in development. Every game also needs namcoc65.zip |
| Namco NA-1 | 1 | [OngoGablogian/MiSTer_Ongo](https://github.com/OngoGablogian/MiSTer_Ongo) |  |
| Namco System 11 | 1 | [OngoGablogian/MiSTer_Ongo](https://github.com/OngoGablogian/MiSTer_Ongo) |  |
| Raiden | 1 | [rmonic79/Arcade-Raiden_MiSTer](https://github.com/rmonic79/Arcade-Raiden_MiSTer) | Core and MRAs in the repository's releases folder |
| Raiden2 | 2 | [rmonic79/Arcade-Raiden2_MiSTer](https://github.com/rmonic79/Arcade-Raiden2_MiSTer) | Core and MRAs in the repository's releases folder; Raiden II and Raiden DX share it |
| SKNS | 2 | [srg320/Arcade-SKNS_MiSTer](https://github.com/srg320/Arcade-SKNS_MiSTer) | Core and MRAs in the repository's releases folder; every game also needs skns.zip, the system BIOS |
| Sega System 24 | 1 | [OngoGablogian/MiSTer_Ongo](https://github.com/OngoGablogian/MiSTer_Ongo) |  |
| SeibuSPI | 4 | [zakk4223/Arcade-SeibuSPI_MiSTer](https://github.com/zakk4223/Arcade-SeibuSPI_MiSTer) | Core and MRAs in the repository's releases folder; an early core, the author describes it as unvalidated against hardware |
| Seta | 8 | [ppriest/Arcade-Seta_MiSTer](https://github.com/ppriest/Arcade-Seta_MiSTer) |  |
| SetaDowntown | 4 | [ppriest/Arcade-Seta_MiSTer](https://github.com/ppriest/Arcade-Seta_MiSTer) | Core and MRAs in the repository's releases folder; a separate core from Seta, for the Downtown board |
| SunA | 1 | [OngoGablogian/MiSTer_Ongo](https://github.com/OngoGablogian/MiSTer_Ongo) |  |
| System C2 | 1 | [Mezzow/Arcade-SystemC2_MiSTer](https://github.com/Mezzow/Arcade-SystemC2_MiSTer) | Core and MRAs in the repository's releases folder |
| Taito B | 3 | [Mezzow/Arcade-TaitoB_MiSTer](https://github.com/Mezzow/Arcade-TaitoB_MiSTer) | Core and MRAs in the repository's releases folder |
| Taito F3 | 5 | [spacestate1/Arcade-taitoF3_MiSTer](https://github.com/spacestate1/Arcade-taitoF3_MiSTer) |  |
| Taito FX-1B | 2 | [XelaNotPu/ZN1-TaitoFX1B_MiSTer](https://github.com/XelaNotPu/ZN1-TaitoFX1B_MiSTer) |  |
| Toaplan | 5 | [TheJesusFish/Slop-Core](https://github.com/TheJesusFish/Slop-Core) | Core and MRAs in the repository's _Arcade folder |
| TwinHawk | 1 | [bazset/Twin-Hawk-FPGA](https://github.com/bazset/Twin-Hawk-FPGA) | MRAs in the repository; the core build is on the author's Patreon |
| Video System | 2 | [OngoGablogian/MiSTer_Ongo](https://github.com/OngoGablogian/MiSTer_Ongo) |  |
| ZN-1 | 2 | [OngoGablogian/MiSTer_Ongo](https://github.com/OngoGablogian/MiSTer_Ongo) |  |

## Arcade games

### Aleck64

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Star Soldier: Vanishing Earth | 1998 | MiSTer main distribution | `starsldr.zip` | same | `aleck64.zip` |

### Alpha 68K

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Sky Adventure | 1989 | Coin-Op Collection | `skyadvnt.zip` | same |  |
| Sky Soldiers | 1988 | Coin-Op Collection | `skysoldr.zip` | same |  |

### Asuka

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Asuka & Asuka | 1988 | [GitHub](https://www.patreon.com/bazset/posts/asuka-asuka-1988-169899343) | `asuka.zip` | same |  |

### Capcom

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| 1942 | 1984 | JOTEGO cores | `1942.zip` | same |  |
| 1943 | 1987 | JOTEGO cores | `1943.zip` | same |  |
| 1943 Kai: Midway Kaisen | 1987 | JOTEGO cores | `1943kai.zip` | same |  |
| Exed Exes | 1985 | JOTEGO cores | `exedexes.zip` | same |  |
| Gun.Smoke | 1985 | JOTEGO cores | `gunsmoke.zip` | same |  |
| Last Duel | 1988 | [GitHub](https://github.com/OngoGablogian/MiSTer_Ongo) | `lastduel.zip` | same |  |
| Legendary Wings | 1986 | JOTEGO cores | `lwings.zip` | same |  |
| Section Z | 1985 | JOTEGO cores | `sectionz.zip` | same |  |
| Side Arms | 1986 | JOTEGO cores | `sidearms.zip` | same |  |
| Vulgus | 1984 | JOTEGO cores | `vulgus.zip` | same |  |

### Cave

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Air Gallet | 1996 | MiSTer main distribution | `agallet.zip` | same |  |
| Dangun Feveron | 1998 | MiSTer main distribution | `dfeveron.zip` | `feversos.zip` |  |
| DoDonPachi | 1997 | MiSTer main distribution | `ddonpach.zip` | same |  |
| DonPachi | 1995 | MiSTer main distribution | `donpachi.zip` | same |  |
| ESP Ra.De. | 1998 | MiSTer main distribution | `esprade.zip` | same |  |
| Guwange | 1999 | MiSTer main distribution | `guwange.zip` | same |  |
| Hotdog Storm | 1996 | MiSTer main distribution | `hotdogst.zip` | same |  |
| Mazinger Z | 1994 | MiSTer main distribution | `mazinger.zip` | same |  |

### CPS1

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| 1941 Counter Attack | 1990 | JOTEGO cores | `1941.zip` | same |  |
| Carrier Air Wing | 1990 | JOTEGO cores | `cawing.zip` | same |  |
| Forgotten Worlds | 1988 | JOTEGO cores | `forgottn.zip` | same |  |
| U.N. Squadron | 1989 | JOTEGO cores | `unsquad.zip` | same |  |
| Varth | 1992 | JOTEGO cores | `varth.zip` | same |  |

### CPS2

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| 1944 The Loop Master | 2000 | JOTEGO cores | `1944.zip` | same | `qsound.zip` |
| 19XX | 1996 | JOTEGO cores | `19xx.zip` | same | `qsound.zip` |
| Dimahoo | 2000 | JOTEGO cores | `dimahoo.zip` | same | `qsound.zip` |
| Eco Fighters | 1993 | JOTEGO cores | `ecofghtr.zip` | same | `qsound.zip` |
| Giga Wing | 1999 | JOTEGO cores | `gigawing.zip` | same | `qsound.zip` |
| Mars Matrix | 2000 | JOTEGO cores | `mmatrix.zip` | same | `qsound.zip` |
| Progear | 2001 | JOTEGO cores | `progear.zip` | same | `qsound.zip` |
| Progear: Red Label, Halfway to Hell * | 2016 | JOTEGO cores | `progear.zip` | same | `qsound.zip` |

\* Progear: Red Label, Halfway to Hell: A second-loop rework by atrac17 and terminator2k2. The MRA comes from Arcade Offset, an optional Update All database..

### CV1000

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Akai Katana * | 2010 | [GitHub](https://github.com/ika-musume/ikacore_CV1k) | `akatana.zip` | same |  |
| Deathsmiles | 2007 | [GitHub](https://github.com/ika-musume/ikacore_CV1k) | `deathsml.zip` | same |  |
| Deathsmiles MegaBlack Label | 2008 | [GitHub](https://github.com/ika-musume/ikacore_CV1k) | `dsmbl.zip` | same |  |
| DoDonPachi Dai-Fukkatsu 1.5 | 2008 | [GitHub](https://github.com/ika-musume/ikacore_CV1k) | `ddpdfk.zip` | same |  |
| DoDonPachi Dai-Fukkatsu Black Label | 2010 | [GitHub](https://github.com/ika-musume/ikacore_CV1k) | `dfkbl.zip` | same |  |
| DoDonPachi SaiDaiOuJou * | 2012 | [GitHub](https://github.com/ika-musume/ikacore_CV1k) | `ddpsdoj.zip` | same |  |
| Espgaluda II | 2005 | [GitHub](https://github.com/ika-musume/ikacore_CV1k) | `espgal2.zip` | same |  |
| Ibara | 2005 | [GitHub](https://github.com/ika-musume/ikacore_CV1k) | `ibara.zip` | same |  |
| Ibara Kuro Black Label | 2006 | [GitHub](https://github.com/ika-musume/ikacore_CV1k) | `ibarablk.zip` | same |  |
| Muchi Muchi Pork! | 2007 | [GitHub](https://github.com/ika-musume/ikacore_CV1k) | `mmpork.zip` | same |  |
| Mushihime-Sama | 2004 | [GitHub](https://github.com/ika-musume/ikacore_CV1k) | `mushisam.zip` | same |  |
| Mushihime-Sama Futari 1.5 | 2006 | [GitHub](https://github.com/ika-musume/ikacore_CV1k) | `futari15.zip` | same |  |
| Mushihime-Sama Futari Black Label | 2009 | [GitHub](https://github.com/ika-musume/ikacore_CV1k) | `futaribl.zip` | same |  |
| Pink Sweets | 2006 | [GitHub](https://github.com/ika-musume/ikacore_CV1k) | `pinkswts.zip` | same |  |

\* DoDonPachi SaiDaiOuJou: Removed from MAME after 0.238; use a 0.238 or older set. The MRA is not in the core author's releases; get it from funkycochise/CV1K_Res.
\* Akai Katana: Removed from MAME after 0.238; use a 0.238 or older set. The MRA is not in the core author's releases; get it from funkycochise/CV1K_Res.

### Darius

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Darius | 1986 | [GitHub](https://github.com/rmonic79/Arcade-Darius_MiSTer) | `darius.zip` | same |  |

### Darius II

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Darius II | 1989 | [GitHub](https://github.com/rmonic79/Arcade-Darius2NinjaWarriors_MiSTer) | `darius2.zip` | same |  |

### Data East

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Boogie Wings | 1992 | MiSTer main distribution | `boogwinga.zip` | same |  |
| Cobra-Command | 1988 | Coin-Op Collection | `cobracom.zip` | same |  |
| Double Wings | 1993 | Coin-Op Collection | `dblewingb.zip` | `dblewing.zip` |  |
| Vapor Trail | 1989 | MiSTer main distribution | `vaportra.zip` | same |  |
| Wonder Planet | 1987 | JOTEGO cores | `wndrplnt.zip` | same |  |

### Dooyong

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Blue Hawk | 1993 | [GitHub](https://github.com/searchsolved/Arcade-Dooyong_MiSTer) | `bluehawk.zip` | same |  |
| Flying Tiger | 1992 | [GitHub](https://github.com/searchsolved/Arcade-Dooyong_MiSTer) | `flytiger.zip` | same |  |
| Gulf Storm | 1991 | [GitHub](https://github.com/searchsolved/Arcade-Dooyong_MiSTer) | `gulfstrm.zip` | same |  |
| Pollux | 1991 | [GitHub](https://github.com/searchsolved/Arcade-Dooyong_MiSTer) | `pollux.zip` | same |  |
| R-Shark | 1995 | [GitHub](https://github.com/searchsolved/Arcade-Dooyong_MiSTer) | `rshark.zip` | same |  |
| Super-X | 1994 | [GitHub](https://github.com/searchsolved/Arcade-Dooyong_MiSTer) | `superx.zip` | same |  |
| The Last Day | 1990 | [GitHub](https://github.com/searchsolved/Arcade-Dooyong_MiSTer) | `lastday.zip` | same |  |

### EarthJoker

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| U.N. Defense Force: Earth Joker | 1993 | [GitHub](https://www.patreon.com/bazset/posts/u-n-defense-1993-169900198) | `earthjkr.zip` | same |  |

### Galivan

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| UFO Robo Dangar | 1986 | MiSTer main distribution | `dangar.zip` | same |  |

### Galmedes

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Galmedes | 1992 | [GitHub](https://www.patreon.com/bazset/posts/galmedes-visco-169900687) | `galmedes.zip` | same |  |

### Gigandes

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Gigandes | 1989 | [GitHub](https://github.com/bazset/Gigandes-FPGA) | `gigandes.zip` | same |  |

### Gulf War II

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Gulf War II | 1991 | MiSTer main distribution | `gulfwar2.zip` | same |  |

### Hyper Duel

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Hyper Duel | 1993 | MiSTer main distribution | `hyprduel.zip` | same |  |

### Kaneko

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Sand Scorpion | 1992 | [GitHub](https://github.com/kuzearcade/Arcade-SandScrp_MiSTer) | `sandscrp.zip` | same |  |

### Kaneko16

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Blaze On | 1992 | [GitHub](https://github.com/alphanu1/kaneko16-mister) | `blazeonj.zip` | `blazeon.zip` |  |
| Explosive Breaker | 1992 | [GitHub](https://github.com/alphanu1/kaneko16-mister) | `explbrkr.zip` | same |  |
| Wing Force | 1993 | [GitHub](https://github.com/alphanu1/kaneko16-mister) | `wingforc.zip` | same |  |

### Konami

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Ajax | 1987 | JOTEGO cores | `ajax.zip` | same |  |
| Detana!! TwinBee | 1991 | [GitHub](https://github.com/jlrh/konami-fpga) | `detatwin.zip` | `blswhstl.zip` |  |
| Fantastic Journey | 1994 | [GitHub](https://github.com/ppriest/Arcade-KonamiGX_MiSTer) | `fantjour.zip` | same | `konamigx.zip` |
| Finalizer | 1985 | MiSTer main distribution | `finalizr.zip` | same |  |
| Gradius | 1985 | MiSTer main distribution | `gradius.zip` | `nemesis.zip` |  |
| Gradius III * | 1989 | JOTEGO cores | `gradius3.zip` | same | `jtbeta.zip` |
| Lightning Fighters | 1990 | JOTEGO cores | `lgtnfght.zip` | same |  |
| MX5000 | 1987 | JOTEGO cores | `mx5000.zip` | same |  |
| Parodius Da! | 1990 | JOTEGO cores | `parodius.zip` | same |  |
| Salamander | 1986 | MiSTer main distribution | `salamand.zip` | same |  |
| Salamander 2 | 1996 | [GitHub](https://github.com/ppriest/Arcade-KonamiGX_MiSTer) | `salmndr2.zip` | same | `konamigx.zip` |
| Sexy Parodius | 1996 | [GitHub](https://github.com/ppriest/Arcade-KonamiGX_MiSTer) | `sexyparo.zip` | same | `konamigx.zip` |
| Thunder Cross | 1988 | JOTEGO cores | `thunderx.zip` | same |  |
| Thunder Cross II | 1991 | JOTEGO cores | `thndrx2.zip` | same |  |
| Twin Bee Yahhoo! | 1995 | [GitHub](https://github.com/ppriest/Arcade-KonamiGX_MiSTer) | `tbyahhoo.zip` | same | `konamigx.zip` |
| TwinBee | 1985 | MiSTer main distribution | `twinbee.zip` | same |  |
| Vulcan Venture | 1988 | JOTEGO cores | `vulcan.zip` | same |  |
| Xexex | 1991 | [GitHub](https://github.com/jlrh/konami-fpga) | `xexex.zip` | same |  |

\* Gradius III: jtbeta.zip is the JOTEGO beta key (Patreon), not a MAME file.

### Kyugo

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Airwolf | 1987 | MiSTer main distribution | `airwolf.zip` | same |  |
| Gyrodine | 1984 | MiSTer main distribution | `gyrodine.zip` | same |  |
| S.R.D. Mission | 1986 | MiSTer main distribution | `srdmissn.zip` | same |  |

### Lady Bug

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Cosmic Avenger | 1981 | MiSTer main distribution | `cavenger.zip` | same |  |

### M107

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Fire Barrel | 1993 | MiSTer main distribution | `firebarr.zip` | `airass.zip` |  |

### M62

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Horizon | 1985 | MiSTer main distribution | `horizon.zip` | same |  |
| Youjyuden | 1986 | MiSTer main distribution | `youjyudn.zip` | same |  |

### M72

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Air Duel | 1990 | MiSTer main distribution | `airduelm72.zip` | `airduel.zip` |  |
| Dragon Breed | 1989 | MiSTer main distribution | `dbreedjm72.zip` | `dbreed.zip` |  |
| Gallop | 1991 | MiSTer main distribution | `gallopm72.zip` | `cosmccop.zip` |  |
| Image Fight | 1988 | MiSTer main distribution | `imgfight.zip` | same |  |
| R-Type | 1987 | MiSTer main distribution | `rtype.zip` | same |  |
| R-Type II | 1989 | MiSTer main distribution | `rtype2.zip` | same |  |
| X Multiply | 1989 | MiSTer main distribution | `xmultiplm72.zip` | `xmultipl.zip` |  |

### M92

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| In the Hunt | 1993 | MiSTer main distribution | `inthunt.zip` | same |  |
| Lethal Thunder | 1991 | MiSTer main distribution | `lethalth.zip` | same |  |
| Mystic Riders | 1992 | MiSTer main distribution | `mysticri.zip` | same |  |
| R-Type Leo | 1992 | MiSTer main distribution | `rtypeleo.zip` | same |  |

### Mega System 1

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Chimera Beast | 1993 | [GitHub](https://github.com/kuzearcade/Arcade-JalecoMS1BCD_MiSTer) | `chimerab.zip` | same |  |
| Cybattler | 1993 | [GitHub](https://github.com/kuzearcade/Arcade-JalecoMS1BCD_MiSTer) | `cybattlr.zip` | same |  |
| E.D.F.: Earth Defense Force | 1991 | [GitHub](https://github.com/kuzearcade/Arcade-JalecoMS1BCD_MiSTer) | `edf.zip` | same |  |
| P-47: The Phantom Fighter | 1988 | Coin-Op Collection | `p47j.zip` | `p47.zip` |  |
| Plus Alpha | 1989 | Coin-Op Collection | `plusalph.zip` | same |  |
| Saint Dragon | 1989 | Coin-Op Collection | `stdragon.zip` | same |  |

### MegaSystem 32

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Desert War | 1995 | [GitHub](https://github.com/ppriest/Arcade-JalecoMS32_MiSTer) | `desertwr.zip` | same |  |
| Gratia: Second Earth | 1996 | [GitHub](https://github.com/ppriest/Arcade-JalecoMS32_MiSTer) | `gratia.zip` | same |  |
| P-47 Aces | 1995 | [GitHub](https://github.com/ppriest/Arcade-JalecoMS32_MiSTer) | `p47aces.zip` | same |  |
| The Game Paradise | 1995 | [GitHub](https://github.com/ppriest/Arcade-JalecoMS32_MiSTer) | `gametngk.zip` | same |  |

### Namco

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Blast Off | 1989 | JOTEGO cores | `blastoff.zip` | same |  |
| Dangerous Seed | 1989 | JOTEGO cores | `dangseed.zip` | same |  |
| Dragon Saber * | 1990 | [GitHub](https://github.com/kuzearcade/Arcade-NamcoSystem2_MiSTer) | `dsaber.zip` | same | `namcoc65.zip` |
| Dragon Spirit | 1987 | JOTEGO cores | `dspirit.zip` | same |  |
| Ordyne | 1988 | [GitHub](https://github.com/kuzearcade/Arcade-NamcoSystem2_MiSTer) | `ordyne.zip` | same | `namcoc65.zip` |
| Phelios * | 1988 | [GitHub](https://github.com/kuzearcade/Arcade-NamcoSystem2_MiSTer) | `phelios.zip` | same | `namcoc65.zip` |
| Pistol Daimyo no Bouken | 1990 | JOTEGO cores | `pistoldm.zip` | same |  |
| Sky Kid Deluxe | 1986 | JOTEGO cores | `skykiddx.zip` | same |  |

\* Phelios: On first launch the game stops at a warning screen; press 1P Start. Open the MiSTer menu once it is running (or use Save NVRAM) and the core keeps the setting, so it only happens once.
\* Dragon Saber: On first launch the game stops at a warning screen; press 1P Start. Open the MiSTer menu once it is running (or use Save NVRAM) and the core keeps the setting, so it only happens once.

### Namco NA-1

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Fighter & Attacker | 1992 | [GitHub](https://github.com/OngoGablogian/MiSTer_Ongo) | `fa.zip` | `fghtatck.zip` | `namcoc69.zip` |

### Namco System 11

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Xevious 3D/G | 1995 | [GitHub](https://github.com/OngoGablogian/MiSTer_Ongo) | `xevi3dg.zip` | same | `namcoc76.zip` |

### Nichibutsu

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Armed F | 1988 | Coin-Op Collection | `armedf.zip` | same |  |
| Legion | 1987 | Coin-Op Collection | `legion.zip` | same |  |
| Terra Cresta | 1985 | Coin-Op Collection | `terracre.zip` | same |  |
| Terra Force | 1987 | Coin-Op Collection | `terraf.zip` | same |  |

### NMK

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Macross Plus | 1996 | [GitHub](https://github.com/kuzearcade/Arcade-NMKBP964_MiSTer) | `macrossp.zip` | same |  |

### NMK16

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Acrobat Mission | 1991 | [GitHub](https://github.com/kuzearcade/Arcade-NMK16_MiSTer) | `acrobatm.zip` | same | `nmk004.zip` |
| Air Attack | 1996 | [GitHub](https://github.com/kuzearcade/Arcade-NMK16_MiSTer) | `airattck.zip` | same | `nmk004.zip` |
| Bio-ship Paladin | 1990 | [GitHub](https://github.com/kuzearcade/Arcade-NMK16_MiSTer) | `bioship.zip` | same | `nmk004.zip` |
| Black Heart | 1991 | [GitHub](https://github.com/kuzearcade/Arcade-NMK16_MiSTer) | `blkheart.zip` | same | `nmk004.zip` |
| Guardian Storm | 1998 | [GitHub](https://github.com/kuzearcade/Arcade-NMK16_MiSTer) | `grdnstrm.zip` | same | `nmk004.zip` |
| GunNail | 1993 | [GitHub](https://github.com/kuzearcade/Arcade-NMK16_MiSTer) | `gunnail.zip` | same | `nmk004.zip` |
| Hacha Mecha Fighter | 1991 | [GitHub](https://github.com/kuzearcade/Arcade-NMK16_MiSTer) | `hachamf.zip` | same | `nmk004.zip` |
| Koutetsu Yousai Strahl | 1992 | [GitHub](https://github.com/kuzearcade/Arcade-NMK16_MiSTer) | `strahl.zip` | same | `nmk004.zip` |
| Rapid Hero | 1994 | [GitHub](https://github.com/kuzearcade/Arcade-NMK16_MiSTer) | `raphero.zip` | `arcadian.zip` |  |
| S.S. Mission | 1992 | [GitHub](https://github.com/kuzearcade/Arcade-NMK16_MiSTer) | `ssmissin.zip` | same | `nmk004.zip` |
| Spectrum 2000 | 2000 | [GitHub](https://github.com/kuzearcade/Arcade-NMK16_MiSTer) | `spec2k.zip` | same | `nmk004.zip` |
| Stagger I | 1998 | [GitHub](https://github.com/kuzearcade/Arcade-NMK16_MiSTer) | `stagger1.zip` | same | `nmk004.zip` |
| Super Spacefortress Macross | 1992 | [GitHub](https://github.com/kuzearcade/Arcade-NMK16_MiSTer) | `macross.zip` | same | `nmk004.zip` |
| Super Spacefortress Macross II | 1993 | [GitHub](https://github.com/kuzearcade/Arcade-NMK16_MiSTer) | `macross2.zip` | same |  |
| Task Force Harrier | 1989 | [GitHub](https://github.com/kuzearcade/Arcade-NMK16_MiSTer) | `tharrier.zip` | same | `nmk004.zip` |
| Thunder Dragon | 1991 | [GitHub](https://github.com/kuzearcade/Arcade-NMK16_MiSTer) | `tdragon.zip` | same | `nmk004.zip` |
| Thunder Dragon 2 | 1993 | [GitHub](https://github.com/kuzearcade/Arcade-NMK16_MiSTer) | `tdragon2.zip` | same |  |
| Twin Action | 1995 | [GitHub](https://github.com/kuzearcade/Arcade-NMK16_MiSTer) | `twinactn.zip` | same | `nmk004.zip` |
| US AAF Mustang | 1990 | [GitHub](https://github.com/kuzearcade/Arcade-NMK16_MiSTer) | `mustang.zip` | same | `nmk004.zip` |

### PGM

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| DoDonPachi Dai-Ou-Jou | 2002 | MiSTer main distribution | `ddp3.zip` | same | `pgm.zip` |
| DoDonPachi Dai-Ou-Jou Black Label * | 2002 | MiSTer main distribution | `ddpdojblk.zip` | `ddp3.zip` | `pgm.zip` |
| DoDonPachi II | 2001 | MiSTer main distribution | `ddp2.zip` | same | `pgm.zip` |
| Espgaluda | 2003 | MiSTer main distribution | `espgal.zip` | same | `pgm.zip` |
| Ketsui | 2002 | MiSTer main distribution | `ket.zip` | same | `pgm.zip` |
| Ketsui Arrange * | 2014 | MiSTer main distribution | `ket.zip` | same | `pgm.zip` |
| Ketsui: IKD 2007 Special * | 2007 | MiSTer main distribution | `ket.zip` | same | `pgm.zip` |

\* Ketsui: IKD 2007 Special: The 2007 Cave Matsuri version. Its MRA is in the PGM core's _alternatives folder..
\* Ketsui Arrange: A fan arrange version, 1.7 first. Its MRAs are in the PGM core's _alternatives folder..
\* DoDonPachi Dai-Ou-Jou Black Label: Its MRA is in the PGM core's _alternatives folder..

### Psikyo

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Gunbird | 1994 | MiSTer main distribution | `gunbird.zip` | same |  |
| Samurai Aces | 1993 | MiSTer main distribution | `samuraia.zip` | same |  |
| Strikers 1945 | 1995 | MiSTer main distribution | `s1945.zip` | same |  |
| Tengai | 1996 | MiSTer main distribution | `tengai.zip` | same |  |

### PsikyoSH2

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Dragon Blaze | 2000 | MiSTer main distribution | `dragnblz.zip` | same |  |
| Gunbird 2 | 1998 | MiSTer main distribution | `gunbird2.zip` | same |  |
| Sol Divide | 1997 | MiSTer main distribution | `soldivid.zip` | same |  |
| Space Bomber | 1998 | MiSTer main distribution | `sbomber.zip` | same |  |
| Strikers 1945 II | 1997 | MiSTer main distribution | `s1945ii.zip` | same |  |
| Strikers 1945 III | 1999 | MiSTer main distribution | `s1945iii.zip` | same |  |

### Raiden

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Raiden | 1990 | [GitHub](https://github.com/rmonic79/Arcade-Raiden_MiSTer) | `raiden.zip` | same |  |

### Raiden2

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Raiden DX | 1994 | [GitHub](https://github.com/rmonic79/Arcade-Raiden2_MiSTer) | `raidendx.zip` | same |  |
| Raiden II | 1993 | [GitHub](https://github.com/rmonic79/Arcade-Raiden2_MiSTer) | `raiden2.zip` | same |  |

### Raizing

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Armed Police Batrider | 1998 | Coin-Op Collection | `batrider.zip` | same |  |
| Battle Bakraid | 1999 | Coin-Op Collection | `bbakraid.zip` | same |  |
| Battle Garegga | 1996 | Coin-Op Collection | `bgaregga.zip` | same |  |
| Kingdom Grandprix | 1994 | Coin-Op Collection | `kingdmgp.zip` | same |  |
| Sorcer Striker | 1993 | Coin-Op Collection | `sstriker.zip` | same |  |

### Scramble

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Scramble | 1981 | MiSTer main distribution | `scrambp.zip` | same |  |
| Super Cobra | 1981 | MiSTer main distribution | `scobra.zip` | same |  |

### Sega

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Fantasy Zone | 1986 | JOTEGO cores | `fantzone.zip` | same |  |
| Fantasy Zone II | 1987 | MiSTer main distribution | `fantzn2.zip` | same |  |
| SDI Strategic Defense Initiative | 1987 | JOTEGO cores | `sdib.zip` | `sdi.zip` |  |

### Sega System 1

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| 4-D Warriors | 1985 | MiSTer main distribution | `4dwarrio.zip` | same |  |
| Rafflesia | 1986 | MiSTer main distribution | `raflesia.zip` | same |  |
| Star Jacker | 1983 | MiSTer main distribution | `starjacks.zip` | same |  |

### Sega System 16B

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Cotton | 1991 | JOTEGO cores | `cotton.zip` | same |  |
| Sonic Boom | 1987 | JOTEGO cores | `sonicbom.zip` | same |  |

### Sega System 18

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Hammer Away | 1991 | JOTEGO cores | `hamaway.zip` | same |  |

### Sega System 24

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Scramble Spirits | 1988 | [GitHub](https://github.com/OngoGablogian/MiSTer_Ongo) | `sspirits.zip` | same |  |

### SeibuSPI

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Raiden Fighters | 1996 | [GitHub](https://github.com/zakk4223/Arcade-SeibuSPI_MiSTer) | `rdft.zip` | same |  |
| Raiden Fighters 2: Operation Hell Dive | 1997 | [GitHub](https://github.com/zakk4223/Arcade-SeibuSPI_MiSTer) | `rdft2.zip` | same |  |
| Raiden Fighters Jet | 1998 | [GitHub](https://github.com/zakk4223/Arcade-SeibuSPI_MiSTer) | `rfjet.zip` | same |  |
| Viper Phase 1 | 1995 | [GitHub](https://github.com/zakk4223/Arcade-SeibuSPI_MiSTer) | `viprp1.zip` | same |  |

### Seta

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Daioh | 1993 | [GitHub](https://github.com/ppriest/Arcade-Seta_MiSTer) | `daioh.zip` | same |  |
| Eight Forces | 1994 | [GitHub](https://github.com/ppriest/Arcade-Seta_MiSTer) | `eightfrc.zip` | same |  |
| Mad Shark | 1993 | [GitHub](https://github.com/ppriest/Arcade-Seta_MiSTer) | `madshark.zip` | same |  |
| Rezon | 1992 | [GitHub](https://github.com/ppriest/Arcade-Seta_MiSTer) | `rezon.zip` | same |  |
| SD Gundam Neo Battling | 1992 | [GitHub](https://github.com/ppriest/Arcade-Seta_MiSTer) | `neobattl.zip` | same |  |
| Strike Gunner S.T.G | 1991 | [GitHub](https://github.com/ppriest/Arcade-Seta_MiSTer) | `stg.zip` | same |  |
| War of Aero: Project MEIOU | 1993 | [GitHub](https://github.com/ppriest/Arcade-Seta_MiSTer) | `wrofaero.zip` | same |  |
| Zing Zing Zip | 1992 | [GitHub](https://github.com/ppriest/Arcade-Seta_MiSTer) | `zingzip.zip` | same |  |

### SetaDowntown

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Arbalester | 1989 | [GitHub](https://github.com/ppriest/Arcade-Seta_MiSTer) | `arbalest.zip` | same |  |
| Meta Fox | 1989 | [GitHub](https://github.com/ppriest/Arcade-Seta_MiSTer) | `metafox.zip` | same |  |
| Thundercade | 1987 | [GitHub](https://github.com/ppriest/Arcade-Seta_MiSTer) | `tndrcade.zip` | same |  |
| Twin Eagle | 1988 | [GitHub](https://github.com/ppriest/Arcade-Seta_MiSTer) | `twineagl.zip` | same |  |

### SKNS

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Cyvern: The Dragon Weapons | 1998 | [GitHub](https://github.com/srg320/Arcade-SKNS_MiSTer) | `cyvern.zip` | same | `skns.zip` |
| Sengeki Striker | 1997 | [GitHub](https://github.com/srg320/Arcade-SKNS_MiSTer) | `sengekis.zip` | same | `skns.zip` |

### Sky Smasher

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Sky Smasher | 1990 | MiSTer main distribution | `skysmash.zip` | same |  |

### SlapFight

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Alcon / Slap Fight | 1986 | MiSTer main distribution | `slapfighb1.zip` | `alcon.zip` |  |
| Tiger Heli | 1985 | MiSTer main distribution | `tigerhb1.zip` | `tigerh.zip` |  |

### SNK

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| ASO | 1985 | MiSTer main distribution | `aso.zip` | same |  |
| Prehistoric Isle in 1930 | 1989 | Coin-Op Collection | `prehisle.zip` | same |  |
| The Next Space | 1989 | Coin-Op Collection | `tnextspcj.zip` | `tnextspc.zip` |  |

### SNK 6502

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Vanguard | 1981 | MiSTer main distribution | `vanguard.zip` | same |  |

### SSV

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Change Air Blade | 1999 | MeatCores | `cairblad.zip` | same |  |
| Storm Blade | 1996 | MeatCores | `stmblade.zip` | same |  |
| Twin Eagle II | 1994 | MeatCores | `twineag2.zip` | same |  |
| Ultra X Weapons | 1995 | MeatCores | `ultrax.zip` | same |  |
| Vasara | 2000 | MeatCores | `vasara.zip` | same |  |
| Vasara 2 | 2001 | MeatCores | `vasara2.zip` | same |  |

### ST-V

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Cotton 2 | 1997 | MiSTer main distribution | `cotton2.zip` | same | `stvbios.zip` |
| Cotton Boomerang | 1998 | MiSTer main distribution | `cottonbm.zip` | same | `stvbios.zip` |
| Guardian Force | 1998 | MiSTer main distribution | `grdforce.zip` | same | `stvbios.zip` |
| Radiant Silvergun | 1998 | MiSTer main distribution | `rsgun.zip` | same | `stvbios.zip` |
| Radiant Silvergun EX * | 1998 | MiSTer main distribution | `rsgun.zip` | same | `stvbios.zip` |
| Shienryu | 1997 | MiSTer main distribution | `shienryu.zip` | same | `stvbios.zip` |
| Terra Diver | 1996 | MiSTer main distribution | `sokyugrt.zip` | same | `stvbios.zip` |

\* Radiant Silvergun EX: trap15's patched release. The MRA comes from Arcade Offset, an optional Update All database..

### Star Force

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Star Force | 1984 | MiSTer main distribution | `starforc.zip` | same |  |

### SunA

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Star Fighter | 1990 | [GitHub](https://github.com/OngoGablogian/MiSTer_Ongo) | `starfigh.zip` | same |  |

### System C2

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Thunder Force AC | 1990 | [GitHub](https://github.com/Mezzow/Arcade-SystemC2_MiSTer) | `tfrceacj.zip` | `tfrceac.zip` |  |

### Taito

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Chuka Taisen | 1988 | JOTEGO cores | `chukatai.zip` | same |  |
| Extermination | 1987 | JOTEGO cores | `extrmatn.zip` | same |  |
| Tokio | 1986 | JOTEGO cores | `tokio.zip` | same |  |

### Taito B

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Ashura Blaster | 1990 | [GitHub](https://github.com/Mezzow/Arcade-TaitoB_MiSTer) | `ashuraj.zip` | `ashura.zip` |  |
| Master of Weapon | 1989 | [GitHub](https://github.com/Mezzow/Arcade-TaitoB_MiSTer) | `masterwj.zip` | `masterw.zip` |  |
| Ryu Jin | 1993 | [GitHub](https://github.com/Mezzow/Arcade-TaitoB_MiSTer) | `ryujina.zip` | `ryujin.zip` |  |

### Taito F2

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Gun & Frontier | 1990 | MiSTer main distribution | `gunfront.zip` | same |  |
| Mega Blast | 1989 | MiSTer main distribution | `megablst.zip` | same |  |
| Metal Black | 1991 | MiSTer main distribution | `metalb.zip` | same |  |

### Taito F3

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Darius Gaiden | 1994 | [GitHub](https://github.com/spacestate1/Arcade-taitoF3_MiSTer) | `dariusg.zip` | same |  |
| Gekirindan | 1995 | [GitHub](https://github.com/spacestate1/Arcade-taitoF3_MiSTer) | `gekiridn.zip` | same |  |
| Grid Seeker: Project Storm Hammer | 1992 | [GitHub](https://github.com/spacestate1/Arcade-taitoF3_MiSTer) | `gseeker.zip` | same |  |
| RayForce | 1993 | [GitHub](https://github.com/spacestate1/Arcade-taitoF3_MiSTer) | `gunlock.zip` | same |  |
| Twin Cobra II | 1995 | [GitHub](https://github.com/spacestate1/Arcade-taitoF3_MiSTer) | `tcobra2.zip` | same |  |

### Taito FX-1B

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| G-Darius | 1997 | [GitHub](https://github.com/XelaNotPu/ZN1-TaitoFX1B_MiSTer) | `gdarius.zip` | `gdarius2.zip` | `coh1000t.zip` |
| RayStorm * | 1996 | [GitHub](https://github.com/XelaNotPu/ZN1-TaitoFX1B_MiSTer) | `raystorm.zip` | same | `coh1000t.zip` |

\* RayStorm: On first launch the game opens its test menu; choose FACTORY SETTING, then EXIT. The core saves this, so it only happens once.

### Tecmo

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Back Fire | 1988 | MiSTer main distribution | `backfirt.zip` | same |  |
| Gemini Wing | 1987 | MiSTer main distribution | `gemini.zip` | same |  |
| Raiga Strato Fighter | 1991 | JOTEGO cores | `stratof.zip` | same |  |
| Silkworm | 1988 | MiSTer main distribution | `silkworm.zip` | same |  |

### TimePilot84

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Time Pilot '84 | 1984 | MiSTer main distribution | `tp84.zip` | same |  |

### Toaplan

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Batsugun | 1993 | [GitHub](https://github.com/TheJesusFish/Slop-Core) | `batsugun.zip` | same |  |
| Batsugun Special Version | 1994 | [GitHub](https://github.com/TheJesusFish/Slop-Core) | `batsugunsp.zip` | `batsugun.zip` |  |
| Dogyuun | 1992 | [GitHub](https://github.com/TheJesusFish/Slop-Core) | `dogyuun.zip` | same |  |
| Dr. Toppel's Adventure | 1987 | JOTEGO cores | `drtoppel.zip` | same |  |
| Fire Shark | 1989 | Coin-Op Collection | `fireshrk.zip` | same |  |
| FixEight | 1992 | [GitHub](https://github.com/TheJesusFish/Slop-Core) | `fixeightt.zip` | `fixeight.zip` |  |
| Flying Shark | 1987 | Coin-Op Collection | `fshark.zip` | same |  |
| Grind Stormer | 1992 | [GitHub](https://github.com/TheJesusFish/Slop-Core) | `grindstm.zip` | same |  |
| Hellfire | 1989 | Coin-Op Collection | `hellfire.zip` | same |  |
| Insector X | 1989 | JOTEGO cores | `insectx.zip` | same |  |
| Out Zone | 1990 | Coin-Op Collection | `outzone.zip` | same |  |
| Truxton | 1988 | Coin-Op Collection | `truxton.zip` | same |  |
| Truxton II | 1992 | Coin-Op Collection | `truxton2.zip` | same |  |
| Twin Cobra | 1987 | Coin-Op Collection | `twincobr.zip` | same |  |
| Vimana | 1991 | Coin-Op Collection | `vimana.zip` | same |  |
| Zero Wing | 1989 | Coin-Op Collection | `zerowing.zip` | same |  |

### TwinHawk

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Twin Hawk | 1989 | [GitHub](https://github.com/bazset/Twin-Hawk-FPGA) | `twinhawk.zip` | same |  |

### UPL

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Omega Fighter | 1989 | MiSTer main distribution | `omegaf.zip` | same |  |

### Vastar

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Vastar | 1983 | MiSTer main distribution | `vastar.zip` | same |  |

### Video System

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Aero Fighters | 1992 | [GitHub](https://github.com/OngoGablogian/MiSTer_Ongo) | `aerofgtb.zip` | `aerofgt.zip` |  |
| Turbo Force | 1991 | [GitHub](https://github.com/OngoGablogian/MiSTer_Ongo) | `turbofrc.zip` | same |  |

### Xevious

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Super Xevious | 1984 | MiSTer main distribution | `sxevious.zip` | `xevious.zip` | `namco50.zip`, `namco51.zip`, `namco54.zip` |
| Xevious | 1982 | MiSTer main distribution | `xevious.zip` | same | `namco50.zip`, `namco51.zip`, `namco54.zip` |

### Zaxxon

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Future Spy | 1984 | MiSTer main distribution | `futspy.zip` | same |  |
| Super Zaxxon | 1982 | MiSTer main distribution | `szaxxon.zip` | same |  |
| Zaxxon | 1982 | MiSTer main distribution | `zaxxon.zip` | same |  |

### ZN-1

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Aero Fighters Special | 1996 | [GitHub](https://github.com/OngoGablogian/MiSTer_Ongo) | `aerofgts.zip` | same | `coh1002v.zip` |
| Brave Blade | 2000 | [GitHub](https://github.com/OngoGablogian/MiSTer_Ongo) | `brvblade.zip` | same | `coh1002m.zip` |

## Neo Geo games

Neo Geo games run on the Neo Geo core from the MiSTer main distribution and go in `games/NeoGeo`, on the SD card or a USB drive. Subfolders are fine. The Neo Geo core also needs its BIOS files in that folder; see the core's own documentation.

| Game | Year | Setname | Accepted files |
| --- | --- | --- | --- |
| Aero Fighters 2 | 1994 | `sonicwi2` | `sonicwi2.neo`, `Title (sonicwi2).neo`, or a `sonicwi2` Darksoft or MAME zip or folder |
| Aero Fighters 3 | 1995 | `sonicwi3` | `sonicwi3.neo`, `Title (sonicwi3).neo`, or a `sonicwi3` Darksoft or MAME zip or folder |
| Alpha Mission II | 1991 | `alpham2` | `alpham2.neo`, `Title (alpham2).neo`, or a `alpham2` Darksoft or MAME zip or folder |
| Andro Dunos | 1992 | `androdun` | `androdun.neo`, `Title (androdun).neo`, or a `androdun` Darksoft or MAME zip or folder |
| Blazing Star | 1998 | `blazstar` | `blazstar.neo`, `Title (blazstar).neo`, or a `blazstar` Darksoft or MAME zip or folder |
| Captain Tomaday | 1999 | `ctomaday` | `ctomaday.neo`, `Title (ctomaday).neo`, or a `ctomaday` Darksoft or MAME zip or folder |
| Ghost Pilots | 1991 | `gpilots` | `gpilots.neo`, `Title (gpilots).neo`, or a `gpilots` Darksoft or MAME zip or folder |
| Last Resort | 1992 | `lresort` | `lresort.neo`, `Title (lresort).neo`, or a `lresort` Darksoft or MAME zip or folder |
| Prehistoric Isle 2 | 1999 | `preisle2` | `preisle2.neo`, `Title (preisle2).neo`, or a `preisle2` Darksoft or MAME zip or folder |
| Pulstar | 1995 | `pulstar` | `pulstar.neo`, `Title (pulstar).neo`, or a `pulstar` Darksoft or MAME zip or folder |
| Strikers 1945 Plus | 1999 | `s1945p` | `s1945p.neo`, `Title (s1945p).neo`, or a `s1945p` Darksoft or MAME zip or folder |
| Twinkle Star Sprites | 1996 | `twinspri` | `twinspri.neo`, `Title (twinspri).neo`, or a `twinspri` Darksoft or MAME zip or folder |
| Viewpoint | 1992 | `viewpoin` | `viewpoin.neo`, `Title (viewpoin).neo`, or a `viewpoin` Darksoft or MAME zip or folder |
| Zed Blade | 1994 | `zedblade` | `zedblade.neo`, `Title (zedblade).neo`, or a `zedblade` Darksoft or MAME zip or folder |

## All arcade zip names

One per line, for filtering a download. Non-merged or split set:

```
1941.zip
1942.zip
1943.zip
1943kai.zip
1944.zip
19xx.zip
4dwarrio.zip
acrobatm.zip
aerofgtb.zip
aerofgts.zip
agallet.zip
airattck.zip
airduelm72.zip
airwolf.zip
ajax.zip
akatana.zip
aleck64.zip
arbalest.zip
armedf.zip
ashuraj.zip
aso.zip
asuka.zip
backfirt.zip
batrider.zip
batsugun.zip
batsugunsp.zip
bbakraid.zip
bgaregga.zip
bioship.zip
blastoff.zip
blazeonj.zip
blkheart.zip
bluehawk.zip
boogwinga.zip
brvblade.zip
cairblad.zip
cavenger.zip
cawing.zip
chimerab.zip
chukatai.zip
cobracom.zip
coh1000t.zip
coh1002m.zip
coh1002v.zip
cotton.zip
cotton2.zip
cottonbm.zip
cybattlr.zip
cyvern.zip
daioh.zip
dangar.zip
dangseed.zip
darius.zip
darius2.zip
dariusg.zip
dblewingb.zip
dbreedjm72.zip
ddonpach.zip
ddp2.zip
ddp3.zip
ddpdfk.zip
ddpdojblk.zip
ddpsdoj.zip
deathsml.zip
desertwr.zip
detatwin.zip
dfeveron.zip
dfkbl.zip
dimahoo.zip
dogyuun.zip
donpachi.zip
dragnblz.zip
drtoppel.zip
dsaber.zip
dsmbl.zip
dspirit.zip
earthjkr.zip
ecofghtr.zip
edf.zip
eightfrc.zip
espgal.zip
espgal2.zip
esprade.zip
exedexes.zip
explbrkr.zip
extrmatn.zip
fa.zip
fantjour.zip
fantzn2.zip
fantzone.zip
finalizr.zip
firebarr.zip
fireshrk.zip
fixeightt.zip
flytiger.zip
forgottn.zip
fshark.zip
futari15.zip
futaribl.zip
futspy.zip
gallopm72.zip
galmedes.zip
gametngk.zip
gdarius.zip
gekiridn.zip
gemini.zip
gigandes.zip
gigawing.zip
gradius.zip
gradius3.zip
gratia.zip
grdforce.zip
grdnstrm.zip
grindstm.zip
gseeker.zip
gulfstrm.zip
gulfwar2.zip
gunbird.zip
gunbird2.zip
gunfront.zip
gunlock.zip
gunnail.zip
gunsmoke.zip
guwange.zip
gyrodine.zip
hachamf.zip
hamaway.zip
hellfire.zip
horizon.zip
hotdogst.zip
hyprduel.zip
ibara.zip
ibarablk.zip
imgfight.zip
insectx.zip
inthunt.zip
ket.zip
kingdmgp.zip
konamigx.zip
lastday.zip
lastduel.zip
legion.zip
lethalth.zip
lgtnfght.zip
lwings.zip
macross.zip
macross2.zip
macrossp.zip
madshark.zip
masterwj.zip
mazinger.zip
megablst.zip
metafox.zip
metalb.zip
mmatrix.zip
mmpork.zip
mushisam.zip
mustang.zip
mx5000.zip
mysticri.zip
namco50.zip
namco51.zip
namco54.zip
namcoc65.zip
namcoc69.zip
namcoc76.zip
neobattl.zip
nmk004.zip
omegaf.zip
ordyne.zip
outzone.zip
p47aces.zip
p47j.zip
parodius.zip
pgm.zip
phelios.zip
pinkswts.zip
pistoldm.zip
plusalph.zip
pollux.zip
prehisle.zip
progear.zip
qsound.zip
raflesia.zip
raiden.zip
raiden2.zip
raidendx.zip
raphero.zip
raystorm.zip
rdft.zip
rdft2.zip
rezon.zip
rfjet.zip
rsgun.zip
rshark.zip
rtype.zip
rtype2.zip
rtypeleo.zip
ryujina.zip
s1945.zip
s1945ii.zip
s1945iii.zip
salamand.zip
salmndr2.zip
samuraia.zip
sandscrp.zip
sbomber.zip
scobra.zip
scrambp.zip
sdib.zip
sectionz.zip
sengekis.zip
sexyparo.zip
shienryu.zip
sidearms.zip
silkworm.zip
skns.zip
skyadvnt.zip
skykiddx.zip
skysmash.zip
skysoldr.zip
slapfighb1.zip
sokyugrt.zip
soldivid.zip
sonicbom.zip
spec2k.zip
srdmissn.zip
ssmissin.zip
sspirits.zip
sstriker.zip
stagger1.zip
starfigh.zip
starforc.zip
starjacks.zip
starsldr.zip
stdragon.zip
stg.zip
stmblade.zip
strahl.zip
stratof.zip
stvbios.zip
superx.zip
sxevious.zip
szaxxon.zip
tbyahhoo.zip
tcobra2.zip
tdragon.zip
tdragon2.zip
tengai.zip
terracre.zip
terraf.zip
tfrceacj.zip
tharrier.zip
thndrx2.zip
thunderx.zip
tigerhb1.zip
tndrcade.zip
tnextspcj.zip
tokio.zip
tp84.zip
truxton.zip
truxton2.zip
turbofrc.zip
twinactn.zip
twinbee.zip
twincobr.zip
twineag2.zip
twineagl.zip
twinhawk.zip
ultrax.zip
unsquad.zip
vanguard.zip
vaportra.zip
varth.zip
vasara.zip
vasara2.zip
vastar.zip
vimana.zip
viprp1.zip
vulcan.zip
vulgus.zip
wingforc.zip
wndrplnt.zip
wrofaero.zip
xevi3dg.zip
xevious.zip
xexex.zip
xmultiplm72.zip
youjyudn.zip
zaxxon.zip
zerowing.zip
zingzip.zip
```

Merged set:

```
1941.zip
1942.zip
1943.zip
1943kai.zip
1944.zip
19xx.zip
4dwarrio.zip
acrobatm.zip
aerofgt.zip
aerofgts.zip
agallet.zip
airass.zip
airattck.zip
airduel.zip
airwolf.zip
ajax.zip
akatana.zip
alcon.zip
aleck64.zip
arbalest.zip
arcadian.zip
armedf.zip
ashura.zip
aso.zip
asuka.zip
backfirt.zip
batrider.zip
batsugun.zip
bbakraid.zip
bgaregga.zip
bioship.zip
blastoff.zip
blazeon.zip
blkheart.zip
blswhstl.zip
bluehawk.zip
boogwinga.zip
brvblade.zip
cairblad.zip
cavenger.zip
cawing.zip
chimerab.zip
chukatai.zip
cobracom.zip
coh1000t.zip
coh1002m.zip
coh1002v.zip
cosmccop.zip
cotton.zip
cotton2.zip
cottonbm.zip
cybattlr.zip
cyvern.zip
daioh.zip
dangar.zip
dangseed.zip
darius.zip
darius2.zip
dariusg.zip
dblewing.zip
dbreed.zip
ddonpach.zip
ddp2.zip
ddp3.zip
ddpdfk.zip
ddpsdoj.zip
deathsml.zip
desertwr.zip
dfkbl.zip
dimahoo.zip
dogyuun.zip
donpachi.zip
dragnblz.zip
drtoppel.zip
dsaber.zip
dsmbl.zip
dspirit.zip
earthjkr.zip
ecofghtr.zip
edf.zip
eightfrc.zip
espgal.zip
espgal2.zip
esprade.zip
exedexes.zip
explbrkr.zip
extrmatn.zip
fantjour.zip
fantzn2.zip
fantzone.zip
feversos.zip
fghtatck.zip
finalizr.zip
fireshrk.zip
fixeight.zip
flytiger.zip
forgottn.zip
fshark.zip
futari15.zip
futaribl.zip
futspy.zip
galmedes.zip
gametngk.zip
gdarius2.zip
gekiridn.zip
gemini.zip
gigandes.zip
gigawing.zip
gradius3.zip
gratia.zip
grdforce.zip
grdnstrm.zip
grindstm.zip
gseeker.zip
gulfstrm.zip
gulfwar2.zip
gunbird.zip
gunbird2.zip
gunfront.zip
gunlock.zip
gunnail.zip
gunsmoke.zip
guwange.zip
gyrodine.zip
hachamf.zip
hamaway.zip
hellfire.zip
horizon.zip
hotdogst.zip
hyprduel.zip
ibara.zip
ibarablk.zip
imgfight.zip
insectx.zip
inthunt.zip
ket.zip
kingdmgp.zip
konamigx.zip
lastday.zip
lastduel.zip
legion.zip
lethalth.zip
lgtnfght.zip
lwings.zip
macross.zip
macross2.zip
macrossp.zip
madshark.zip
masterw.zip
mazinger.zip
megablst.zip
metafox.zip
metalb.zip
mmatrix.zip
mmpork.zip
mushisam.zip
mustang.zip
mx5000.zip
mysticri.zip
namco50.zip
namco51.zip
namco54.zip
namcoc65.zip
namcoc69.zip
namcoc76.zip
nemesis.zip
neobattl.zip
nmk004.zip
omegaf.zip
ordyne.zip
outzone.zip
p47.zip
p47aces.zip
parodius.zip
pgm.zip
phelios.zip
pinkswts.zip
pistoldm.zip
plusalph.zip
pollux.zip
prehisle.zip
progear.zip
qsound.zip
raflesia.zip
raiden.zip
raiden2.zip
raidendx.zip
raystorm.zip
rdft.zip
rdft2.zip
rezon.zip
rfjet.zip
rsgun.zip
rshark.zip
rtype.zip
rtype2.zip
rtypeleo.zip
ryujin.zip
s1945.zip
s1945ii.zip
s1945iii.zip
salamand.zip
salmndr2.zip
samuraia.zip
sandscrp.zip
sbomber.zip
scobra.zip
scrambp.zip
sdi.zip
sectionz.zip
sengekis.zip
sexyparo.zip
shienryu.zip
sidearms.zip
silkworm.zip
skns.zip
skyadvnt.zip
skykiddx.zip
skysmash.zip
skysoldr.zip
sokyugrt.zip
soldivid.zip
sonicbom.zip
spec2k.zip
srdmissn.zip
ssmissin.zip
sspirits.zip
sstriker.zip
stagger1.zip
starfigh.zip
starforc.zip
starjacks.zip
starsldr.zip
stdragon.zip
stg.zip
stmblade.zip
strahl.zip
stratof.zip
stvbios.zip
superx.zip
szaxxon.zip
tbyahhoo.zip
tcobra2.zip
tdragon.zip
tdragon2.zip
tengai.zip
terracre.zip
terraf.zip
tfrceac.zip
tharrier.zip
thndrx2.zip
thunderx.zip
tigerh.zip
tndrcade.zip
tnextspc.zip
tokio.zip
tp84.zip
truxton.zip
truxton2.zip
turbofrc.zip
twinactn.zip
twinbee.zip
twincobr.zip
twineag2.zip
twineagl.zip
twinhawk.zip
ultrax.zip
unsquad.zip
vanguard.zip
vaportra.zip
varth.zip
vasara.zip
vasara2.zip
vastar.zip
vimana.zip
viprp1.zip
vulcan.zip
vulgus.zip
wingforc.zip
wndrplnt.zip
wrofaero.zip
xevi3dg.zip
xevious.zip
xexex.zip
xmultipl.zip
youjyudn.zip
zaxxon.zip
zerowing.zip
zingzip.zip
```
