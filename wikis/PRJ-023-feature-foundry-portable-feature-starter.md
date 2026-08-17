# Feature Foundry Portable Feature Starter Wiki

**Project Constellation ID:** `PRJ-023`  
**Status:** GENERATED FEATURE FOUNDRY 2.6 STARTER, NOT SHIPPABLE  
**Verified artifact:** `Feature_Foundry_Portable_Feature_Starter.zip`  
**Package:** `feature-foundry-portable-feature-base` v0.1.0

## Purpose

The recovered starter is a generated **Feature Foundry 2.6** foundation for portable feature capsules and ownership-aware upgrades. It is more than a bare desktop template: its App DNA, capsule lifecycle, validation, promotion, rollback, preview/runtime, and golden-fleet structures are intended to preserve reusable product features across generated applications.

It remains a starter/template. The included release scenarios were not executed and `shippable` is false.

## Verified implementation stack

Direct archive inspection records the actual implementation as:

- Vue 3.5.40;
- `@vitejs/plugin-vue` 6.0.8;
- Vite 8.1.5;
- TypeScript 5.8.3;
- `vue-tsc` 3.x;
- Vitest `^3.2.4`;
- Tauri 2.11.1 JS API;
- Tauri CLI 2.11.1;
- Rust/native Tauri backend expectations;
- SQLite in the Feature Foundry composition contract;
- Playwright, Biome, Tailwind, Howler, and signals support in the generated toolchain/capability surface.

The package exposes development, production build, testing, Foundry lifecycle, Tauri, stack-update, capsule install/upgrade/remove, validation, rehearsal, rollback, and promotion-oriented scripts.

## Important metadata mismatch

The archive contains a correctness issue that should be fixed before this starter is used as a canonical generator reference:

- the actual package/source is Vue-based (`src/App.vue`, Vue dependency, Vue Vite plugin, `vue-tsc`);
- the blueprint and adapter metadata include `stack: tauri-react` / `preferredStack: tauri-react`.

That mismatch can misroute future generators, adapters, documentation, migrations, or capability selection. Treat it as a real metadata defect, not a cosmetic naming issue.

The corrected metadata should describe the actual Tauri + Vue stack unless project-owned evidence proves the React label intentionally refers to a different adapter layer.

## Reproducibility issue

Several generated dependency declarations use floating `latest` specifiers, and the package manager is recorded as `pnpm@latest`.

A reusable starter should not rely on whatever package happens to be current at the next install. Before promotion:

1. inspect and preserve the current lockfile/resolution state;
2. replace floating `latest` declarations with reviewed versions or an explicit supported range policy;
3. pin the package-manager line intentionally;
4. regenerate once from a clean state;
5. prove that the generated output, validation, capsules, ownership data, and native build remain equivalent.

## Portable feature capsule system

The archive contains portable feature capsule operations for install, upgrade, and removal. Preserve the key capsule properties:

- stable capsule identity and version;
- ownership-aware files/state;
- target compatibility;
- capabilities and permissions;
- upgrade semantics;
- rollback path;
- evidence/validation requirements;
- host-neutral data where practical.

Do not convert capsule installation into blind file copying that loses ownership or rollback information.

## Foundry module surface

The recovered starter records a broad Feature Foundry module set, including generated App DNA, mod/theme/sound capabilities, validation and promotion structures, preview/native-runner metadata, and related operational modules. Project Constellation previously recorded this starter only as a simple Vue/Tauri/Vitest/Playwright/Biome template; the direct archive inspection establishes the stronger portable-feature foundation intent.

## Native runtime boundary

`foundry/preview-runtime.json` identifies a **native runner** and states that a real native build is required. It names Tauri CLI, a Rust toolchain, and a local process bridge as requirements, and explicitly notes that native windows cannot run inside a browser sandbox.

Therefore:

- a browser preview is not the final runtime test;
- a successful Vite build is not enough;
- a native Tauri build and launch must be part of promotion evidence;
- the exact generated application should be exercised, not a mock shell.

## Validation boundary

The included validation report records the generated release scenarios as not run. It does not claim a build, runtime, install, package, rollback, or native workflow passed.

Keep these statuses separate:

- artifact recovered;
- archive inspected;
- dependency state resolved;
- web build passed;
- native Tauri build passed;
- tests passed;
- Foundry validation passed;
- Foundry rehearsal passed;
- rollback passed;
- real workflow passed;
- restart/persistence passed;
- shippable confirmed.

Do not compress them into one `done` state.

## Current technology delta, checked 2026-08-17

Primary package sources show:

- Vite 8.2.0 is current while the starter pins 8.1.5;
- Tauri CLI 2.11.4 is current while the starter pins 2.11.1;
- Biome 2.5.6 is current while the starter floats `latest`;
- TypeScript 7.0.2 is current while the starter pins 5.8.3;
- Vitest 4.1.10 is current while the starter uses the 3.x line;
- Vue 3.5.40 and `@vitejs/plugin-vue` 6.0.8 in the archive already match the current package lines observed during this pass.

These are migration candidates, not automatic upgrade instructions.

## Recommended migration order for this starter

The smallest attributable sequence is:

1. establish a clean v0.1.0 baseline and native-build proof;
2. correct `tauri-react` versus Vue metadata without changing runtime behavior;
3. pin floating package/dependency declarations and prove reproducibility;
4. evaluate paired Tauri CLI/API patch updates;
5. evaluate Vite/plugin updates;
6. migrate TypeScript separately because it is a major compiler jump;
7. migrate Vitest separately because it is a major test-runner jump;
8. rerun build, tests, Foundry validation, rehearsal, rollback, capsule lifecycle, native package, runtime, and restart/persistence gates after every coherent migration.

## Anti-degradation requirements

Do not improve this starter by removing or weakening:

- portable capsules;
- ownership metadata;
- upgrade/rehearsal/rollback;
- App DNA;
- mod/theme/sound capability contracts;
- validation scenarios;
- native Tauri target coverage;
- golden-fleet checks;
- evidence requirements;
- compatibility declarations.

A smaller generated scaffold is not an upgrade if it loses these contracts.

## Exact current next action

**Correct the stack metadata/reproducibility defects, then prove the exact recovered starter through a fresh native Tauri build and the complete Foundry validation/rehearsal/rollback path before using it as a generator baseline or declaring it shippable.**

## Wiki maintenance

Update this page when the metadata mismatch is corrected, floating versions are pinned, a native build is proven, validation/rehearsal scenarios are actually executed, capsule behavior changes, the Feature Foundry generation version advances, or a downstream production app proves this starter's real integration.