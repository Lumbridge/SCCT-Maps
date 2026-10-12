# Plant — GoldenEye 007: Reloaded

Editable scenery of the Plant multiplayer map from GoldenEye 007: Reloaded (Xbox 360), for Enhanced SCCT Versus 4.0 and the Reloaded Chaos Theory Editor.

## Install

In SCCT Map Manager, pick **Plant (editable scenery)** under Ports / GoldenEye 007: Reloaded and tick **Include editable source maps (MapsEd)**. Or download `GE007_Plant-v1.0.0.zip` from [this release](https://github.com/Lumbridge/SCCT-Maps/releases/tag/ge007-plant-v1.0.0) and copy its Packages folder into your installation. Close the game and editor first and keep any files you have edited.

Open `Packages/MapsEd/GE007_Plant.sdc` in the editor. It needs `Packages/StaticMeshes/GE007_Plant.usx`, which holds the meshes, materials and textures. The same package is in **Asset Packs** as **GoldenEye 007: Reloaded — Plant**.

## Known issues

- Scenery only: no objectives, spawns, lighting, sound or interactions. Not a match-ready map.
- Multi-layer materials, water, reflections and effects are approximate.
- Props are separate static meshes (`_P`) and large scenery is split into chunks (`_C`). The original object names are not available.
- 811 actors, 154 materials. Reloads in the editor; not playtested in game.

Version: v1.0.0. Source scene: 4090037e.
