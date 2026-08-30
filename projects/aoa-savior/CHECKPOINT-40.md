# AoA Savior Checkpoint 40 - Batch34 Nowhere Direct-Melee - Server/Common Runtime Proven

Date: 2026-08-30
Source authority: AoA 3.6.11 source, `Tslat/Advent-Of-Ascension` branch `1.16.5`, commit `822ea7515eebf5756a43b436c8616594f1c48a4f`
Target: Minecraft 1.20.1 Forge 47.4.23 / Java 17
Baseline: frozen Checkpoint 39 v6; CP39 was not mutated.

## Restored family

Batch34 restores eleven direct-melee Nowhere entities:

- Fenix
- Ghastus
- Goldum
- Goldus
- Reaver
- Shavo
- Skeledon
- Skelekyte
- Urioh
- Urv
- Visage

The port preserves source-backed dimensions, attributes, eye heights, sound identities, undead flags, Ghastus per-tick healing, Goldus Pure Gold reward ownership/deduplication, Reaver body-slam knockback, Skeledon/Skelekyte cloak cadence and invisibility payload, Urioh health-scaled dimensions, Urv golem step, and the Visage host/mirage server contract plus source-faithful client mirage state logic.

## Fail-closed repair history

The first complete native runtime attempt that reached the Batch34 gate intentionally failed closed on three QA-fixture defects:

- Urioh was being measured before the fixture was explicitly put into canonical full-health state.
- Skeledon and Skelekyte cloak probes were polluted by the test entity's no-AI physics state.

No source behavior was weakened. The repaired harness explicitly establishes Urioh's full-health fixture state and factors the exact cloak payload into a deterministic QA helper while production `aiStep()` still owns the 80-tick trigger.

Failed proof is preserved in `receipts/cp40-batch34-native-v2.log` and its exit receipt.

## Final dedicated-server proof

Final native gate: `cp40-batch34-native-v3`

- Forge readiness: `Done (21.066s)!`
- Batch34 semantic entity rows: 11 / 11 true
- Batch34 live runtime entity rows: 11 / 11 true
- special/shared matrix: every Batch34 boolean true
- Batch34 aggregate: `shared=true entity_semantics=true runtime=true batch=true`
- global harness: `nowhere_melee=true bulk=true entities_expected=146 bulk_expected=61`
- final validator: `dimensions=11 entities=146 bulk_melee_waves=61 ... wave33_semantics=15 wave34_semantics=20`
- clean `Stopping server`
- every dimension saved
- Gradle `BUILD SUCCESSFUL in 1m 4s`
- wrapper exit: 0
- Gradle exit: 0
- independent runtime audit: 12 / 12 PASS
- independent static/source-contract audit: 19 / 19 PASS

## Build candidate

- source build output: `build/libs/aoa3-0.6.0.jar`
- SHA-256: `07b3ad6202ce01fc31d19bd59f7616638491215ab2fc7ac315dcdf6362b6ab8c`
- size: 512,877 bytes

The candidate was built with the Dev Kit's exact Forge 1.20.1 / 47.4.23 Gradle cache, Gradle 8.8, and Temurin JDK 17.0.20.1+1. The recovered Gradle cache matched its Dev Kit manifest SHA-256 `6929fe95880d90a504ddee419e90037ba9b5aa64ac2ac9482a65901f8f82710b` before use.

## Progress after Checkpoint 40

- restored missing semantic rows since CP04: 168
- decisive present/restored: 2,940 / 8,360 = 35.17%
- resolved including review: 36.18%
- entity IDs restored: 146 / 377 = 38.73%
- remaining missing entity IDs: 231
- dimension spine: 11 / 11 dimensions and 11 / 12 dimension types
- curated melee candidate pool: 78 / 78

## Client-visual status

The upstream client source mapping has been recovered and recorded in `receipts/cp40-batch34-client-source-map.md`. Dedicated models exist for the cohort; Goldum/Goldus intentionally share `GoldCreatureModel`, while Visage has a dedicated `VisageModel` and texture.

This checkpoint deliberately does **not** claim native client visual/render fidelity for Batch34. The exact 3.6.11 binary texture payload is not contained in the restored checkpoint and an exact Drive search did not locate the original AoA JAR. The server/common mechanics are runtime-proven; native client model/texture/render proof remains the next visual gate rather than being silently waived.

## Promotion rule

Checkpoint 40 is the sealed server/common mechanics checkpoint. Full visual promotion of Batch34 requires exact source assets/model adaptation, renderer registration, and native client proof of the real entities and Visage mirage rendering. No placeholder or guessed renderer is accepted as parity.

## Durable artifacts

- Canonical AoA Drive folder: `1wqWkeEqcNI3VVeqoNxzd0a-J8oPde_Xn`
- CP40 ZIP Drive file: `1Sz_Mwb03RrEqLWIqEQO3xzxpOLl2deGJ`
- CP40 JAR Drive file: `1gBErBh4hSrDFXErUcL7qWT1Tea2_bDfa`
- CP40 checkpoint Drive file: `16bYVPdo2sWH1lhxg9AGpi-lmWbCiyyRf`
- CP40 checksum Drive file: `1iZ1FIN6nLrDuphIO_ABi2WQ1o6-281WL`
- Drive publication receipt: `1V5fvisaxhunMvbTT2StP8VIyl5DPqMsR`
- CP40 ZIP SHA-256: `7d8b691d...bdccb`
- CP40 JAR SHA-256: `07b3ad6202ce01fc31d19bd59f7616638491215ab2fc7ac315dcdf6362b6ab8c`
