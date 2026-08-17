# Feral Unified Native Base Wiki

**Project Constellation ID:** `PRJ-022`  
**Status:** IDENTITY RESOLVED / GENERATED FEATURE FOUNDRY BASE, NOT SHIPPABLE  
**Verified artifact:** `Feral_Unified_Native_Base.zip`

## Purpose and resolved identity

Direct inspection of the recovered archive resolves the previously ambiguous identity. The package identifies itself as **Feral Unified App Base**, package `feral-unified-app-base` version `0.1.0`.

Its Feature Foundry blueprint describes it as a complete, moddable Feature Foundry 2.0 foundation ready for product-specific work, targeting `desktop-app` on a `react-vite` stack. Treat it as a generated reusable Feature Foundry foundation, not a separately proven finished Feral product.

## Verified archive structure and stack

The inspected package records:

- package `feral-unified-app-base` version `0.1.0`;
- React 19.2.7;
- React DOM 19.2.7;
- Vite 8.1.5;
- `@vitejs/plugin-react` 6.0.4;
- TypeScript 5.8.3;
- Vitest `^3.2.4`;
- development, build, preview, lint, test, Foundry check/validate/rehearse and rollback scripts.

The archive also carries Feature Foundry-style App DNA, mod-cartridge, preview-runtime, validation, promotion, ownership and golden-fleet structures.

## Feature Foundry contracts present

Preserve these contracts if the base is reused or upgraded:

- App DNA and stable application identity;
- theme and UI-sound capability manifests;
- mod-cartridge composition;
- semantic event declarations;
- explicit file ownership and generated-file boundaries;
- validation and promotion evidence;
- upgrade rehearsal;
- rollback capability;
- golden-fleet CI expectations;
- preview/runtime metadata.

Do not flatten this into a generic React starter.

## Current validation boundary

The included validation report records generated `desktop-tool` and `embedded-panel` scenarios as **not run**:

- passed: 0;
- failed: 0;
- blocked: 0;
- `shippable: false`.

Archive completeness and configuration do not prove a runnable or shippable application.

## Preview runtime

The archive's preview runtime describes a browser-native React/Vite path and indicates that the generated framework build should be verified through an appropriate local or WebContainer-style runner. Treat that as scaffolding metadata, not production runtime proof.

## Current technology delta, checked 2026-08-17

Current primary package/release evidence is newer than several pins in the recovered 0.1.0 base:

- **Vite 8.2.2** versus recovered 8.1.5;
- **TypeScript 7.0.2** versus recovered 5.8.3;
- **Vitest 4.1.10** versus recovered 3.x;
- **React 19.2.8** versus recovered 19.2.7.

This corrects the earlier wiki note that stopped at Vite 8.2.0. The Vite delta is a small build-tool patch/minor-line movement; the TypeScript and Vitest deltas are major migrations and must not be bundled into a blind all-at-once upgrade.

## Sequenced upgrade strategy

1. extract the exact recovered archive into a fresh location;
2. record archive/package hashes and lockfile state;
3. install the baseline exactly as recoverable;
4. run build, lint, tests, Foundry check, validation, rehearsal, rollback and any supported preview/runtime smoke;
5. capture baseline generated output and behavior;
6. update Vite and its React plugin coherently, beginning with the current 8.2.x line only after checking peer compatibility;
7. rerun every baseline gate and compare output;
8. evaluate TypeScript 7 separately as a major compiler migration;
9. evaluate Vitest 4 separately as a major test-runner migration;
10. only promote changes that preserve all Foundry contracts and improve maintainability or correctness without reducing behavior or evidence.

## Anti-degradation requirements

A toolchain upgrade must not:

- remove App DNA fields;
- weaken validation or promotion requirements;
- remove semantic events or capabilities;
- bypass file ownership;
- disable rollback/rehearsal;
- reduce generated scenarios;
- change target identity from `desktop-app` without a product decision;
- mark the package shippable merely because dependencies/builds are newer.

## Exact current next action

**Preserve Feral as a generated Feature Foundry 2.0 foundation, establish a clean v0.1.0 baseline, and run its complete build/test/Foundry validation flow before reuse. Then evaluate Vite 8.2.2 as the smallest toolchain delta, with TypeScript 7 and Vitest 4 isolated behind their own migration and regression gates.**

## Evidence still needed

To move beyond generated-foundation status, resolve:

- exact archive SHA-256 if not already cataloged elsewhere;
- clean dependency-install result;
- build output;
- test result;
- Foundry validation/rehearsal result;
- rollback proof;
- actual preview/runtime behavior;
- whether a downstream Feral product repository adopted this base.

## Wiki maintenance

Update this page if a canonical downstream repository is found, clean runtime proof is obtained, dependency migrations are verified, Foundry validation becomes shippable, or ownership/promotion contracts change. Preserve the original 0.1.0 evidence as lineage.
