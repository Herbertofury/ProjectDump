# Feature Foundry Living Ecology Wiki

**Project Constellation ID:** `PCX-044`  
**Status:** ACTIVE / TRACKED  
**Strongest verified ecology artifact:** `Feature Foundry V33 - Recovered Ecology`  
**Verified build ID:** `V33-RECOVERED-ECOLOGY-OUTSIDE-BOX`  
**Verified artifact SHA-256:** `83aac630afa4e6522d28452bb6a7c0ebe183eee6812b89b6d742662876af06ec`  
**Verified release ZIP SHA-256:** `680978a3aa8f16b47e767720ebfdc3b89fda5c148c5f3d4d3f308390b09385d9`  
**Canonical V33 Drive HTML:** file ID `1QL4u4MTrpATCVQxFrt4scEq32ky8hqvk`  
**Canonical V33 Drive ZIP:** file ID `1_mLbBXiS0yL7g2cKP7qQJxqyyRHP4RSY`

## Purpose

Living Ecology is the Feature Foundry subsystem for worlds that behave like coherent, inspectable systems rather than decorative backgrounds. It owns theme-native interaction language, world signals, memory-derived presentation, transition depth, presentation tiers, host adaptation, soundtrack handoff, optical/spatial treatment, reduced-motion equivalence, and the rules that keep all authored content available while presentation cost changes.

The core contract is:

`user/system input -> world signal -> bounded reaction -> persisted or replayable evidence`

The subsystem is not allowed to make performance appear better by removing authored entities, hiding off-screen content, reducing collection quantity, silently changing factual state, or substituting decorative animation for a real state transition.

## Source authority and recovery lineage

The current verified ecology implementation is V33. Its durable checkpoint records this lineage:

```text
V25 verified runnable base
+ V30/V31 verified capability contracts
+ V32 themed library/ecology specification
-> V33 recovered and forward-evolved artifact
```

The V32 marker survived without recoverable project bytes. V33 therefore preserves the exact verified V25 runtime and source baseline, then injects a separate dependency-free ecology/evolution host adapter rather than pretending the missing V31/V32 package still exists.

The V33 build script refuses to proceed if the preserved baseline changes. Verified baseline identities are:

| Preserved baseline | SHA-256 |
| --- | --- |
| `Feature-Foundry-V25.html` | `dde6257193e3da6b2b2a914df766cb948759738c7b6b96388474bde044b36e94` |
| `apps/feature-foundry/src/App.tsx` | `ab2158f53ab24866d4a8041e538176f93d3009422d0ca08552b92ac382e5b048` |
| `apps/feature-foundry/src/styles.css` | `3ac03b0cb2204999a207a738d8d1f2bf29f76806890ff04ed66d9f1b13dc6c5b` |

This preservation boundary matters. Changes to the V33 ecology layer should normally happen in `v33-runtime/` and be reinjected through `tools-v33/build_v33.py`. Do not casually rewrite the recovered V25 baseline and then call the output the same V33 lineage.

## Verified release package

The verified Drive release is:

```text
Feature-Foundry-V33-RECOVERED-ECOLOGY-OUTSIDE-BOX-VERIFIED.zip
size: 2,471,022 bytes
SHA-256: 680978a3aa8f16b47e767720ebfdc3b89fda5c148c5f3d4d3f308390b09385d9
```

The ZIP was re-downloaded during this documentation pass and passed archive-integrity verification. The contained V33 HTML was independently re-hashed to:

```text
83aac630afa4e6522d28452bb6a7c0ebe183eee6812b89b6d742662876af06ec
```

The release checkpoint records remote byte verification of the ZIP.

## Package layout

The V33 package contains both the preserved source baseline and the progressive ecology layer:

