# Sewer — GoldenEye 007: Reloaded

Editable multiplayer scenery converted from the Xbox 360 game for Enhanced SCCT Versus 4.0 and the Reloaded Chaos Theory Editor. This release contains the Sewer layout and its embedded mesh, material and texture package.

## Install

In SCCT Map Manager, select **Sewer (editable scenery)** under Ports / GoldenEye 007: Reloaded and enable **Include editable source maps (MapsEd)** before installing. The reusable mesh package is also listed separately in **Asset Packs** as **GoldenEye 007: Reloaded — Sewer**.

Alternatively, download `GE007_Sewer-v1.0.0.zip` from [this release](https://github.com/Lumbridge/SCCT-Maps/releases/tag/ge007-sewer-v1.0.0) and copy its Packages folder into your installation. Save your work and close the game/editor first. Preserve any locally edited files with these names.

Open `Packages/MapsEd/GE007_Sewer.sdc` in the editor. Keep `Packages/StaticMeshes/GE007_Sewer.usx` alongside it; the package embeds all converted materials and textures. Maps and asset packs use the same file, so either installation preserves the dependency.

## Scope and checks

This is an editable scenery conversion. It does not include recreated multiplayer objectives, spawns, source lighting, sound or interactions, and is not a match-ready SCCT map. Multi-layer materials, water, reflection and effect blending are approximations. Converted meshes retain baked placement coordinates; account for their offsets when reusing them.

The saved map passed a fresh native-editor reload with 497 actors and 55 materials. Saved texture pixels were compared against 55 source/baked images. 47 effect actors passed saved-material and collision-flag checks. Native collision probes produced 22 hits from 1014 traces, with maximum cache index 3711 (below 5000). Source-normal comparison mean dot: 0.900. These checks do not replace rendered review or in-game playtesting.

Version: v1.0.0. Source scene: 40900360.
