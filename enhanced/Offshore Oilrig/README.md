# "Enhanced" Offshore Oilrig
Saved enhanced map: `OffsE`. Includes the playable map, editable source, map-selection package, recovered mesh package, and additional Oilrig dependencies used by these saved files. Original map authorship and embedded credits are retained.

## Changes (15 September 2026)

- Improved lighting.
- Fixed several incorrect textures.
- Spies can now pole-climb sections of the elevator when it is down.
- Fixed the broken flame emitter.
- Fixed several broken portal volumes.

## Install

Close the game/editor and copy this folder's `Packages` directory into your **Enhanced SCCT Versus 3.6** installation. Back up matching files first and keep all included assets together. Players should use the same files. The `OffsE` map filename is separate from the recovered `OffsD` version.

- Playable map: `Packages/Maps/OffsE.sdc`
- Editable map: `Packages/MapsEd/OffsE.sdc`

## Required installed packages

Following the repository's existing community-map convention, the following dependencies supplied by the game installation are not duplicated here:

`Amb_Aqua`, `amb_Bank`, `Amb_Club`, `Amb_factory`, `Amb_Gare`, `Armes_impacts`, `Aquarium_STM`, `BNK_STM`, `FAC_STM`, `GAR_STM`, `Missile`, `STM_ORP`, `stm_war`, `TestMapStaticM`, `Aquarium_TXT`, `CTF_txt_xbox`, `Echelon`, `FAC_TXT`, `GAR_TXT`, `sfx`, `SGameplayObjectsTex`, `SGameplayObjectsTex_XBOX`, `TestMapTextures`, `TXT_BNK`, `TXT_ORP`, `txt_war`.

Native game/editor packages (`Core`, `Engine`, `Editor`, `SBase`, `SGameplayObjects`) are not redistributed. Editor namespace references are retained in the saved import tables.

`dependencies.json` records every traced asset and its SHA-256, including installed dependencies. `SHA256SUMS.txt` verifies the bundled files. Serialized imports were checked for both playable and editable maps; this is not an in-game playtest, and assets loaded only through script strings may need additional files.
