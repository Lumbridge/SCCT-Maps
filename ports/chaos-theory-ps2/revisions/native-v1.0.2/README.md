# Native PS2 Neutralization through the PC Story menu — 1.0.2

Choose **Story** in Enhanced/Reloaded when hosting these twelve PS2 maps.
Their gameplay is the original Neutralization objective chain: hack the animated
ND133 cases in place. Extraction, vial carrying and Sabotage remain excluded from
this native profile. OpenSCCT and the two one-sided native tutorials are unchanged.

Version 1.0.1 used the original Neutralization mode ID 3. The shipped PC selector
only handles Disk Hunt, Story, Deathmatch and Merc Deathmatch; a normal Story
launch therefore activated no mission, hid the cases and displayed zero objectives.
The explicit mode-3 editor tests did not cover this path. Version 1.0.2 maps only
the source Neutralization SMission value 3 to supported PC Story value 5, and
advertises Story in the native map settings. No other world or gameplay field is
changed from the reviewed 1.0.1 profile.

Independent comparisons pass for all twelve worlds: geometry, rendering/lightmaps,
PlayerStarts, class visuals and shared dependency bytes are preserved. Twelve clean
Story-mode launches load 74 case actors, show active visible cases and positive HUD
objective totals. Station additionally loads the real GAR09P filename, follows the
native Loading_Menu start path, and completes a normal ten-second Use hack with
the mission counter changing from 3 to 2. The named-flow proof explicitly uses a
calls-only test bridge, without a ProcessInternal detour or game-text change;
pawn placement is setup, and objective fields/timers are never written. The clean
twelve-map activation batch has no game hook or renderer proxy. These tests do not
claim twelve completed matches, every front-end click, or remote-client parity.

The release contains 24 changed map/UI files and 54 byte-identical dependency
copies, plus twelve complete map ZIPs. Every dependency uses the version-1.0.2
release tag as required by the released Map Manager 0.6.2 parser. The other 118
ordered catalog entries, including both native tutorials, remain unchanged.
