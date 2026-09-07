# Potatoptimize Forge 1.20.1 - Parity Safe Port

A native Forge 1.20.1 port of Tater-Certified's Potatoptimize 1.20.1 optimization set, rebuilt around a conservative rule: **vanilla parity is the default; behavior-changing speedups are opt-in**.

## Target
- Minecraft **1.20.1**
- Forge **47.4.23+**
- Java **17**
- Native Forge packaging/remapping via Architectury Loom

## Default profile
Only the small set that survived a strict equivalence audit is enabled by default:
- `mixin.block_entity.sign_ticking = true`
- `mixin.logic.data_bits = true`
- `mixin.unstream.nearest_item = true`

Everything involving changed RNG sequences, altered chunk-loading semantics, executor/thread replacement, profiler removal, unsafe random, entity/client threading, teleport/fall/stat behavior, world-save suppression, explosion replacement, heuristic world logic, semivanilla navigation, or other uncertain semantics starts **OFF**.

The generated `config/potatoptimize.properties` writes every effective option explicitly on first run, so there are no hidden aggressive defaults. Experienced users can opt into selected rules individually; an example is included at `assets/potatoptimize/potatoptimize-aggressive.properties.example`.

## Forge compatibility hardening
The Mixin plugin performs loader-safe early detection so known overlap rules are disabled before they can apply. Current guards cover ModernFix, ServerCore, C2ME, FasterRandom, Chronos Carpet Addons, Lithium/Canary/Radium-style explosion replacements, Valkyrien Skies, and EnhancedVisuals where relevant.

Krypton Reno/FNP is also detected for diagnostics. The old upstream Krypton guard referenced `mixin.logic.var_int`, but that optimization does not exist in this 1.20.1 source set, so this port deliberately does **not** pretend there is an overlap to disable.

## Upstream bugs / portability issues repaired
- Native Forge bootstrap and metadata replace Fabric-only initialization.
- Fabric loader/environment dependencies were removed or replaced with Forge equivalents.
- Modern navigation-cancellation semantics were backported; the rule is still opt-in because upstream classifies navigation as semivanilla.
- `ChunkSectionPos.stream(center, radius, minY, maxY)` now honors the supplied vertical bounds instead of hardcoding sections `0..15`; the family remains opt-in pending broader parity proof.
- The 1.20.1 travel-stat fast-rounding mixin now targets the class that actually declares the method.
- Worker-executor overwrite visibility now matches the target method.
- A FastUtil injection point is explicitly excluded from Minecraft remapping, removing a production remap hazard.
- The legacy broad `memory.reduce_alloc` family is opt-in because some members reuse mutable arrays where vanilla creates fresh arrays, which can be observable to other mods.
- Known Valkyrien Skies pathfinding and EnhancedVisuals explosion collisions are automatically guarded.

## Upstream lineage
Source lineage is pinned to Potatoptimize `1.20.1` commit `35d97cf913ae39d45740a51d23cdd161d06e4a43`, with selected modern parity fixes backported where applicable.

## License
The upstream 1.20.1 source is GPL-3.0-only. This derivative port preserves the GPL license and source availability.
