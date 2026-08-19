# Ferrum Browser Wiki

**Project Constellation ID:** `PCX-034`
**Canonical repository:** [Herbertofury/Ferrum-Browser](https://github.com/Herbertofury/Ferrum-Browser)
**Canonical branch:** `main`
**Verified project version:** `0.2.0`
**Latest verified merged product commit:** `8ff1d85d26500f415c01b7de1753608c4d689f80`
**Latest verified full Ferrum CI:** `32201388085`
**Native Windows qualification commit:** `eb88b2149cf695edde2591e8e16d13bb43a90c8e`
**Native Windows workflows:** Ferrum CI `32199800957`, Native Windows `32199800977`
**Tauri v2 qualification commit:** `cf79303b8788d58fe274d7ce3e4a9b87d889c310`
**Tauri qualification workflow:** `32194473469`
**Latest observed main commit:** `dcff27b8c2a2b365aad43fff626fcf233cb3a969` (evolution ledger for run 33)
**Earlier important verified product commits:** Playwright-stack `1217144c626fade0a52596e16d78f995f827652b`; MV3 recovery `7360184f154f9182f9d754126a0348d2b10b1738`; service parity `09c8334ef5b744afd8ca94732cd9c458744058fb`
**Project state:** verified complete product checkpoint on main with later verified Tauri v2, native Windows WPF/UIA, and CI critical-path improvements

## Purpose

Ferrum is an agent-native full application tester and the preferred full-fidelity extension acceptance layer for GameSync when available. It is designed to make repeated verification fast while preserving target identity, runtime fidelity, diagnostics, evidence, restart proof, and failure visibility.

Ferrum is broader than a browser wrapper. The same deterministic test/evidence model covers:

- ordinary web applications;
- unpacked Manifest V3 extensions;
- Electron applications;
- Tauri v2 desktop applications;
- native Windows applications through W3C/Appium UI Automation providers;
- arbitrary processes/services;
- remote WebDriver targets;
- Appium-backed native/mobile targets;
- packaged Ferrum desktop builds;
- GitHub Wiki bootstrap/probe workflows.

Ferrum orchestrates real runtimes. A successful tool handshake, mock, rendered dashboard, or compilation is not a substitute for exercising the target application.

## Current verified status, refreshed 2026-08-19

The older `.agents-memory/STATUS.json` remains a valid verified product checkpoint but is not the newest additive evidence. Newer evolution checkpoints supersede it for the capabilities below without invalidating its prior matrix.

The currently verified baseline toolchain remains:

- Playwright **1.63.0-alpha-2026-08-17**;
- Electron **43.4.0**;
- `@electron/packager` **20.3.0**;
- Node.js **24+**.

The Playwright alpha is verified project state, not an unqualified freshness experiment. Exact proposal trees pass the affected acceptance surface before merge and project-memory promotion.

The earlier MV3 product change at commit `7360184f154f9182f9d754126a0348d2b10b1738` remains an important verified milestone because it added CDP-confirmed Manifest V3 service-worker forced termination and on-demand recovery. Ferrum CI run `32088206572` verified that capability across unit/MCP Inspector/evidence integrity, Linux, Windows, browser/MV3/workload paths, Selenium Grid, packaged desktop, Lightpanda, and real Android/Appium.

Ferrum subsequently added and verified:

- bounded-parallel evidence-history scans with no result cap;
- monotonic run-relative evidence timing and direct compact-result duration;
- no implicit 400-element snapshot ceiling;
- stable agent snapshot refs across DOM mutation and replacement;
- prompt process readiness/log failure when the child has already terminated;
- direct HTTP interaction for process/service targets with retained response artifacts and authoritative child-exit attribution;
- a zero-additional-dependency local/Docker real-service parity fixture;
- real Tauri v2 application qualification on Linux and Windows through the existing provider-neutral W3C runner;
- real native Windows WPF/UIA qualification through two independent Appium 3 Windows drivers;
- CI critical-path parallelization that retained all five Windows browsers while reducing the measured full CI wall clock from 349 seconds to 149 seconds in the verified comparison.

### Latest verified CI critical-path improvement

Commit `8ff1d85d26500f415c01b7de1753608c4d689f80` keeps Chromium, Chrome, Edge, the Windows MV3/restart path, Spaces, Workbench replay, Electron, desktop-source, package, and fresh packaged-desktop gates in the core Windows job. Brave and Opera GX now run as independent Windows matrix jobs with `--require-all` and distinct retained evidence.

Ferrum CI `32201388085` passed unit, Linux, Windows core, Windows Brave, Windows Opera GX, Selenium Grid, Lightpanda, and Android/Appium jobs. The recorded comparison reduced overall workflow wall clock from **349 seconds to 149 seconds**, a **57.31%** reduction, without removing any browser target or acceptance surface. This proves faster feedback, not lower total hosted-runner consumption.

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

Brave and Opera GX may execute in independent CI jobs. That is scheduling isolation only. Their browser coverage and retained evidence remain required.

### Selenium Grid / remote WebDriver

Ferrum's provider-neutral remote WebDriver lane is runtime-qualified against a real Selenium Grid endpoint with bounded visible-state convergence and evidence retention.

### Tauri v2 desktop lane

Ferrum now qualifies real Tauri v2 applications through the same provider-neutral W3C WebDriver runner used for remote browser endpoints.

The required production-like acceptance uses the embedded [`tauri-plugin-wdio-webdriver`](https://github.com/Samyssmile/tauri-plugin-wdio-webdriver) provider rather than adding a special Ferrum runner. The verified stack is:

- `tauri-plugin-wdio-webdriver` **1.3.0**;
- Tauri **2.11.5**;
- `tauri-build` **2.6.3**;
- `tauri-runtime` **2.11.3**;
- `tauri-runtime-wry` **2.11.4**;
- pinned Tauri fixture repository `tauri-apps/webdriver-example` at `e4c2607cd60287a0ceb69458a0d69d0b676f39a6`.

Workflow `32194473469` verified the embedded provider on both Linux and Windows. The real acceptance includes:

- building and launching the pinned real Tauri v2 application;
- bounded provider readiness;
- a real Ferrum WebDriver session;
- real UI input and click;
- Rust `greet` IPC round trip;
- screenshot and page-source capture;
- session evidence;
- application SHA-256 and runtime identity;
- clean WebDriver/application teardown.

The workflow also retains `tauri-driver` **2.0.6** as an official reference lane. The official Linux reference passed. The direct official Windows path remains diagnostic because WebView2/msedgedriver can fail before session creation, so it is not used as the required Windows acceptance gate.

Important recovered failure history:

- a mixed Tauri runtime family blocked an earlier build;
- `tauri-build` 2.6.0 was incompatible with Tauri 2.11.5 and was corrected to 2.6.3;
- Windows embedded capability generation needed deterministic JSON escaping for Windows paths.

Do not loosen those version/fixture controls merely to make a Tauri job green.

### Native Windows WPF/UIA lane

Ferrum now qualifies native Windows applications through its existing W3C WebDriver runner and Appium 3 instead of adding a separate action schema.

The dedicated `.github/workflows/native-windows.yml` matrix currently verifies two independent providers:

- `appium-desktop-driver` **2.4.5**, automation name `DesktopDriver`;
- `appium-novawindows-driver` **1.4.4**, automation name `NovaWindows`.

Both providers ran the same deterministic .NET 8 WPF/UIA fixture twice through distinct clean WebDriver sessions. Workflow `32199800977` passed both matrix jobs, and broad Ferrum CI `32199800957` passed the surrounding regression surface.

The fixture SHA-256 recorded by the evolution checkpoint is:

`E865F876A7999CEF1F067484C8E7007A809EA2A8A4EE7A65812498D4123A9330`

The required native workload proves:

1. launch of the real WPF fixture;
2. `AutomationId` lookup for a text input;
3. text fill;
4. `AutomationId` lookup and click for a submit control;
5. exact `hello Ferrum` status assertion;
6. a second toggle interaction and visibility transition;
7. screenshot capture;
8. page-source capture;
9. a second distinct clean session;
10. bounded Appium teardown.

The native desktop providers are not browser endpoints. A browser-only WebDriver command such as `GET /url` must not be required for provider-neutral native-app acceptance. NovaWindows exposed that mismatch during failure-first qualification, and the fixture was corrected to assert provider-neutral session evidence instead.

The dedicated PowerShell smoke is:

```powershell
.\scripts\appium-windows-desktop-smoke.ps1
```

The workflow builds the deterministic fixture with:

```powershell
dotnet build .\fixtures\windows-uia\Ferrum.WindowsFixture.csproj -c Release --nologo
```

Native Windows support currently proves WPF/UIA acceptance through these two providers. It does not imply that every Windows framework or accessibility edge case has already been qualified.

### Lightpanda

Verified:

- Lightpanda **0.3.7**;
- native direct-CDP transport;
- release binary SHA-256 `895339b02205171a181dde743ae0068bb4564884076feac8482baca9c212aa5a`.

Lightpanda remains a fast web-only lane. It is not proof for Chromium-specific extension APIs or MV3 behavior.

### Appium Android lane

Appium is runtime-qualified.

Verified target:

- Android 15 system Settings;
- Appium **3.6.0**;
- UiAutomator2 **8.4.0**;
- real session lifecycle;
- real element lookup/actions;
- source capture;
- screenshot evidence for home/detail/return states;
- separate 60,000 ms startup budget for server readiness/session creation.

The native Windows and Android lanes share Ferrum's principle of keeping the common W3C/evidence contract while allowing provider-specific capabilities where required.

## Manifest V3 service-worker recovery

Ferrum goes beyond discovering a service worker or proving recovery only through a full browser restart.

The `terminate-service-worker` step uses Chromium CDP to:

1. enumerate targets through `Target.getTargets`;
2. select the exact `service_worker` whose URL belongs to the loaded extension ID;
3. refuse ambiguous multiple-worker matches;
4. close the exact target with `Target.closeTarget`;
5. poll `Target.getTargets` until the target's disappearance is confirmed within a bounded timeout;
6. record `service-worker-termination` evidence;
7. trigger the extension again and verify on-demand worker recovery;
8. continue to a full browser-restart proof as an independent persistence/restart gate.

The extension self-test proves behavior before forced termination, after forced recovery, and after full restart. Service-worker diagnostics require fresh console/request/response evidence after recovery rather than accepting a stale worker handle.

This capability is directly valuable for MV3 extensions such as GameSync because background workers can be killed by the browser independently of a full browser restart.

## Runtime and package baseline

Current `package.json` pins:

```text
Node >= 24.0.0
playwright 1.63.0-alpha-2026-08-17
electron 43.4.0
@electron/packager 20.3.0
```

Electron 43.4.0 has passed the required real Linux + Windows Electron and packaged-desktop lanes.

Tauri and native Windows provider dependencies are CI/fixture qualifications rather than blanket Ferrum core dependencies. Keep them isolated to the relevant target workflow unless a measured requirement justifies promotion into the default installation.

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

Run the disposable local/container service parity smoke:

```bash
npm run smoke:service-fixture
```

Run the Tauri reference/provider smokes when the required external fixture/runtime prerequisites are present:

```bash
npm run smoke:tauri
npm run smoke:tauri-embedded
```

Current package scripts include:

```bash
npm test
npm run smoke:web
npm run smoke:extension
npm run smoke:network
npm run smoke:service-fixture
npm run smoke:webdriver
npm run smoke:tauri
npm run smoke:tauri-embedded
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

## Locator, snapshot, and asynchronous-state behavior

Ferrum keeps deterministic selectors first and uses semantic recovery only as an explicit additive fallback. Verified regression coverage includes:

- deterministic-first semantic locator fallback;
- first/nth deterministic disambiguation;
- bounded asynchronous text convergence;
- last-observed-text diagnostics on failure.

Semantic recovery must never hide a broken deterministic selector or silently interact with the wrong control.

### Complete snapshots by default

Ferrum previously imposed an implicit 400-element ceiling on browser snapshots. That was removed at commit `c43c3d6be08ccf58253a56904289d0ee490b880d`.

Current behavior:

- generic browser snapshots return every qualifying element by default;
- Lightpanda snapshots return every qualifying element by default;
- StepEngine passes no implicit maximum;
- an explicit positive `max` remains supported when the caller deliberately requests a limit.

Failure-first coverage reproduced the old cap. Ferrum CI run `32124761222` then verified the uncapped behavior, including a real Lightpanda fixture with **451** qualifying elements and a separate explicit `max: 123` proof, while preserving the complete Windows browser matrix, MV3/workloads/restart, packaged desktop, WebDriver Grid, and Android/Appium acceptance surface.

This matters for agent use because a hidden snapshot ceiling can silently remove valid actionable controls from the agent-visible page model.

### Snapshot ref lifetime and DOM mutation

Snapshot refs are now page-session identities rather than recyclable positional labels.

Commit `dfa3712b4b03aa8b58c396f7caf3694e4639941c` fixed two failure modes:

- a retired ref could previously be reassigned to a different element after DOM replacement;
- Lightpanda could duplicate live refs after DOM insertion.

Current behavior preserves existing ref ownership, advances new refs above reserved/live values, rejects forged unsafe numeric refs, and prevents a retired ref from silently targeting another element later in the same page session. Ferrum CI run `32126705729` verified this across the full matrix, and the Lightpanda smoke inserts a new button after an initial snapshot and then proves the original `e1` still activates the original control.

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

Treat reappearance of an implementation-only Electron state as a regression unless newer project-owned evidence proves an actual failure.

## Process and service lane

Ferrum can launch arbitrary CLI tools, services, or desktop processes and retain stdout, stderr, health/exit evidence, related artifacts, and interactive stdin write/close controls.

Current process lifecycle behavior includes:

- startup health polling bounded by the remaining startup deadline;
- immediate readiness failure when the child terminates before health becomes ready;
- prompt `assert-log` failure after child exit while still checking final unterminated output;
- optional secret-safe structured Node diagnostic reports for real uncaught process failures;
- direct HTTP requests from the process target after readiness.

### `http-request` step

A process spec can now exercise the running service directly:

```json
{
  "action": "http-request",
  "method": "POST",
  "url": "http://127.0.0.1:8080/echo",
  "json": { "source": "local" },
  "status": 200,
  "text": "\"source\":\"local\""
}
```

Verified semantics:

- `method` defaults to `GET`;
- `headers` are supported;
- `json` automatically uses JSON serialization and adds `content-type: application/json` unless already supplied;
- raw `body` is supported instead of `json`;
- defining both `body` and `json` is rejected;
- each request has a positive bounded timeout;
- request transport is raced against the authoritative child lifecycle;
- a child that exits during the request is reported as a process exit with code/signal instead of a generic fetch failure;
- response bodies are retained under the run evidence directory before status/text assertions are evaluated;
- `process-http-response` evidence records method, URL, status, request bytes, response bytes, content type, and retained artifact path;
- optional `status` and substring `text` assertions fail only after the complete response artifact is preserved.

This closes the gap where Ferrum could previously prove a service became healthy but could not exercise its API through the same process target.

### Disposable real-service parity fixture

`scripts/disposable-service-smoke.mjs` is a zero-additional-dependency acceptance fixture for the process/service lane.

It runs the same small HTTP service in two modes:

1. a local Node child process;
2. a real Docker container based on `node:24-alpine`.

Both modes are exercised through the same Ferrum process specification:

- health request to `/health`;
- `POST /echo` with JSON body and status/text assertions;
- `GET /state` with status/text assertions;
- two retained `process-http-response` events and non-empty response artifacts.

The container lane additionally verifies:

- Docker server availability;
- real 64-character container ID;
- mapped host port;
- exact image ID in `sha256:<64 hex>` form;
- image repository digests;
- container Node runtime version;
- explicit `docker rm -f` cleanup;
- proof that the container is absent after cleanup.

The final summary records local/container durations, response sizes/statuses, provision time, cleanup time, image/runtime identity, and `additionalNodeDependencyCount: 0`.

Dedicated workflow `.github/workflows/service-fixture.yml` runs this smoke on Ubuntu with Node 24 and retains `artifacts/service-fixture/` even when the job fails. The additive acceptance was verified by Ferrum CI `32139957979` and dedicated service-fixture run `32139957988`.

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
- `webdriver`;
- `appium`.

Tauri and native Windows qualifications intentionally reuse `webdriver` rather than inventing separate target schemas.

Common browser steps include open, wait, click, fill, press, snapshot, screenshot, text/visibility/url assertions, evaluate, vitals, console-clean assertions, network-state control, and extension/service-worker actions.

Process steps additionally include stdin write/close, log assertions, HTTP request, waiting for exit, and exit-code assertions as supported by the current runner.

WebDriver/native steps use the provider-neutral find/fill/click/assert/screenshot/source/session contract where the underlying provider supports them. Browser-only commands must not be imposed on native providers merely because both speak W3C WebDriver.

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
- process/Appium/WebDriver output;
- Tauri application/provider identity;
- native Windows fixture/provider/session identity;
- process HTTP response artifacts;
- benchmark machine/workload/reliability metadata;
- `evidence-manifest.json` with SHA-256 integrity information.

Failed runs preserve evidence. Compact agent output does not mean evidence was discarded.

### Evidence timing

Current finalized events preserve the original wall-clock timestamp and also expose monotonic run-relative `elapsedMs`. Finalized and compact results expose direct `durationMs` so agents do not have to derive runtime duration from wall-clock timestamps.

This timing path was verified as additive. It does not replace raw timestamps or discard full evidence.

### Evidence history completeness and speed

Evidence-history summary scans now use bounded parallel I/O while retaining every finalized run. The implementation intentionally avoids hidden caps, pagination shortcuts, or cache staleness. Incomplete and malformed entries remain skippable without truncating valid finalized history.

This matters to long-lived Ferrum installations where evidence history can grow large but still has to remain complete.

## Evidence integrity

Project-owned status records content-addressed evidence verification with:

- SHA-256 manifest generation;
- CLI verification;
- MCP verification;
- changed/missing/unexpected-payload detection;
- tamper detection;
- legacy bundles reported as unverifiable instead of receiving false success.

Evidence run IDs reject dot and dot-dot traversal aliases before path resolution.

Credentials and remote-provider secrets must remain outside published evidence.

## Compact CLI and MCP contract

Ferrum returns concise actionable CLI/MCP summaries by default where requested while preserving complete evidence on disk and exposing the exact evidence directory. An explicit full-output path remains available.

This is an efficiency improvement with **no evidence reduction**.

Verified agent-facing surfaces include CLI commands for test, suite, matrix, pack, Spaces, evidence, bench, dashboard, and GitHub Wiki operations, plus MCP surfaces for doctor, run, suite, browser matrix, benchmark, workload packs, Spaces, durable evidence, and GitHub Wiki probe/bootstrap.

Current compact results include monotonic event timing and direct run duration, and process targets now expose HTTP request capability through the same runner/evidence model.

MCP Inspector compatibility is independently smoke-tested.

## GitHub Wiki automation

Ferrum includes verified GitHub Wiki Git-remote probe and first-page browser bootstrap capabilities.

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

The run-33 CI change follows the same rule: the measured wall-clock improvement is accepted only because all five Windows browsers and the prior required jobs remained green with retained artifacts.

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

Project-owned status and evolution checkpoints preserve regression coverage for incidents including:

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
- secret leakage risk at recursive evidence boundaries;
- evidence IDs accepting unsafe dot-only aliases;
- evidence-history scans serializing unnecessary I/O;
- compact evidence lacking direct run-relative timing;
- snapshots silently stopping at 400 qualifying elements;
- snapshot refs being duplicated or silently retargeted after DOM mutation/replacement;
- process log assertions consuming the remaining timeout after the child had already exited;
- process health checks consuming the startup deadline after a terminal child state;
- process targets proving health without being able to exercise the service API;
- HTTP transport errors hiding an authoritative child-process exit;
- container/service acceptance lacking exact image/runtime identity and cleanup proof;
- mixed Tauri runtime-family versions blocking the real fixture build;
- Windows Tauri capability JSON requiring deterministic path escaping;
- direct official Windows `tauri-driver` being unsuitable as the required gate when WebView2/msedgedriver fails before session creation;
- nested `cmd.exe` quoting breaking Appium readiness on the native Windows fixture;
- native Appium providers being incorrectly asked to satisfy browser-only `GET /url` behavior;
- alternate browser installation serializing the Windows CI critical path even though Brave and Opera GX are independent acceptance lanes.

Do not remove regression coverage for these just because they are currently fixed.

## Development workflow

Before editing:

1. read repository `AGENTS.md`;
2. read `.agents-memory/PROJECT.json`, `STATUS.json`, `HANDOFF.md`, and `COMPASS.json`;
3. confirm the exact current main commit;
4. read newer `EVOLUTION_RUN_*` checkpoints when they postdate `STATUS.json`;
5. reproduce the target issue with an existing or minimal new spec;
6. establish the current target/evidence baseline.

After editing, run all applicable changed-path and convergence checks. Typical local scripts include:

```bash
npm test
npm run smoke:web
npm run smoke:extension
npm run smoke:network
npm run smoke:service-fixture
npm run smoke:electron
npm run smoke:dashboard
```

Run Selenium Grid when remote WebDriver changes, the browser matrix when browser/runtime behavior changes, Lightpanda when that lane changes, the service fixture when process HTTP/service behavior changes, real Linux/Windows Electron and package acceptance when desktop/Electron changes, and real Appium when native/mobile behavior changes.

For Tauri changes, run the dedicated Tauri WebDriver workflow because it builds a pinned real Tauri application on Linux and Windows and verifies the embedded W3C provider. Preserve the official `tauri-driver` reference lane as diagnostic/reference evidence rather than silently substituting it for the required embedded Windows gate.

For native Windows changes, run the dedicated Native Windows matrix and require both `DesktopDriver` and `NovaWindows` against the same deterministic WPF/UIA workload unless project-owned evidence deliberately revises the provider set.

A process/service change that claims container parity should retain explicit runtime/image identity and cleanup proof rather than treating container startup alone as acceptance.

## Current next actions

Current project-owned direction includes:

- use Ferrum as the acceptance layer for applicable GameSync changes;
- extend grounded GameSync workload packs with exact changed workflows;
- keep forced MV3 worker termination/recovery in the extension regression surface;
- keep complete uncapped snapshots and page-session ref identity as agent-facing correctness guarantees;
- preserve exact-head severe CI promotion discipline for future stack changes;
- keep Tauri v2 embedded WebDriver qualification on both Linux and Windows;
- keep the two-provider native Windows differential so provider-specific assumptions remain visible;
- evaluate compact Windows-native adapter ideas only against the same deterministic fixture and evidence contract;
- keep Brave and Opera GX parallelized independently while preserving their exact acceptance/evidence requirements;
- use the local/container service fixture as a baseline before adopting heavier service-test dependencies;
- evaluate fixed-seed stateful API testing only if it produces a minimized repeatable defect reproducer without weakening current evidence;
- evaluate deterministic transport-fault injection only if exact fault configuration and recovery are preserved;
- continue improving evidence replay/inspection, target breadth, reliability, and speed only when coverage and fidelity remain unchanged or improve.

## Source-of-truth hierarchy

For Ferrum facts, prefer:

1. current [Herbertofury/Ferrum-Browser](https://github.com/Herbertofury/Ferrum-Browser) source and real evidence;
2. the newest project-owned `EVOLUTION_RUN_*` checkpoint when it postdates `STATUS.json`;
3. `.agents-memory/STATUS.json` and other current project memory;
4. repository docs/manifests;
5. Project Constellation summaries.

Project-owned evidence supersedes stale Project Constellation wording.

## Wiki maintenance triggers

Update this page whenever the verified commit/workflow, supported target matrix, Tauri qualification, native Windows provider matrix, CI scheduling/critical-path architecture, service-worker recovery/diagnostics, process/service HTTP capability, disposable service acceptance, snapshot completeness/ref semantics, evidence schema/history/timing, CLI/MCP contract, Workbench behavior, GameSync acceptance contract, Electron/Appium qualification, dependency pins, packaging status, GitHub Wiki automation, or project-owned next actions materially change.
