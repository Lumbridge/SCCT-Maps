# SCCT Maps

Maps and editor files for **Splinter Cell: Chaos Theory Versus**.

## Original maps

| Map | Package | Version | Files |
| --- | --- | --- | --- |
| Shipment | `ShipD` | v1.1 | [Download ZIP](https://github.com/Lumbridge/SCCT-Maps/releases/download/shipd-v1.1/Shipment-v1.1.zip) · [Editor files](release/ShipD/v1.1/Packages/MapsEd) · [Source assets](src/ShipD) |

![Shipment map preview](src/ShipD/TGA%20textures/LevelPreview_Menu_256_display_check.png)

## Recovered / editable maps

Existing maps converted into editable maps. Original brush history is not preserved, and rebuilding lighting can change their appearance.

| Map | Package | Files |
| --- | --- | --- |
| Eden | `EDE64` | [Map and assets](recovered/Eden/Packages) · [Editor map](recovered/Eden/Packages/MapsEd/EDE64.sdc) |
| Sublabs | `sub18` | [Map and assets](recovered/Sublabs/Packages) · [Editor map](recovered/Sublabs/Packages/MapsEd/sub18.sdc) |
| Offshore Oilrig | `OffsD` | [Map and assets](recovered/OffsD/Packages) · [Editor map](recovered/OffsD/Packages/MapsEd/OffsD.sdc) |

## Using the files

Close the game, back up any matching files, and copy the map's `Packages` folder into your Enhanced SCCT Versus installation. Keep all included assets together. Players should use the same files.

| Folder | Contents |
| --- | --- |
| `Maps` | Compiled maps for the game |
| `MapsEd` | Editable maps for the [Reloaded Editor](https://github.com/Lumbridge/SCCT_Versus_Reloaded_Editor) |
| `StaticMeshes` / `Textures` | Required assets and menu settings |

The recovered maps use the original package names and will replace installed copies of `EDE64`, `sub18`, or `OffsD`. Gameplay testing is still needed.
