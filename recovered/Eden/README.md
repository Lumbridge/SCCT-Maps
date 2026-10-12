# Eden (EDE64)

Editable version of Eden, recovered from the compiled map (saved 15 September 2026). It replaces the installed `EDE64` map.

## Install

Close the game and the editor, back up files with the same names, then copy the `Packages` folder into your Enhanced SCCT Versus 3.6 installation.

- Playable map: `Packages/Maps/EDE64.sdc`
- Editable map: `Packages/MapsEd/EDE64.sdc` (open it in the Reloaded Editor)

Keep all the included mesh and texture packages, and do not rename `EDE64_Recovered_Assets.usx`. The older `EDE64_Assets.usx` is included for files that still use it.

## Known issues

- Brush history is not preserved (259 structural brushes rebuilt, 1,403 actors kept).
- The original baked lighting is kept. Rebuilding lighting will change the look.
- Not playtested in game.