```text
Feature-Foundry-V33-RECOVERED-ECOLOGY-OUTSIDE-BOX/
  Feature-Foundry-V25.html
  Feature-Foundry-V33-RECOVERED-ECOLOGY-OUTSIDE-BOX.html
  START-FEATURE-FOUNDRY-V33.cmd
  START-HERE-V33.md
  CHANGES-V33.md
  RECOVERY-LINEAGE-V33.md
  FINAL-VERIFICATION-V33.json
  V33-BUILD-MANIFEST.json
  VERSION-V33.json
  SOURCE-BASELINE-AND-FINAL-HASHES.json
  SHA256SUMS.txt
  apps/
    feature-foundry/
      package.json
      src/
        App.tsx
        main.tsx
        styles.css
  packages/
    core/
      src/theme-foundry.ts
  v33-runtime/
    evolution-runtime.js
    evolution-runtime.css
  tools-v33/
    build_v33.py
  evidence-v33/
    audit_v33_runtime.py
    test_v33_runtime.py
    feature-foundry-v33-static-audit.json
    feature-foundry-v33-runtime-report.json
    screenshots...
  evidence/
    test_actual_app_runtime.py
    audit-actual-controls.mjs
    recovered V25 reports and fixtures...
  dist/
    index.html
```

## Launching the verified ecology artifact

### Windows quick launch

From the extracted release directory, run:

```text
START-FEATURE-FOUNDRY-V33.cmd
```

The launcher opens:

```text
Feature-Foundry-V33-RECOVERED-ECOLOGY-OUTSIDE-BOX.html
```

### Direct browser launch

The V33 release is a self-contained HTML artifact. It can be opened directly in a modern Chromium-family browser without installing npm dependencies.

Confirm the document title reads:

```text
Feature Foundry V33 - Ecology + Outside Box
```

and that the page exposes:

```text
window.__FEATURE_FOUNDRY_V33__.buildId
```

with value:

```text
V33-RECOVERED-ECOLOGY-OUTSIDE-BOX
```

That runtime identity is a stronger check than trusting a filename alone.

## Runtime architecture

V33 has two cooperating layers.

### Layer 1: recovered V25 production workspace

The preserved V25 application owns the main Feature Foundry state, themes, authored objects, Theme Studio, World Explorer, Runtime Evidence, Inspector, persistence, undo/redo, import/export, workspace layouts, weather, time/lighting, sound, mascot, interactions, transitions, performance and accessibility controls.

Its primary workspace storage key is:

```text
gamesync:feature-foundry:workspace:v2
```

The package validates 17 registered themes and 85 authored objects, five objects per theme.

### Layer 2: V33 evolution/ecology adapter

`v33-runtime/evolution-runtime.js` and `evolution-runtime.css` are injected into the verified V25 HTML by `tools-v33/build_v33.py`.

At runtime the adapter locates the live `.foundry`, `.studio`, `.studio-toolbar`, and `.bottom-dock` surfaces, stamps the real app with the V33 build identity, reads current theme variables, and adds an independent fifth top-level workspace called **Evolution Lab**.

The V33 ecology state uses a separate storage key:

```text
gamesync:feature-foundry:evolution:v33
```

Keeping the storage layers separate is intentional. The ecology layer augments the preserved product rather than silently becoming the owner of all Feature Foundry state.

## Evolution Lab navigation

Evolution Lab is a real top-level workspace, not a modal or decorative overlay. Its verified panels are:

1. Library Ecology
2. Optical + Spatial
3. Soundtrack Hub
4. Ecology Director
5. Causal Signals
6. Host Parity

Deep-link state uses query parameters:

```text
ffv33=evolution
ffv33panel=<panel-id>
```

Browser Back and Forward were verified to leave and restore Evolution Lab without losing the underlying Feature Foundry route. Direct URL entry into a specific Evolution Lab panel is also covered by the runtime test.

## Library Ecology

The V33 library-evolution fixture uses 12 normalized items as an inspectable host-neutral collection. The important architecture is not the fixture data itself, but the invariants exercised by it:

