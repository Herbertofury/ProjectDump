# Pinterest Nocturne Wiki

**Project Constellation ID:** `PCX-040`
**Status:** ACTIVE / TRACKED
**Current verified source line:** `2.0.0`
**Canonical project repository:** [Herbertofury/Pinterest-Nocturne](https://github.com/Herbertofury/Pinterest-Nocturne)
**Canonical Drive artifact folder:** `Pinterest Nocturne 2.0.0`, folder ID `1WQ2cHAGxDxqJMTXPW00bLbMksIHiwRvw`
**Historical lineage:** [Herbertofury/UltraDeck](https://github.com/Herbertofury/UltraDeck) remains useful recovery-era evidence, but it is not the current project repository.

## Purpose

Pinterest Nocturne is a dependency-light Manifest V3 browser extension that gives Pinterest a polished dark interface while reducing evidence-backed page-owned JavaScript waste and accelerating full-quality feed/media readiness. Its performance work is constrained by a strict fidelity contract: it must not tint, dim, invert, blur, filter, virtualize, cull, hide, reduce organic feed quantity, or lower pin/media quality.

Lean Browsing is a separately controllable optimization layer. It removes only evidence-backed promoted, tracking, logging, and reporting work and is designed to be immediately reversible.

Version 2.0.0 adds a persistent sidebar control surface with separate Chromium and Opera GX manifest wiring, and repairs a promoted-card false-positive in which an ordinary Pinterest card could be treated as promoted merely because a link contained the `epik` query parameter.

## Current verified version and provenance

The current verified source line is **Pinterest Nocturne 2.0.0**. The exact 2.0.0 source archive is durably present in Google Drive and was re-downloaded during this documentation pass.

Source archive SHA-256:

`e5a592b20be11b48459754999db96e3d2949a882b13362fa9f47be89f14ee5fa`

That digest matches the project-owned `SHA256SUMS-2.0.0.txt` record. ZIP integrity passed.

Current Drive artifacts independently re-downloaded and verified during this pass:

| Artifact | Drive file ID | Size | SHA-256 |
| --- | --- | ---: | --- |
| `Pinterest-Nocturne-2.0.0-Source.zip` | `1v0hZ76qcfzGvn1aoq5MgeJyDiWrWvL5b` | 410,707 bytes | `e5a592b20be11b48459754999db96e3d2949a882b13362fa9f47be89f14ee5fa` |
| `Pinterest-Nocturne-2.0.0-Chromium.zip` | `1fjyHiWu0JntY7x1a0Huz3pfPXdqYc2r0` | 50,982 bytes | `680a05a40344dc6808ef46da7ad96c001081a7ee98a6bb7eb3a91764f7ab82c7` |
| `Pinterest-Nocturne-2.0.0-Opera-GX.zip` | `1ktsPkj02rPTWb0H5SQ2GybMO_m2Lda3z` | 50,975 bytes | `07555faaeab2a96523b9440313306d870539a27707e9c4331f2dd841fc9d9162` |
| `Pinterest-Nocturne-2.0.0-Firefox.zip` | `1r4AuQ0M_eAhqc84klwEVIuG3upb_t6z0` | 51,003 bytes | `9779dae05cb2564388872e1c34919f0660e3da5976bd609592341c97dd0267d3` |
| `Pinterest-Nocturne-2.0.0-Release.zip` | `1vLm6ZdmR_8-NZtPz_icHPjNXR9jaGVHh` | 581,193 bytes | `5bb685b30f15dab885aa6516480ff105bf1988c2f623f090c77bc0f512623f47` |

All five downloaded ZIPs passed archive-integrity checks.

## Canonical GitHub repository and publication state

The canonical repository is `Herbertofury/Pinterest-Nocturne` on `main`.

The latest verified bootstrap commit in the publication chain is:

`6167038fac5f362dbabb83c2497edb64e588ad01` - `Bootstrap full Pinterest Nocturne 2.0.0 publish`

The repository currently contains staged source payloads plus `.github/workflows/publish-v2.yml`. That workflow is designed to:

1. reconstruct the full source from `.release-bootstrap/source.tar.xz.part.*.b64`;
2. commit/push the expanded full source tree;
3. run `npm run build`;
4. run `npm run test:static`;
5. run `npm run package`;
6. assemble Chromium, Opera GX, Firefox, source, checksum, notes, and release-bundle assets;
7. publish or update GitHub release `v2.0.0`.

The current continuity record reports that private GitHub Actions hosted execution is blocked before the runner starts by an account-level payment/spending-limit condition. Until that external runner blocker clears, the repository root can remain in staged bootstrap form even though the exact 2.0.0 source and built artifacts are verified in Drive.

This blocker is separate from the ProjectDump GitHub Wiki publication path.

## Current-run verification

The exact Drive `Pinterest-Nocturne-2.0.0-Source.zip` was extracted into a clean working directory and exercised during this documentation pass.

Completed successfully:

- `npm run build`
- `npm run test:static`
- `npm run package`
- `python3 tests/runtime/lean_browsing.py`
- the initial `npm test` lanes for static verification, runtime extension behavior, performance fixture, and site-acceleration fixture before the overall chained command exceeded the execution window

The focused Lean Browsing runtime gate passed. With Lean on, the strong sponsored fixture was removed, the ordinary `epik`-only card remained present and visible, its media loaded, tracked/reporting endpoints stayed suppressed, and pausing/disabling Nocturne restored the tested paths. Restart persistence for the disabled Lean setting also passed in that focused run.

The complete chained `npm test` command did not finish before the execution window expired, so this page does not claim a complete current-run 2.0.0 full-suite pass. The `VERIFICATION.md` currently stored with the 2.0 source begins with the preserved 1.9 acceptance record and is therefore historical baseline evidence rather than a complete 2.0 release certification.

## Source layout

The verified 2.0.0 source archive contains:

```text
AGENTS.md
README.md
VERIFICATION.md
package.json
research/
 RESEARCH.md
scripts/
 build.mjs
 make_icons.py
 package.mjs
 static-test.mjs
src/
 manifest.json
 background/
 background.js
 content/
 base.css
 content.js
 page-engine.js
 icons/
 popup/
 popup.html
 popup.css
 popup.js
 rules/
 lean.json
 sidebar/
 sidebar.html
 sidebar.css
 sidebar.js
tests/
 fixtures/
 pinterest-current.html
 runtime/
 deep_horizon.py
 engine_tamer.py
 feed_horizon.py
 feed_turbo.py
 interaction_latency.py
 lean_browsing.py
 lean_perf.py
 perf_extension.py
 prepare_browser.py
 quick_intent.py
 render_pipeline.py
 site_acceleration.py
 test_extension.py
```

Generated output is written under `dist/` and `artifacts/`.

## Architecture

Pinterest Nocturne has five main runtime/product layers in 2.0.0.

### 1. Main-world page engine

`src/content/page-engine.js` runs at `document_start` in Pinterest's MAIN world. It handles bounded observer/event/timer work, feed continuation acceleration, response-ahead media warming, promoted/tracking payload pruning, and interaction-priority scheduling.

Important rules:

- preserve native `IntersectionObserver` semantics and observer identity;
- use Pinterest's own continuation behavior as the discovery/growth source rather than inventing an unrelated feed loader;
- stop speculative work on constrained connections, hidden tabs, user input, or heap pressure;
- do not ship content culling or virtualization shortcuts;
- keep response/media warming bounded;
- require actual feed growth before repeatedly advancing a proven continuation sentinel;
- preserve event semantics such as `currentTarget` when coalescing deferred root events.

### 2. Isolated content/theme layer

`src/content/content.js` and `src/content/base.css` provide the dark-theme surface, feed/media readiness logic, promoted-card cleanup, settings application, and coordination with the page engine.

Version 2.0.0 narrows promoted-card detection. The verified source defines `epik` only as a weak hint. A card needs stronger Pinterest promotion evidence before suppression. Static tests explicitly reject CSS or JavaScript rules in which `epik` alone is sufficient promotion evidence.

### 3. Background/settings layer

`src/background/background.js` owns normalized persistent settings and the declarative network-rule state. It uses `chrome.storage.local` and enables/disables the `lean_network` ruleset according to the extension and Lean Browsing settings.

Default settings:

```text
enabled: true
theme: nocturne
accent: #e60023
surfaceBrightness: 100
contrast: standard
performance: adaptive
leanBrowsing: true
```

Settings are normalized on install/startup. Invalid or stale values fall back to safe defaults.

### 4. Popup controls

The popup remains the compact extension configuration surface. It exposes extension enabled/paused state, theme, accent, brightness, contrast, performance profile, Lean Browsing, and reset behavior.

### 5. Sidebar control deck

Version 2.0.0 adds `src/sidebar/sidebar.html`, `sidebar.css`, and `sidebar.js`. The sidebar uses the same `chrome.storage.local` `settings` object as the popup and background layer.

The verified sidebar implementation exposes:

- enable/pause Nocturne;
- theme selection: Nocturne, OLED, or Graphite;
- performance selection: Adaptive, Maximum, or Off;
- Lean Browsing toggle;
- surface brightness from 84% through 116%;
- standard versus higher contrast;
- safe-default restore.

The sidebar listens to `chrome.storage.onChanged`, so changes made from another extension surface are reflected without a separate settings store.

The project README describes the release motivation more broadly as an Opera GX sidebar/blank-feed repair. The extracted 2.0.0 source confirms target-specific sidebar manifest wiring and the promoted-card filter repair. It does not currently contain a separate `ResizeObserver`-driven diagnostic/targeted-repair subsystem in the sidebar/content source inspected during this pass. Treat broader release prose as intent unless a later source revision adds and verifies that runtime path.

## Manifest and browser targets

Pinterest Nocturne remains Manifest V3 and now builds three explicit targets from the canonical `src/manifest.json`.

### Chromium

`dist/chromium/manifest.json` uses:

- `background.service_worker: background/background.js`
- permissions `storage`, `declarativeNetRequest`, and `sidePanel`
- `side_panel.default_path: sidebar/sidebar.html`

### Opera GX

`dist/opera/manifest.json` uses:

- `background.service_worker: background/background.js`
- permissions `storage` and `declarativeNetRequest`
- `sidebar_action.default_panel: sidebar/sidebar.html`
- target-specific sidebar title/icon metadata

### Firefox

`dist/firefox/manifest.json` uses:

- `background.scripts: [background/background.js]`
- permissions `storage` and `declarativeNetRequest`
- Gecko ID `pinterest-nocturne@local.dev`
- minimum Firefox version `128.0`

The content scripts cover the Pinterest host families listed in `src/manifest.json`, including the principal `.com`, `.fr`, `.de`, `.co.uk`, `.jp`, `.pt`, `.it`, `.es`, `.ca`, `.com.au`, `.at`, `.ch`, `.cl`, `.co.kr`, `.com.mx`, `.dk`, `.ie`, `.nz`, `.ph`, `.se`, `.nl`, `.be`, `.no`, `.fi`, `.pl`, `.cz`, `.hu`, `.ro`, `.com.br`, `.com.ar`, `.co.in`, `.co.za`, and `.com.tr` domains. Major Pinterest help domains are excluded.

## Version 2.0.0: Opera GX sidebar and feed-safety repair

Version 2.0.0 has two source-verified product changes.

First, it adds a persistent control deck that is packaged as a Chromium MV3 side panel and an Opera GX `sidebar_action` panel. A dedicated Opera target avoids forcing one ambiguous manifest shape onto every browser.

Second, it repairs the promoted-pin filter so `epik` is a weak suspicion hint only. An ordinary card that merely contains `&epik=` must remain visible and its media must load. Strong Pinterest promoted-card markers can still trigger Lean Browsing suppression.

The static gate enforces both behaviors:

- Chromium must include `sidePanel` and point `side_panel.default_path` to the sidebar;
- Opera must point `sidebar_action.default_panel` to the sidebar;
- `epik` must not appear as sufficient evidence in the strong promoted marker selector;
- CSS must not hide feed cards merely through an `epik` link match.

The focused runtime Lean test additionally verifies positive suppression of the strong promoted fixture, survival of the `epik`-only fixture, media delivery for the `epik`-only fixture, reversibility on Pause/Off, network rule disablement, and restart persistence.

## Version 1.9.0: Interaction Priority

Version 1.9.0 remains the major interaction-priority baseline inherited by 2.0.0.

Real user input, especially Pinterest click/React commit work, outranks speculative feed work, stale short interval ticks, semantic fallback scans, and response-ahead warm queues. Large mutation commits use a small synchronous fast path, with remaining media/theme/Lean work deferred into bounded background slices.

Pin intent warming is earlier:

- Adaptive begins low-priority full-resolution warming after 25 ms of stable hover.
- Maximum begins after 10 ms.
- Pointer-down upgrades the clicked pin to high priority.

The preserved 1.9 verification record reports a 90 ms hover-to-click closeup improving from 243.1 ms on exact 1.8 to 148.5 ms on 1.9 without a duplicate full-resolution transfer. It also records the 240-card interaction benchmark reducing median click-to-two-frame latency from 16.15 ms to 7.0 ms, with p95 moving from 18.5 ms to 7.5 ms. These are controlled benchmark results, not universal real-site guarantees.

## Deep Horizon and feed readiness

The 1.7 line introduced Deep Horizon and response-ahead media warming. Those mechanisms remain part of the 2.0 source lineage.

Pinterest itself must prove that a continuation sentinel can grow the feed. A sentinel is promoted into a bounded pipeline only after it has produced real grid-count or feed-height growth. Pinterest must re-observe/re-arm the same sentinel after the previous commit. No growth stops the pipeline.

Speculative continuation pauses or stops under conditions such as Performance Off, Save-Data, 2G/slow-2G, constrained 3G, hidden-tab state, heap pressure, or recent user input. This is deliberately different from synthetic auto-scroll or arbitrary infinite prefetching.

## Media-gated idle runway

Version 1.8 added deeper media-gated idle expansion, preserved by later source lines. Deeper speculative expansion occurs only after the previous response-ahead media queue has drained. The runway expands in bounded steps and collapses/back-offs under memory, connection, visibility, or input pressure.

The preserved controlled 24-post 1.8/1.9 evidence records:

- Adaptive: 312/312 fully ready;
- Maximum: 408/408 fully ready;
- Performance Off and forced 2G: native 24/24 starting feed.

The 312/408 values are speculative ahead-of-scroll test runways, not limits on Pinterest's native infinite scrolling.

## Lean Browsing

Lean Browsing is an evidence-backed reversible layer rather than a blanket network blocker.

The static ruleset is `src/rules/lean.json`. The background worker toggles it through `declarativeNetRequest.updateEnabledRulesets()` only when both the extension and Lean Browsing are enabled.

When adding or changing a Lean rule:

1. capture evidence that the endpoint/work is non-essential tracking/report/promoted work;
2. add the smallest matching rule;
3. add or update a deterministic fixture/runtime assertion;
4. verify organic pins/media and required application requests still work;
5. verify Lean Off immediately restores the path;
6. verify restart persistence;
7. for DOM promotion detection, distinguish strong promotion evidence from weak hints such as `epik`.

Do not convert Lean Browsing into a generic Pinterest request blocker.

## Performance profiles

### Adaptive

Adaptive is the default profile. It enables bounded performance improvements while using lower-priority warming and conservative speculation.

### Maximum

Maximum uses more aggressive bounded lookahead/warming while retaining the same fidelity, reversibility, connection-pressure, memory-pressure, and user-input guardrails.

### Off

Performance Off disables the speculative acceleration path and is an important native-baseline/reversibility lane. Dark-theme configuration remains separate.

## Building from source

Prerequisites verified from the source/scripts:

- Node.js capable of running ESM scripts. The project GitHub publish workflow explicitly provisions Node 22.
- Python 3 for icon generation and runtime tests.
- the system `zip` command for packaging.
- a compatible Chromium environment for Chromium runtime fixtures.
- a compatible Firefox environment when exercising Firefox-specific runtime behavior.

The package manifest declares no npm dependency installation step.

From the extracted source root:

```bash
npm run build
```

`build.mjs`:

1. runs `scripts/make_icons.py`;
2. clears/recreates `dist/`;
3. copies content, background, popup, sidebar, icons, and rules into each target;
4. creates the Chromium target with service worker plus `sidePanel` permission and `side_panel` path;
5. creates the Opera target with service worker plus `sidebar_action` path;
6. creates the Firefox target with `background.scripts` and preserved Gecko metadata.

Verified output directories:

```text
dist/chromium/
dist/opera/
dist/firefox/
```

## Packaging

Run:

```bash
npm run package
```

The verified package script rebuilds all targets and writes:

```text
artifacts/pinterest-nocturne-2.0.0-chromium.zip
artifacts/pinterest-nocturne-2.0.0-opera.zip
artifacts/pinterest-nocturne-2.0.0-firefox.zip
artifacts/Pinterest-Nocturne-extension.zip
```

`Pinterest-Nocturne-extension.zip` is the Chromium compatibility copy.

The GitHub publication workflow then renames/copies target archives into release-facing names such as `Pinterest-Nocturne-2.0.0-Chromium.zip`, `Pinterest-Nocturne-2.0.0-Opera-GX.zip`, and `Pinterest-Nocturne-2.0.0-Firefox.zip`, creates a source ZIP, writes release SHA-256 sums, and assembles the release bundle.

## Testing

### Static gate

```bash
npm run build
npm run test:static
```

The 2.0 static gate verifies release version/identity, browser-target manifest transforms, sidebar wiring, popup/settings behavior, theme and Lean behavior, Feed/Deep Horizon implementation markers, connection guardrails, JavaScript syntax, Firefox requirements, rejected performance shortcuts, and the `epik` false-positive regression.

### Declared full suite

```bash
npm test
```

The package's declared full command chains:

```text
static-test.mjs
test_extension.py
perf_extension.py
site_acceleration.py
feed_turbo.py
lean_browsing.py
lean_perf.py
engine_tamer.py
deep_horizon.py
```

Additional individual lanes:

```bash
npm run test:runtime
npm run test:perf
npm run test:site
npm run test:feed
npm run test:lean
npm run test:leanperf
npm run test:engine
npm run test:horizon
npm run test:render
npm run test:interaction
npm run test:intent
```

Do not claim a lane passed unless the exact package/environment completed it.

## Installing the Chromium build

1. Extract the verified `Pinterest-Nocturne-2.0.0-Chromium.zip` or build `dist/chromium/` locally.
2. Open the Chromium-family browser extension-management page.
3. Enable developer mode.
4. Choose **Load unpacked**.
5. Select the extracted directory containing the transformed Chromium `manifest.json`.
6. Open Pinterest and confirm Nocturne is active.
7. Verify popup controls and, on a browser exposing MV3 side panels, the sidebar control deck.
8. Test theme, performance mode, Lean Browsing, feed scrolling, pin closeups, and restart persistence.

Do not load the canonical `src/manifest.json` directly when testing target-specific behavior. Use the built target manifest.

## Installing the Opera GX build

1. Extract `Pinterest-Nocturne-2.0.0-Opera-GX.zip` or build `dist/opera/` locally.
2. Use Opera GX's extension-development loading flow to load the extracted target containing `manifest.json`.
3. Confirm the target manifest exposes `sidebar_action` with `sidebar/sidebar.html` as the default panel.
4. Open the sidebar and exercise enable/pause, theme, performance, Lean Browsing, brightness, contrast, and safe-default restore.
5. Open Pinterest and verify an ordinary `epik`-only card is not suppressed solely because of that parameter.

The verified source does not currently justify claiming a separate resize-diagnostic or targeted feed-repair command beyond the sidebar/settings surface and safe filtering behavior.

## Installing the Firefox build

Use the verified Firefox ZIP or build `dist/firefox/`. The current manifest requires Firefox 128+.

For development/testing, use Firefox's temporary add-on loading workflow with the built Firefox manifest/package. The source package does not itself prove a completed store-signing workflow, so do not describe one as current behavior without later evidence.

## Configuration and daily use

Popup and sidebar controls share the same normalized settings object. A practical troubleshooting baseline is:

1. leave the theme enabled;
2. set Performance to **Off**;
3. disable **Lean Browsing**;
4. reproduce the problem;
5. enable Adaptive performance only;
6. then enable Lean Browsing;
7. finally compare Maximum if the problem is performance-profile specific.

This sequence separates theme/CSS issues from page-engine acceleration and network/filter behavior.

## Modification map

### Change visual styling

Edit `src/content/base.css` and the isolated theme application logic in `src/content/content.js`. Preserve pin/media fidelity and avoid whole-page filters that alter media quality.

### Change page-engine performance behavior

Edit `src/content/page-engine.js`. This runs in Pinterest's MAIN world at `document_start`, so preserve native observer/event semantics, reversibility, bounded work, and input priority. Add/update runtime evidence for scheduling, observer, timer, feed-continuation, or response-warming changes.

### Change popup/settings

Edit:

- `src/popup/popup.html`
- `src/popup/popup.css`
- `src/popup/popup.js`
- `src/background/background.js`

Any new setting must have a real runtime consumer, persistence, migration/default behavior, reset behavior, and restart verification.

### Change sidebar/settings

Edit:

- `src/sidebar/sidebar.html`
- `src/sidebar/sidebar.css`
- `src/sidebar/sidebar.js`
- `scripts/build.mjs` if manifest integration changes

The sidebar and popup must remain synchronized through `chrome.storage.local`. Avoid duplicating settings state or adding controls that have no real runtime consumer.

### Change promoted-card detection

The 2.0 regression rule is explicit: weak hints such as `epik` are insufficient by themselves. Changes to promoted-marker selectors, Lean CSS, or DOM pruning must preserve the strong-marker/weak-hint distinction and update both static and runtime regression tests.

### Change Lean Browsing

Edit `src/rules/lean.json` and, when necessary, page-engine/content pruning logic. Require evidence and reversibility for each new rule.

### Change browser packaging

Edit `scripts/build.mjs`, `scripts/package.mjs`, and `src/manifest.json`. Keep Chromium, Opera GX, and Firefox target transforms explicit and verify all three outputs.

### Change performance gates

Update the corresponding fixture/script under `tests/runtime/` and preserve raw evidence. Do not weaken a gate merely to make a new implementation pass.

## Important correctness rules

- Organic feed quantity must remain intact.
- Pin/media quality must remain full fidelity.
- No viewport virtualization or content culling as a performance shortcut.
- No blanket `content-visibility`/containment shortcut for feed correctness.
- No duplicate-feed request coalescing without proven Pinterest semantic safety.
- No unbounded lookahead pipeline.
- No speculative work that ignores Save-Data, slow connections, heap pressure, hidden-tab state, or recent user input.
- Lean Browsing must remain reversible.
- `epik` alone must never be sufficient promotion evidence.
- Performance Off must remain a trustworthy baseline.
- Native observer/event semantics must be preserved.
- Sidebar controls must be wired to the same persisted settings behavior they advertise.
- Controlled benchmark improvements must not be presented as universal real-site guarantees.

## Troubleshooting

### Theme loads but Pinterest interaction feels delayed

Switch Performance to Off. If the delay disappears, inspect page-engine scheduling, mutation fast paths, root event handling, and intent warming before changing CSS.

### Feed stops expanding or expansion is too conservative

Check connection type, Save-Data, tab visibility, heap pressure, recent input, and whether the continuation sentinel actually produced/reported growth. The pipeline is intentionally self-stopping when Pinterest does not prove growth.

### Images appear as shells but are not ready

Inspect response-ahead warm queue drainage and media-gated runway behavior. Do not increase card budgets merely to inflate shell counts. Saturation is based on fully ready media.

### An ordinary card containing `epik` disappears

Treat this as a 2.0 regression. Verify that `epik` appears only in the weak hint path, that the strong promoted marker selector still requires stronger Pinterest promotion evidence, and that the Lean regression fixture keeps the `epik`-only card visible with its media loaded.

### Strong promoted/tracking work still appears with Lean Browsing on

Verify the static ruleset is enabled through the background worker, then inspect whether the request/payload matches an evidence-backed Lean path. Add new matching only after confirming it is non-essential.

### Organic media or application behavior breaks with Lean Browsing

Disable Lean Browsing and treat the rule/pruning change as a regression. Narrow/remove the offending rule and add a fixture covering the essential path.

### Sidebar is missing in Chromium

Verify that the loaded build is `dist/chromium/` or the Chromium package, not the canonical source manifest. The built Chromium manifest must include `sidePanel` and `side_panel.default_path`.

### Sidebar is missing in Opera GX

Verify that the dedicated Opera build is loaded. The built Opera manifest must contain `sidebar_action.default_panel: sidebar/sidebar.html`. Do not substitute the Chromium package when validating Opera-specific sidebar wiring.

### Sidebar setting does not match the popup

Inspect `chrome.storage.local.settings` and the `chrome.storage.onChanged` listener in `src/sidebar/sidebar.js`. Both surfaces are expected to share the same normalized settings record.

### Firefox build behaves differently

Check the transformed Firefox manifest first. Firefox uses `background.scripts`, carries the Gecko ID, and requires Firefox 128+ in this source line.

### Project GitHub repository still shows bootstrap files

Check the `Publish Pinterest Nocturne 2.0.0` Actions workflow. The current continuity record indicates hosted execution is blocked before the job starts by an account-level private Actions payment/spending-limit condition. The workflow is expected to expand `.release-bootstrap`, commit the full source, run build/static/package, and publish the `v2.0.0` release once hosted execution is available. Do not confuse the bootstrap repository state with absence of the verified Drive source archive.

### Runtime benchmark hangs or exceeds the environment limit

Preserve the exact static/package/runtime evidence that completed and rerun the unfinished lane in a browser-capable environment. Do not convert a timeout into a pass.

## Historical lineage

The source archive preserves detailed verification history for 1.5 through 1.9, and 2.0 extends that line without discarding prior performance work.

- 1.5: stronger page-engine/Lean work reduction and promoted/tracking pruning.
- 1.6: Feed Horizon and deeper saturation-tested post readiness.
- 1.7: Deep Horizon and response-ahead media warming.
- 1.8: media-gated idle runway expansion and rejected GPU/decode experiments.
- 1.9: Interaction Priority and faster pin-intent warming.
- 2.0: browser-specific sidebar targets plus the `epik` promoted-card false-positive repair.

Preserve historical benchmark/evidence records. Newer results should supersede individual claims only when they use an equally or more representative fixture and retain raw evidence.

## Current documentation boundary

Verified now:

- exact 2.0.0 source archive identity, hash, and integrity;
- exact Drive Chromium, Opera GX, Firefox, and Release archive identities, hashes, sizes, and integrity;
- 2.0 source layout including the sidebar surface;
- three target build transforms;
- local 2.0 build, static, and package success from a clean extraction;
- focused 2.0 Lean Browsing runtime regression success, including `epik`-only organic-card survival;
- initial full-suite runtime/performance/site lanes completed before the aggregate test command exceeded the execution window.

Not yet claimed as complete:

- a full current-run 2.0 chained runtime suite;
- successful private GitHub Actions expansion of the staged project repository;
- a completed `v2.0.0` GitHub release from that private repository workflow.

These boundaries are intentional. Source/runtime evidence takes precedence over older catalog summaries or broader release prose when they disagree.

## Wiki maintenance

Update this page when the canonical source version, project repository state, Drive artifact identity, browser target manifests, sidebar behavior, settings, performance profiles, Lean rules, Deep Horizon/runway behavior, build/package commands, browser support, test gates, publication workflow status, or project-owned runtime evidence changes. Prefer current project-owned source/runtime evidence over older Project Constellation summaries.
