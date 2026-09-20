# Sublabs (sub18)

Editable version of Sublabs, recovered from the compiled map with the Reloaded Editor (saved 15 September 2026). It keeps the `sub18.sdc` filename so it works with the existing menu entry, and **replaces the installed `sub18` map**.

## Install

1. Close the game and the editor.
2. Back up any files with the same names.
3. Copy the `Packages` folder into your Enhanced SCCT Versus 3.6 installation.

Playable map: `Packages/Maps/sub18.sdc`. Editable map: `Packages/MapsEd/sub18.sdc` (open it in the Reloaded Editor).

Keep every included mesh and texture package with the map, and do not rename `sub18_Recovered_Assets.usx`; the map refers to it by name.
The older `sub18_Assets.usx` is included too, for files that still reference it.

## What to expect

The recovery rebuilt 333 structural brushes and kept 1,812 actors, and the map builds, saves and reopens cleanly. Original brush history is not preserved. The original baked lighting is kept; recalculating lighting will change the look. File checksums were verified for this release, but it has not been playtested in game since.
