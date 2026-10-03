# Call of Duty 4 - Showdown assets v1.0.0

Static meshes and textures from the Call of Duty 4 multiplayer map Showdown (`mp_showdown`), for
reuse in your own SCCT maps. Install from the SCCT Map Manager's **Asset Packs** section.

| Package | Folder | Contents |
| --- | --- | --- |
| `COD4_showdown.usx` | `Packages/StaticMeshes` | 442 static meshes (source props and leftover world geometry) with embedded materials |
| `COD4_showdown_TXT.utx` | `Packages/Textures` | 267 textures, 266 materials |

The texture package holds exact copies of the materials embedded in the mesh package. Use it when texturing
your own BSP or meshes; maps that use it must ship that `.utx`. The same mesh package is used by the
[editable BSP port](../../../ports/call-of-duty-4/showdown/README.md).

[Release and downloads](https://github.com/Lumbridge/SCCT-Maps/releases/tag/cod4-showdown-v1.0.0).
