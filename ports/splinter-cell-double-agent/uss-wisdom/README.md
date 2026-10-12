# USS Wisdom (SCDA_USSG8) from Splinter Cell: Double Agent

The Splinter Cell: Double Agent (PC) map **USS Wisdom** (`USSG8`), ported to Enhanced SCCT Versus 3.6.

## Install

Close the game and the editor, back up files with the same names, then copy the files into your Enhanced SCCT Versus 3.6 installation:

| File | Goes to |
| --- | --- |
| `SCDA_USSG8-Playable.sdc` | `Packages/Maps/SCDA_USSG8.sdc` |
| `SCDA_USSG8-Editable.sdc` | `Packages/MapsEd/SCDA_USSG8.sdc` |
| `SCDA_USSG8-i.utc` | `Packages/Textures/SCDA_USSG8-i.utc` |
| `SCDA_USSG8_VS.usx` | `Packages/StaticMeshes/SCDA_USSG8_VS.usx` |

Playable map: `Packages/Maps/SCDA_USSG8.sdc`. Editable map: `Packages/MapsEd/SCDA_USSG8.sdc` (open it in the [Reloaded Editor](https://github.com/Lumbridge/SCCT_Versus_Reloaded_Editor)).

Both maps need `SCDA_USSG8_VS.usx` (meshes and materials, 33.4 MB) and no other package. Other players need the same files to join you.

## Known issues

- Converted meshes and materials. Check collision, materials, lighting and gameplay before building on it.
- Not playtested in game.
- The map-settings file is bare. See the [collection notes](../README.md).
