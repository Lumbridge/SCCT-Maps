# Call of Duty 4 - Creek assets v1.0.0

Static meshes and textures from the Call of Duty 4 multiplayer map Creek (`mp_creek`), for
reuse in your own SCCT maps. Install from the SCCT Map Manager's **Asset Packs** section.

| Package | Folder | Contents |
| --- | --- | --- |
| `COD4_creek.usx` | `Packages/StaticMeshes` | 717 static meshes (source props and leftover world geometry) with embedded materials |
| `COD4_creek_TXT.utx` | `Packages/Textures` | 256 textures, 243 materials |

The texture package holds exact copies of the materials embedded in the mesh package. Use it when texturing
your own BSP or meshes; maps that use it must ship that `.utx`. The same mesh package is used by the
[editable BSP port](../../../ports/call-of-duty-4/creek/README.md).

[Release and downloads](https://github.com/Lumbridge/SCCT-Maps/releases/tag/cod4-creek-v1.0.0).
