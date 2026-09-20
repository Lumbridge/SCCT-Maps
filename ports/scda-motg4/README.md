# Motorway 90 (SCDA_MOTG4) from Splinter Cell: Double Agent

Ported from `MOTG4`, the Splinter Cell: Double Agent PC map its menu calls **Motorway 90**, into Enhanced SCCT Versus 3.6. The port is four files: the playable and editable `SCDA_MOTG4.sdc` maps, the `SCDA_MOTG4-i.utc` map-settings file, and `SCDA_MOTG4_VS.usx`, the converted package holding this map's meshes and materials (47.8 MB).

## Install

1. Close the game and the editor.
2. Back up any files with the same names.
3. Copy the files into your Enhanced SCCT Versus 3.6 installation:

| File | Goes to |
| --- | --- |
| `SCDA_MOTG4-Playable.sdc` | `Packages/Maps/SCDA_MOTG4.sdc` |
| `SCDA_MOTG4-Editable.sdc` | `Packages/MapsEd/SCDA_MOTG4.sdc` |
| `SCDA_MOTG4-i.utc` | `Packages/Textures/SCDA_MOTG4-i.utc` |
| `SCDA_MOTG4_VS.usx` | `Packages/StaticMeshes/SCDA_MOTG4_VS.usx` |

Playable map: `Packages/Maps/SCDA_MOTG4.sdc`. Editable map: `Packages/MapsEd/SCDA_MOTG4.sdc` (open it in the [Reloaded Editor](https://github.com/Lumbridge/SCCT_Versus_Reloaded_Editor)).

`SCDA_MOTG4_VS` is the only package either map imports from, so keep it installed alongside them; everything else they use is native to the game or the editor. Other players need the same files to join you.

## What to expect

The source game is Splinter Cell: Double Agent for PC. The port uses converted meshes and SCCT-compatible materials; review collision, materials, lighting and gameplay before building on it. It has not been playtested in game. The [collection notes](../scda/README.md) cover what all eight ports share, including the bare map-settings file and the filenames these builds were saved under.
