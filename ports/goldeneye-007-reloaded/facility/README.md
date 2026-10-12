# Facility — GoldenEye 007: Reloaded

Editable scenery of the Facility multiplayer map from GoldenEye 007: Reloaded (Xbox 360), for Enhanced SCCT Versus 4.0 and the Reloaded Chaos Theory Editor.

## Install

In SCCT Map Manager, pick **Facility (editable scenery)** under Ports / GoldenEye 007: Reloaded and tick **Include editable source maps (MapsEd)**. Or download `GE007_Facility-v1.0.0.zip` from [this release](https://github.com/Lumbridge/SCCT-Maps/releases/tag/ge007-facility-v1.0.0) and copy its Packages folder into your installation. Close the game and editor first and keep any files you have edited.

Open `Packages/MapsEd/GE007_Facility.sdc` in the editor. It needs `Packages/StaticMeshes/GE007_Facility.usx`, which holds the meshes, materials and textures. The same package is in **Asset Packs** as **GoldenEye 007: Reloaded — Facility**.

## Known issues

- Scenery only: no objectives, spawns, lighting, sound or interactions. Not a match-ready map.
- Multi-layer materials, water, reflections and effects are approximate.
- Props are separate static meshes (`_P`) and large scenery is split into chunks (`_C`). The original object names are not available.
- 1010 actors, 119 materials. Reloads in the editor; not playtested in game.

Version: v1.0.0. Source scene: 40900314.
