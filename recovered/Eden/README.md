# Eden (EDE64)

Updated from the local `EDE64_Recovered` editable and playable maps saved on 15 September 2026. The distributed map filenames remain `EDE64.sdc` for compatibility with the existing Eden installation and menu package; the map contents are unchanged from those local saves.

Close the game and editor, back up existing files, then copy the included `Packages` folder into your Enhanced SCCT Versus 3.6 installation. These files replace the installed `EDE64` map.

Open `Packages/MapsEd/EDE64.sdc` in the Reloaded Editor. The playable map is `Packages/Maps/EDE64.sdc`.

Keep all included mesh and texture packages with the map. In particular, do not rename `EDE64_Recovered_Assets.usx`: the recovered maps reference that package name. The earlier `EDE64_Assets.usx` is retained for compatibility with existing files.

The local recovery report records 259 reconstructed structural brushes, 1,403 retained actors, and successful build, save, and reopening checks. Original brush history is not preserved. Compatible baked lighting is retained; explicit lighting recalculation can change the appearance. This release update verifies file and archive checksums; no new in-game playtest was performed.
