# Rainbow Six Vegas - Calypso Casino v1.0.0

Reusable Calypso Casino static meshes and textures converted for the SCCT editor. These are editor assets, not a playable map.

## Download

Use SCCT Map Manager v0.3.0 or newer: **Tools → Textures & static meshes**, select **Rainbow Six Vegas - Calypso Casino**, then **Download & install**.

Alternatively, [download the complete pack](https://github.com/Lumbridge/SCCT-Maps/releases/download/r6v-calypso-casino-v1.0.0/Calypso-Casino-Editor-Assets-v1.0.0.zip) and copy its `Packages` folder into your SCCT installation. Close the game and editor first and preserve any existing edited packages. Individual packages and SHA-256 checksums are also available on the [release page](https://github.com/Lumbridge/SCCT-Maps/releases/tag/r6v-calypso-casino-v1.0.0).

## Packages

| Package | Contents / use |
| --- | --- |
| `StaticMeshes/R6V_MP_Casino_01.usx` | Current named Casino conversion, including its embedded materials and textures. Start here for new work. |
| `StaticMeshes/CalypsoMeshes.usx` | Earlier Calypso mesh collection, retained for projects referencing that package name. |
| `StaticMeshes/CalypsoPlacementMirrors.usx` | Earlier mirrored placement meshes. |
| `Textures/CalypsoColours_Expanded.utx` | Expanded recovered Calypso colour textures. |
| `Textures/CalypsoColours_Partial.utx` | Earlier partial colour collection, retained for existing references. |
| `Textures/CalypsoPlacementMaterials.utx` | Separate materials used by the earlier Calypso placements. |

Keep the package names unchanged. The texture collections and earlier mesh packages are included together to preserve existing references. Placement maps, menu entries, experimental proof/test meshes and BSP/shader research packages are excluded.

## Version history

### v1.0.0

Initial published snapshot of six Calypso Casino packages. Future updates will use a new version and show as an available update in the manager. Downloaded and installed versions are tracked separately.

## Conversion limits

These are converted assets, not the original Vegas renderer. Missing colours and approximated shaders may remain; review collision, materials and lighting in your own map before releasing it. File hashes and installation were verified using a disposable SCCT folder; this release does not claim a fresh native-editor or gameplay validation of every mesh.
