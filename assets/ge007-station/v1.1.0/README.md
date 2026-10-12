# GoldenEye 007: Reloaded — Station assets v1.1.0

v1.1.0 adds a texture package for each static-mesh package, so you can use the textures and materials on your own BSP and meshes without loading the mesh package.

| Package | Folder | Contents |
| --- | --- | --- |
| `GE007_Station.usx` | `Packages/StaticMeshes` | 766 static meshes (unchanged from v1.0.0) |
| `GE007_Station_TXT.utx` | `Packages/Textures` | 169 textures, 169 materials |

`GE007_Station_TXT.utx` holds exact copies of the textures and materials in `GE007_Station.usx`. The meshes still use their own copies, so existing maps are unaffected. Maps that use a `_TXT` package must ship that `.utx`.

---

# GoldenEye 007: Reloaded — Station assets v1.0.0

Static meshes from the Station multiplayer scenery, with their textures and materials, for your own SCCT maps. Install from the SCCT Map Manager's **Asset Packs** section. It installs `Packages/StaticMeshes/GE007_Station.usx` only.

The [editable Station port](../../../ports/goldeneye-007-reloaded/station/README.md) uses the same package. Props are separate meshes with base-centred pivots. Large scenery may be split into `_C` chunks. Check collision and the approximated shaders before use. No playable map is included.

[Release and downloads](https://github.com/Lumbridge/SCCT-Maps/releases/tag/ge007-station-v1.0.0). Close the editor before installing and keep any packages you have edited.
