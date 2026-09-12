# SCCT Maps

Custom maps and working assets for **Splinter Cell: Chaos Theory Versus**.

## Maps

| Map | Package name | Version | Files |
| --- | --- | --- | --- |
| Shipment | `ShipD` | v1.1 | [Download playable ZIP](https://github.com/Lumbridge/SCCT-Maps/releases/download/shipd-v1.1/Shipment-v1.1.zip) · [Release notes](https://github.com/Lumbridge/SCCT-Maps/releases/tag/shipd-v1.1) |

![Shipment map preview](src/ShipD/TGA%20textures/LevelPreview_Menu_256_display_check.png)

## Install Shipment

1. Download **[Shipment-v1.1.zip](https://github.com/Lumbridge/SCCT-Maps/releases/download/shipd-v1.1/Shipment-v1.1.zip)** from the [Shipment v1.1 release](https://github.com/Lumbridge/SCCT-Maps/releases/tag/shipd-v1.1) and extract it.
2. Close the game and back up any existing `ShipD` files you intend to replace.
3. Copy the extracted `Packages` folder into your **Versus installation directory**, merging the matching folders. For a standalone Enhanced SCCT Versus installation, use the directory containing its `Packages` and `System` folders.
4. Start Versus and look for **Shipment** in level selection.

Keep the package filenames and folder structure intact:

| Folder | File | Purpose |
| --- | --- | --- |
| `Maps` | `ShipD.sdc` | Playable map |
| `StaticMeshes` | `ShipD_STM.usx` | Custom static meshes |
| `Textures` | `ShipD_TXT.utx` | Custom textures |
| `Textures` | `ShipD-i.utc` | Map settings and menu preview |

Players should install the same map version and accompanying packages.

**Shipment v1.1 released on 12 September 2026:** includes the latest saved playable map and menu settings. The matching editor source is retained under `release/ShipD/v1.1/Packages/MapsEd`. The previous v1 release remains available.

## Repository layout

- `release/<map>/<version>/Packages/` — versioned map packages, arranged for installation.
- `src/ShipD/raw textures/` — original PNG textures and preview capture.
- `src/ShipD/TGA textures/` — converted textures and the 256×256 menu preview prepared for import.
- `src/ShipD/raw unused textures/` — reference images and unused texture candidates.

Use the downloadable ZIP under [GitHub Releases](https://github.com/Lumbridge/SCCT-Maps/releases) to play. The `src` directory and `MapsEd` copy in the repository are for authoring and reference. Machine-specific game/editor configuration is kept local and excluded from this repository.

## Editing

The maps are developed with the [SCCT Versus Reloaded Editor](https://github.com/Lumbridge/SCCT_Versus_Reloaded_Editor).

Shipment's level-selection texture is named `ShipD-i.Menu`. The supplied `LevelPreview_Menu_256.tga` is prepared as a 256×256 uncompressed TGA for that texture. Import it into package `ShipD-i`, with no group and the name `Menu`, then save the package.
