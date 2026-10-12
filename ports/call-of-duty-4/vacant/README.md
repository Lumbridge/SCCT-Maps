# Vacant - Call of Duty 4: Modern Warfare

Editable version of the Call of Duty 4 multiplayer map Vacant (`mp_vacant`) for Enhanced SCCT Versus 4.0 and the Reloaded Chaos Theory Editor. Walls, floors, ceilings, roofs and building shells are real BSP brushes, so you can change the layout for SvM play.

## Install

In SCCT Map Manager, pick **Vacant (editable BSP)** under Ports / Call of Duty 4 and tick **Include editable source maps (MapsEd)**. Or download the files from [this release](https://github.com/Lumbridge/SCCT-Maps/releases/tag/cod4-vacant-v1.0.0). The meshes and textures are also in **Asset Packs** as **Call of Duty 4 - Vacant**.

Open `Packages/MapsEd/COD4_vacant_BSP.sdc`. It needs `Packages/StaticMeshes/COD4_vacant.usx`.

## What is in the map

- 1347 `COD4_BSP_nnnnn` brushes in group `COD4_Architecture`. Edit them, then rebuild.
- 278 `WorldRest_*` static meshes: terrain, curved surfaces, trims and detail that are not brushes.
- 4030 props, vehicles, foliage and doors in their original places.
- `COD4_PlaySpace` (the box the map sits in) and `COD4_SkyRoom` (sky zone). Leave these.
- `COD4_vacant_TXT.utx`: the same 367 textures and 359 materials as a texture package, for use on other maps.

## Known issues

- Not a match-ready map: no spawns, objectives, lights, sounds or effects. Place SCCT lights and build lighting. The meshes keep their baked vertex lighting.
- SCCT BSP has hard limits, so smaller details stay as meshes. This map uses 6626 nodes, 11674 points and 16577 of 32768 collision-hull entries.
- If a rebuild fails after heavy editing, remove small or angled `COD4_BSP` brushes first.
