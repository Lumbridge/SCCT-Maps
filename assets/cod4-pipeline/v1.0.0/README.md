# Call of Duty 4 - Pipeline assets v1.0.0

Static meshes and textures from the Call of Duty 4 multiplayer map Pipeline (`mp_pipeline`), for your own SCCT maps. Install from the SCCT Map Manager's **Asset Packs** section.

| Package | Folder | Contents |
| --- | --- | --- |
| `COD4_pipeline.usx` | `Packages/StaticMeshes` | 708 static meshes (source props and leftover world geometry) with embedded materials |
| `COD4_pipeline_TXT.utx` | `Packages/Textures` | 290 textures, 282 materials |

The texture package has exact copies of the materials in the mesh package. Use it to texture your own BSP or meshes. Maps that use it must ship that `.utx`. The [editable BSP port](../../../ports/call-of-duty-4/pipeline/README.md) uses the same mesh package.

[Release and downloads](https://github.com/Lumbridge/SCCT-Maps/releases/tag/cod4-pipeline-v1.0.0).
