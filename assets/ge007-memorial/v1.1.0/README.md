# GoldenEye 007: Reloaded — Memorial assets v1.1.0

v1.1.0 adds a separate texture package for each static-mesh package, so the
textures and materials can be used on your own BSP and meshes without loading
the mesh package.

| Package | Folder | Contents |
| --- | --- | --- |
| `GE007_Memorial.usx` | `Packages/StaticMeshes` | 1038 static meshes (unchanged from v1.0.0) |
| `GE007_Memorial_TXT.utx` | `Packages/Textures` | 195 textures, 195 materials |

The texture package holds exact copies (same compression, same names and
groups) of the textures and materials embedded in `GE007_Memorial.usx`. The static meshes
still use their own embedded copies, so existing maps are unaffected. Use the
`_TXT` package (`GE007_Memorial_TXT.utx`) when texturing your own work: 195 textures and
195 materials in total. Maps that use it must ship that `.utx`.

---

# GoldenEye 007: Reloaded — Memorial assets v1.0.0

Reusable SCCT static meshes with embedded textures and materials from the multiplayer Memorial scenery conversion. Install this entry from the SCCT Map Manager's **Asset Packs** section. It installs `Packages/StaticMeshes/GE007_Memorial.usx` only.

The same package is included with the [editable Memorial port](../../../ports/goldeneye-007-reloaded/memorial/README.md). Meshes have local, base-centred pivots for placement in new maps. Spatially separated props are individual meshes; overlapping components stay together. Large connected scenery may have multiple `_C` chunks. Review collision and approximated shaders when reusing them. No playable map or multiplayer gameplay is included in this asset pack.

[Release and downloads](https://github.com/Lumbridge/SCCT-Maps/releases/tag/ge007-memorial-v1.0.0). Close the editor before installation and preserve locally edited packages.
