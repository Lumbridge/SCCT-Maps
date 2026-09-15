# Clarity Soft (ClarD)

Updated from the local `ClarD_Recovered` editable and playable maps saved on 15 September 2026. The distributed map filenames remain `ClarD.sdc` for compatibility with the existing Clarity Soft installation and menu package; the map contents are unchanged from those local saves.

Close the game and editor, back up existing files, then copy the included `Packages` folder into your Enhanced SCCT Versus 3.6 installation. These files replace the installed `ClarD` map.

Open `Packages/MapsEd/ClarD.sdc` in the Reloaded Editor. The playable map is `Packages/Maps/ClarD.sdc`.

Keep all included mesh and texture packages with the map. In particular, do not rename `ClarD_Recovered_Assets.usx`: the recovered maps reference that package name. The earlier `ClarD_Assets.usx` is retained for compatibility with existing files.

The local recovery report records 1,254 reconstructed structural brushes, 5,167 retained actors, and successful build, save, and reopening checks. Original brush history is not preserved. Compatible baked lighting is retained; explicit lighting recalculation can change the appearance. This release update verifies file and archive checksums; no new in-game playtest was performed.
