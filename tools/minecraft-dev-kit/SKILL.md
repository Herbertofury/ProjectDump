---
name: minecraft-dev-kit
description: "Build, port, convert, benchmark, test, and release Minecraft mods with the user's Minecraft Dev Kit and real runtime proof. Use for Forge/NeoForge/Fabric/Quilt development, version ports, Bedrock-to-Java conversions, gameplay/worldgen/network changes, model/texture/animation implementation, premium mob/boss pack production, reference-to-model reconstruction from images/GIFs, authorized server-plugin/resource-pack asset conversion into native mod assets, cache/toolchain work, release QA, or explicit in-game testing. For a primarily broken user instance/modpack/log/JAR/world, prefer Minecraft Repair; if Repair or Visual QA is invoked as a subtask, preserve this Dev Kit acceptance state and return to its exact next action. Compose with zero-loss-chat-accelerator when installed; never restart resolved work on skill activation."
---

# Minecraft Dev Kit

Treat each Minecraft development task as one acceptance contract. Compilation is intermediate evidence; prove behavior in the strongest applicable real Minecraft runtime.

## Zero-Loss composition

Compose with `zero-loss-chat-accelerator`: preserve acceptance, canonical IDs/paths, evidence freshness, hashes/run IDs, last mutation/test/checkpoint, blockers/no-repeat history, and exact next action across skill/tool/handoff changes. Use single-flight reads, implementation crossing, retry-only-with-new-information, checkpoint-before-long-gate, and a strategy change after two no-progress waves. Do not enumerate whole Dev Kit/Drive/skill trees when exact IDs/paths are known. Native runtime proof is never replaced by orchestration shortcuts.

## Core workflow

1. Resolve canonical project, Minecraft/loader/Java versions, source lineage, requested artifact, Dev Kit, and current verified checkpoint. Reuse known-good caches/toolchains.
2. Establish one factual baseline from source/build metadata and fresh relevant QA; do not repeat it after skill switches.
3. Make the narrowest complete edit, then run cheap changed-path/static checks first.
4. Run real dedicated-server proof for common/server/registry/world/network/data/save changes; run real client/integrated-server proof for rendering/models/textures/animation/UI/sound/input/synced gameplay. Read `native-runtime-qa.md` before native client work.
5. For ports, follow `port-conversion-gates.md`; use `vanilla-feature-atlas.md` for cross-version vanilla dependencies.
6. Inspect fresh logs/captures and live state; diagnose -> repair -> retest every task-related failure. Repair/Visual-QA skills are bounded subroutines that return here.
7. At convergence, build/hash/package source + runnable artifact + evidence, then persist the coherent checkpoint to Drive and repository-owned GitHub state when applicable.

## Reference reconstruction mode

Use when authorized image/GIF/video evidence must become a Minecraft model, texture, prop/entity/cosmetic, or animation. “Exact” means measured observable parity; hidden surfaces stay inferred until observed.

1. Read `references/reference-exact-reconstruction.md` plus only the relevant pixel/animation/model reference.
2. Prefer `reference_reconstruction_pipeline.py`: preserve/hash media, probe motion, inverse-fit camera/cuboids and GIF bone poses, back-project visible texels, then run strict still/GIF parity. Use individual tools for bounded subproblems.
3. Solve camera -> silhouette/depth -> pivots/UV/material -> motion; never distort a later layer to hide an earlier error.
4. Keep the reconstruction contract, source hashes, fit reports and coverage/parity evidence; use Project Visual QA for real multi-view/multi-time renders.
5. Native client/integrated-server proof remains required for scale, lighting, culling, grounding, state sync and gameplay. Never claim unseen geometry was recovered exactly.

## Premium mob-pack production mode

Use for original commercial-grade mob/boss families. Read `references/premium-mob-pack-production.md`; load art/animation/AI and creature-spec/rig references only for the active subproblem. Scaffold with `premium_mob_pack_scaffold.py`; use the blockout/UV/spec tools for original model structure; at convergence run `premium_mob_pack_pipeline.py`, then Visual QA and native runtime stress proof. Marketplace counts benchmark scope, never original art/gameplay/runtime quality.

## Server asset conversion mode

Use for **authorized** server packs/configs, `.bbmodel`/`.ajmodel`, ModelEngine/Mythic-style packs, custom-item/furniture systems, or downloaded resource-pack assets that must become complete native mod assets.

1. Read `references/server-asset-conversion.md`; add `server-plugin-ecosystem.md` when ecosystem/renderer choice matters.
2. Hash/preserve source and rights; prefer `server_asset_pipeline.py` for staged intake, registry audit, plugin/extension inventory+coverage, IR/link/renderer/manifest, or use individual tools for a bounded subproblem. Never bypass encryption, obfuscation, pack protection, paywalls, or licensing controls.
3. The pipeline validates `server-plugin-registry.json`, reads Bukkit/Paper/Bungee/Velocity/Geyser-extension metadata without executing JARs, runs broad + category-aware long-tail semantic IR, then first-class/resource/model adapters, cross-link audit, renderer selection and the conversion manifest. Unknown plugins are semantically triaged into review-only registry candidates, and unmatched family fields stay explicit; preserve every intermediate report as provenance.
4. Prefer authoring source -> plugin configs -> generated RP -> runtime evidence -> visual reconstruction. Recover **visual**, **model-runtime** (states/special bones/seats/hitboxes/locators), and **gameplay** (AI/skills/targeters/items/furniture/drops/persistence) layers independently; visual-only is not a full conversion.
5. Translate semantics into normal target-mod logic and choose the least-lossy version-compatible renderer (native, GeckoLib/AzureLib, direct `.bbmodel`, player/CEM route) rather than forcing one library.
6. Translate cross-version asset schemas explicitly; preserve every source state. Require dependency closure, deterministic parity, and strongest applicable native client/server proof. Missing server-only semantics remain explicitly unknown until sourced or reconstructed.

