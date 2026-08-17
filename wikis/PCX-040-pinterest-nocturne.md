# Pinterest Nocturne Wiki

**Project Constellation ID:** `PCX-040`  
**Status:** ACTIVE / TRACKED  
**Current verified source line:** `1.9.0`  
**Durable publication repository:** [Herbertofury/UltraDeck](https://github.com/Herbertofury/UltraDeck)  
**Canonical Drive artifact folder:** `Pinterest Nocturne 1.9.0`, folder ID `1_-2KUx44nJ78wZsRF6po6xbxcK0-SoXP`

## Purpose

Pinterest Nocturne is a dependency-light Manifest V3 browser extension that gives Pinterest a polished dark interface while reducing evidence-backed page-owned JavaScript waste and accelerating feed/media readiness. Its performance work is constrained by a strict fidelity contract: it must not tint, dim, invert, blur, filter, virtualize, cull, hide, reduce organic feed quantity, or lower pin/media quality.

Lean Browsing is a separately controllable optimization layer. It removes only evidence-backed promoted, tracking, logging, and reporting work and is designed to be immediately reversible.

## Current verified version and provenance

The project-owned recovery repository identifies **Pinterest Nocturne v1.9.0** as the newest substantively distinct recovered source line. The exact recovered source is also present in connected Google Drive.

Current Drive artifacts:

| Artifact | Drive file ID | Size |
| --- | --- | ---: |
| `Pinterest-Nocturne-1.9.0-Source.zip` | `1q_UAzX12s436uZX6PTKEfI6HQZ8JPbOL` | 400,272 bytes |
| `Pinterest-Nocturne-1.9.0-Chromium.zip` | `1N3SPSqM4aCPvy3GqrhsChi-3-Xx37-Te` | 46,617 bytes |
| `Pinterest-Nocturne-1.9.0-Firefox.zip` | `10FmJzY5V5ix9e6iVrvqSlvFQ7mAr1aIo` | 46,667 bytes |
| `Pinterest-Nocturne-1.9.0-Release.zip` | `1qN4s_wFqQ6oTNhPtIwpI6t352Deajroc` | 479,931 bytes |

During the documentation pass the exact Drive source ZIP was downloaded and checked locally:

- SHA-256: `e2fa38831c8969fc4a8b1919f92a69e1e50dec607a5c6425ee2e3b5a6734a8d7`
- ZIP integrity: passed with no compressed-data errors
- `npm run build`: passed
- `npm run test:static`: passed
- `npm run package`: passed and produced fresh Chromium and Firefox ZIPs
- `npm run test:interaction`: attempted, but the browser/runtime benchmark did not complete before the execution timeout, so current-run interaction-latency success is not claimed here

## Source layout

The 1.9.0 source archive contains:

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

Pinterest Nocturne has four main runtime layers.

### 1. Main-world page engine

`src/content/page-engine.js` runs at `document_start` in the page's MAIN world. This is the lowest-level performance layer. It handles Pinterest page-engine behavior that cannot be controlled cleanly from an isolated extension world, including bounded observer/event/timer work, feed continuation acceleration, response-ahead media warming, promoted/tracking payload pruning, and interaction-priority scheduling.

Important architectural rules include:

- preserve native `IntersectionObserver` semantics and observer identity;
- use Pinterest's own continuation behavior as the discovery/growth source rather than inventing an unrelated feed loader;
- stop speculative work on constrained connections, hidden tabs, user input, or heap pressure;
- do not ship content culling/virtualization shortcuts;
- keep response/media warming bounded;
- require actual feed growth before repeatedly advancing a proven continuation sentinel;
- preserve currentTarget and other event semantics when coalescing deferred root events.

### 2. Isolated content/theme layer

`src/content/content.js` and `src/content/base.css` provide the dark-theme surface, feed/media readiness logic, promoted-card cleanup, settings application, and coordination with the page engine.

The isolated layer signals page-engine release barriers so speculative response-ahead work does not outrun the visible first-row experience.

### 3. Background/settings layer

`src/background/background.js` owns normalized persistent settings and the declarative network-rule state. It uses `chrome.storage.local` and enables/disables the `lean_network` ruleset according to the extension and Lean Browsing settings.

Default settings are:

```text
enabled: true
theme: nocturne
accent: #e60023
surfaceBrightness: 100
contrast: standard
performance: adaptive
leanBrowsing: true
```

Settings are normalized on install and browser startup. Invalid or stale values fall back to safe defaults.

### 4. Popup controls

The popup is a real configuration surface rather than a decorative status panel. It exposes:

- extension enabled/paused state;
- theme selection: Nocturne, OLED, or Graphite;
- preset accent swatches;
- custom accent color;
- surface brightness from 84% through 116%;
- standard/high contrast;
- performance profile: Adaptive, Maximum, or Off;
- Lean Browsing on/off;
- reset to defaults.

Changes persist through `chrome.storage.local`.

## Manifest and browser support

Pinterest Nocturne is Manifest V3.

Requested permissions are intentionally small:

- `storage`
- `declarativeNetRequest`

The Chromium build uses a service worker. The Firefox build transforms the background declaration to `background.scripts` and retains a Gecko extension ID.

The Firefox manifest requires Firefox **128+** for the extension's declarative-net-request condition support.

The content scripts cover the main Pinterest domains represented in the manifest, including the `.com`, `.fr`, `.de`, `.co.uk`, `.jp`, `.pt`, `.it`, `.es`, `.ca`, `.com.au`, `.at`, `.ch`, `.cl`, `.co.kr`, `.com.mx`, `.dk`, `.ie`, `.nz`, `.ph`, `.se`, `.nl`, `.be`, `.no`, `.fi`, `.pl`, `.cz`, `.hu`, `.ro`, `.com.br`, `.com.ar`, `.co.in`, `.co.za`, and `.com.tr` host families. Pinterest help domains are excluded for the listed major locales.

## Version 1.9.0: Interaction Priority

Version 1.9.0 is the **Interaction Priority** release.

Its central change is scheduling priority. Real user input, especially Pinterest click/React commit work, outranks speculative feed work, stale short interval ticks, semantic fallback scans, and response-ahead warm queues.

Large mutation commits are reduced to a small synchronous fast path, with remaining media/theme/Lean work deferred into bounded background slices.

Pin intent warming is also earlier:

- Adaptive begins low-priority full-resolution warming after 25 ms of stable hover.
- Maximum begins after 10 ms.
- Pointer-down upgrades the clicked pin to high priority.

The preserved verification document records the exact-package 1.9 fixture improving a 90 ms hover-to-click closeup from 243.1 ms on exact 1.8 to 148.5 ms on 1.9 without a duplicate full-resolution transfer.

The same verification record reports the 240-card interaction benchmark reducing median click-to-two-frame latency from 16.15 ms on exact 1.8 to 7.0 ms on 1.9, with p95 moving from 18.5 ms to 7.5 ms. These are controlled benchmark results, not universal real-site latency guarantees.

## Deep Horizon and feed readiness

The 1.7 line introduced Deep Horizon and response-ahead media warming. Those mechanisms remain part of 1.9.

The key rule is that Pinterest itself must prove a continuation sentinel can grow the feed. A sentinel is promoted into a bounded pipeline only after it has produced real grid-count or feed-height growth. Pinterest must re-observe/re-arm the same sentinel after the previous commit. No growth stops the pipeline.

Speculative continuation pauses or stops under conditions such as:

- Performance Off;
- Save-Data;
- 2G/slow-2G;
- constrained 3G;
- hidden tab;
- heap pressure;
- recent user input.

This is deliberately different from synthetic auto-scroll or arbitrary infinite prefetching.

## Media-gated idle runway

Version 1.8 added a deeper media-gated idle runway that is preserved by 1.9.

The important contract is that deeper speculative expansion occurs only after the previous response-ahead media queue has drained. The runway expands in bounded steps and collapses/back-offs under memory, connection, visibility, or input pressure.

The preserved controlled 24-post fixture records:

- Adaptive: 312/312 fully ready by 6 seconds;
- Maximum: 408/408 fully ready by 7.5 seconds;
- Performance Off and forced 2G: native 24/24 starting feed.

The 312/408 values are speculative ahead-of-scroll test runways, not limits on Pinterest's native infinite scrolling.

## Lean Browsing

Lean Browsing is an evidence-backed reversible layer rather than a blanket network blocker.

The static ruleset is `src/rules/lean.json`. The background worker toggles it through `declarativeNetRequest.updateEnabledRulesets()` only when both the extension and Lean Browsing are enabled.

The static verification requires coverage for known analytics/report patterns while preserving essential/organic requests. Historical runtime tests also verify that disabling or pausing Lean Browsing restores the previously blocked paths.

When adding a new Lean rule:

1. capture evidence that the endpoint/work is non-essential tracking/report/promoted work;
2. add the smallest matching rule;
3. add/update a deterministic fixture or runtime assertion;
4. verify organic pins/media and required application requests still work;
5. verify Lean Off immediately restores the path;
6. verify the setting remains correct after restart.

Do not convert Lean Browsing into a generic Pinterest request blocker.

## Performance profiles

### Adaptive

Adaptive is the default profile. It enables bounded performance improvements while using lower-priority warming and conservative speculation.

### Maximum

Maximum uses more aggressive bounded lookahead/warming while retaining the same fidelity, reversibility, connection-pressure, memory-pressure, and user-input guardrails.

### Off

Performance Off disables the speculative acceleration path and is used as an important native-baseline/reversibility lane. Dark-theme configuration remains a separate concern.

## Building from source

Prerequisites verified from the source/scripts:

- Node.js capable of running ESM scripts;
- Python 3 for icon generation and runtime tests;
- the system `zip` command for packaging;
- a compatible Chromium/Firefox environment for runtime tests.

The project is dependency-light and the package manifest declares no npm dependency installation step.

From the extracted source root:

```bash
npm run build
```

This:

1. runs `scripts/make_icons.py`;
2. clears/recreates `dist/`;
3. copies content/background/popup/icons/rules into each target;
4. writes a Chromium MV3 manifest using `background.service_worker`;
5. writes a Firefox MV3 manifest using `background.scripts`.

Freshly verified output directories:

```text
dist/chromium/
dist/firefox/
```

## Packaging

Run:

```bash
npm run package
```

This rebuilds both browser targets and writes:

```text
artifacts/pinterest-nocturne-1.9.0-chromium.zip
artifacts/pinterest-nocturne-1.9.0-firefox.zip
artifacts/Pinterest-Nocturne-extension.zip
```

The compatibility `Pinterest-Nocturne-extension.zip` copy is the Chromium package.

## Testing

### Static gate

```bash
npm run build
npm run test:static
```

The static gate checks manifest identity/version/permissions, browser-target transforms, popup wiring, theme and Lean behavior, feed-turbo and Deep Horizon implementation markers, constrained-network guardrails, rejected-shortcut absence, JavaScript syntax, Firefox requirements, and other release invariants.

### Full declared suite

```bash
npm test
```

The package's full test command chains static verification with the primary runtime, performance, site-acceleration, feed, Lean, engine-tamer, and Deep Horizon suites.

Individual lanes are available:

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

Do not claim a runtime lane passed unless the exact package/environment completed it. In the current documentation pass, build/static/package succeeded, while `test:interaction` exceeded the execution window and therefore remains unverified in this environment.

## Installing the Chromium build

Use a verified Chromium build ZIP or build locally first.

1. Extract `Pinterest-Nocturne-1.9.0-Chromium.zip` or `artifacts/pinterest-nocturne-1.9.0-chromium.zip` to a stable directory.
2. Open the Chromium-family browser's extension-management page.
3. Enable developer mode.
4. Choose **Load unpacked**.
5. Select the extracted directory containing `manifest.json`.
6. Open Pinterest and confirm the popup shows Nocturne as active.
7. Test theme controls, performance mode, Lean Browsing, feed scrolling, pin closeups, and restart persistence.

Do not load the source root directly. Load the built Chromium target/package content containing the transformed manifest.

## Installing the Firefox build

Use the verified Firefox ZIP or build locally first. The current manifest requires Firefox 128+.

For development/testing, use Firefox's temporary add-on loading workflow with the built Firefox manifest/package. For a persistent signed distribution, use the project's normal Firefox packaging/signing path when available. The source package itself does not contain evidence of a completed store-signing workflow, so do not claim one here.

## Configuration and daily use

Open the extension popup and choose the desired theme, accent, brightness, contrast, performance profile, and Lean Browsing state.

Recommended troubleshooting baseline:

1. leave the theme enabled;
2. set Performance to **Off**;
3. disable **Lean Browsing**;
4. reproduce the problem;
5. enable Adaptive performance only;
6. then enable Lean Browsing;
7. finally compare Maximum if the problem is performance-profile specific.

This sequence helps separate theme/CSS issues from page-engine acceleration and network-rule behavior.

## Modification map

### Change visual styling

Edit `src/content/base.css` and the isolated theme application logic in `src/content/content.js`. Preserve pin/media fidelity and avoid whole-page filters that alter media quality.

### Change page-engine performance behavior

Edit `src/content/page-engine.js`. This is high-risk because it runs in Pinterest's MAIN world at `document_start`. Preserve native observer/event semantics, reversibility, bounded work, and input priority. Add or update runtime evidence for any scheduling/observer/timer change.

### Change popup/settings

Edit:

- `src/popup/popup.html`
- `src/popup/popup.css`
- `src/popup/popup.js`
- `src/background/background.js` for defaults/normalization

Any new setting must have a real runtime consumer, persistence, migration/default behavior, reset behavior, and restart verification.

### Change Lean Browsing

Edit `src/rules/lean.json` and, when necessary, the page-engine/content pruning logic. Require evidence and reversibility for each new rule.

### Change browser packaging

Edit `scripts/build.mjs`, `scripts/package.mjs`, and `src/manifest.json`. Keep Chromium/Firefox target transforms explicit and verify both outputs.

### Change performance gates

Update the corresponding runtime fixture/script under `tests/runtime/` and preserve raw evidence. Do not weaken a gate merely to make a new implementation pass.

## Important correctness rules

- Organic feed quantity must remain intact.
- Pin/media quality must remain full fidelity.
- No viewport virtualization or content culling as a performance shortcut.
- No blanket `content-visibility`/containment shortcut for feed correctness.
- No duplicate-feed request coalescing without proven Pinterest semantic safety.
- No unbounded lookahead pipeline.
- No speculative work that ignores Save-Data, slow connections, heap pressure, hidden-tab state, or recent user input.
- Lean Browsing must remain reversible.
- Performance Off must remain a trustworthy baseline.
- Native observer/event semantics must be preserved.
- Controlled benchmark improvements must not be presented as universal real-site guarantees.

## Troubleshooting

### Theme loads but Pinterest interaction feels delayed

Switch Performance to Off. If the delay disappears, inspect page-engine scheduling, mutation fast paths, root event handling, and intent warming before changing CSS.

### Feed stops expanding or expansion is too conservative

Check connection type, Save-Data, tab visibility, heap pressure, recent input, and whether the continuation sentinel actually produced/reported growth. The pipeline is intentionally self-stopping when Pinterest does not prove growth.

### Images appear as shells but are not ready

Inspect response-ahead warm queue drainage and media-gated runway behavior. Do not increase card budgets merely to inflate shell counts; the saturation rule is based on fully ready media.

### Promoted/tracking work still appears with Lean Browsing on

Verify the static ruleset is enabled through the background worker, then inspect whether the request/payload matches an evidence-backed Lean path. Add new matching only after confirming it is non-essential.

### Organic media or application behavior breaks with Lean Browsing

Disable Lean Browsing immediately and treat the rule/pruning change as a regression. Narrow or remove the offending rule and add a fixture covering the essential path.

### Firefox build behaves differently

Check the transformed Firefox manifest first. Firefox uses `background.scripts`, carries the Gecko ID, and requires Firefox 128+ in this source line.

### Runtime benchmark hangs or exceeds the environment limit

Do not convert that into a pass/fail claim for the extension. Preserve the exact static/package evidence that did complete and rerun the runtime lane in a browser-capable environment with its expected fixture dependencies.

## Historical lineage

The source archive preserves detailed verification history for 1.5 through 1.9. Important evolution points include:

- 1.5: stronger page-engine/Lean work reduction and promoted/tracking pruning;
- 1.6: Feed Horizon and deeper saturation-tested post readiness;
- 1.7: Deep Horizon and response-ahead media warming;
- 1.8: media-gated idle runway expansion and rejected GPU/decode cargo-cult experiments;
- 1.9: Interaction Priority and faster pin-intent warming.

Preserve the historical benchmark/evidence record. Newer results should supersede individual claims only when they use an equally or more representative fixture and retain raw evidence.

## Current documentation boundary

The exact 1.9.0 source and built artifacts are durably present in Drive and the source can be built, statically verified, and packaged from a fresh extraction. Full current-run interactive browser verification was not completed in this wiki pass because the interaction benchmark exceeded the execution window. Existing `VERIFICATION.md` remains the project-owned runtime evidence record for the release.

## Wiki maintenance

Update this page when the canonical source version, Drive artifact identity, manifest permissions/domains, settings, performance profiles, Lean rules, Deep Horizon/runway behavior, build/package commands, browser support, test gates, or project-owned runtime evidence changes. Prefer source-owned evidence over the older generic Project Constellation summary.