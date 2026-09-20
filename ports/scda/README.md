# Splinter Cell: Double Agent ports

The eight versus maps from Splinter Cell: Double Agent (PC), converted for Enhanced SCCT Versus 3.6. Each one is self-contained: a playable map, an editable map for the [Reloaded Editor](https://github.com/Lumbridge/SCCT_Versus_Reloaded_Editor), a map-settings file, and one converted package holding that map's meshes and materials.

| Map | Package | Source map | Meshes | Files |
| --- | --- | --- | --- | --- |
| Blackwing | `SCDA_BLKG1` | `BLKG1` | 38.3 MB | [Port notes](Blackwing/README.md) &middot; [Checksums](Blackwing/SHA256SUMS.txt) |
| Boss House | `SCDA_BOSG2` | `BOSG2` | 30.8 MB | [Port notes](Boss%20House/README.md) &middot; [Checksums](Boss%20House/SHA256SUMS.txt) |
| Dawn Waves | `SCDA_DWG` | `DWG` | 29.9 MB | [Port notes](Dawn%20Waves/README.md) &middot; [Checksums](Dawn%20Waves/SHA256SUMS.txt) |
| Motorway 90 | `SCDA_MOTG4` | `MOTG4` | 47.8 MB | [Port notes](Motorway%2090/README.md) &middot; [Checksums](Motorway%2090/SHA256SUMS.txt) |
| Red Diamond | `SCDA_REDG6` | `REDG6` | 37.8 MB | [Port notes](Red%20Diamond/README.md) &middot; [Checksums](Red%20Diamond/SHA256SUMS.txt) |
| Slaughterhouse | `SCDA_SLHG7` | `SLHG7` | 38.6 MB | [Port notes](Slaughterhouse/README.md) &middot; [Checksums](Slaughterhouse/SHA256SUMS.txt) |
| Terminus | `SCDA_TERG5` | `TERG5` | 42.6 MB | [Port notes](Terminus/README.md) &middot; [Checksums](Terminus/SHA256SUMS.txt) |
| USS Wisdom | `SCDA_USSG8` | `USSG8` | 33.4 MB | [Port notes](USS%20Wisdom/README.md) &middot; [Checksums](USS%20Wisdom/SHA256SUMS.txt) |

## Install

Close the game and the editor, back up any files with the same names, then copy each map's four files to the paths listed in its notes. The maps are independent of each other, so install only the ones you want. Nothing here replaces an existing Chaos Theory map. Keep every file a map comes with — other players need the same ones to join you.

## Map names

The display names above are the ones Double Agent itself uses. Each source map ships a description package (`PKG_BLKG1_Desc.mcd` and the rest) naming a menu string, and those strings resolve in the game's English menu text: `BLKG1` is Blackwing, `MOTG4` is Motorway 90, and so on. The `SCDA_` prefix on the package names keeps them clear of the Chaos Theory map codes.

## What to expect

These are converted assets with SCCT-compatible materials, not a finished conversion. Review collision, materials, lighting and gameplay before building on them. They have not been playtested in game.

Each map's imports were read out of its package tables: every one references exactly a single mesh package, `SCDA_<CODE>_VS`, and nothing else beyond what the game and editor provide natively. Earlier working packages left in the map-editing copy — `SCDA_DWG.usx` and `DA_BOSG2_OpacityFixed.usx` — are superseded and are not part of these ports.

The `-i.utc` map-settings files are minimal. They carry the settings object but no map name, game-mode list or briefing images, so a map's menu entry is bare until those are filled in. The [Calypso Casino port](../rainbow-six-vegas/README.md) ships the same way.

The playable maps and their `-i.utc` files were built under the names `SCDA_<CODE>_VSPlacements`; the release assets drop that suffix so the `Maps` and `MapsEd` names match, as they do everywhere else in this collection. The file contents are untouched, and neither map carries an internal reference to its own filename, but the renamed files have not been loaded in game yet.

Release downloads are not published yet. The checksums in each map's folder describe the build these notes were written from.
