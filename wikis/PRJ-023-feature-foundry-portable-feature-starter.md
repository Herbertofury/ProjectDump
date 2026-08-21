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

### Observed proof that floating versions are already drifting

This is no longer only a theoretical reproducibility concern. Primary npm package records have continued changing while the recovered starter bytes have not:

- Biome stable moved from **2.5.6** at the original documentation baseline to **2.5.8** and then **2.5.9** by the 2026-08-21 check;
- Vue stable moved from **3.5.40** to **3.5.41**;
- Vue's 3.6 pre-release line advanced from **3.6.0-rc.2** to **3.6.0-rc.4**;
- Vitest's 5.x pre-release channel no longer matches the older `5.0.0-rc.1` note; npm currently tags **5.0.0-beta.7** as the 5.x beta while stable remains 4.1.10.

Vue is recorded explicitly in the recovered starter, so its movement is a normal candidate patch update rather than automatic runtime drift. Biome is different: the starter's floating dependency policy means a clean install performed later can resolve a different Biome version without any source change. That is direct evidence that `latest` weakens repeatability and makes two builds from the same starter archive capable of using different toolchain bytes.

Treat lockfiles, exact resolved versions and the package-manager version as part of the generated artifact identity. A successful build is not enough if the same archive cannot be reproduced intentionally.

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

## Current technology delta, checked 2026-08-21

Current primary package evidence shows:

- **Vite 8.2.2** versus starter 8.1.5;
- **Tauri CLI 2.11.4** versus starter 2.11.1;
- **Biome 2.5.9** while the starter floats `latest`;
- **TypeScript 7.0.2** versus starter 5.8.3;
- **Vitest 4.1.10** versus starter 3.x;
- **Vue 3.5.41** versus starter 3.5.40;
- Vue **3.6.0-rc.4** remains a release candidate rather than the stable baseline;
- Vitest **5.0.0-beta.7** remains pre-release and is not a reason to combine another major test-runner migration with the starter's baseline repair.

These are migration candidates, not automatic upgrade instructions. The smallest current deltas are the Vue 3.5.41 stable patch, Biome 2.5.9 after version pinning, Tauri 2.11.4 and Vite 8.2.2. TypeScript 7 and Vitest 4 remain larger migration gates, while Vue 3.6 and Vitest 5 should stay outside the stable baseline until a deliberate pre-release evaluation is requested and independently qualified.

### Why the fresh 2026-08-21 check matters

The observed Biome movement from 2.5.8 to 2.5.9 happened without any starter-source change. That is exactly the failure mode the reproducibility repair is intended to prevent. The updated Vue and Vitest pre-release channels reinforce the same rule: pre-release package labels are moving targets and must never be treated as part of a stable generator baseline merely because they are newer.

The stable migration target should be defined by an intentional dependency matrix and preserved lock state, not by the newest tag available at install time.

## Sequenced migration order

1. establish a clean v0.1.0 baseline and native-build proof;
2. correct `tauri-react` versus Vue metadata without changing runtime behavior;
3. pin floating package/dependency declarations and the package-manager version, then prove reproducibility from a second clean install;
4. evaluate Vue 3.5.41 and pinned Biome 2.5.9 as isolated stable maintenance updates;
5. evaluate paired Tauri CLI/API patch updates;
6. evaluate Vite 8.2.x plus matching Vue plugin compatibility;
7. migrate TypeScript 7 separately because it is a major compiler jump;
8. migrate Vitest 4 separately because it is a major test-runner jump;
9. keep Vue 3.6 and Vitest 5 pre-release evaluation outside the stable baseline until their own acceptance pass is justified;
10. rerun build, tests, Foundry validation, rehearsal, rollback, capsule lifecycle, native package, runtime and restart/persistence gates after each coherent migration.

## Reproducible-build acceptance contract

Before this starter can be promoted as a dependable generator reference, two clean environments using the same preserved source and lock state should prove:

1. the same package-manager version is used;
2. the same direct dependency versions are resolved;
3. the same generated source and owned-file boundaries are produced;
4. build/test/Foundry validation results agree;
5. capsule install/upgrade/remove behavior agrees;
6. rollback restores the same state;
7. native Tauri output is functionally equivalent;
8. differences are either byte-identical where deterministic output is expected or explicitly explained by signed/platform-specific build metadata.

If a second clean install silently selects newer toolchain packages because of `latest`, the reproducibility gate fails even when both builds happen to compile.

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

**Correct the Vue/Tauri stack identity and floating-version reproducibility defects first, then prove the exact recovered starter through two clean dependency resolutions plus a fresh native Tauri build and complete Foundry validation/rehearsal/rollback/capsule lifecycle. After the baseline is reproducible, evaluate Vue 3.5.41, pinned Biome 2.5.9, Tauri 2.11.4 and Vite 8.2.2 as isolated stable maintenance steps before separate TypeScript 7 and Vitest 4 migrations. Keep Vue 3.6 and Vitest 5 pre-release channels outside the stable baseline.**

## Wiki maintenance

Update this page when stack metadata is corrected, floating versions are pinned, clean installs prove reproducibility, native build/runtime proof exists, validation/rehearsal scenarios are actually executed, capsule behavior changes, the generation version advances, or a downstream production app proves real integration. Preserve the original v0.1.0 evidence and resolved dependency identities as lineage.