- all matching items render, with no viewport admission cap;
- search operates on the real rendered set;
- clearing search restores the complete set;
- collection sections include all, favorites, recent, installed, backlog, and completed;
- empty sections render an authored empty state instead of silently falling back to another section;
- favorites are persisted;
- selection is persisted;
- host vocabulary can change without changing the underlying item set;
- lower presentation tiers do not remove collection entries.

The static audit explicitly rejects `IntersectionObserver`-based admission and collection `slice()` truncation.

## Theme-native grammars

V33 defines an explicit ecology grammar for all 17 registered Feature Foundry themes:

```text
Frutiger Aero
Utopian Scholastic
Wacky Pomo
Contempo Eclectic
Vaporwave
Neo-Y2K
Liminal Leisure
Diner Kitsch
Cassette Futurism
Googie Kitsch
French Synthpop
Memphis
Ethereal CGI
Divine Machinery
Dark Fantasy
Atomic Age
Jazz Design
```

Each grammar defines theme-specific surface language plus hover, select, launch, favorite, achievement, search, empty-state, rare-event, and local tone behavior. The Host Parity panel verifies 17 unique hover, launch, and rare recipes and can switch the real underlying Feature Foundry theme.

Theme-native presentation should remain derivative of real product state. Do not mutate titles, completion percentages, sorting facts, or other factual item state merely to make the theme feel more alive.

## Ecology Director

The Ecology Director is the main policy surface for world-level presentation behavior.

### World modes

Verified modes are:

```text
focused
exploring
playful
authoring
urgent
background
presentation
```

Mode changes persist and emit a causal signal.

### Quality tiers

Verified tiers are:

```text
auto
efficient
balanced
high
ultra
cinematic
```

The contract is content parity, not equal rendering cost. Efficient may remove expensive optical ceremony, but it may not remove cards, world objects, tools, state, or interactions.

The runtime test specifically verifies that Efficient still retains all 12 normalized collection items and all five currently mounted authored world objects.

### Transition depth

Transition depth is 0 through 5:

| Depth | V33 label |
| ---: | --- |
| 0 | Instant / Focus |
| 1 | Ambient Echo |
| 2 | Local Material Journey |
| 3 | Shared-Element Continuity |
| 4 | Workspace Recomposition |
| 5 | Full World Traversal |

Depth changes presentation ceremony only. The destination state must already be functional. Reduced Motion, Performance Mode, and the Efficient tier collapse transition ceremony while preserving the immediate destination.

### Sensory budget

The Director exposes a 0-100 sensory budget. It scales optical/signal presentation intensity, not content admission or data availability.

### Material-memory channels

Three independent reversible presentation-memory channels are verified:

```text
age
a handling/use channel
events/world-event memory
```

They drive presentation variables such as age patina, use patina, and event memory. Turning them off must not change factual labels or item state.

The Director reset restores:

```text
world mode: exploring
transition depth: 2
quality tier: auto
sensory budget: 72
memory channels: all enabled
```

## Causal world-signal bus

V33 implements a bounded inspectable signal history shared by Evolution Lab and the recovered live world.

Signal categories include:

```text
hover
select
launch
favorite
achievement
section
search
rare
```

A signal records:

- generated signal ID;
- kind;
- current theme ID;
- optional item ID;
- human-readable cause label;
- timestamp.

History is explicitly bounded to the newest 24 entries. That bound applies to diagnostic history, not to authored content.

Signals can be replayed. Replayed signals create a new trace entry prefixed with `Replay:` so provenance remains visible.

The V33 fixture also contains a deterministic authoring-only rare-event cadence of one rare signal after every nine counted interactions. The release notes correctly treat that as an inspectable test/authoring policy, not a universal production salience algorithm.

Clicks on real recovered `.world-object` elements propagate into the same V33 signal bus. This is the bridge that makes the ecology layer observe actual world interaction instead of remaining a disconnected demo panel.

## Optical and spatial layer

The Optical + Spatial panel owns per-theme presentation settings for:

