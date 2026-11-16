# Station P (GAR09P)

**Enhanced/Reloaded version 1.0.1 supports Neutralization only.** Hack the ND133
consoles in place. Extraction, vial carrying and Sabotage are not selectable in
this native revision. OpenSCCT retains its separate original mode set.

The map-local `P2_PS2Objectives.PS2Computer` class displays the original animated
ND133 console and source materials while retaining the existing PC interaction,
capture timer and collision behavior. Active Extraction flag entries are omitted
from this Neutralization level's actor array, preventing the inherited PC racks.
No global stock script package or other map is replaced.

Install or update through SCCT Map Manager 0.6.2 or newer, keeping every supplied
dependency. The compiled class is distributed as `P2_PS2Objectives.usx` in
`Packages/StaticMeshes`, a normal native autoload path. Its retained stock
`nd133_1mesh` animation package must be present in the game. Other players need
matching files; changed map/UI packages have new content-derived network GUIDs.

Source geometry, lightmaps, PlayerStarts and nonobjective properties are unchanged.
Reviewed player-facing labels are English; IDs, tags and script keys are retained.
Editable brush history is not recovered.

The exact final bytes pass clean native loading on all 12 versus maps using a
byte-identical Autoplay bootstrap alias. A separate clean, ordinary-input Station
check completes the ten-second hack and changes the mission counter from 3 to 2.
Idle, hacking and completed console images use calls-only instrumentation, with
unchanged game code; that visual evidence is separate from the clean input proof.
A private fixture changes only player spawn positions for those Station checks.
The strict world and package identity audits pass. Fresh named-world travel and
full routes were not repeated for all final maps, and native remote multiplayer
and twelve completed matches are not claimed. See the versioned receipts under
`../revisions/native-v1.0.1/evidence`.

The two original tutorial entries remain unchanged at version 1.0.0 and are
one-sided training, outside this competitive Neutralization release.
