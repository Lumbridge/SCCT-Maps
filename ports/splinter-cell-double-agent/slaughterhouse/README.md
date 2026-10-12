# Slaughterhouse (SCDA_SLHG7) from Splinter Cell: Double Agent

The Splinter Cell: Double Agent (PC) map **Slaughterhouse** (`SLHG7`), ported to Enhanced SCCT Versus 3.6.

## Install

Close the game and the editor, back up files with the same names, then copy the files into your Enhanced SCCT Versus 3.6 installation:

| File | Goes to |
| --- | --- |
| `SCDA_SLHG7-Playable.sdc` | `Packages/Maps/SCDA_SLHG7.sdc` |
| `SCDA_SLHG7-Editable.sdc` | `Packages/MapsEd/SCDA_SLHG7.sdc` |
| `SCDA_SLHG7-i.utc` | `Packages/Textures/SCDA_SLHG7-i.utc` |
| `SCDA_SLHG7_VS.usx` | `Packages/StaticMeshes/SCDA_SLHG7_VS.usx` |

Playable map: `Packages/Maps/SCDA_SLHG7.sdc`. Editable map: `Packages/MapsEd/SCDA_SLHG7.sdc` (open it in the [Reloaded Editor](https://github.com/Lumbridge/SCCT_Versus_Reloaded_Editor)).

Both maps need `SCDA_SLHG7_VS.usx` (meshes and materials, 38.6 MB) and no other package. Other players need the same files to join you.

## Known issues

- Converted meshes and materials. Check collision, materials, lighting and gameplay before building on it.
- Not playtested in game.
- The map-settings file is bare. See the [collection notes](../README.md).
