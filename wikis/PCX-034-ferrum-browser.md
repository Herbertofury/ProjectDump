# Ferrum Browser Wiki

**Project Constellation ID:** PCX-034  
**Canonical repository:** `Herbertofury/Ferrum-Browser`  
**Canonical branch:** `main`  
**Verified project version:** `0.2.0`  
**Verified canonical code commit:** `b94902e34db716ffc88395909108901cd4de415a`  
**Project state:** verified canonical implementation on main

## Purpose

Ferrum is an agent-native full application tester. It is designed to make real browser-extension and application verification fast enough to use continuously while preserving runtime fidelity, diagnostics, evidence, restart proof, and exact target identity.

GameSync is the first-class workload, but Ferrum is intentionally broader. The same test-spec model supports browser extensions, ordinary web applications, Electron applications, arbitrary processes/services, and Appium-backed native/mobile targets.

Ferrum does not replace Chromium's rendering engine. It orchestrates real runtimes through deterministic test lanes and produces evidence bundles that can prove what actually ran.

## Current verified status

Ferrum 0.2.0 is recorded in project-owned `.agents-memory/STATUS.json` as a verified canonical implementation on `main`.

The current verified evidence includes:

- 11 unit tests passing with zero failures.
- Syntax checks passing.
- MCP surface validation passing.
- Chromium web smoke passing on Linux and Windows.
- Manifest V3 extension smoke passing on Linux and Windows.
- Workbench smoke passing on Linux and Windows.
- Full browser restart proof passing.
- Post-restart service-worker messaging passing.
- Zero recorded runtime errors for the verified Chromium runs.
- Verified exact extension SHA-256 inventory and runtime extension identity.
- Lightpanda 0.3.7 direct-CDP smoke passing.
- Published artifact round-trip verification with downloaded bytes matching provider digests.

The Electron and Appium target runners are implemented, but project status explicitly says they are not yet runtime-qualified against real target applications. Do not represent those lanes as fully verified until real Electron/Appium acceptance runs exist.

## Requirements

### Runtime

Ferrum requires Node.js 24 or newer.

Install dependencies and Chromium:

```bash
npm install
npx playwright install chromium
```

Lightpanda is optional. To enable it, set `FERRUM_LIGHTPANDA` to a verified Lightpanda binary, or place a compatible `lightpanda` executable on `PATH`.

## Main commands

Inspect local runtime availability:

```bash
npx ferrum doctor
```

Run the built-in web self-test:

```bash
npx ferrum test examples/self-test-web.json --headless
```

Run the built-in Manifest V3 extension self-test:

```bash
npx ferrum test examples/self-test-extension.json --headless
```

Run independent specs concurrently:

```bash
npx ferrum suite examples/self-test-web.json examples/self-test-extension.json --workers 2 --headless
```

Benchmark one workload repeatedly and report median/p95 timings:

```bash
npx ferrum bench path/to/benchmark-spec.json --engines chromium,lightpanda --runs 7 --warmup 1 --headless
```

Open the local Chromium-based workbench:

```bash
npx ferrum dashboard
```

Expose Ferrum to agents over MCP stdio:

```bash
npx ferrum mcp
```

The repository also exposes these package scripts:

```bash
npm test
npm run smoke:web
npm run smoke:extension
npm run smoke:lightpanda
npm run smoke:dashboard
npm run ci
```

`npm run ci` runs unit tests plus Chromium web, extension, and dashboard smoke checks.

## Execution lanes

### Chromium fidelity lane

Ferrum uses Playwright persistent Chromium contexts for browser and extension correctness.

This is the mandatory lane for:

- unpacked Chromium/Manifest V3 extensions;
- service workers;
- content scripts;
- extension pages;
- permissions;
- persistent browser profiles;
- restart and state persistence proof.

Headless extension runs intentionally use Playwright's full `chromium` channel instead of the reduced headless shell because the reduced shell previously failed to provide the required extension behavior.

### Lightpanda speed lane

Lightpanda is an optional fast web lane driven through native CDP.

Use it only for web workloads where a headless DOM/JavaScript engine is sufficient. It is not valid proof for Chromium-specific extension behavior.

The current verified Lightpanda lane uses version 0.3.7 and has smoke coverage for:

- open;
- snapshot;
- click;
- assert-text;
- assert-console-clean.

### Electron lane

Ferrum uses Playwright `_electron` so Electron applications can reuse the same ordered step/evidence model.

The lane is implemented but not yet qualified against a real Electron application in the current verified status.

### Process lane

Ferrum can launch arbitrary CLI tools, services, or desktop processes and capture:

- stdout;
- stderr;
- optional health checks;
- exit status;
- evidence output.

This lane is already part of the verified Workbench flow.

### Appium lane

Ferrum can speak W3C WebDriver directly to an Appium endpoint for native/mobile targets when the required platform driver is available.

The lane is implemented but not yet runtime-qualified against a real device or emulator.

## Test specification format

