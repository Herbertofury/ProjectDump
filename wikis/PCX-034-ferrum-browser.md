# Ferrum Browser Wiki

**Project Constellation ID:** `PCX-034`  
**Canonical repository:** [Herbertofury/Ferrum-Browser](https://github.com/Herbertofury/Ferrum-Browser)  
**Canonical branch:** `main`  
**Verified project version:** `0.2.0`  
**Verified merged Playwright-stack commit:** `1217144c626fade0a52596e16d78f995f827652b`  
**Verified MV3 recovery product commit:** `7360184f154f9182f9d754126a0348d2b10b1738`  
**Latest observed main checkpoint:** `0cf32f0471ecb0b143ceb51dd29ee7e90b4c75c2`  
**Verified stack workflow:** `32084212634`  
**Verified MV3 recovery workflow:** `32088206572`  
**Project state:** verified complete product checkpoint on main, with later verified additive MV3 worker-recovery capability

## Purpose

Ferrum is an agent-native full application tester and the preferred full-fidelity extension acceptance layer for GameSync when available. It is designed to make repeated verification fast while preserving target identity, runtime fidelity, diagnostics, evidence, restart proof, and failure visibility.

Ferrum is broader than a browser wrapper. The same deterministic test/evidence model covers:

- ordinary web applications;
- unpacked Manifest V3 extensions;
- Electron applications;
- arbitrary processes/services;
- remote WebDriver targets;
- Appium-backed native/mobile targets;
- packaged Ferrum desktop builds;
- GitHub Wiki bootstrap/probe workflows.

Ferrum orchestrates real runtimes. A successful tool handshake, mock, rendered dashboard, or compilation is not a substitute for exercising the target application.

## Current verified status, refreshed 2026-08-18

The previous Project Constellation wiki checkpoint was stale. It still described Playwright 1.62.1, Electron 43.2.0, and Appium as unqualified. Current project-owned evidence supersedes those statements.

Project-owned `.agents-memory/STATUS.json` records a verified complete product checkpoint on `main` with merged product commit `1217144c626fade0a52596e16d78f995f827652b` and workflow `32084212634`. The current verified toolchain is:

- Playwright **1.63.0-alpha-2026-08-01**;
- Electron **43.4.0**;
- `@electron/packager` **20.3.0**;
- Node.js **24+**.

The Playwright alpha was not adopted merely because it was newer. The exact proposal head passed Ferrum's complete severe acceptance surface before merge, then the verified state was promoted in project memory.

A later product change, commit `7360184f154f9182f9d754126a0348d2b10b1738`, adds **CDP-confirmed Manifest V3 service-worker forced termination and on-demand recovery**. Its commit records exact-proposal verification by Ferrum CI run `32088206572` across unit/MCP Inspector/evidence integrity, Linux, Windows, browser/MV3/workload paths, Selenium Grid, packaged desktop, Lightpanda, and real Android/Appium.

The latest observed `main` commit in this pass is `0cf32f0471ecb0b143ceb51dd29ee7e90b4c75c2`, a run checkpoint after that verified product work.

## Verified target matrix

### Linux browser/application lane

Verified passed:

- web smoke;
- deterministic offline/recovery smoke;
- cloned Space smoke;
- Chromium and installed Chrome browser matrix;
- MV3 extension smoke;
- workload-pack smoke;
- Workbench evidence replay smoke;
- real Electron application smoke;
- desktop-source smoke;
- packaged desktop build;
- fresh packaged-desktop smoke;
- GitHub Wiki bootstrap browser smoke;
- live ProjectDump Wiki probe.

### Windows browser/application lane

Verified passed:

- web smoke;
- deterministic offline/recovery smoke;
- cloned Space smoke;
- browser matrix across **Chromium, Chrome, Edge, Brave, and Opera GX**;
- Windows browser matrix status **5/5 passed**;
- MV3 extension smoke;
- workload-pack smoke;
- Workbench evidence replay smoke;
- real Electron application smoke;
- desktop-source smoke;
- packaged desktop build;
- fresh packaged-desktop smoke;
- GitHub Wiki bootstrap browser smoke;
- zero Electron force-close events in the recorded acceptance run;
- zero Electron shutdown-warning events in the recorded acceptance run.

### Selenium Grid / remote WebDriver

Ferrum's provider-neutral remote WebDriver lane is runtime-qualified against a real Selenium Grid endpoint with bounded visible-state convergence and evidence retention.

### Lightpanda

Verified:

- Lightpanda **0.3.7**;
- native direct-CDP transport;
- release binary SHA-256 `895339b02205171a181dde743ae0068bb4564884076feac8482baca9c212aa5a`.

Lightpanda remains a fast web-only lane. It is not proof for Chromium-specific extension APIs or MV3 behavior.

### Appium Android lane

Appium is now **runtime-qualified**, superseding the older wiki statement that it remained unqualified.

Verified target:

- Android 15 system Settings;
- Appium **3.6.0**;
- UiAutomator2 **8.4.0**;
- real session lifecycle;
- real element lookup/actions;
- source capture;
- screenshot evidence for home/detail/return states;
- separate 60,000 ms startup budget for server readiness/session creation.

`implementedButNotRuntimeQualifiedYet` is currently empty in project-owned status.

## Manifest V3 service-worker recovery

Ferrum now goes beyond discovering a service worker or proving recovery only through a full browser restart.

The `terminate-service-worker` step uses Chromium CDP to:

1. enumerate targets through `Target.getTargets`;
2. select the exact `service_worker` whose URL belongs to the loaded extension ID;
3. refuse ambiguous multiple-worker matches;
4. close the exact target with `Target.closeTarget`;
5. poll `Target.getTargets` until the target's disappearance is confirmed within a bounded timeout;
6. record `service-worker-termination` evidence;
7. trigger the extension again and verify on-demand worker recovery;
8. continue to a full browser-restart proof as an independent persistence/restart gate.

The extension self-test now proves behavior before forced termination, after forced recovery, and after full restart. Service-worker diagnostics require fresh console/request/response evidence after recovery rather than accepting a stale worker handle.

This capability is directly valuable for MV3 extensions such as GameSync because background workers can be killed by the browser independently of a full browser restart.

## Runtime and package baseline

Current `package.json` pins:

```text
Node >= 24.0.0
playwright 1.63.0-alpha-2026-08-01
electron 43.4.0
@electron/packager 20.3.0
```

Electron 43.4.0 has already passed the required real Linux + Windows Electron and packaged-desktop lanes. The prior “43.4.0 candidate” language is historical and must not be used as the current status.

Any future stack change must repeat the exact affected real-runtime matrix. Never promote a dependency by package freshness alone.

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
npm run smoke:network
npm run smoke:webdriver
npm run smoke:github-wiki
npm run smoke:mcp-inspector
npm run smoke:electron
npm run smoke:desktop
npm run smoke:packaged-desktop
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
- browser restart and state recovery;
- forced service-worker termination and on-demand restart;
- deterministic offline/online transition behavior.

Do not substitute a reduced browser engine for a Chromium-only claim.

## Service-worker observability

Verified worker evidence includes:

- worker discovery and exact extension identity;
- worker console output;
- worker-owned request/response/failure diagnostics;
- interception evidence;
- lifecycle evidence;
- forced termination evidence;
- assertions after on-demand worker recovery;
- assertions before and after full browser restart.

A popup rendering correctly does not prove the background/service-worker path is healthy.

## Spaces and authenticated isolation

Ferrum supports persistent authenticated Spaces plus safe cloned isolation and locking. This enables authenticated workflows without forcing unrelated jobs to share mutable browser state.

A cloned Space must preserve required authenticated state while preventing concurrent jobs from corrupting the canonical profile. Runtime/evidence identity remains explicit.

## Locator and asynchronous-state behavior

Ferrum keeps deterministic selectors first and uses semantic recovery only as an explicit additive fallback. Verified regression coverage includes:

- deterministic-first semantic locator fallback;
- first/nth deterministic disambiguation;
- bounded asynchronous text convergence;
- last-observed-text diagnostics on failure.

Semantic recovery must never hide a broken deterministic selector or silently interact with the wrong control.

## Network recovery

Ferrum can drive deterministic Chromium offline -> failed request -> online recovery while retaining evidence. This is a correctness tool, not merely a network-speed simulator.

Optional deeper transport latency/reset injection should only be added if it proves capability beyond the existing deterministic offline/recovery lane without complicating normal runs.

## Electron lane

Ferrum's Electron runner is runtime-qualified against real Electron applications on Ubuntu and Windows.

Verified evidence includes:

- real application launch;
- main-process console;
- process streams;
- runtime identity;
- renderer diagnostics;
- IPC interaction;
- screenshots/evidence output;
- worker-process containment;
- bounded shutdown;
- packaged-desktop acceptance.

Treat reappearance of an “implementation-only Electron” state as a regression unless newer project-owned evidence proves an actual failure.

## Process lane

Ferrum can launch arbitrary CLI tools, services, or desktop processes and retain stdout, stderr, health/exit evidence, related artifacts, and interactive stdin write/close controls.

## Test specification format

Ferrum JSON specs contain:

- `version`;
- `name`;
- `target`;
- optional timeout/artifact settings;
- ordered `steps`.

Supported target types include:

- `web`;
- `extension`;
- `electron`;
- `process`;
- `appium`.

Common browser steps include open, wait, click, fill, press, snapshot, screenshot, text/visibility/url assertions, evaluate, vitals, console-clean assertions, network-state control, and extension/service-worker actions.

Every step must preserve timing and failure context. Browser failures retain trace/evidence output.

## Evidence model

Each run owns a unique evidence directory. Parallel same-name runs use nonces to avoid collisions.

Evidence may include:

- normalized spec;
- result JSON with per-step timing;
- screenshots;
- Playwright traces;
- page/console/network/service-worker failures;
- worker lifecycle/traffic/termination evidence;
- runtime diagnostics;
- target/build SHA-256 inventory;
- resolved extension ID and discovery path;
- restart proof;
- process/Appium output;
- benchmark machine/workload/reliability metadata;
- `evidence-manifest.json` with SHA-256 integrity information.

Failed runs preserve evidence. Compact agent output does not mean evidence was discarded.

## Evidence integrity

Project-owned status records content-addressed evidence verification with:

- SHA-256 manifest generation;
- CLI verification;
- MCP verification;
- changed/missing/unexpected-payload detection;
- tamper detection;
- legacy bundles reported as unverifiable instead of receiving false success.

Credentials and remote-provider secrets must remain outside published evidence.

## Compact CLI and MCP contract

Ferrum returns concise actionable CLI/MCP summaries by default where requested while preserving complete evidence on disk and exposing the exact evidence directory. An explicit full-output path remains available.

This is an efficiency improvement with **no evidence reduction**.

Verified agent-facing surfaces include CLI commands for test, suite, matrix, pack, Spaces, evidence, bench, dashboard, and GitHub Wiki operations, plus MCP surfaces for doctor, run, suite, browser matrix, benchmark, workload packs, Spaces, durable evidence, and GitHub Wiki probe/bootstrap.

MCP Inspector compatibility is independently smoke-tested.

## GitHub Wiki automation

Ferrum now includes verified GitHub Wiki Git-remote probe and first-page browser bootstrap capabilities.

Verified behavior includes:

- persistent authenticated `github` Space;
- Linux and Windows first-page browser smoke;
- live ProjectDump Wiki remote probe;
- authenticated Git probe when an approved token is available without writing the token to evidence;
- private false-404 protection;
- idempotent behavior when the Wiki already exists;
- before/after browser evidence.

This can bootstrap a repository's first Wiki page before normal source-controlled wiki-Git synchronization begins.

## Benchmarks

`ferrum bench` compares fixed workloads rather than cherry-picked single timings.

Current output retains:

- median and p95;
- machine/runtime metadata;
- workload metadata;
- step budget;
- success rate;
- timeout accounting;
- per-sample evidence directory.

A faster run is not an improvement if it removes steps, diagnostics, evidence, restart proof, target coverage, failure visibility, or fidelity.

## GameSync integration

Ferrum should be used for every applicable GameSync extension change when available, with Opera GX retained as additional compatibility coverage.

For each changed workflow:

1. build the exact GameSync artifact;
2. record its hash/path/runtime identity;
3. load that exact build in Ferrum;
4. exercise the exact changed control/flow;
5. inspect popup/content-script/service-worker behavior;
6. exercise forced MV3 worker termination/recovery when background-worker resilience is relevant;
7. test relevant failure behavior;
8. repeat after reload and full browser restart when stateful;
9. inspect retained evidence;
10. run Opera GX compatibility smoke separately where applicable.

Ferrum also maintains grounded production workload packs for the current GameSync repositories. Extend those packs with change-specific workflows rather than treating a generic smoke as feature-level proof.

If GameSync exposes a reusable Ferrum shortcoming, improve Ferrum rather than masking it with a weaker alternate test.

## Workbench

The Workbench is a real Chromium-controlled workflow, not merely a static dashboard.

Verified coverage includes:

- Doctor;
- spec input/selection;
- Headless control;
- Run action;
- visible result;
- browser diagnostics;
- screenshot evidence;
- durable evidence replay after Workbench restart;
- Linux and Windows desktop/package qualification.

Previously fixed incidents such as ephemeral port reporting and truthful static-asset 404 behavior remain regression targets.

## Important resolved incidents

Project-owned status preserves regression coverage for incidents including:

- a GameSync workload pack invoking a nonexistent build script;
- Android emulator CI shell splitting;
- Android Settings remaining on launcher with `noReset`;
- Appium session creation inheriting too-small step timeout;
- Opera GX startup-page contamination/stalls;
- leaked branded-browser runtimes hanging a matrix indefinitely;
- trace/context teardown hangs;
- Workbench desktop shutdown deadlock;
- Electron handles surviving completed runs;
- reduced Chromium headless behavior breaking MV3 verification;
- Lightpanda timeouts under Chromium lifecycle assumptions;
- evidence-directory collisions;
- warmup `0` coercion;
- checkout line-ending fixture hash drift;
- Workbench ephemeral-port reporting;
- missing static assets returning HTTP 500;
- service-worker observability stopping at discovery/messaging;
- context-heavy successful CLI/MCP output;
- Electron existing without real runtime qualification;
- Appium existing without real runtime qualification;
- benchmarks missing machine/workload/reliability context;
- stale stack-verification markers surviving promotion;
- secret leakage risk at recursive evidence boundaries.

Do not remove regression coverage for these just because they are currently fixed.

## Development workflow

Before editing:

1. read repository `AGENTS.md`;
2. read `.agents-memory/PROJECT.json`, `STATUS.json`, `HANDOFF.md`, and `COMPASS.json`;
3. confirm the exact current main commit;
4. reproduce the target issue with an existing or minimal new spec;
5. establish the current target/evidence baseline.

After editing, run all applicable changed-path and convergence checks. Typical local scripts include:

```bash
npm test
npm run smoke:web
npm run smoke:extension
npm run smoke:network
npm run smoke:electron
npm run smoke:dashboard
```

Run Selenium Grid when remote WebDriver changes, the browser matrix when browser/runtime behavior changes, Lightpanda when that lane changes, real Linux/Windows Electron and package acceptance when desktop/Electron changes, and real Appium when native/mobile behavior changes.

## Current next actions

Current project-owned direction now includes:

- use Ferrum as the acceptance layer for applicable GameSync changes;
- extend grounded GameSync workload packs with exact changed workflows;
- keep forced MV3 worker termination/recovery in the extension regression surface now that it is implemented and verified;
- preserve exact-head severe CI promotion discipline for future stack changes;
- investigate optional transport-level latency/reset fault injection only if it adds useful capability beyond deterministic Chromium offline control;
- continue improving evidence replay/inspection, target breadth, reliability, and speed only when coverage and fidelity remain unchanged or improve.

## Source-of-truth hierarchy

For Ferrum facts, prefer:

1. current `Herbertofury/Ferrum-Browser` source and real evidence;
2. `.agents-memory/STATUS.json` and current project memory;
3. repository docs/manifests;
4. Project Constellation summaries.

Project-owned evidence supersedes stale Project Constellation wording.

## Wiki maintenance triggers

Update this page whenever the verified commit/workflow, supported target matrix, service-worker recovery/diagnostics, evidence schema, CLI/MCP contract, Workbench behavior, GameSync acceptance contract, Electron/Appium qualification, dependency pins, packaging status, GitHub Wiki automation, or project-owned next actions materially change.
