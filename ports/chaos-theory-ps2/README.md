# Original PS2 Versus maps

Fourteen levels recovered from the European PlayStation 2 disc of *Splinter Cell:
Chaos Theory* (`SLES_53287`), including both tutorials. The package code and display
name end in `P`, for example `ORP14P` / **Orphanage P**, so they coexist with PC maps.

This source release supports the separately published OpenSCCT collection.
Native Enhanced/Reloaded publication remains pending separate validation. OpenSCCT
passes load/render checks on all fourteen maps and the original objective profile
smoke on DTK02P. OpenSCCT downloads use the OpenSCCT-Content catalog after runtime0.8.156 is published.

| Map | Package | Notes |
| --- | --- | --- |
| Deftech Belew P | `DTK02P` | [Notes](deftech-belew/README.md) |
| Factory P | `FAC13P` | [Notes](factory/README.md) |
| Station P | `GAR09P` | [Notes](station/README.md) |
| Cinema P | `INI01P` | [Notes](cinema/README.md) |
| Krauser Lab P | `KRA07P` | [Notes](krauser-lab/README.md) |
| Mount Hospital P | `MHO05P` | [Notes](mount-hospital/README.md) |
| Missile Strike P | `MIS10P` | [Notes](missile-strike/README.md) |
| Museum P | `MUS04P` | [Notes](museum/README.md) |
| Orphanage P | `ORP14P` | [Notes](orphanage/README.md) |
| Schermerhorn P | `SCH03P` | [Notes](schermerhorn/README.md) |
| Vertigo Plaza P | `SKY08P` | [Notes](vertigo-plaza/README.md) |
| Mercenary Training P | `TME12P` | [Notes](mercenary-training/README.md) |
| Spy Training P | `TSP11P` | [Notes](spy-training/README.md) |
| Warehouse P | `WAR06P` | [Notes](warehouse/README.md) |

## Installing

The planned native release is for Enhanced/Reloaded Versus. It is not in
the native catalog until validation completes. It will install the complete map and
its supplied `P2_` packages through SCCT Map Manager or copy the release ZIP's
`Packages` tree into the game. Other players need matching files. Editable brush
history is not recovered; these are converted compiled levels.

OpenSCCT uses separate converted content packs in
[OpenSCCT-Content](https://github.com/Lumbridge/OpenSCCT-Content). The minimum
supported game version for the PS2 objective profile is **0.8.156**. Publish and
validate that runtime, including the actual source pickup input path, before
making these packs available. The current content-index format is unchanged.

## Source and conversion

Each map's `source-provenance.json` records the original LIN path, byte size and
SHA-256, and every converted native package's path, size and SHA-256. The complete
[source manifest](evidence/source-manifest.json) also identifies shared COM, menu
streams and PS2 sound banks. `P2_` namespaces isolate recovered shared assets.
Unknown source names retain stable numeric identities instead of guessed names.

The recovery replays the console's ordered archive reads, resolves common/map
object references, converts PS2 native geometry, palettes/textures and audio to PC
serialization, then builds OpenSCCT maps against the existing shared class/audio
hashes. Native packages and OpenSCCT objective overlays are separate artifacts.

## Objective fidelity

OpenSCCT restores the original green vial, animated computer proxy and sabotage
modem profile. The source flag follows its authored computer, drop zones use their
source touch behavior, and the modem preserves captured progress when destroyed.
The native PC ports use the compatible PC interaction/presentation path. They
use the source computer interaction offset of 90 units as the default; specific
native endpoints and flag placement use reviewed PC clearance adjustments recorded
in the per-actor audit. Those native clearance adjustments do not claim original
PS2 stand distances. OpenSCCT uses the original PS2 computer-plus-25 vial position
and rotation, including the authored initial pose, independently of the native
compatibility adjustment. Its pickup approach uses the decoded source 80-unit
target and conditional reposition physics, including the source crouch lift.

The recovered objective overlay has **41 source objects**: both static meshes
match source positions, normals, UVs, section assignments and winding; all **13
texture images** match decoded PS2 RGBA pixels. The computer uses the original
PS2-authored `nd133_1mesh.nd133_mesh` retained in the retail PC files: its bounds,
18 bind bones and all 72 animation tracks match the PS2 source. The cooked PS2 GPU
vertex stream has not been proved identical to the retained PC render geometry.

Four constant zero quaternion keys in the alarm/CTF clips become unit identity
quaternions for glTF. Native PS2 instructions prove the same identity matrix;
their authored zero translations remain unchanged. All other rotation keys and
all translation/time arrays pass the independent final audit in all 14 maps.

The modem active beep uses the same-class retail compatibility alias
`Armes_impacts.Armes.ProxMine_ACTI_1`; exact PS2 PCM is not claimed for that sound.
Its destruction sound uses recovered PS2 PCM. The original UI contributes 50
preview/loading images, all with matching decoded pixels.

## Validation

Automated source/serialization/pixel/geometry/animation audits pass. They do not
establish a completed match or visual parity during play. Native loading, host
menu enumeration and actual native matches remain pending in this draft. The
OpenSCCT real client/server smoke checks the vial, console, panner, alarm, modem,
destruction and carried-vial binding on DTK02P; all fourteen maps pass load/render
captures. This does not claim fourteen completed matches. Per-map `validation.json`
records the exact scope.

The [evidence index](evidence/index.json) binds the portable audit reports to their
SHA-256 hashes and to the original local report hashes. [Objective source
bindings](evidence/objective-bindings.json) distinguish exact captures, retained
original authored assets and the explicit audio compatibility alias. The
[converter source artifact](conversion-source.json) preserves the actual scripts,
builder snapshot and name/schema metadata, without the raw ISO or executable.
