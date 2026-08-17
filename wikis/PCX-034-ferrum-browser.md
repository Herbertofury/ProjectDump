# Ferrum Browser Wiki

**Project Constellation ID:** `PCX-034`  
**Canonical repository:** [Herbertofury/Ferrum-Browser](https://github.com/Herbertofury/Ferrum-Browser)  
**Canonical branch:** `main`  
**Verified project version:** `0.2.0`  
**Verified canonical code commit:** `536bbc23dfee068e26eda8b32574f06ce19a43f1`  
**Verified workflow run:** `31987413168`  
**Verified at:** `2026-08-17T02:16:15Z`  
**Project state:** verified canonical implementation on main

## Purpose

Ferrum is an agent-native full application tester and is the preferred full-fidelity extension acceptance layer for GameSync when available. It is designed to make repeated verification fast while preserving target identity, runtime fidelity, diagnostics, evidence, restart proof, and failure visibility.

Ferrum is broader than a browser wrapper. The same deterministic test/evidence model covers:

- ordinary web applications;
- unpacked Manifest V3 extensions;
- Electron applications;
- arbitrary processes/services;
- Appium-backed native/mobile targets when that lane is qualified.

Ferrum orchestrates real runtimes. A successful tool handshake, mock, or rendered dashboard is not a substitute for exercising the target application.

## Current verified status

Project-owned `.agents-memory/STATUS.json` now records Ferrum 0.2.0 at commit `536bbc23dfee068e26eda8b32574f06ce19a43f1` as the verified canonical implementation.

### Linux Chromium lane

Verified passed:

- web smoke;
- MV3 extension smoke;
- Workbench smoke;
- **real Electron application smoke**;
- service-worker diagnostics before restart;
- service-worker diagnostics after restart;
- full browser restart proof.

### Windows Chromium lane

Verified passed:

- web smoke;
- MV3 extension smoke;
- Workbench smoke;
- **real Electron application smoke**;
- service-worker diagnostics before restart;
- service-worker diagnostics after restart;
- full browser restart proof.

### Lightpanda lane

Verified:

- Lightpanda **0.3.7**;
- native direct-CDP transport;
- release binary SHA-256 `895339b02205171a181dde743ae0068bb4564884076feac8482baca9c212aa5a`.

### Agent interfaces

Verified:

- compact CLI result summaries;
- compact MCP responses by default;
- explicit full-output MCP escape hatch;
- exact evidence-directory return;
- complete evidence preserved on disk.

### Benchmark evidence

Current benchmark output is verified to retain:

- median and p95;
- machine/runtime metadata;
- workload metadata;
- step budget;
- success rate;
- timeout accounting;
- per-sample evidence directory.

### Current unqualified lane

Only the **Appium** runner remains implemented-but-not-runtime-qualified against a real native/mobile application/device/emulator.

The previous wiki statement that Electron was unqualified is obsolete and has been superseded by current project-owned runtime evidence.

## Runtime and package baseline

Ferrum requires Node.js 24 or newer.

Current `package.json` pins:

- Playwright **1.62.1**;
- Electron **43.2.0**.

[Playwright 1.62.1](https://github.com/microsoft/playwright/releases/tag/v1.62.1) is the current official Playwright stable release as of this review.

The official Electron repository currently identifies **Electron 43.4.0** as its latest stable release, published August 11, 2026. Ferrum remains pinned to 43.2.0, so 43.4.0 is a **stack-upgrade candidate**, not a silently accepted dependency change.

### Electron upgrade rule

Before advancing Electron:

1. baseline current 43.2.0 Electron smoke on Linux and Windows;
2. upgrade only the Electron dependency on a proposal branch;
3. rerun unit/regression checks;
4. run the real secure preload/renderer/main IPC Electron target on Linux and Windows;
5. verify runtime identity, main-process console, renderer diagnostics, IPC interaction, screenshot/evidence output, and restart-relevant behavior;
6. compare evidence completeness and timing;
7. keep 43.2.0 if 43.4.0 introduces any target/evidence regression that cannot be repaired in the same proposal.

## Main commands

Inspect runtime availability:

```bash
npx ferrum doctor
```

Web smoke:

```bash
npx ferrum test examples/self-test-web.json --headless
```

MV3 extension smoke:

```bash
npx ferrum test examples/self-test-extension.json --headless
```

Electron smoke:

```bash
npm run smoke:electron
```

Run bounded parallel specs:

```bash
npx ferrum suite examples/self-test-web.json examples/self-test-extension.json --workers 2 --headless
```

Benchmark a fixed workload:

```bash
npx ferrum bench path/to/benchmark-spec.json --engines chromium,lightpanda --runs 7 --warmup 1 --headless
```

Open Workbench:

```bash
npx ferrum dashboard
```

Expose MCP stdio:

```bash
npx ferrum mcp
```

Current package scripts include:

```bash
npm test
npm run smoke:web
npm run smoke:extension
npm run smoke:electron
npm run smoke:lightpanda
npm run smoke:dashboard
npm run ci
```

## Chromium fidelity lane

Ferrum uses real Playwright persistent Chromium contexts for browser and extension correctness.

This lane is required for Chromium-specific claims involving:

- unpacked MV3 extensions;
- service workers;
- content scripts;
- extension pages;
- permissions;
- persistent profiles;
- browser restart and state recovery.

Headless extension runs intentionally use the full Chromium channel rather than Playwright's reduced headless shell because the reduced shell previously failed the required MV3 behavior.

## Service-worker observability

Current Ferrum evidence now goes beyond worker discovery and messaging.

Verified worker evidence includes:

- worker console output;
- worker-owned request/response/failure diagnostics;
- interception evidence;
- lifecycle evidence;
- assertions before restart;
- assertions after restart.

This is particularly important for extension testing because a popup rendering correctly does not prove the background/service-worker path is healthy.

## Lightpanda speed lane

Lightpanda remains a fast web-only lane driven through its native CDP server.

Use it for compatible web workloads where the goal is fast deterministic DOM/JavaScript coverage. It is not proof for Chromium-only behavior, browser-extension APIs, or MV3 service workers.

Do not route Lightpanda back through Playwright lifecycle assumptions; that previously caused timeouts.

## Electron lane

Ferrum's Electron runner is now runtime-qualified against a real Electron application on both Ubuntu and Windows.

Verified evidence includes:

- real Electron application launch;
- main-process console;
- process streams;
- runtime identity;
- renderer diagnostics;
- IPC interaction;
- screenshots/evidence output.

Treat reappearance of an "implementation-only" Electron state as a regression in Project Constellation documentation unless project-owned evidence proves a newer failure.

## Process lane

Ferrum can launch arbitrary CLI tools, services, or desktop processes and retain stdout, stderr, health/exit evidence, and related artifacts.

This remains useful for test infrastructure and companion services that are not browser-native.

## Appium lane

Ferrum can speak W3C WebDriver to an Appium endpoint, but the current status still lacks real native/mobile device or emulator qualification.

Do not present Appium as fully verified until a concrete application/device/emulator run passes and survives the same evidence/identity scrutiny as the other lanes.

## Test specification format

Ferrum JSON specs contain:

- `version`;
- `name`;
- `target`;
- optional timeout/artifact settings;
- ordered `steps`.

Supported target types:

- `web`;
- `extension`;
- `electron`;
- `process`;
- `appium`.

Common browser steps include open, wait, click, fill, press, snapshot, screenshot, text/visibility/url assertions, evaluate, vitals, and console-clean assertions.

Extension workflows add extension-page/service-worker/restart operations.

Every step must preserve timing and failure context. Browser failures retain trace evidence.

## Evidence model

Each run owns a unique evidence directory. Parallel same-name runs use nonces to avoid collisions.

Evidence may include:

- normalized spec;
- result JSON with per-step timing;
- screenshots;
- Playwright traces;
- page/console/network/service-worker failures;
- worker lifecycle/traffic evidence;
- runtime diagnostics;
- target/build SHA-256 inventory;
- resolved extension ID and discovery path;
- restart proof;
- process/Appium output;
- benchmark machine/workload/reliability metadata.

Failed runs preserve evidence. Compact agent output does not mean evidence was discarded.

## Compact CLI and MCP contract

A prior pain point was excessive successful-run output consuming agent context while making the evidence directory harder to find.

Current Ferrum solves this by:

- returning concise actionable CLI/MCP summaries by default where requested;
- always returning or exposing the exact evidence directory;
- preserving the complete evidence set on disk;
- allowing explicit full MCP output when deeper inspection is needed.

This is an efficiency improvement with **no evidence reduction**.

## Manifest V3 verification

For an unpacked extension Ferrum can:

1. load the exact build into a persistent Chromium profile;
2. hash the build files;
3. resolve runtime extension identity;
4. exercise popup/options/content-script/service-worker paths;
5. capture screenshots, traces, console/network/worker diagnostics;
6. restart the browser with the same profile;
7. re-resolve the extension;
8. verify post-restart behavior and worker diagnostics;
9. retain the complete evidence bundle.

This is the core reason Ferrum is preferred for GameSync extension acceptance.

## GameSync integration

Ferrum should be used for every applicable GameSync extension change when available, with Opera GX retained as additional compatibility coverage.

For each changed workflow:

1. build the exact GameSync artifact;
2. record its hash/path/runtime identity;
3. load that build in Ferrum;
4. exercise the exact changed control/flow;
5. inspect popup/content-script/service-worker behavior;
6. test relevant failure behavior;
7. repeat after reload and full browser restart when stateful;
8. inspect retained evidence;
9. run Opera GX compatibility smoke separately where applicable.

If GameSync exposes reusable Ferrum shortcomings, improve Ferrum rather than masking them with a weaker alternate test.

## Workbench

The Workbench is a real Chromium-controlled workflow, not merely a static dashboard.

Current verified Linux and Windows coverage includes:

- Doctor;
- spec input/selection;
- Headless control;
- Run action;
- visible result;
- browser diagnostics;
- screenshot evidence.

Previously fixed Workbench incidents include:

- ephemeral port mode reporting `0` instead of the bound port;
- missing static assets surfacing as HTTP 500 instead of truthful 404.

Reappearance of either behavior is a regression.

## Benchmarks

`ferrum bench` must compare fixed workloads rather than cherry-picked single timings.

Current output records median/p95 plus environment and reliability context. Keep this data when comparing runtimes or performance changes.

A faster run is not an improvement if it removes test steps, diagnostics, evidence, restart proof, target coverage, or failure visibility.

## Important resolved incidents

Project-owned status records fixes for:

- reduced Playwright headless shell breaking MV3 verification;
- Lightpanda timeouts under Chromium lifecycle assumptions;
- evidence-directory collisions during parallel runs;
- explicit warmup `0` being coerced to `1`;
- checkout line-ending differences changing fixture hashes;
- Workbench ephemeral-port reporting;
- missing static assets returning HTTP 500;
- service-worker observability stopping at discovery/messaging;
- agent CLI/MCP output flooding context;
- Electron existing without real runtime qualification;
- benchmark results lacking enough machine/workload/reliability context.

Preserve regression coverage for these behaviors.

## Development workflow

Before editing:

1. read repository `AGENTS.md`;
2. read `.agents-memory/PROJECT.json`, `STATUS.json`, `HANDOFF.md`, and `COMPASS.json`;
3. confirm the exact current main commit;
4. reproduce the target issue with an existing or minimal new spec;
5. establish the current target/evidence baseline.

After editing, run applicable checks such as:

```bash
npm test
npm run smoke:web
npm run smoke:extension
npm run smoke:electron
npm run smoke:dashboard
```

Run Lightpanda smoke when that lane is affected. Run real Electron evidence on Linux and Windows for Electron changes. Appium work remains incomplete until a real target is exercised.

## Current next actions

Project-owned status identifies these continuing improvements:

- use Ferrum on every applicable GameSync extension verification;
- turn real GameSync workflows into reusable production workload packs;
- expand browser compatibility beyond the current Chromium lane to installed Chrome, Edge, Brave, and Opera GX where exact qualification is possible;
- add isolated parallel Spaces/profile cloning for authenticated concurrent workloads;
- build a session replay/evidence viewer over retained traces, screenshots, diagnostics, and summaries;
- add semantic locator recovery as an additive fallback above deterministic selectors without hiding deterministic failures;
- qualify Appium against a real native/mobile application/device/emulator;
- keep improving speed/reliability/observability/setup only when the complete evidence and target contract is preserved.

### Current stack candidate

Electron **43.4.0** is newer than Ferrum's pinned 43.2.0. Evaluate it on a maintained proposal branch with full Linux + Windows real-Electron proof. Do not advance the pin solely because a newer release exists.

## Source-of-truth hierarchy

For Ferrum facts, prefer:

1. current `Herbertofury/Ferrum-Browser` source and real evidence;
2. `.agents-memory/STATUS.json` / current project memory;
3. repository docs/manifests;
4. Project Constellation summaries.

Project-owned evidence supersedes stale Project Constellation wording.

## Wiki maintenance triggers

Update this page whenever the verified commit/workflow, supported target matrix, service-worker diagnostics, evidence schema, CLI/MCP output contract, Workbench behavior, GameSync acceptance contract, Electron/Appium qualification, dependency pins, or project-owned next actions materially change.