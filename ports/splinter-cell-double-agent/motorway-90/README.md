# Motorway 90 (SCDA_MOTG4) from Splinter Cell: Double Agent

The Splinter Cell: Double Agent (PC) map **Motorway 90** (`MOTG4`), ported to Enhanced SCCT Versus 3.6.

## Install

Close the game and the editor, back up files with the same names, then copy the files into your Enhanced SCCT Versus 3.6 installation:

| File | Goes to |
| --- | --- |
| `SCDA_MOTG4-Playable.sdc` | `Packages/Maps/SCDA_MOTG4.sdc` |
| `SCDA_MOTG4-Editable.sdc` | `Packages/MapsEd/SCDA_MOTG4.sdc` |
| `SCDA_MOTG4-i.utc` | `Packages/Textures/SCDA_MOTG4-i.utc` |
| `SCDA_MOTG4_VS.usx` | `Packages/StaticMeshes/SCDA_MOTG4_VS.usx` |

Playable map: `Packages/Maps/SCDA_MOTG4.sdc`. Editable map: `Packages/MapsEd/SCDA_MOTG4.sdc` (open it in the [Reloaded Editor](https://github.com/Lumbridge/SCCT_Versus_Reloaded_Editor)).

Both maps need `SCDA_MOTG4_VS.usx` (meshes and materials, 47.8 MB) and no other package. Other players need the same files to join you.

## Known issues

- Converted meshes and materials. Check collision, materials, lighting and gameplay before building on it.
- Not playtested in game.
- The map-settings file is bare. See the [collection notes](../README.md).
