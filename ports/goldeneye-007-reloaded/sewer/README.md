# Sewer — GoldenEye 007: Reloaded

Editable scenery of the Sewer multiplayer map from GoldenEye 007: Reloaded (Xbox 360), for Enhanced SCCT Versus 4.0 and the Reloaded Chaos Theory Editor.

## Install

In SCCT Map Manager, pick **Sewer (editable scenery)** under Ports / GoldenEye 007: Reloaded and tick **Include editable source maps (MapsEd)**. Or download `GE007_Sewer-v1.0.0.zip` from [this release](https://github.com/Lumbridge/SCCT-Maps/releases/tag/ge007-sewer-v1.0.0) and copy its Packages folder into your installation. Close the game and editor first and keep any files you have edited.

Open `Packages/MapsEd/GE007_Sewer.sdc` in the editor. It needs `Packages/StaticMeshes/GE007_Sewer.usx`, which holds the meshes, materials and textures. The same package is in **Asset Packs** as **GoldenEye 007: Reloaded — Sewer**.

## Known issues

- Scenery only: no objectives, spawns, lighting, sound or interactions. Not a match-ready map.
- Multi-layer materials, water, reflections and effects are approximate.
- Props are separate static meshes (`_P`) and large scenery is split into chunks (`_C`). The original object names are not available.
- 1568 actors, 55 materials. Reloads in the editor; not playtested in game.

Version: v1.0.0. Source scene: 40900360.
