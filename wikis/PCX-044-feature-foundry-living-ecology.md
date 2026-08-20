# Feature Foundry Living Ecology Wiki

**Project Constellation ID:** `PCX-044`  
**Status:** ACTIVE / TRACKED  
**Current canonical production repository:** [Herbertofury/Feature-Foundry](https://github.com/Herbertofury/Feature-Foundry)  
**Current released product line:** `v24.0.0`  
**Current verified repository head:** `e1ba080b5c7590f1c844a6ed13b3a471709920b9`  
**Current production ecology owners:** `src/world/ObjectEcologyLayer.ts`, `src/world/ThemeDirector.ts`, `src/world/CinematicWorld.ts`, `src/premium.ts`  
**Historical high-confidence ecology benchmark:** `Feature Foundry V33 - Recovered Ecology` / `V33-RECOVERED-ECOLOGY-OUTSIDE-BOX`  
**Historical V33 artifact SHA-256:** `83aac630afa4e6522d28452bb6a7c0ebe183eee6812b89b6d742662876af06ec`  
**Historical V33 release ZIP SHA-256:** `680978a3aa8f16b47e767720ebfdc3b89fda5c148c5f3d4d3f308390b09385d9`

## Purpose

Living Ecology is the Feature Foundry subsystem for worlds that behave like coherent, inspectable systems rather than decorative backgrounds. It owns theme-native interaction language, world signals, memory-derived presentation, transition depth, presentation tiers, host adaptation, soundtrack handoff, optical/spatial treatment, reduced-motion equivalence, and the rules that keep all authored content available while presentation cost changes.

The core contract is:

`user/system input -> world signal -> bounded reaction -> persisted or replayable evidence`

The subsystem is not allowed to make performance appear better by removing authored entities, hiding off-screen content, reducing collection quantity, silently changing factual state, or substituting decorative animation for a real state transition.

## Current authority model

Living Ecology now has two verified authority lanes that must remain distinct.

### Current production implementation: Feature Foundry v24.0.0

The canonical production repository is `Herbertofury/Feature-Foundry`. Current `main` is a complete released TypeScript 7 + Vite 8 + Three.js/WebGL + Tauri 2/Rust application, not a placeholder or recovery shell. Its project-owned build record identifies v24.0.0 as released and records successful V24 contract, data-authority, TypeScript, Rust, production-build, and 1536x1024 browser interaction/screenshot verification.

For current implementation, install, modification, build, package, runtime diagnostics, and release work, use this repository and release line first.

Current production ecology is owned by:

- `src/world/ObjectEcologyLayer.ts` for object spawning, selection, pointer dragging, throwing, keyboard movement, reactions, media/music affordance routing, pulse behavior, and ecology diagnostics;
- `src/world/ThemeDirector.ts` for the 17 verified V33-derived runtime worlds plus 10 artist worlds, room/weather/object presentation, theme persistence, world switching, Theme Atlas, and object affordance dispatch;
- `src/world/CinematicWorld.ts` for the continuously rendered Three.js world layer;
- `src/premium.ts` for cross-system world signals, diagnostics, browser/native snapshot behavior, room/theme/media/music/ecology event routing, fullscreen, and native-shell integration;
- `src/data/theme-world-packages.json` and `src/world/themeCatalog.ts` for current theme/world/object authority;
- `src-tauri/` for native persistence, SQLite authority, snapshots, and desktop packaging.

### Historical V33 ecology benchmark

V33 remains a high-confidence runnable non-regression benchmark and preserves ecology capabilities that are more explicitly instrumented than the current v24 production implementation, including Evolution Lab, quality tiers, transition depth, bounded causal-signal history, replay, host-adapter fixtures, material-memory presentation channels, and the older standalone verification matrices.

Current v24 intentionally consumes the V33 runtime catalog authority rather than discarding it. V33 should therefore remain available for regression comparison, but it is no longer the default maintainable production-source authority.

Do not infer that every V33 Evolution Lab control or host-adapter fixture ships unchanged in v24 unless current v24 source or runtime verification proves it. Conversely, do not describe V33 as the newest production source now that the released v24 repository exists.

## Current v24 production ecology

### Verified catalog and world authority

Current repository tests require:

- 17 approved V33-derived theme packages;
- 34 rooms across those packages;
- 85 exact ecology objects, five per approved theme;
- 17 weather systems;
- 10 current artist worlds across Frawgy, Lightweaverart, Dreamrelicc, Karoline Georges, and saveroom;
- 27 total worlds in Theme Atlas verification coverage.

The current authority test fails if those counts or approved theme IDs drift. It also verifies the paired artist-world database and native SQLite command surface.

### Object ecology runtime

`ObjectEcologyLayer` materializes every object in the active theme as an interactive button inside the left or right living-world lane. Current source does not use viewport admission, object-count slicing, or a near-viewport render cap for the active theme's ecology actors.

Each actor carries stable object metadata through `data-object-id`, shape and material attributes, an accessible label, visible object name, and the authored affordance list. The runtime supports:

- pointer selection;
- pointer capture during drag;
- live x/y movement;
- velocity tracking;
- bounded drag positions inside the owning lane;
- release-to-throw behavior;
- gravity, damping, wall/floor restitution, and settle detection;
- keyboard activation with Enter or Space;
- keyboard movement with arrow keys and a larger Shift step;
- visual activation/reaction state;
- media-surface routing for screen/video affordances;
- Music Hub routing for music/note affordances;
- generic `ff:object-ecology-action` dispatch for other authored interactions;
- a world pulse method used by broader living-world reactions;
- diagnostics reporting the active theme, actor count, selected actor, and moving actor count.

Current source keeps object identity separate from placement state. The actor map is keyed by the authored object record ID, while x/y/velocity/drag state remain runtime placement state.

### Theme and room routing

`ThemeDirector` keeps current theme selection under `ff.premium-theme.v1`, exposes separate V33-runtime and artist-world authority lanes, and populates Theme Atlas from the full current catalog rather than flattening the two sources together.

Applying a theme updates the active premium-theme identity, palette, room list, weather list, object summary, mascot label, soundtrack summary, and room/weather selectors, then emits `ff:premium-theme-change`. Room selection emits `ff:premium-room-change`. The object ecology reloads from the selected theme's exact object list.

Theme Atlas object controls route screen/video objects to Living Screen Studio, music/note objects to Music Hub, and other objects to the ecology action bus. A rendered affordance therefore has a real runtime consumer rather than being a decorative label.

### World reaction bus

The current premium runtime connects ecology to the surrounding world instead of leaving object interactions isolated. Theme changes, room changes, music signals, media signals, and object-ecology actions pulse the Three.js world and the ecology actors through the shared `signalWorld()` path.

`window.render_game_to_text()` exposes current runtime state including theme lineage, world mode/view, object snapshots, ecology diagnostics, selected state, mascots, runtime diagnostics, catalog diagnostics, Theme Director state, Music Hub state, media-surface state, pointer position, last interaction, native profile/catalog state, and snapshot status. This provides a machine-readable qualification surface for agents and automated tests.

### Browser and native snapshots

`Ctrl+S` saves a world snapshot. In the browser build the runtime stores the rendered diagnostic state under `ff.browser-snapshot.v1`. In the Tauri build it invokes the native `save_world_snapshot` command and reports `saving`, `saved`, or `error` state rather than hardcoding success.

The native shell also retrieves runtime-profile and catalog-summary information through Tauri commands when available.

### Current build and verification commands

From the canonical v24 repository:

```powershell
npm install
npm run dev
npm run verify
npm run desktop:build
npm run package
```

For native development:

```powershell
npm run desktop:dev
```

The declared `verify` chain runs:

1. exact V24 contract tests;
2. catalog/artist-world/provider/native-authority tests;
3. TypeScript type checking;
4. optimized Vite production build;
5. `cargo check` against `src-tauri/Cargo.toml`;
6. the Playwright browser UI test.

The current UI fixture runs at 1536x1024 and verifies the left/center/right living shell, a procedural world canvas at least 1300x850, exactly five active ecology actors for the current V33-derived theme, Frawgy world switching, 27 Theme Atlas cards, Music Hub provider controls, media-surface URL validation, runtime diagnostics, and zero page errors.

### Current v24 source layout

The production ecology-relevant tree is:

```text
src/
  premium.ts
  data/
    theme-world-packages.json
    artist-worlds-v4.0.1.json
  world/
    CinematicWorld.ts
    ObjectEcologyLayer.ts
    ThemeDirector.ts
    themeCatalog.ts
  media/
  music/
src-tauri/
  src/
tests/
  contract.test.ts
  authority.test.ts
  ui.test.ts
scripts/
```

The original V24 imperative runtime remains preserved inside the compatibility layer and protected by an exact source-contract test. Current premium ecology code is layered around that contract rather than silently replacing it.

## Historical V33 source authority and recovery lineage

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
ffv33panel=\<panel-id>
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

External navigation validates `http:` or `https:` before calling `window.open(.., "noopener,noreferrer")`.

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

- v24.0.0 is now the current maintainable production source for Living Ecology. V33 is retained as a historical high-confidence benchmark, not the default source tree.
- Current v24 verifies the active theme's five ecology actors and the broader production world shell, but its current UI fixture does not independently replay every V33 Evolution Lab quality-tier, causal-history, host-adapter, or transition-depth assertion. Keep those V33 claims historical until equivalent v24 tests prove them.
- The current production object runtime verifies drag/throw/keyboard/affordance implementation from source and broad browser UI qualification, but source presence alone is not a substitute for adding focused interaction regressions when object-physics behavior changes.

- V33 is the strongest verified runnable ecology artifact, but it is not the newest maintainable Feature Foundry production-source lineage overall. PCX-043 separately tracks the newer V2 recovery source line.
- The 12-item collection is a normalized host-adapter verification fixture, not a production library-size limit.
- Five host adapters are verified inside the artifact; they are not proof that five external production applications already consume the ecology engine.
- Six soundtrack providers ar real destinations and persisted mappings; authenticated remote playback is not claimed.
- The causal rare-event 1-in-9 cadence is deterministic verification/authoring behavior, not a universal production ranking algorithm.
- Material memory affects presentation only and must not mutate factual user/library data.

## Current v24 production checkpoint

Current production evidence records:

```text
canonical repository: Herbertofury/Feature-Foundry
release: v24.0.0
repository head: e1ba080b5c7590f1c844a6ed13b3a471709920b9
package version: 24.0.0
approved runtime themes: 17
rooms: 34
weather systems: 17
ecology objects: 85
artist worlds: 10
Theme Atlas total worlds: 27
web stack: TypeScript 7 + Vite 8 + Three.js/WebGL
native stack: Tauri 2 + Rust + bundled SQLite
browser qualification viewport: 1536x1024
verification chain: contract + authority + typecheck + Vite build + cargo check + browser UI
release state: published GitHub release plus mirrored Google Drive release set
```

Current v24 is the default production source for new Living Ecology engineering. Historical V33 remains the explicit deeper ecology/non-regression benchmark where it still has stronger instrumentation or capability-specific acceptance evidence.

## Historical V33 verified checkpoint

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

Update this page when the canonical v24 production ecology changes, a newer released production source supersedes v24, the historical V33 benchmark changes, the base-source preservation contract changes, the signal model changes, world modes/quality tiers change, host adapters change, soundtrack ownership changes, persistence keys/schema change, or new regression evidence replaces the current V33 matrix. Preserve historical verified identities rather than overwriting them with unverified newer filenames.
