# Call of Duty 4 - Winter Crash assets v1.0.0

Static meshes and textures from the Call of Duty 4 multiplayer map Winter Crash (`mp_crash_snow`), for
reuse in your own SCCT maps. Install from the SCCT Map Manager's **Asset Packs** section.

| Package | Folder | Contents |
| --- | --- | --- |
| `COD4_crash_snow.usx` | `Packages/StaticMeshes` | 558 static meshes (source props and leftover world geometry) with embedded materials |
| `COD4_crash_snow_TXT.utx` | `Packages/Textures` | 328 textures, 323 materials |

The texture package holds exact copies of the materials embedded in the mesh package. Use it when texturing
your own BSP or meshes; maps that use it must ship that `.utx`. The same mesh package is used by the
[editable BSP port](../../../ports/call-of-duty-4/winter-crash/README.md).

[Release and downloads](https://github.com/Lumbridge/SCCT-Maps/releases/tag/cod4-winter-crash-v1.0.0).
