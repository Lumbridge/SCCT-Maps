# GoldenEye 007: Reloaded — Solar assets v1.1.0

v1.1.0 adds a texture package for each static-mesh package, so you can use the textures and materials on your own BSP and meshes without loading the mesh package.

| Package | Folder | Contents |
| --- | --- | --- |
| `GE007_Solar.usx` | `Packages/StaticMeshes` | 452 static meshes (unchanged from v1.0.0) |
| `GE007_Solar_TXT.utx` | `Packages/Textures` | 100 textures, 100 materials |

`GE007_Solar_TXT.utx` holds exact copies of the textures and materials in `GE007_Solar.usx`. The meshes still use their own copies, so existing maps are unaffected. Maps that use a `_TXT` package must ship that `.utx`.

---

# GoldenEye 007: Reloaded — Solar assets v1.0.0

Static meshes from the Solar multiplayer scenery, with their textures and materials, for your own SCCT maps. Install from the SCCT Map Manager's **Asset Packs** section. It installs `Packages/StaticMeshes/GE007_Solar.usx` only.

The [editable Solar port](../../../ports/goldeneye-007-reloaded/solar/README.md) uses the same package. Props are separate meshes with base-centred pivots. Large scenery may be split into `_C` chunks. Check collision and the approximated shaders before use. No playable map is included.

[Release and downloads](https://github.com/Lumbridge/SCCT-Maps/releases/tag/ge007-solar-v1.0.0). Close the editor before installing and keep any packages you have edited.
