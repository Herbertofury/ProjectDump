# Potatoptimize Forge 1.20.1 - Parity Safe Port

A native Forge 1.20.1 port of Tater-Certified's Potatoptimize 1.20.1 optimization set.

## Design contract
- Minecraft 1.20.1, Forge 47.4.23+, Java 17.
- Vanilla-parity / low-risk optimizations are the only default-on set.
- Behavior-changing, RNG-changing, chunk-loading-changing, profiler-removing, unsafe, or experimental threading optimizations are default **OFF**.
- User overrides remain available through `config/potatoptimize.properties`.
- An opt-in example lives at `assets/potatoptimize/potatoptimize-aggressive.properties.example` inside the JAR/source.
- Built-in conflict avoidance covers ModernFix, ServerCore, Krypton variants, C2ME, FasterRandom, Chronos Carpet Addons, and Lithium/Canary/Radium-style explosion optimization overlaps where relevant.

## Upstream
Source lineage is pinned to Potatoptimize `1.20.1` commit `35d97cf913ae39d45740a51d23cdd161d06e4a43`, with selected modern parity fixes backported where applicable.

## License
The upstream 1.20.1 source is GPL-3.0-only. This port preserves that license and derivative-source availability.

## Strict parity default
The broad `memory.reduce_alloc` family is intentionally OFF by default in this Forge port. Several legacy members reuse mutable arrays that vanilla normally recreates; while useful for allocation pressure, that identity/mutation behavior can be observed by other mods. It remains opt-in rather than being mislabeled as zero-risk.

Known aggressive-path guards also automatically disable conflicting pathfinding/explosion rewrites when Valkyrien Skies or EnhancedVisuals is present.
