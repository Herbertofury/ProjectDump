# Forge 1.20.1 Port Notes

## Default policy
The old 1.20.1 branch enabled many optimizations that could alter vanilla semantics. This port inverts that philosophy: uncertain or behavior-changing patches are opt-in.

Default-off includes chunk-loading avoidance, RNG replacement/sequence changes, explosion replacement, entity/client threading, unsafe random, profiler removal, fall behavior changes, teleport changes, statistics throttling, and other higher-risk patches.

## Modern fixes pulled back
- Navigation cancellation follows modern Potatoptimize semantics: riding a living entity no longer suppresses navigation ticking; only non-living vehicles take the fast path.
- Forge-native mod detection replaces FabricLoader detection.
- Additional Forge overlap guards are included for Krypton Reforged and Canary/Radium-style explosion optimization families.

## Compatibility
Potatoptimize mixins remain individually configurable. If a modpack exposes an interaction, disable only the implicated optimization rather than removing the entire mod.

## Additional strict-parity hardening
- `memory.reduce_alloc` is opt-in because legacy shared-array reuse can change observable object identity/mutation isolation.
- Valkyrien Skies automatically blocks `unstream.pathfinding` due to a known Pathfinder mixin collision.
- EnhancedVisuals automatically blocks `world.explosion` due to a known explosion injection collision.