```text
opticalDepth
bloom
grain
spatialDepth
```

These settings are stored per theme. The adapter applies optical CSS variables to the real Feature Foundry root and assigns deterministic Z offsets to real world objects.

Performance Mode and Efficient collapse expensive presentation while retaining the world objects. Reduced Motion collapses transition animation. These fallbacks are part of the feature, not a degraded alternate product.

## Soundtrack Hub

V33 reconstructs a six-provider soundtrack handoff surface:

```text
Spotify
Apple Music
Deezer
SoundCloud
TIDAL
YouTube Music
```

Each theme can persist:

- selected provider;
- optional soundtrack URL mapping.

External navigation validates `http:` or `https:` before calling `window.open(..., "noopener,noreferrer")`.

The verified capability boundary is important: V33 performs real provider navigation and persists real mappings, but it does not claim authenticated remote playback or pretend that a local preview control started a remote music session.

## Host adapters

V33 defines five host profiles:

```text
games
apps
albums
shows
documents
```

The adapter changes product vocabulary such as noun, open action, installed status, recent status, and activity metric while retaining the same underlying collection and ecology engine.

This is a portability contract, not proof that five independent production host applications are already integrated. Treat the host profiles as verified adapter behavior inside the V33 artifact until a real external host consumes the same contract.

## Persistence and restart behavior

V33 persists ecology state through `localStorage` under `gamesync:feature-foundry:evolution:v33`.

Verified restart persistence includes:

- favorites;
- provider choice;
- soundtrack mappings;
- per-theme optical settings;
- current Evolution Lab panel;
- Evolution Lab direct-route state.

The release runtime test closes the document, recreates a clean page with the exact persisted storage snapshot, and verifies the state reloads.

## Rebuilding the V33 single-file artifact

The V33 release includes a deterministic Python injector. From the extracted release root:

```bash
python3 tools-v33/build_v33.py
```

The builder:

1. verifies the preserved V25 HTML, `App.tsx`, and `styles.css` hashes;
2. reads `v33-runtime/evolution-runtime.css` and `.js`;
3. injects exactly one V33 stylesheet before `</head>`;
4. injects exactly one V33 runtime before `</body>`;
5. writes the root V33 HTML and `dist/index.html`;
6. requires root and dist bytes to match;
7. rewrites V33 build/version/change/lineage metadata.

If the preserved V25 baseline hash changes, the script exits rather than silently producing a new artifact under the old lineage.

## Building the recovered React source

The package also preserves the recovered source application under `apps/feature-foundry/`.

Declared scripts are:

```bash
npm run dev
npm run typecheck
npm run build
npm test
```

The package declares `@gamesync/core` as `workspace:*`, so this source application is intended to build inside the matching GameSync/Feature Foundry monorepo workspace. Do not assume copying only `apps/feature-foundry` into an empty directory is a complete build environment.

The preserved package manifest records React 19.2.8, React DOM 19.2.8, TypeScript 7.0.2, Vite 8.1.5, Vitest 4.1.10, and `@vitejs/plugin-react` 6.0.4 for this artifact. Those are artifact facts, not a recommendation to force unrelated current repositories onto the same versions.

## Static verification

From the extracted V33 release root:

```bash
python3 evidence-v33/audit_v33_runtime.py
```

The audit verifies, among other things:

- exact V25 baseline preservation;
- root/dist output byte identity;
- exactly one V33 stylesheet and runtime injection;
- every rendered V33 action has a handler;
- every interactive role has a real consumer;
- no TODO or coming-soon paths remain;
- no `IntersectionObserver` viewport admission;
- no collection slice/truncation;
- 24-entry causal history bound;
- safe external URL protocol validation;
- six HTTPS provider destinations;
- 17 explicit theme grammars and 17 theme style identities;
- Efficient tier does not hide collection content;
- reduced-motion replacement is explicit;
- transition depths 1-5 have authored cues;
- memory remains presentation-only.

