# Potatoptimize Midnight + DimThread + C2ME benchmark

Native Forge 1.20.1 A/B benchmark for the certified Potatoptimize parity-safe profile.

Common stack in both A and B:
- The Midnight 0.6.7 (with the Noxviola v4 `onLevelTick` serialization repair)
- SmartBrainLib 1.20.1-1.15
- Dimensional Threading 1.2.1 with Noxviola PER-OBJECT-INTEROP-v3 content
- C2ME Forge 0.2.0-forge.9.1 with the Noxviola PERF-HARDENED-v3 transforms carried forward plus v4 DimThread effective-main interop
- Forge 47.4.23 / Java 17

B adds only the exact certified Potatoptimize r1 JAR (SHA-256 `5292a29d99eb4f51ef130043b5189b316d8f9274c459a47c8c03a2e0408832c6`).

The template forces Overworld, Nether, and `midnight:midnight` active simultaneously and creates sign block-entity, villager/item-sensor, and palette/chunk workloads. Three repetitions per case run on one hosted runner in ABBAAB order. Forge rolling MSPT is sampled 12 times per repetition; a cloned-world fresh-region generation/fill/save challenge is timed separately.

A >=3% median steady-state MSPT improvement with no >5% generation regression is classified as a real gain. Any runtime deadlock/CME/mixin/linkage signature fails the gate.
