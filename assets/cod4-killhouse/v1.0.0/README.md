# Call of Duty 4 - Killhouse assets v1.0.0

Static meshes and textures from the Call of Duty 4 multiplayer map Killhouse (`mp_killhouse`), for
reuse in your own SCCT maps. Install from the SCCT Map Manager's **Asset Packs** section.

| Package | Folder | Contents |
| --- | --- | --- |
| `COD4_killhouse.usx` | `Packages/StaticMeshes` | 896 static meshes (source props and leftover world geometry) with embedded materials |
| `COD4_killhouse_TXT.utx` | `Packages/Textures` | 211 textures, 208 materials |

The texture package holds exact copies of the materials embedded in the mesh package. Use it when texturing
your own BSP or meshes; maps that use it must ship that `.utx`. The same mesh package is used by the
[editable BSP port](../../../ports/call-of-duty-4/killhouse/README.md).

[Release and downloads](https://github.com/Lumbridge/SCCT-Maps/releases/tag/cod4-killhouse-v1.0.0).
