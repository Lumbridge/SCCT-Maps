# Dawn Waves (SCDA_DWG) from Splinter Cell: Double Agent

Ported from `DWG`, the Splinter Cell: Double Agent PC map its menu calls **Dawn Waves**, into Enhanced SCCT Versus 3.6. The port is four files: the playable and editable `SCDA_DWG.sdc` maps, the `SCDA_DWG-i.utc` map-settings file, and `SCDA_DWG_VS.usx`, the converted package holding this map's meshes and materials (29.9 MB).

## Install

1. Close the game and the editor.
2. Back up any files with the same names.
3. Copy the files into your Enhanced SCCT Versus 3.6 installation:

| File | Goes to |
| --- | --- |
| `SCDA_DWG-Playable.sdc` | `Packages/Maps/SCDA_DWG.sdc` |
| `SCDA_DWG-Editable.sdc` | `Packages/MapsEd/SCDA_DWG.sdc` |
| `SCDA_DWG-i.utc` | `Packages/Textures/SCDA_DWG-i.utc` |
| `SCDA_DWG_VS.usx` | `Packages/StaticMeshes/SCDA_DWG_VS.usx` |

Playable map: `Packages/Maps/SCDA_DWG.sdc`. Editable map: `Packages/MapsEd/SCDA_DWG.sdc` (open it in the [Reloaded Editor](https://github.com/Lumbridge/SCCT_Versus_Reloaded_Editor)).

`SCDA_DWG_VS` is the only package either map imports from, so keep it installed alongside them; everything else they use is native to the game or the editor. Other players need the same files to join you.

## What to expect

The source game is Splinter Cell: Double Agent for PC. The port uses converted meshes and SCCT-compatible materials; review collision, materials, lighting and gameplay before building on it. It has not been playtested in game. The [collection notes](../README.md) cover what all eight ports share, including the bare map-settings file and the filenames these builds were saved under.
