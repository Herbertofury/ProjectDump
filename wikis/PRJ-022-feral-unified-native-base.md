# Feral Unified Native Base Wiki

**Project Constellation ID:** `PRJ-022`  
**Status:** IDENTITY RESOLVED / GENERATED FEATURE FOUNDRY BASE, NOT SHIPPABLE  
**Verified artifact:** `Feral_Unified_Native_Base.zip`

## Purpose and resolved identity

Direct inspection of the recovered archive resolves the previously ambiguous project identity. The package identifies itself as **Feral Unified App Base**, package `feral-unified-app-base` version `0.1.0`.

Its Feature Foundry blueprint describes it as **a complete, fully moddable Feature Foundry 2.0 foundation ready for product-specific work**, targeting `desktop-app` on a `react-vite` stack. It is therefore best treated as a generated reusable Feature Foundry base/foundation, not as a separately proven finished Feral product.

This corrects the older Project Constellation state that left Feral unresolved between standalone product, generic native base, generated experiment, or precursor.

## Verified archive structure and stack

The inspected `package.json` records:

- package name `feral-unified-app-base`;
- package version `0.1.0`;
- React 19.2.7;
- React DOM 19.2.7;
- Vite 8.1.5;
- `@vitejs/plugin-react` 6.0.4;
- TypeScript 5.8.3;
- Vitest `^3.2.4`;
- development, build, preview, lint, test, Foundry check/validate/rehearse, and rollback scripts.

The archive also carries Feature Foundry-style App DNA, mod-cartridge, preview-runtime, validation, promotion, ownership, and golden-fleet structures.

## Feature Foundry contracts present

The recovered foundation includes contracts for reusable generated-app behavior rather than only a bare Vite scaffold. Preserve these when reusing or upgrading the base:

- App DNA and stable application identity;
- theme and UI-sound capability manifests;
- mod-cartridge composition;
- semantic event declarations;
- explicit file ownership / generated-file boundaries;
- validation and promotion evidence;
- upgrade rehearsal;
- rollback capability;
- golden-fleet CI expectations;
- preview/runtime metadata.

Do not flatten this into a generic React starter if the base is promoted for future product work.

## Current validation boundary

The included validation report records generated scenarios for `desktop-tool` and `embedded-panel`, but both are **not run**. The report records:

- passed: 0;
- failed: 0;
- blocked: 0;
- `shippable: false`.

This is an explicit acceptance boundary. Archive completeness and generated configuration do not prove a runnable/shippable application.

## Preview runtime

The archive's preview runtime describes a browser-native React/Vite path and indicates that the generated framework build should be verified through an appropriate local/WebContainer-style runner. Treat that as scaffolding metadata, not production runtime proof.

## Current technology delta, checked 2026-08-17

Primary package sources show newer maintained releases than several pins in the recovered 0.1.0 base:

- Vite 8.2.0 versus recovered 8.1.5;
- TypeScript 7.0.2 versus recovered 5.8.3;
- Vitest 4.1.10 versus recovered `^3.2.4`;
- React 19.2.8 versus recovered 19.2.7.

The React/Vite plugin line is already close to current. The TypeScript and Vitest gaps are larger and should be treated as migrations rather than blind version bumps.

## Upgrade strategy

Do not update every dependency at once. The narrow evidence-backed path is:

1. extract the exact recovered archive into a fresh location;
2. record archive/package hashes and lockfile state;
3. install the baseline exactly as recoverable;
4. run build, lint, tests, Foundry check, Foundry validation, Foundry rehearsal, rollback checks, and any preview/runtime smoke that is actually supported;
5. capture the baseline generated output and behavior;
6. update Vite and its React plugin as one coherent build-tool pair;
7. rerun every baseline gate and compare output;
8. evaluate TypeScript 7 separately because it is a major compiler migration;
9. evaluate Vitest 4 separately because it is a major test-runner migration;
10. only promote changes that preserve all Foundry contracts and improve maintainability without reducing behavior or evidence.

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

**Preserve Feral as a generated Feature Foundry 2.0 foundation, establish a fresh clean baseline, and run its complete build/test/Foundry validation flow before deciding whether it is suitable for reuse.** Only then evaluate isolated current-toolchain upgrades.

## Evidence still needed

To move this project beyond generated-foundation status, resolve:

- the exact archive SHA-256 if not already cataloged elsewhere;
- a clean dependency install result;
- build output;
- test result;
- Foundry validation/rehearsal result;
- rollback proof;
- actual preview/runtime behavior;
- whether a real downstream Feral product repository adopted this base.

## Wiki maintenance

Update this page if a canonical downstream repository is found, a clean build/runtime is proven, dependency migrations are verified, Foundry validation becomes shippable, or the base's ownership/promotion contracts change. Preserve the original 0.1.0 evidence as lineage.