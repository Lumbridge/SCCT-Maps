# UMP Vertigo Plaza

Original compiled community-pack map: `SKY08.sdc`. Original authorship and embedded credits are preserved. No editable conversion is included.

Close the game, back up matching files, and copy this folder's `Packages` folder into your SCCT Versus installation, merging the existing directories. Also copy the collection's [`_shared`](../_shared) folders for loose supporting files whose map association could not be established. Keep original filenames.

The dependency scan follows package imports recursively and includes both texture variants when supplied, menu packages, and matching sound/localization sidecars. Files supplied by the pack are preserved byte for byte.

## Required installed packages

The following referenced packages are absent from the community pack and were found in the local Enhanced SCCT Versus 3.6 installation. They are not copied from that installation:

`Amb_Aqua`, `Amb_Club`, `Amb_Gare`, `Amb_Miss`, `Amb_Museum`, `Amb_Orph`, `Amb_factory`, `Aquarium_STM`, `Aquarium_TXT`, `Armes_impacts`, `BNK_STM`, `CLU04_STM`, `CLU04_TXT`, `Echelon`, `FAC_STM`, `GAR_TXT`, `Missile`, `SEffectStatic`, `SGameplayObjectsTex`, `STM_MALL`, `STM_ORP`, `Sound_Persos`, `TXT_MAL`, `TXT_ORP`, `TestMapStaticM`, `sfx`.

Native game/editor packages (Core, Engine, SBase, SGameplayObjects, SoftBody, Editor) are not redistributed. Runtime gameplay and string-loaded assets have not been verified in-game.

## Original pack inconsistency

The source pack contains different `SKY08-i.utc` files in `Packages/StaticMeshes` and `Packages/Textures`. Both are preserved in their original locations in UMP Vertigo Plaza; runtime package selection has not been tested.