The original release records 22/22 passing. This documentation pass re-downloaded the exact verified ZIP and reran the static audit successfully: **22 passed, 0 failed**.

## V33 runtime verification

The release runtime test requires Python Playwright and a Chromium executable at `/usr/bin/chromium` as currently written:

```bash
python3 evidence-v33/test_v33_runtime.py
```

The test mounts the exact built HTML and exercises the real controls rather than only inspecting source strings.

Coverage includes:

- exact V33 build identity;
- 17 theme grammars;
- 12 uncapped normalized collection items;
- six soundtrack providers;
- five host adapters;
- seven world modes;
- six quality tiers;
- transition depth 0-5;
- V25 17-theme / 85-object preservation;
- Evolution Lab as a real fifth workspace;
- search, sections, favorites, host selection and persistence;
- soundtrack provider/mapping behavior;
- optics and real DOM Z depth;
- Director mode/tier/memory/reset behavior;
- causal signal injection, history, replay and bounded rare cadence;
- live world-object signal bridging;
- 17-theme host parity matrix;
- browser Back/Forward behavior;
- direct deep-link entry;
- clean-document persistence reload;
- 1600x1000 and 1280x800 clipping checks;
- console and page-error capture.

The original release records 101/101 passing with zero console or page errors. This documentation pass reran the exact extracted V33 runtime test successfully: **101 passed, 0 failed, zero console errors, zero page errors**.

## Preserved V25 regression verification

Run:

```bash
python3 evidence/test_actual_app_runtime.py
node evidence/audit-actual-controls.mjs
```

The exact extracted release was rechecked during this documentation pass:

- recovered V25 runtime: **117 passed, 0 failed**, zero console/page errors;
- static control audit: **59 controls**, zero missing handlers;
- 17-theme validation: passed;
- 85-object validation: passed;
- all active-theme objects remain rendered;
- all studio panels and workspace presets remain rendered;
- import and persisted state use sanitization;
- Focus and Performance modes preserve their ownership/non-regression contracts.

## Acceptance contract for ecology changes

Any new ecology change should prove all of the following before replacing V33 evidence:

1. **Content parity**: every authored object/entity and every applicable collection item remains available at every quality tier.
2. **State parity**: quality, reduced-motion, or presentation-mode changes do not alter factual authored state.
3. **Causal evidence**: interactions produce inspectable signals or equivalent runtime evidence instead of decorative-only feedback.
4. **Reversibility**: Director, optics, memory and host-adapter settings can be changed and restored without corrupting base state.
5. **Persistence**: state survives clean document restart.
6. **Navigation**: direct entry, Back/Forward and top-level workspace switching preserve the promised destination.
7. **Accessibility**: Reduced Motion preserves all actions and state transitions while collapsing motion.
8. **Performance integrity**: lower-cost modes reduce presentation work, not data quantity or feature availability.
9. **Host integrity**: an adapter changes vocabulary/presentation without silently creating a divergent state model.
10. **Regression proof**: preserved V25 controls, themes, objects, undo/redo, import/export and workspace behavior still pass.

## Modification map

### Change Ecology Director behavior

Edit `v33-runtime/evolution-runtime.js` and `evolution-runtime.css`, then rebuild with `tools-v33/build_v33.py` and rerun both V33 audits plus the preserved V25 regression suite.

### Change world modes or quality tiers

Update the runtime constants, state sanitizer/defaults, Director controls, CSS behavior and runtime assertions together. A newly rendered option without corresponding behavior is a dead control and should fail verification.

### Change causal signals

Keep signal provenance inspectable. If a new signal kind is added, update the allowed classes, label grammar, rendering, replay behavior, bounded-history tests and any live-world bridge that emits it.

### Change theme grammars

Keep one explicit grammar per registered theme and preserve the 17-theme identity matrix unless the canonical Feature Foundry theme registry itself changes. Do not silently map multiple themes to one generic behavior language.