Ferrum test specs are JSON documents containing:

- `version`;
- `name`;
- `target`;
- optional timeouts/artifact settings;
- ordered `steps`.

Supported target types are:

- `web`;
- `extension`;
- `electron`;
- `process`;
- `appium`.

Common browser steps include:

- `open`;
- `wait`;
- `click`;
- `fill`;
- `press`;
- `snapshot`;
- `screenshot`;
- `assert-text`;
- `assert-visible`;
- `assert-url`;
- `evaluate`;
- `vitals`;
- `assert-console-clean`.

Extension-only steps include:

- `extension-page`;
- `assert-service-worker`;
- `restart`.

Every step records timing and failure context. Browser failures preserve a Playwright trace.

## Repository architecture

The current top-level source layout is:

| Path | Responsibility |
| --- | --- |
| `bin/ferrum.mjs` | Package CLI entry point exposed as `ferrum`. |
| `src/cli.mjs` | Command parsing and CLI orchestration. |
| `src/core/` | Test-spec handling, runner orchestration, benchmarking, evidence, hashing, paths, statistics, doctor, and suites. |
| `src/browser/` | Browser-specific control and browser test primitives. |
| `src/runners/` | Target-specific runners. |
| `src/mcp/` | MCP stdio exposure for agent control. |
| `src/server/` | Local server/workbench support. |
| `ui/` | Workbench UI assets. |
| `examples/` | Built-in executable example specs including web and extension self-tests. |
| `tests/` | Automated regression tests. |
| `docs/ARCHITECTURE.md` | Execution-lane and evidence architecture. |
| `docs/TEST_SPEC.md` | Test-spec contract. |
| `docs/UPSTREAMS.md` | Upstream/reference implementations and sources. |
| `.agents-memory/` | Project identity, Compass, verified status, and handoff state. |

### Core modules

`src/core/` currently contains modules for:

- `benchmark.mjs` - repeatable benchmark orchestration;
- `doctor.mjs` - environment/runtime detection;
- `evidence.mjs` - evidence-bundle management;
- `hash.mjs` - target/file hashing;
- `paths.mjs` - path resolution;
- `process-utils.mjs` - process lifecycle utilities;
- `runner.mjs` - common run orchestration;
- `spec.mjs` - test-spec normalization/validation;
- `stats.mjs` - benchmark statistics;
- `suite.mjs` - bounded concurrent suites.

## Evidence model

Each Ferrum run creates its own unique evidence folder under an `artifacts/` path. The current model uses a timestamp, test name, and nonce so parallel same-name runs cannot collide.

Evidence can include:

- normalized `spec.json`;
- `result.json` with per-step timing;
- screenshots;
- Playwright trace files;
- console/page/network failure events;
- runtime diagnostics;
- extension build SHA-256 inventory;
- resolved runtime extension ID and how that identity was obtained;
- browser restart proof;
- process or Appium output when applicable.

Failed runs preserve their artifacts. Parallel runs must never share the same evidence directory.

## Manifest V3 extension verification

Ferrum's extension lane is designed to prove more than build success.

For an unpacked extension it can:

1. load the exact build directory into a persistent Chromium profile;
2. hash extension files;
3. resolve the runtime extension ID;
4. exercise popup/options/content-script/service-worker behavior;
5. capture screenshots, diagnostics, and traces;
6. restart the browser using the same profile;
7. resolve the extension again after restart;
8. prove post-restart messaging/behavior;
9. retain the complete evidence bundle.

The verified self-test currently resolves extension ID `felmepoiflfponlkemhjaadagpppepgf` and a fixture extension SHA-256 of `57024706eed1b4dc2f07ab0f343a0bbc0524bf10c43fb7a2c810c4ddb8bebebb` on both Linux and Windows.

## GameSync integration

`examples/gamesync-extension.json` is the starting acceptance workload for the standalone GameSync extension.

Point its `target.path` at the freshly built GameSync `dist` directory.

Ferrum is an additional full-fidelity acceptance layer. Generic CI or an Opera smoke test alone is not considered sufficient evidence for a changed GameSync extension workflow when Ferrum coverage applies.

For each changed GameSync feature:

1. build the current GameSync extension;
2. point the Ferrum workload at the exact new build;
3. exercise the changed user flow;
4. verify relevant service-worker/content-script behavior;
5. include restart/persistence checks when stateful;
6. preserve evidence;
7. keep Opera GX as an additional compatibility lane rather than replacing Ferrum.

If real GameSync testing exposes reusable Ferrum defects such as slow discovery, weak diagnostics, flaky selectors, missing target coverage, evidence collisions, or unnecessary round trips, fix Ferrum itself, add regression coverage, and rerun GameSync instead of routing around the tester.

## Workbench

`npx ferrum dashboard` opens Ferrum's local Workbench inside controlled Chromium.

The current verified status records end-to-end Workbench proof on Linux and Windows for:

