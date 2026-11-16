# Native PS2 Neutralization revision 1.0.1

Twelve versus maps use the original ND133 console appearance with compatible PC Neutralization gameplay. Both tutorials retain their version 1.0.0 catalog entries and files. OpenSCCT modes and source origins are separate and unchanged.

The map-local PS2Computer class source and exact compiler provenance are included in the converter artifact. No stock script package is modified. The compiled bytes autoload normally as P2_PS2Objectives.usx from Packages/StaticMeshes. All changed SDC/UI package GUIDs are derived from their content, while unchanged dependencies retain their bytes and identities.

The exact final bytes pass clean native loading on all 12 versus maps using a
byte-identical Autoplay bootstrap alias. A separate clean, ordinary-input Station
check completes the ten-second hack and changes the mission counter from 3 to 2.
Idle, hacking and completed console images use calls-only instrumentation, with
unchanged game code; that visual evidence is separate from the clean input proof.
A private fixture changes only player spawn positions for those Station checks.
The strict world and package identity audits pass. Fresh named-world travel and
full routes were not repeated for all final maps, and native remote multiplayer
and twelve completed matches are not claimed. See the versioned receipts under
`evidence/`.

The distribution catalog copies 54 unchanged dependencies under the version 1.0.1 release tag. Map Manager 0.6.2 requires every dependency tag to match its map entry version. These copies retain their original bytes, hashes, sizes and destinations; the earlier draft receipt that describes 187 reused version 1.0.0 URLs is superseded only for URL placement. Both training entries still use their original version 1.0.0 files. The converter ZIP, maps and runtime validation receipts are unchanged. See `asset-url-compatibility-correction.json` for the supplemental distribution record.
