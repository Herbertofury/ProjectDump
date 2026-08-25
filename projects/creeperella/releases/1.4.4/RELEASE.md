# Creeperella: Bloom & Boom 1.4.4 — Standalone Source-Pack Sidecars

Checkpoint date: 2026-08-24
Target: Minecraft 1.20.1 / Forge 47.4.23 / Java 17

## Objective
Every author-intended gameplay/visual sidecar from a supplied mob pack is carried into Creeperella as standalone namespaced content for that mob/family rather than discarded or applied as a global vanilla replacement.

## 1.4.4 Cherry sidecars
- `creeperella:cherry_gunpowder`: exact source sprite, Cherry Creeper drop, Forge gunpowder tag, Cherry TNT / Bonbon recipes.
- `creeperella:cherry_tnt`: exact source texture and namespace-only adaptation of the source Blockbench model; dedicated block/item/primed entity/renderer with standard TNT ignition/chain behavior.
- `creeperella:cherry_creeper_head`: generated from exact `head_creeper.jem`; standing/wall/item rendering and powered-Creeper skull-drop semantics.
- `creeperella:cherry_creebet`: exact 32x16 source painting art as a dedicated painting variant/item.
- Source English/Russian Cherry mob, spawn-egg, and head identity values preserved under Creeperella keys.
- Vanilla TNT, gunpowder, Creeper Head, paintings, and vanilla language keys remain untouched.

## Verification
- Complete source mirrors: Pie 21/21 + Cherry 12/12 + Cat 12/12 = 45/45 exact.
- 14/14 exact active source texture/egg/sidecar mappings.
- 14/14 exact generator/audit input mappings.
- 84 runtime JSON resources parse.
- Pie numerical animation parity: 712 sampled values.
- Cherry/Blossom numerical animation parity: 235 sampled values / 47 channels.
- Cat: 39/39 base cubes, 14/14 charged cubes, source target/sign accounting clean, no invented tail yaw/roll.
- 24/24 six-variant 3D egg states resolve.
- Deterministic QA only; no image generation.

## Persisted artifacts
Canonical Google Drive folder contains full 1.4.4 source, deterministic QA showcase, SHA-256 manifest, final verification, and source-pack parity report.

## Production boundary
Do not label a 1.4.4 binary production-verified until Java 17 ForgeGradle compile/remap and a real Forge 47.4.23 dedicated-server startup pass. Source/static/model/data/animation QA is green.
