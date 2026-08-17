# Feature Foundry Wiki

**Project Constellation ID:** `PRJ-002`  
**Status:** ACTIVE, major production rebuild; V24 executable reference verified  
**Connected repository:** [Herbertofury/Feature-Foundry](https://github.com/Herbertofury/Feature-Foundry)  
**Production-source boundary:** the connected repository still does not prove the complete production application source. The newest verified standalone lineage is V24, but it remains an executable reference rather than the canonical production app.

## Mission

Feature Foundry is intended to be a professional, deeply moddable authoring application for living theme worlds rather than a static theme generator or prototype gallery. It covers living worlds, UI skins, rooms, objects, weather, time, lighting, soundtracks, UI sounds, mascots, interactions, assets, research, mixing, packaging, and exports to multiple hosts.

The continuity rule is strict: database validation, standalone HTML demonstrations, generated starter packages, and design directives are valuable evidence, but none substitute for proving the real production application and its workflows.

## Current verified lineage

Project Constellation previously stopped at V11. Newer project-owned evidence now supersedes that latest-version claim while preserving all earlier history.

### V23 verified baseline

`feature-foundry-v23-validation-report.md` records **142 passed, 0 failed** for the V23 bundle. It records schema/build version 23.0.0, extensive Object Atlas and Theme Worlds integrity checks, a static UI audit, and **28 Chromium runtime checks with no page or console errors**.

Important V23 artifact identities:

- Object Atlas SHA-256: `dcf8e7000b6a32f3a0960e85d2b662d1d0d860e7f228975a35042f785bb56765`
- Theme Worlds SHA-256: `ed4a3f97b71e5927e7a191dfc0f6dfc7f67fbc07e012bdbb4b54c8122940c468`
- executable prototype SHA-256: `07b529aec512e0572630c802c431d3dd84b15f75a34746773ea726c1c506759d`
- master directive SHA-256: `5dbe307e8bd5a1e62d9968ce43f369b6223f0483993a6a2c82d0dd298da2dc5f`

The verified V23 runtime includes real object/context operations such as duplicate, lock/unlock, bring-to-front, layer reveal, delete/undo/redo, sticker pin/peel behavior, keyboard context invocation, object dragging, and persistence checks. It also preserves the rule that final production artwork and the canonical production application remain separate from the executable reference.

### V24 verified runtime hardening

`feature-foundry-v24-final-validation.json` records **PASS** for `feature-foundry-living-world-prototype-v24.html`, build **24.0.0**, 561,462 bytes, SHA-256 `353e39446238f5ad4a3006fc8eaa91b9a3e0138eb190c7de715ca267c7449403`.

The V24 validation records:

- inline JavaScript syntax PASS;
- **78 internal self-tests passed, 0 failed**;
- **14 external CDP assertions passed, 0 failed**;
- zero console errors;
- zero page exceptions;
- clean extraction PASS;
- ZIP integrity PASS;
- SHA-256 manifest PASS;
- Performance Mode and Focus UI suspend heavy runtime owners;
- living mode resumes governed owners;
- object count is preserved through suspension;
- moving-object physics state is suspended and resumed rather than discarded;
- measured adaptive quality responds to sustained frame/long-frame pressure;
- user-pinned quality modes remain authoritative;
- no card, object, workflow, or data quantity is removed to gain performance.

V24 centralizes scene lifecycle ownership in a Runtime Governor rather than allowing independent heavy loops to run indefinitely. Clock, ambient/environment/cinematic work, selection-HUD tracking, mascot autonomy, physics, quality monitoring, and long-animation-frame observation are released in suspended modes and restored when appropriate.

### V24 truth boundary

The V24 validation explicitly records that the **canonical production repository was not modified**. Treat V24 as the newest verified self-contained executable continuation of the recovered V23 reference, not as the final production app or final authored-art ceiling.

## Historical V11 state preserved

V11 remains important lineage rather than current latest state. It established the production data-platform direction and validated the earlier Object Atlas / Theme Worlds bundle.

Recovered V11-era artifacts include:

- `feature-foundry-aesthetic-worlds-codex-master-directive.md`
- `feature-foundry-codex-final-implementation-directive-v11.md`
- `feature-foundry-aesthetic-world-guide-v11.md`
- `feature-foundry-living-world-prototype-v11-bundle-reference.html`
- `V11-VALIDATION-REPORT.md`
- Object Atlas SQLite database
- Theme Worlds SQLite database

The preserved V11 report records 61 passed, 0 failed for the supplied schema/data bundle, including 178 object archetypes/families, 52 materials, 178 behavior profiles, 17 themes, 72 districts, 17 room presets, 51 weather profiles, 17 soundtrack profiles, 17 mascot profiles, 170 object-pool members, database integrity, foreign keys, FTS/RTree, cross-database references, and manifest hashes.

That validation did not prove final artwork, production runtime integration, Blender conversion, provider authentication, complete editor workflows, packaging/export behavior, or the finished application.

## Approved durable theme set

The preserved production direction keeps 17 full themes:

1. Frutiger Aero
2. Utopian Scholastic
3. Wacky Pomo
4. Contempo Eclectic
5. Vaporwave
6. Neo-Y2K
7. Liminal Leisure
8. Diner Kitsch
9. Cassette Futurism
10. Googie Kitsch
11. French Synthpop
12. Memphis
13. Ethereal CGI
14. Divine Machinery
15. Dark Fantasy
16. Atomic Age
17. Jazz / Solo Jazz

The broader aesthetics/research guide must not silently promote every researched aesthetic into a shipping theme.

## Major product subsystems

The durable production direction covers:

- professional application shell and configurable workspace;
- living world / environment runtime;
- focused full UI and performance modes;
- Theme Studio;
- Aesthetic Explorer and Mixer;
- Asset Vault;
- World Studio and Room Studio;
- Object Studio and semantic affordance/rig system;
- weather, time, lighting, soundtrack, UI sound, mascot, and interaction studios;
- package/export system;
- Object Atlas and Theme Worlds databases;
- multi-provider Music Hub;
- GameSync migration and host adapters.

Each top-level workspace must be a real functional workspace rather than a tab that merely changes highlighting or exposes placeholder UI.

## Professional workspace contract

Feature Foundry should behave like a serious authoring application. Where implemented, workspaces and panels should support docking, resizing, moving, hiding, tabs, floating panels, saved layouts, task-specific workspaces, multi-monitor use, customizable toolbars/shortcuts/density/inspectors, and safe layout reset/restore.

This is a product requirement, not proof that the unresolved production runtime already provides all of it.

## Living-world and runtime contract

Feature Foundry's living environments are interactive systems rather than decorative backgrounds. Preserve:

- theme-native objects and semantic identity;
- bounded weather/time/lighting/sound behavior;
- mascot and actor interaction;
- deterministic/recoverable authoring state;
- accessibility variants;
- user-pinned quality decisions;
- performance modes that suspend work rather than deleting content;
- no hidden quantity/fidelity reduction as a speed shortcut.

The verified V24 Runtime Governor is now evidence for how lifecycle release/resume and measured adaptive quality can work without degrading content. Production should preserve or improve those contracts rather than reintroducing permanent idle loops.

## Object intelligence contract

The Object Atlas / Object Studio direction requires semantic identity rather than treating assets as anonymous pictures. Preserve:

- object identity and archetype/family;
- materials;
- affordances;
- rigs;
- behavior profiles;
- source/provenance;
- immutable originals;
- reversible derivation lineage;
- context-aware actor commands;
- user-added object/mascot state.

Generated or transformed assets should remain traceable to originals.

## Asset Vault contract

The Asset Vault is intended to be a real asset operating system, not an empty drawer. Preserve persistent assets, source provenance, visual DNA, hot-drop/capture flows, search, organization, selected-asset context, placement modes, and reversible operations.

V23/V24 provide useful executable interaction evidence, but the production Asset Vault still needs proof in the actual app and persistence layer.

## Aesthetic Explorer / Mixer contract

The preserved project history identifies prior Explorer implementations as generic/flat and insufficient. A production Explorer should support real discovery, comparison, mixing, source evidence, saved decisions, and promotion into production themes without conflating research with shipping content.

The history also warns that the best Explorer/media base may be an earlier branch than an apparently newer numbered branch. Version number alone is not enough to choose latest-good production source.

## Room Studio contract

Room Studio remains a major production verification target. A valid implementation needs real authoring operations, persistent scene state, object placement/manipulation, environment controls, semantic room intelligence, and proof that saved content can be reopened and modified.

V23/V24 executable references include room/object interaction evidence, but that does not close the production-runtime gap.

## Source Hubs and external providers

External media/asset providers should use explicit source adapters with recorded:

- provider identity;
- authentication mode;
- capabilities;
- limits;
- cache behavior;
- fallback behavior;
- provenance/evidence;
- review date.

Provider research is not production integration until authenticated runtime flows are exercised.

## GameSync relationship

Feature Foundry is a source/authoring system for content that may be consumed by GameSync hosts. Avoid implementing theme behavior independently in each host. Prefer one source-of-truth theme/content contract plus explicit host adapters and migration/parity evidence.

## Current production-source problem

The connected [Feature-Foundry repository](https://github.com/Herbertofury/Feature-Foundry) still does not expose enough verified production source to establish complete install/build/run instructions for the real app.

Do not initialize a new replacement project or treat V24 HTML as that repository.

## Required source reconciliation before production implementation

1. Locate the canonical production app repository/worktree/branch.
2. Record commit/tree identity and compare it to the V24 executable reference plus V23/V11 data contracts.
3. Preserve newer user work rather than replacing it with a numerically newer reference artifact.
4. Reproduce current Room Studio, Explorer, Vault, provider, persistence, package/export, and host-integration behavior in the real runtime.
5. Build a migration ledger from current production implementation to the verified contracts.
6. Port only changes whose behavior can be proved in the real production application.
7. Run the actual application through save/reopen, reload/restart, provider/authenticated flows, packaging/export, and GameSync host import where applicable.

## Current technology research

Current primary package sources show that Vite 8.2.0, TypeScript 7.0.2, Vitest 4.1.10, Tauri CLI 2.11.4, and Biome 2.5.6 are active current lines as of the 2026-08-17 research pass. These are research inputs, not automatic migration instructions for the unresolved production app.

Do not update the production toolchain until the canonical repository and its actual manifests/lockfiles are recovered. Any migration must be isolated, baseline-first, and fully verified rather than selected because a package number is newer.

## Verification ladder

Maintain separate evidence for:

1. data/schema validation;
2. executable reference validation;
3. build/type/lint/unit checks;
4. application launch;
5. workspace navigation;
6. real authoring operations;
7. save/reopen persistence;
8. source-provider/authenticated flows;
9. package/export behavior;
10. host import behavior;
11. reload/restart persistence;
12. performance/fidelity regression checks.

Do not collapse these into one `validated` label.

## Exact current next action

**Locate and verify the canonical production application source, then reconcile it against the verified V24 executable reference and V23 data contracts before porting any further implementation.** Preserve the V24 Runtime Governor and interaction evidence as requirements to match or improve, not as a substitute for the real app.

## Wiki maintenance

Update this page whenever the production repository is resolved, V24 is superseded by newer verified evidence, a workspace becomes production-runtime verified, data schema/artifact hashes change, host/export contracts change, or a previously documented gap is closed. Preserve historical V11/V23 evidence and the distinction between executable-reference proof and production-app proof.