# PS2 Version maps for Enhanced/Reloaded

Revision **1.1.0** lists each supported native mode separately: **31 competitive
entries** (10 Extraction, 9 Sabotage, 12 Neutralization), plus the two retained
one-sided training levels. Names use **PS2 Map (Mode)**; package codes keep `P` as
their final suffix. Neutralization preserves its existing map IDs and SDC bytes.

Use **SCCT Map Manager 0.6.3** and the **PS2 Version** filter. Choose the named
mode variant, then select **Story** in the PC lobby. Each package activates only
its selected original objective graph through the supported PC mode 5 selector.
The variants coexist and require their supplied, hash-matched `P2_` dependencies.

| Map | Extraction | Sabotage | Neutralization |
| --- | --- | --- | --- |
| PS2 Deftech Belew | [`DTK02EP`](deftech-belew-extraction/README.md) | [`DTK02SP`](deftech-belew-sabotage/README.md) | [`DTK02P`](deftech-belew/README.md) |
| PS2 Factory | [`FAC13EP`](factory-extraction/README.md) | [`FAC13SP`](factory-sabotage/README.md) | [`FAC13P`](factory/README.md) |
| PS2 Station | [`GAR09EP`](station-extraction/README.md) | [`GAR09SP`](station-sabotage/README.md) | [`GAR09P`](station/README.md) |
| PS2 Cinema | — | — | [`INI01P`](cinema/README.md) |
| PS2 Krauser Lab | [`KRA07EP`](krauser-lab-extraction/README.md) | [`KRA07SP`](krauser-lab-sabotage/README.md) | [`KRA07P`](krauser-lab/README.md) |
| PS2 Mount Hospital | [`MHO05EP`](mount-hospital-extraction/README.md) | [`MHO05SP`](mount-hospital-sabotage/README.md) | [`MHO05P`](mount-hospital/README.md) |
| PS2 Missile Strike | [`MIS10EP`](missile-strike-extraction/README.md) | [`MIS10SP`](missile-strike-sabotage/README.md) | [`MIS10P`](missile-strike/README.md) |
| PS2 Museum | — | [`MUS04SP`](museum-sabotage/README.md) | [`MUS04P`](museum/README.md) |
| PS2 Orphanage | [`ORP14EP`](orphanage-extraction/README.md) | [`ORP14SP`](orphanage-sabotage/README.md) | [`ORP14P`](orphanage/README.md) |
| PS2 Schermerhorn | [`SCH03EP`](schermerhorn-extraction/README.md) | [`SCH03SP`](schermerhorn-sabotage/README.md) | [`SCH03P`](schermerhorn/README.md) |
| PS2 Vertigo Plaza | [`SKY08EP`](vertigo-plaza-extraction/README.md) | — | [`SKY08P`](vertigo-plaza/README.md) |
| PS2 Warehouse | [`WAR06EP`](warehouse-extraction/README.md) | — | [`WAR06P`](warehouse/README.md) |

Mercenary Training (`TME12P`) and Spy Training (`TSP11P`) retain their native
version 1.0.0 files and training routes. Their names and category are clarified;
they are not advertised as competitive variants.

The release combines original PS2 layouts, recovered assets, English labels and
animated ND133/vial presentation with compatible PC gameplay. Extraction uses
the PC flag interaction/carry/delivery rules; Sabotage adapts source target areas
to linked PC modem points. Per-map provenance preserves original graphs,
references and source/target positions. This is a documented native adaptation,
with no replacement of global Core, Engine or SBase scripts.

The independent offline audit passes all 31 worlds, 62 unique map/UI identities,
117 unique payloads and 20,627 property bags. Named Story activation passed on all 31
frozen maps in private native runs. Source/compiler hashes and qualified native validation are recorded in the
shared evidence. Publication and installation verification have separate receipts. Representative
gameplay and visual receipts retain their specific coverage/instrumentation
qualifications; separate-machine Internet multiplayer and complete matches on
every map are not claimed. OpenSCCT uses its separate published content.

## Converter source

[Native 1.1.0 source snapshot](https://github.com/Lumbridge/SCCT-Maps/releases/download/ps2-original-svm-v1.1.0/SCCT-PS2-SVM-converter-source-v1.1.0.zip)

SHA-256: `98247552c5b8ec378eb4cc733a148211ff7b213cc6e8db905f74fc489e2f9abf`. The [source record](revisions/native-v1.1.0/converter-source.json)
and [manifest](revisions/native-v1.1.0/SOURCE-MANIFEST.json) bind the converter,
compiler recipes, exact name/schema metadata and independent validation sources.