- selected process spec;
- Headless control;
- populated Doctor output;
- Run button;
- visible PASSED result;
- browser diagnostics;
- screenshots with zero browser errors.

A prior Workbench bug where an ephemeral port was reported as port `0` was fixed. The server now reports the actual bound port.

A missing favicon/static-asset request also previously surfaced as HTTP 500. Missing static assets now return a truthful 404, and the Workbench uses an inline data favicon.

## MCP agent interface

`npx ferrum mcp` exposes Ferrum over MCP stdio.

The current MCP surface includes:

- doctor;
- single-run execution;
- suites;
- benchmarks.

The design intentionally keeps deterministic Playwright/CDP behavior under the agent-facing surface rather than replacing the underlying runner with opaque semantic automation.

## Parallel suites and benchmarking

`ferrum suite` runs independent specs with bounded concurrency. Each run keeps a separate evidence ID and evidence directory.

`ferrum bench` repeats an identical workload with explicit warmup and run counts and reports median and p95 timing.

An earlier bug coerced explicit warmup `0` to `1`; current 0.2.0 status records that explicit zero warmup is now preserved.

When a spec is compatible with both engines, the same workload can compare Chromium and Lightpanda without duplicating the test definition.

## Important correctness rules

- Chromium is the proof lane for Chromium-only behavior.
- Lightpanda performance results do not prove extension behavior.
- Evidence/diagnostics may not be reduced merely to improve speed.
- A run must identify the exact build it tested.
- Stateful extension verification should include restart proof.
- Failed tests keep their evidence.
- Parallel runs must not collide on artifact directories.
- A generic browser test is not equivalent to testing the real extension/service-worker flow.

## Development workflow

Before editing:

1. read `AGENTS.md`;
2. read `.agents-memory/PROJECT.json`, `STATUS.json`, `HANDOFF.md`, and `COMPASS.json`;
3. confirm the canonical branch and current verified commit;
4. reproduce the target issue with an existing spec or a new minimal spec.

After editing:

```bash
npm test
npm run smoke:web
npm run smoke:extension
npm run smoke:dashboard
```

Run `npm run smoke:lightpanda` when the change affects the Lightpanda lane and the binary is available.

Changes affecting one target runner should also exercise that target's exact workflow. Electron/Appium work is not fully complete until tested against a real application/device path.

For release-level verification, preserve the resulting evidence bundle and update project-owned `.agents-memory/STATUS.json` only with behavior that was actually exercised.

## Troubleshooting

### Extension fails only in headless mode

Confirm the test is using Ferrum's full Playwright Chromium channel rather than the reduced headless shell. This exact issue previously broke Manifest V3 verification.

### Lightpanda times out through Playwright

Ferrum's verified design uses Lightpanda's native CDP server directly. Do not route the Lightpanda lane back through Chromium lifecycle assumptions.

### Parallel runs overwrite evidence

The current evidence ID includes a random nonce. If collisions reappear, treat that as a Ferrum regression rather than serializing all work as a workaround.

### Extension identity changes unexpectedly

Check the target build path and SHA-256 inventory first. Ferrum is intended to prove exact build identity, not simply that some extension with a similar name loaded.

### Restart test passes before restart but fails after relaunch

Inspect the persistent profile, runtime extension ID, service-worker discovery, and post-restart evidence. The verified acceptance model requires the same build to return and remain functional after relaunch.

### Workbench reports the wrong local port

The known port-0 bug is resolved in the current verified implementation. Reappearance should be treated as a regression.

### Missing static files appear as server 500 errors

The current server should return 404 for missing assets. A 500 is a regression and should be covered by a server/Workbench test.

## Known limitations and open work

Project-owned status currently lists these next actions:

- use Ferrum in every applicable GameSync extension verification;
- convert real GameSync flows into reusable Ferrum workload packs;
- improve speed, reliability, observability, setup, and target coverage when real workloads expose reusable problems;
- add richer extension service-worker CDP console/network inspection;
- qualify Electron against a real Electron application;
- qualify Appium against a real device/emulator path.

There are currently no recorded blockers in `.agents-memory/STATUS.json`.

## Source-of-truth hierarchy

For Ferrum facts, prefer sources in this order:

1. current `Herbertofury/Ferrum-Browser` repository and runtime evidence;
2. `.agents-memory/STATUS.json` and current handoff/Compass;
3. `README.md` and project docs;
4. Project Constellation catalog summaries.

If Project Constellation conflicts with the project repository, update the wiki from the project-owned evidence rather than preserving stale catalog text.

## Wiki maintenance triggers

Update this page when any of the following materially changes:

- Ferrum version;
- verified canonical commit/workflow;
- supported target types;
- test-spec schema or step set;
- Chromium/Lightpanda behavior;
- evidence format;
- MCP tool surface;
- Workbench controls;
- GameSync integration contract;
- runtime qualification status for Electron/Appium;
- required Node/Playwright versions;
- verification commands;
- known incidents or troubleshooting guidance.