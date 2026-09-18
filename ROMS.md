# Supported games and ROMs

Shmup Deck supports 178 games: 165 arcade games that run from MRA files and 13 Neo Geo games. This page lists the core and ROM files each one needs.

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
| CV1000 | 14 | [ika-musume/ikacore_CV1k](https://github.com/ika-musume/ikacore_CV1k) | The repository has no core build or MRAs; builds come from the developer. MRAs for all games, including DoDonPachi SaiDaiOuJou and Akai Katana, are in [funkycochise/CV1K_Res](https://github.com/funkycochise/CV1K_Res) |
| MegaSystem 32 | 4 | [ppriest/Arcade-JalecoMS32_MiSTer](https://github.com/ppriest/Arcade-JalecoMS32_MiSTer) |  |
| NMK16 | 19 | [kuzearcade/Arcade-NMK16_MiSTer](https://github.com/kuzearcade/Arcade-NMK16_MiSTer) |  |
| Seta | 8 | [ppriest/Arcade-Seta_MiSTer](https://github.com/ppriest/Arcade-Seta_MiSTer) |  |
| Taito F3 | 5 | [spacestate1/Arcade-taitoF3_MiSTer](https://github.com/spacestate1/Arcade-taitoF3_MiSTer) |  |
| Taito FX-1B | 2 | [XelaNotPu/ZN1-TaitoFX1B_MiSTer](https://github.com/XelaNotPu/ZN1-TaitoFX1B_MiSTer) |  |
| Toaplan | 2 | [TheJesusFish/Arcade-Batsugun_MiSTer](https://github.com/TheJesusFish/Arcade-Batsugun_MiSTer) | The repository has MRAs but no core build |

## Arcade games

### Capcom

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| 1942 | 1984 | JOTEGO cores | `1942.zip` | same |  |
| 1943 | 1987 | JOTEGO cores | `1943.zip` | same |  |
| Exed Exes | 1985 | JOTEGO cores | `exedexes.zip` | same |  |
| Legendary Wings | 1986 | JOTEGO cores | `lwings.zip` | same |  |
| Section Z | 1985 | JOTEGO cores | `sectionz.zip` | same |  |
| Side Arms | 1986 | JOTEGO cores | `sidearms.zip` | same |  |
| Vulgus | 1984 | JOTEGO cores | `vulgus.zip` | same |  |

### Cave

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Dangun Feveron | 1998 | MiSTer main distribution | `dfeveron.zip` | `feversos.zip` |  |
| DoDonPachi | 1997 | MiSTer main distribution | `ddonpach.zip` | same |  |
| DonPachi | 1995 | MiSTer main distribution | `donpachi.zip` | same |  |
| ESP Ra.De. | 1998 | MiSTer main distribution | `esprade.zip` | same |  |
| Guwange | 1999 | MiSTer main distribution | `guwange.zip` | same |  |
| Hotdog Storm | 1996 | MiSTer main distribution | `hotdogst.zip` | same |  |

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

### Data East

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Cobra-Command | 1988 | Coin-Op Collection | `cobracom.zip` | same |  |

### Gyruss

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Gyruss | 1983 | MiSTer main distribution | `gyruss.zip` | same |  |

### Konami

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Ajax | 1987 | JOTEGO cores | `ajax.zip` | same |  |
| Finalizer | 1985 | MiSTer main distribution | `finalizr.zip` | same |  |
| Gradius | 1985 | MiSTer main distribution | `gradius.zip` | `nemesis.zip` |  |
| Gradius III * | 1989 | JOTEGO cores | `gradius3.zip` | same | `jtbeta.zip` |
| MX5000 | 1987 | JOTEGO cores | `mx5000.zip` | same |  |
| Parodius Da! | 1990 | JOTEGO cores | `parodius.zip` | same |  |
| Salamander | 1986 | MiSTer main distribution | `salamand.zip` | same |  |
| Thunder Cross | 1988 | JOTEGO cores | `thunderx.zip` | same |  |
| TwinBee | 1985 | MiSTer main distribution | `twinbee.zip` | same |  |
| Vulcan Venture | 1988 | JOTEGO cores | `vulcan.zip` | same |  |

\* Gradius III: jtbeta.zip is the JOTEGO beta key (Patreon), not a MAME file.

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
| Dragon Spirit | 1987 | JOTEGO cores | `dspirit.zip` | same |  |

### Nichibutsu

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Armed F | 1988 | Coin-Op Collection | `armedf.zip` | same |  |
| Legion | 1987 | Coin-Op Collection | `legion.zip` | same |  |
| Terra Cresta | 1985 | Coin-Op Collection | `terracre.zip` | same |  |
| Terra Force | 1987 | Coin-Op Collection | `terraf.zip` | same |  |

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
| DoDonPachi II | 2001 | MiSTer main distribution | `ddp2.zip` | same | `pgm.zip` |
| Espgaluda | 2003 | MiSTer main distribution | `espgal.zip` | same | `pgm.zip` |
| Ketsui | 2002 | MiSTer main distribution | `ket.zip` | same | `pgm.zip` |

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
| Space Bomber | 1998 | MiSTer main distribution | `sbomber.zip` | same |  |
| Strikers 1945 II | 1997 | MiSTer main distribution | `s1945ii.zip` | same |  |
| Strikers 1945 III | 1999 | MiSTer main distribution | `s1945iii.zip` | same |  |

### Raizing

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Armed Police Batrider | 1998 | Coin-Op Collection | `batrider.zip` | same |  |
| Battle Bakraid | 1999 | Coin-Op Collection | `bbakraid.zip` | same |  |
| Battle Garegga | 1996 | Coin-Op Collection | `bgaregga.zip` | same |  |
| Kingdom Grandprix | 1994 | Coin-Op Collection | `kingdmgp.zip` | same |  |
| Sorcer Striker | 1993 | Coin-Op Collection | `sstriker.zip` | same |  |

### Sega

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Fantasy Zone | 1986 | JOTEGO cores | `fantzone.zip` | same |  |
| Fantasy Zone II | 1987 | MiSTer main distribution | `fantzn2.zip` | same |  |
| SDI Strategic Defense Initiative | 1987 | JOTEGO cores | `sdib.zip` | `sdi.zip` |  |

### Sega System 1

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Rafflesia | 1986 | MiSTer main distribution | `raflesia.zip` | same |  |

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

### SlapFight

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Alcon / Slap Fight | 1986 | MiSTer main distribution | `slapfighb1.zip` | `alcon.zip` |  |
| Tiger Heli | 1985 | MiSTer main distribution | `tigerhb1.zip` | `tigerh.zip` |  |

### SNK

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| ASO | 1985 | MiSTer main distribution | `aso.zip` | same |  |

### SSV

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
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
| Shienryu | 1997 | MiSTer main distribution | `shienryu.zip` | same | `stvbios.zip` |
| Terra Diver | 1996 | MiSTer main distribution | `sokyugrt.zip` | same | `stvbios.zip` |

### Taito

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Extermination | 1987 | JOTEGO cores | `extrmatn.zip` | same |  |
| Tokio | 1986 | JOTEGO cores | `tokio.zip` | same |  |

### Taito F2

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
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
| Batsugun | 1993 | [GitHub](https://github.com/TheJesusFish/Arcade-Batsugun_MiSTer) | `batsugun.zip` | same |  |
| Batsugun Special Version | 1994 | [GitHub](https://github.com/TheJesusFish/Arcade-Batsugun_MiSTer) | `batsugunsp.zip` | `batsugun.zip` |  |
| Dr. Toppel's Adventure | 1987 | JOTEGO cores | `drtoppel.zip` | same |  |
| Fire Shark | 1989 | Coin-Op Collection | `fireshrk.zip` | same |  |
| Flying Shark | 1987 | Coin-Op Collection | `fshark.zip` | same |  |
| Hellfire | 1989 | Coin-Op Collection | `hellfire.zip` | same |  |
| Insector X | 1989 | JOTEGO cores | `insectx.zip` | same |  |
| Out Zone | 1990 | Coin-Op Collection | `outzone.zip` | same |  |
| Truxton | 1988 | Coin-Op Collection | `truxton.zip` | same |  |
| Truxton II | 1992 | Coin-Op Collection | `truxton2.zip` | same |  |
| Twin Cobra | 1987 | Coin-Op Collection | `twincobr.zip` | same |  |
| Vimana | 1991 | Coin-Op Collection | `vimana.zip` | same |  |
| Zero Wing | 1989 | Coin-Op Collection | `zerowing.zip` | same |  |

### Xevious

| Game | Year | Core source | Zip | Merged set zip | Also needs |
| --- | --- | --- | --- | --- | --- |
| Xevious | 1982 | MiSTer main distribution | `xevious.zip` | same | `namco50.zip`, `namco51.zip`, `namco54.zip` |

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
| Viewpoint | 1992 | `viewpoin` | `viewpoin.neo`, `Title (viewpoin).neo`, or a `viewpoin` Darksoft or MAME zip or folder |
| Zed Blade | 1994 | `zedblade` | `zedblade.neo`, `Title (zedblade).neo`, or a `zedblade` Darksoft or MAME zip or folder |

## All arcade zip names

One per line, for filtering a download. Non-merged or split set:

```
1941.zip
1942.zip
1943.zip
1944.zip
19xx.zip
acrobatm.zip
airattck.zip
airduelm72.zip
ajax.zip
akatana.zip
armedf.zip
aso.zip
batrider.zip
batsugun.zip
batsugunsp.zip
bbakraid.zip
bgaregga.zip
bioship.zip
blkheart.zip
cawing.zip
cobracom.zip
coh1000t.zip
cotton2.zip
cottonbm.zip
daioh.zip
dariusg.zip
dbreedjm72.zip
ddonpach.zip
ddp2.zip
ddp3.zip
ddpdfk.zip
ddpsdoj.zip
deathsml.zip
desertwr.zip
dfeveron.zip
dfkbl.zip
dimahoo.zip
donpachi.zip
dragnblz.zip
drtoppel.zip
dsmbl.zip
dspirit.zip
ecofghtr.zip
eightfrc.zip
espgal.zip
espgal2.zip
esprade.zip
exedexes.zip
extrmatn.zip
fantzn2.zip
fantzone.zip
finalizr.zip
firebarr.zip
fireshrk.zip
forgottn.zip
fshark.zip
futari15.zip
futaribl.zip
gallopm72.zip
gametngk.zip
gdarius.zip
gekiridn.zip
gemini.zip
gigawing.zip
gradius.zip
gradius3.zip
gratia.zip
grdforce.zip
grdnstrm.zip
gseeker.zip
gunbird.zip
gunbird2.zip
gunlock.zip
gunnail.zip
guwange.zip
gyruss.zip
hachamf.zip
hellfire.zip
horizon.zip
hotdogst.zip
ibara.zip
ibarablk.zip
imgfight.zip
insectx.zip
inthunt.zip
ket.zip
kingdmgp.zip
legion.zip
lethalth.zip
lwings.zip
macross.zip
macross2.zip
madshark.zip
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
neobattl.zip
nmk004.zip
outzone.zip
p47aces.zip
parodius.zip
pgm.zip
pinkswts.zip
progear.zip
qsound.zip
raflesia.zip
raphero.zip
raystorm.zip
rezon.zip
rsgun.zip
rtype.zip
rtype2.zip
rtypeleo.zip
s1945.zip
s1945ii.zip
s1945iii.zip
salamand.zip
samuraia.zip
sbomber.zip
sdib.zip
sectionz.zip
shienryu.zip
sidearms.zip
silkworm.zip
slapfighb1.zip
sokyugrt.zip
spec2k.zip
ssmissin.zip
sstriker.zip
stagger1.zip
stg.zip
stmblade.zip
strahl.zip
stratof.zip
stvbios.zip
tcobra2.zip
tdragon.zip
tdragon2.zip
tengai.zip
terracre.zip
terraf.zip
tharrier.zip
thunderx.zip
tigerhb1.zip
tokio.zip
tp84.zip
truxton.zip
truxton2.zip
twinactn.zip
twinbee.zip
twincobr.zip
twineag2.zip
ultrax.zip
unsquad.zip
varth.zip
vasara.zip
vasara2.zip
vimana.zip
vulcan.zip
vulgus.zip
wrofaero.zip
xevious.zip
xmultiplm72.zip
youjyudn.zip
zerowing.zip
zingzip.zip
```

Merged set:

```
1941.zip
1942.zip
1943.zip
1944.zip
19xx.zip
acrobatm.zip
airass.zip
airattck.zip
airduel.zip
ajax.zip
akatana.zip
alcon.zip
arcadian.zip
armedf.zip
aso.zip
batrider.zip
batsugun.zip
bbakraid.zip
bgaregga.zip
bioship.zip
blkheart.zip
cawing.zip
cobracom.zip
coh1000t.zip
cosmccop.zip
cotton2.zip
cottonbm.zip
daioh.zip
dariusg.zip
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
donpachi.zip
dragnblz.zip
drtoppel.zip
dsmbl.zip
dspirit.zip
ecofghtr.zip
eightfrc.zip
espgal.zip
espgal2.zip
esprade.zip
exedexes.zip
extrmatn.zip
fantzn2.zip
fantzone.zip
feversos.zip
finalizr.zip
fireshrk.zip
forgottn.zip
fshark.zip
futari15.zip
futaribl.zip
gametngk.zip
gdarius2.zip
gekiridn.zip
gemini.zip
gigawing.zip
gradius3.zip
gratia.zip
grdforce.zip
grdnstrm.zip
gseeker.zip
gunbird.zip
gunbird2.zip
gunlock.zip
gunnail.zip
guwange.zip
gyruss.zip
hachamf.zip
hellfire.zip
horizon.zip
hotdogst.zip
ibara.zip
ibarablk.zip
imgfight.zip
insectx.zip
inthunt.zip
ket.zip
kingdmgp.zip
legion.zip
lethalth.zip
lwings.zip
macross.zip
macross2.zip
madshark.zip
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
nemesis.zip
neobattl.zip
nmk004.zip
outzone.zip
p47aces.zip
parodius.zip
pgm.zip
pinkswts.zip
progear.zip
qsound.zip
raflesia.zip
raystorm.zip
rezon.zip
rsgun.zip
rtype.zip
rtype2.zip
rtypeleo.zip
s1945.zip
s1945ii.zip
s1945iii.zip
salamand.zip
samuraia.zip
sbomber.zip
sdi.zip
sectionz.zip
shienryu.zip
sidearms.zip
silkworm.zip
sokyugrt.zip
spec2k.zip
ssmissin.zip
sstriker.zip
stagger1.zip
stg.zip
stmblade.zip
strahl.zip
stratof.zip
stvbios.zip
tcobra2.zip
tdragon.zip
tdragon2.zip
tengai.zip
terracre.zip
terraf.zip
tharrier.zip
thunderx.zip
tigerh.zip
tokio.zip
tp84.zip
truxton.zip
truxton2.zip
twinactn.zip
twinbee.zip
twincobr.zip
twineag2.zip
ultrax.zip
unsquad.zip
varth.zip
vasara.zip
vasara2.zip
vimana.zip
vulcan.zip
vulgus.zip
wrofaero.zip
xevious.zip
xmultipl.zip
youjyudn.zip
zerowing.zip
zingzip.zip
```
