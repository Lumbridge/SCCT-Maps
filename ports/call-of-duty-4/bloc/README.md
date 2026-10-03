# Bloc - Call of Duty 4: Modern Warfare

Editable BSP conversion of the multiplayer map Bloc (`mp_bloc`) for Enhanced SCCT Versus 4.0
and the Reloaded Chaos Theory Editor. World architecture (walls, floors, ceilings, roofs, building shells)
is real, editable BSP built from the source map's own brushes, so the layout can be changed for SvM play.

## Install

In SCCT Map Manager, select **Bloc (editable BSP)** under Ports / Call of Duty 4 and enable
**Include editable source maps (MapsEd)** before installing. The meshes and textures are also listed in
**Asset Packs** as **Call of Duty 4 - Bloc**. Or download the files from
[this release](https://github.com/Lumbridge/SCCT-Maps/releases/tag/cod4-bloc-v1.0.0).

Open `Packages/MapsEd/COD4_bloc_BSP.sdc`. Keep `Packages/StaticMeshes/COD4_bloc.usx` alongside it.

## What is in the map

- `COD4_BSP_nnnnn` brushes (1911), group `COD4_Architecture`: additive brushes; move, resize,
  delete or add, then rebuild. Textures are aligned from the source render UVs where the face was visible.
- `WorldRest_*` static meshes (589): terrain, curved surfaces, trims and detail that are
  not brushes in the source. Parts reproduced by BSP were cut out, so BSP and meshes do not overlap.
- Source props, vehicles, foliage and doors (11919 actors) at their original placement.
- `COD4_PlaySpace` (subtractive box, sky backdrop faces) and `COD4_SkyRoom` (sky zone). Leave these.

## Limits

SCCT BSP has hard limits (16-bit CSG point storage, collision-hull index below 32768). The map was filled
with the most significant source brushes up to a safety margin; smaller details remain meshes. If a rebuild
fails after heavy editing, remove small `COD4_BSP` brushes or angled ones first.

Not included: spawns, objectives, source lighting (place SCCT lights and build lighting; meshes carry the
source's baked vertex lighting), sounds, effects. Not a match-ready map.

## Textures

`COD4_bloc_TXT.utx` holds the same 278 textures and
274 materials as a texture package for use on other maps.

## Checks

Compiled BSP: 12245 nodes, 29335 collision-hull entries (limit 32768),
20048 points. Saved, cold-reloaded in a fresh editor and reviewed at four source spawns.
