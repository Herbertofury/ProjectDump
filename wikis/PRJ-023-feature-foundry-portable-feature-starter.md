# Feature Foundry Portable Feature Starter Wiki

**Project Constellation ID:** `PRJ-023`
**Status:** GENERATED FEATURE FOUNDRY 2.6 STARTER, NOT SHIPPABLE
**Verified artifact:** `Feature_Foundry_Portable_Feature_Starter.zip`
**Package:** `feature-foundry-portable-feature-base` v0.1.0

## Purpose

The recovered starter is a generated **Feature Foundry 2.6** foundation for portable feature capsules and ownership-aware upgrades. It is more than a bare desktop template: its App DNA, capsule lifecycle, validation, promotion, rollback, preview/runtime and golden-fleet structures are intended to preserve reusable product features across generated applications.

It remains a starter/template. The included release scenarios were not executed and `shippable` is false.

## Verified implementation stack

Direct archive inspection records:

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
- Playwright, Biome, Tailwind, Howler and signals support in the generated toolchain/capability surface.

The package exposes development, production build, testing, Foundry lifecycle, Tauri, stack-update, capsule install/upgrade/remove, validation, rehearsal, rollback and promotion-oriented scripts.

## Important metadata mismatch

The archive contains a correctness defect that should be fixed before the starter is used as a canonical generator reference:

- actual package/source is Vue-based (`src/App.vue`, Vue dependency, Vue Vite plugin, `vue-tsc`);
- blueprint and adapter metadata include `stack: tauri-react` / `preferredStack: tauri-react`.

That mismatch can misroute generators, adapters, documentation, migrations or capability selection. Treat it as a real stack-identity defect, not cosmetic naming.

The corrected metadata should describe the actual Tauri + Vue stack unless project-owned evidence proves the React label intentionally identifies a separate adapter layer.

## Reproducibility issue

Several generated dependency declarations use floating `latest` specifiers, and the package manager is recorded as `pnpm@latest`.

A reusable starter should not depend on whatever package becomes current on the next install. Before promotion:

1. preserve the current lockfile/resolution state;
2. replace floating declarations with reviewed versions or an explicit supported-range policy;
3. pin the package-manager line intentionally;
4. regenerate from a clean state;
5. prove generated output, validation, capsules, ownership data and native build remain equivalent.

## Portable feature capsule system

Preserve these capsule properties:

- stable capsule identity and version;
- ownership-aware files/state;
- target compatibility;
- capabilities and permissions;
- upgrade semantics;
- rollback path;
- evidence/validation requirements;
- host-neutral data where practical.

Do not convert capsule installation into blind file copying that loses ownership or rollback information.

## Native runtime boundary

`foundry/preview-runtime.json` identifies a **native runner** and states that a real native build is required. It names Tauri CLI, a Rust toolchain and a local process bridge as requirements, and explicitly notes that native windows cannot run inside a browser sandbox.

Therefore a Vite/browser preview is not the final runtime test. A native Tauri build, launch, workflow exercise and persistence/restart check belong in promotion evidence.

## Validation boundary

The included validation report records release scenarios as not run. Keep these states distinct:

- artifact recovered;
- archive inspected;
- dependency state resolved;
- web build passed;
- native Tauri build passed;
- tests passed;
- Foundry validation passed;
- Foundry rehearsal passed;
- rollback passed;
- capsule lifecycle passed;
- real workflow passed;
- restart/persistence passed;
- shippable confirmed.

Do not compress them into one `done` state.

## Current technology delta, checked 2026-08-17

Current primary package/release evidence shows:

- **Vite 8.2.2** versus starter 8.1.5;
- **Tauri CLI 2.11.4** versus starter 2.11.1;
- **Biome 2.5.6** while the starter floats `latest`;
- **TypeScript 7.0.2** versus starter 5.8.3;
- **Vitest 4.1.10** versus starter 3.x;
- Vue stable remains **3.5.40** in the recovered/current stable line while newer 3.6 packages are release candidates, not a reason to move the starter's stable baseline automatically.

This corrects the previous Vite 8.2.0 note to the current 8.2.2 line. These are migration candidates, not automatic upgrade instructions.

## Sequenced migration order

1. establish a clean v0.1.0 baseline and native-build proof;
2. correct `tauri-react` versus Vue metadata without changing runtime behavior;
3. pin floating package/dependency declarations and prove reproducibility;
4. evaluate paired Tauri CLI/API patch updates;
5. evaluate Vite 8.2.x plus matching Vue plugin compatibility;
6. migrate TypeScript 7 separately because it is a major compiler jump;
7. migrate Vitest 4 separately because it is a major test-runner jump;
8. rerun build, tests, Foundry validation, rehearsal, rollback, capsule lifecycle, native package, runtime and restart/persistence gates after each coherent migration.

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

**Correct the Vue/Tauri stack identity and floating-version reproducibility defects first, then prove the exact recovered starter through a fresh native Tauri build and complete Foundry validation/rehearsal/rollback/capsule lifecycle. After that, evaluate Tauri 2.11.4 and Vite 8.2.2 as isolated low-risk toolchain steps before separate TypeScript 7 and Vitest 4 migrations.**

## Wiki maintenance

Update this page when stack metadata is corrected, floating versions are pinned, native build/runtime proof exists, validation/rehearsal scenarios are actually executed, capsule behavior changes, the generation version advances, or a downstream production app proves real integration.
