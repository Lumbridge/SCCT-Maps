# Splinter Cell: Double Agent ports

The eight versus maps from Splinter Cell: Double Agent (PC), ported to Enhanced SCCT Versus 3.6. Each map is four files: a playable map, an editable map for the [Reloaded Editor](https://github.com/Lumbridge/SCCT_Versus_Reloaded_Editor), a map-settings file and one package with that map's meshes and materials.

| Map | Package | Source map | Meshes | Files |
| --- | --- | --- | --- | --- |
| Blackwing | `SCDA_BLKG1` | `BLKG1` | 38.3 MB | [Download ZIP](https://github.com/Lumbridge/SCCT-Maps/releases/download/scda-blkg1-v1.0.0/Blackwing-SCDA-v1.0.0.zip) &middot; [Port notes](blackwing/README.md) &middot; [Checksums](blackwing/SHA256SUMS.txt) |
| Boss House | `SCDA_BOSG2` | `BOSG2` | 30.8 MB | [Download ZIP](https://github.com/Lumbridge/SCCT-Maps/releases/download/scda-bosg2-v1.0.0/Boss-House-SCDA-v1.0.0.zip) &middot; [Port notes](boss-house/README.md) &middot; [Checksums](boss-house/SHA256SUMS.txt) |
| Dawn Waves | `SCDA_DWG` | `DWG` | 29.9 MB | [Download ZIP](https://github.com/Lumbridge/SCCT-Maps/releases/download/scda-dwg-v1.0.0/Dawn-Waves-SCDA-v1.0.0.zip) &middot; [Port notes](dawn-waves/README.md) &middot; [Checksums](dawn-waves/SHA256SUMS.txt) |
| Motorway 90 | `SCDA_MOTG4` | `MOTG4` | 47.8 MB | [Download ZIP](https://github.com/Lumbridge/SCCT-Maps/releases/download/scda-motg4-v1.0.0/Motorway-90-SCDA-v1.0.0.zip) &middot; [Port notes](motorway-90/README.md) &middot; [Checksums](motorway-90/SHA256SUMS.txt) |
| Red Diamond | `SCDA_REDG6` | `REDG6` | 37.8 MB | [Download ZIP](https://github.com/Lumbridge/SCCT-Maps/releases/download/scda-redg6-v1.0.0/Red-Diamond-SCDA-v1.0.0.zip) &middot; [Port notes](red-diamond/README.md) &middot; [Checksums](red-diamond/SHA256SUMS.txt) |
| Slaughterhouse | `SCDA_SLHG7` | `SLHG7` | 38.6 MB | [Download ZIP](https://github.com/Lumbridge/SCCT-Maps/releases/download/scda-slhg7-v1.0.0/Slaughterhouse-SCDA-v1.0.0.zip) &middot; [Port notes](slaughterhouse/README.md) &middot; [Checksums](slaughterhouse/SHA256SUMS.txt) |
| Terminus | `SCDA_TERG5` | `TERG5` | 42.6 MB | [Download ZIP](https://github.com/Lumbridge/SCCT-Maps/releases/download/scda-terg5-v1.0.0/Terminus-SCDA-v1.0.0.zip) &middot; [Port notes](terminus/README.md) &middot; [Checksums](terminus/SHA256SUMS.txt) |
| USS Wisdom | `SCDA_USSG8` | `USSG8` | 33.4 MB | [Download ZIP](https://github.com/Lumbridge/SCCT-Maps/releases/download/scda-ussg8-v1.0.0/USS-Wisdom-SCDA-v1.0.0.zip) &middot; [Port notes](uss-wisdom/README.md) &middot; [Checksums](uss-wisdom/SHA256SUMS.txt) |

## Install

Close the game and the editor, back up files with the same names, then copy each map's four files to the paths in its notes. Install only the maps you want. They do not depend on each other and do not replace any Chaos Theory map. Other players need the same files to join you.

## Map names

The names are the ones Double Agent uses in its English menu: `BLKG1` is Blackwing, `MOTG4` is Motorway 90, and so on. The `SCDA_` prefix keeps the package names clear of the Chaos Theory map codes.

## Known issues

- Converted assets, not a finished conversion. Check collision, materials, lighting and gameplay before building on them.
- Not playtested in game.
- The `-i.utc` map-settings files are bare: no map name, game-mode list or briefing images, so the menu entry is empty until you fill them in. The [Calypso Casino port](../rainbow-six-vegas/calypso-casino/README.md) is the same.
- Each map uses one mesh package, `SCDA_<CODE>_VS`, and nothing else beyond the game and editor. The older `SCDA_DWG.usx` and `DA_BOSG2_OpacityFixed.usx` are not part of these ports.
- The playable maps and `-i.utc` files were built as `SCDA_<CODE>_VSPlacements` and renamed so the `Maps` and `MapsEd` names match. The contents are unchanged, but the renamed files have not been loaded in game yet.

Each map has its own release, tagged `scda-<code>-v1.0.0`, with the four files and a ZIP of the same build. The checksums in each map's folder are for that build, and the Map Manager installs it from the same release.
