# Bloc - Call of Duty 4: Modern Warfare

Editable version of the Call of Duty 4 multiplayer map Bloc (`mp_bloc`) for Enhanced SCCT Versus 4.0 and the Reloaded Chaos Theory Editor. Walls, floors, ceilings, roofs and building shells are real BSP brushes, so you can change the layout for SvM play.

## Install

In SCCT Map Manager, pick **Bloc (editable BSP)** under Ports / Call of Duty 4 and tick **Include editable source maps (MapsEd)**. Or download the files from [this release](https://github.com/Lumbridge/SCCT-Maps/releases/tag/cod4-bloc-v1.0.0). The meshes and textures are also in **Asset Packs** as **Call of Duty 4 - Bloc**.

Open `Packages/MapsEd/COD4_bloc_BSP.sdc`. It needs `Packages/StaticMeshes/COD4_bloc.usx`.

## What is in the map

- 1911 `COD4_BSP_nnnnn` brushes in group `COD4_Architecture`. Edit them, then rebuild.
- 589 `WorldRest_*` static meshes: terrain, curved surfaces, trims and detail that are not brushes.
- 11919 props, vehicles, foliage and doors in their original places.
- `COD4_PlaySpace` (the box the map sits in) and `COD4_SkyRoom` (sky zone). Leave these.
- `COD4_bloc_TXT.utx`: the same 278 textures and 274 materials as a texture package, for use on other maps.

## Known issues

- Not a match-ready map: no spawns, objectives, lights, sounds or effects. Place SCCT lights and build lighting. The meshes keep their baked vertex lighting.
- SCCT BSP has hard limits, so smaller details stay as meshes. This map uses 12245 nodes, 20048 points and 29335 of 32768 collision-hull entries.
- If a rebuild fails after heavy editing, remove small or angled `COD4_BSP` brushes first.
