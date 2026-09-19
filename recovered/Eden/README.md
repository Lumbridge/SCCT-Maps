# Eden (EDE64)

Editable version of Eden, recovered from the compiled map with the Reloaded Editor (saved 15 September 2026). It keeps the `EDE64.sdc` filename so it works with the existing menu entry, and **replaces the installed `EDE64` map**.

## Install

1. Close the game and the editor.
2. Back up any files with the same names.
3. Copy the `Packages` folder into your Enhanced SCCT Versus 3.6 installation.

Playable map: `Packages/Maps/EDE64.sdc`. Editable map: `Packages/MapsEd/EDE64.sdc` (open it in the Reloaded Editor).

Keep every included mesh and texture package with the map, and do not rename `EDE64_Recovered_Assets.usx` — the map refers to it by name.
The older `EDE64_Assets.usx` is included too, for files that still reference it.

## What to expect

The recovery rebuilt 259 structural brushes and kept 1,403 actors, and the map builds, saves and reopens cleanly. Original brush history is not preserved. The original baked lighting is kept; recalculating lighting will change the look. File checksums were verified for this release, but it has not been playtested in game since.