### Change host adapters

Keep the underlying data and state stable while changing host vocabulary. A host adapter should not become an excuse to fork the ecology engine.

### Change soundtrack integration

Preserve protocol validation and truthful remote-capability claims. Authenticated playback, if later implemented, needs a real provider adapter, observable result and failure handling rather than a button that only opens a URL.

### Change optical/spatial behavior

Verify real world objects remain present, pointer-interactive and semantically unchanged. Performance/Efficient/Reduced Motion paths must keep full object availability.

## Troubleshooting

### V33 build script refuses to run

Compare the reported baseline hash with the preserved V25 identities above. The refusal is intentional. Restore the exact verified V25 baseline instead of editing the hash constants to bypass the guard.

### Evolution Lab is missing

Confirm the loaded document is the V33 artifact and check:

```text
window.__FEATURE_FOUNDRY_V33__
```

If absent, the V33 runtime was not loaded. Do not debug only the visible tab CSS.

### Evolution Lab opens but is positioned incorrectly

The host position is derived from `.studio`, `.studio-toolbar`, and `.bottom-dock`, with resize handling through `ResizeObserver` when available. Verify those recovered V25 ownership elements still exist before changing the positioning math.

### A quality tier hides cards or world objects

Treat that as a regression. Efficient/Performance presentation may remove expensive visual effects, but it must not cull authored content.

### Reduced Motion changes behavior instead of animation

Treat that as a regression. V33 uses near-zero animation/transition durations while preserving destination state and controls.

### Signal history grows without bound

The verified contract is 24 entries. Preserve a bounded diagnostic history while keeping authored content itself uncapped.

### Soundtrack button claims playback but only opens a provider

The verified V33 boundary is navigation plus persisted mapping. Do not label it authenticated playback unless a real provider integration is present and tested.

### Persistence appears stale

Inspect both storage domains separately:

```text
gamesync:feature-foundry:workspace:v2
gamesync:feature-foundry:evolution:v33
```

The base workspace and ecology adapter intentionally have separate ownership.

### Browser runtime test fails before assertions

The current Python fixture launches Chromium from `/usr/bin/chromium`. Verify Chromium and Python Playwright are available, or update the fixture explicitly for the target environment. Do not convert a browser-launch failure into a product pass or product regression claim.

## Known boundaries

- V33 is the strongest verified runnable ecology artifact, but it is not the newest maintainable Feature Foundry production-source lineage overall. PCX-043 separately tracks the newer V2 recovery source line.
- The 12-item collection is a normalized host-adapter verification fixture, not a production library-size limit.
- Five host adapters are verified inside the artifact; they are not proof that five external production applications already consume the ecology engine.
- Six soundtrack providers are real destinations and persisted mappings; authenticated remote playback is not claimed.
- The causal rare-event 1-in-9 cadence is deterministic verification/authoring behavior, not a universal production ranking algorithm.
- Material memory affects presentation only and must not mutate factual user/library data.

## Current verified checkpoint

The durable V33 checkpoint records:

```text
status: FINAL_READY
V33 runtime assertions: 101/101 PASS
preserved V25 runtime assertions: 117/117 PASS
V33 static assertions: 22/22 PASS
legacy controls audited: 59, missing handlers: 0
console errors: 0
page errors: 0
visual clipping audits: 1600x1000 and 1280x800 PASS
fresh extraction: PASS
remote ZIP byte verification: PASS
noArtificialCaps: true
nonRegression: true
```

The same major gates were independently rerun from the exact downloaded release during this documentation pass and passed.

## Wiki maintenance

Update this page when the verified ecology artifact changes, a newer runnable ecology source supersedes V33, the base-source preservation contract changes, the signal model changes, world modes/quality tiers change, host adapters change, soundtrack ownership changes, persistence keys/schema change, or new regression evidence replaces the current V33 matrix. Preserve historical verified identities rather than overwriting them with unverified newer filenames.