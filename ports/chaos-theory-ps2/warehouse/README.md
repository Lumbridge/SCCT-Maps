# PS2 Warehouse (Neutralization) (`WAR06P`)

Enhanced/Reloaded native revision **1.1.0**. Select **Story** in the PC lobby mode
selector. This separately named map activates the original source **Neutralization**
mission graph through PC mode 5, the mode supported by the shipped lobby UI.

Hack the recovered animated ND133 consoles using the existing PC interaction, capture timer and collision rules. This map’s SDC and shared/class packages are byte-identical to the accepted native 1.0.2 Neutralization baseline; the UI package updates its display name. Extraction and Sabotage have their own separately named entries.

The converted PS2 world, recovered materials, English labels and objective visuals
are combined with Enhanced/Reloaded-compatible PC mechanics. The map-specific
provenance records the original graph, retained references, visual classes and
explicit compatibility adjustments. This profile does not claim a complete
reimplementation of PS2 gameplay or separate-machine multiplayer validation.

Install through **SCCT Map Manager 0.6.3 or newer**, using **PS2 Version**, or copy
the complete release ZIP’s `Packages` tree into the game. Keep every dependency.
The map packages use `WAR06P` and `WAR06P-i`; other players need matching files.
Normal base-game assets, including the retained `nd133_1mesh` animation package,
must be present. The isolated `P2_` classes use normal StaticMeshes autoloading.
Global Core, Engine and SBase script packages are not replaced.

The independent offline audit passes for all 31 variants, 62 map/UI identities
and unchanged world geometry, render/lightmaps, spawns and unrelated properties.
All 31 frozen packages passed named Story activation in private native runs.
Source/compiler hashes and qualified native validation are recorded in the
shared evidence. Publication and installation verification have separate receipts.
Representative gameplay/visual evidence retains its individual instrumentation
and coverage qualifications; these checks do not establish completed matches on
every map. The original one-sided tutorials remain separate version 1.0.0 entries.

See `native-v1.1.0-provenance.json`, `SHA256SUMS.txt`, and the shared evidence under
`../evidence/v1.1.0/`. OpenSCCT content uses its separate published collection.
