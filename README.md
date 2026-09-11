# SCCT Maps

Custom maps and working assets for **Splinter Cell: Chaos Theory Versus**.

## Maps

| Map | Package name | Version | Files |
| --- | --- | --- | --- |
| Shipment | `ShipD` | v1 | [Map packages](release/ShipD/v1/Packages) · [Working assets](src/ShipD) |

![Shipment map preview](src/ShipD/TGA%20textures/LevelPreview_Menu_256_display_check.png)

## Install Shipment

1. Download this repository with **Code → Download ZIP**, or clone it.
2. Close the game and back up any existing `ShipD` files you intend to replace.
3. Copy the contents of `release/ShipD/v1/Packages` into your **Versus `Packages`** directory, merging the matching folders. For a standalone Enhanced SCCT Versus installation, use its `Packages` directory.
4. Start Versus and look for **Shipment** in level selection.

Keep the package filenames and folder structure intact:

| Folder | File | Purpose |
| --- | --- | --- |
| `Maps` | `ShipD.sdc` | Playable map |
| `MapsEd` | `ShipD.sdc` | Map copy supplied for the editor |
| `StaticMeshes` | `ShipD_STM.usx` | Custom static meshes |
| `Textures` | `ShipD_TXT.utx` | Custom textures |
| `Textures` | `ShipD-i.utc` | Map settings and menu preview |

Players should install the same map version and accompanying packages.

## Repository layout

- `release/<map>/<version>/Packages/` — versioned map packages, arranged for installation.
- `src/ShipD/raw textures/` — original PNG textures and preview capture.
- `src/ShipD/TGA textures/` — converted textures and the 256×256 menu preview prepared for import.
- `src/ShipD/raw unused textures/` — reference images and unused texture candidates.

The `src` directory is for authoring and reference; install maps from `release`. Machine-specific game/editor configuration is kept local and excluded from this repository.

## Editing

The maps are developed with the [SCCT Versus Reloaded Editor](https://github.com/Lumbridge/SCCT_Versus_Reloaded_Editor).

Shipment's level-selection texture is named `ShipD-i.Menu`. The supplied `LevelPreview_Menu_256.tga` is prepared as a 256×256 uncompressed TGA for that texture. Import it into package `ShipD-i`, with no group and the name `Menu`, then save the package.