## Validation scheduling: prevent gate thrash

Do not run the entire static + server + client + package stack after every edit.

- During iteration, run the cheapest decisive changed-path test that can falsify the current fix.
- After a real state change, rerun only gates invalidated by that change.
- Run the strongest applicable native runtime gate once the candidate is coherent; rerun it only after a change that could affect its proof.
- Run broad release/package gates at convergence, not as a repeated reassurance loop.
- Before a long native/CI gate, preserve a source checkpoint and current runnable candidate when practical.

If a native process must outlive the orchestration command and the environment supports safe detachment, launch it detached, record the exact PID/run identity, observe authoritative milestone/log markers, and clean up only that identity. A shell/foreground timeout is not proof Minecraft hung. Do not exceed two unchanged milestone/status observations; then do independent work or change the evidence route rather than busy-waiting.

## Runtime verification policy

Choose the strongest applicable gate:

- **Compile/build only:** only when no meaningful runtime behavior changed or no runtime can realistically be executed; state that limitation.
- **Dedicated server:** require real readiness (`Done (...)!`) for affected server/common paths, then exercise the changed workflow and inspect the fresh log.
- **Native client:** require for visual/entity/animation/client-integrated behavior when feasible.
- **Client + integrated server:** prefer for synced entity state, gameplay, commands, datapacks, rendering tied to server state, and conversion QA.
- **Restart/persistence:** require for save/config/state changes.

A deterministic renderer/unit/model audit can complement native proof but cannot replace it when the defect exists only in the actual client.

## Native visual QA minimum

For model/entity/animation work, follow `references/native-runtime-qa.md`. At minimum:

- use a deterministic QA world/camera/time/weather fixture;
- assert authoritative live entity/state counts after each phase;
- capture the actual Minecraft window/runtime evidence;
- inspect non-obvious animation frames and fresh logs;
- fail disappearing/floating/clipping models, transform accumulation, missing textures, or task-related model/atlas warnings.

For custom articulated models, ensure custom parent/root `ModelPart`s return to bind pose before additive per-frame transforms. Transform accumulation is a release blocker.

## Cache and offline-first policy

Prefer verified Dev Kit JDK/Gradle/loader/cache assets over network resolution. Reuse known-good caches; do not repeatedly redownload or re-audit unchanged assets.

For Forge 1.20.1 native client work, the established path is:

```text
mmv-devkit cache-doctor
mmv-devkit client-assets
mmv-devkit client-natives
world QA normalization / command enable
Gradle runClient
native capture + authoritative log assertions
```

Run cache-doctor only when cache integrity is unknown, stale, or implicated; a previous green cache result remains valid until the cache changes.

Full Mojang external asset objects are required when sound/resource completeness is under test. A visual-only harness may use a verified mapped client JAR only when it explicitly proves the resources it needs and reports unavailable external sound objects truthfully.

## Versioned vanilla dependency closure

Never delete/stub a target-missing vanilla identifier. For ports, record the full cross-version dependency closure with `vanilla-feature-atlas.md`, certify the mod-owned target-native base first, then offer any future-vanilla parity layer explicitly. Keep it default OFF until opt-in and prove provider-present/absent/fallback/removal lanes as applicable.

## Port-first / opt-in backport invariant

Base port first: complete and certify all mod-owned content with future-vanilla additions disabled. Then publish an exact requirements manifest, offer the parity layer even when none is needed, require explicit opt-in, and certify that layer separately while preserving the runnable base. Never use an optional backport to hide an incomplete base conversion.

## Production-linkage and Forge special gates

For optional-provider/future-feature bridges or code crossing mapped-dev and production Forge APIs, read `references/future-feature-bridge-qa.md` and run its production-linkage gate before native launch. For namespace/remap/Mixin/reflection/invokedynamic hazards, also read `references/forge-production-client-qa.md` and require a real packaged `forgeclient` gate when userdev can hide the defect.

Known stall-relevant hazards:

- a foreground/container timeout is not a hang; prefer detached exact-PID milestone observation;
- hard-killing `runClient` can corrupt generated runtime config, so repair/validate it before relaunch;
- do not repeatedly rediscover window/PID state when the exact process is already recorded;
- a successful command is not proof of a live rendered entity;
- mapped-dev success is not proof of production JVM symbolic linkage.

The detailed false-pass catalog lives in the three QA references above; load only the one(s) implicated by the current failure.

## Evidence and release contract

For a substantive release preserve the exact build command/result, final artifact hash/size, source checkpoint, applicable static/server/client evidence, warnings classified as task-related vs benign, known limitations, and Drive/GitHub publication identities.

Do not call a release verified if the strongest applicable runtime gate was skipped without stating why.
