# Shimeji Desktop Wiki

**Project Constellation ID:** `PCX-037`  
**Status:** ACTIVE / TRACKED  
**Canonical user-owned source:** unresolved in connected GitHub  
**Current Java compatibility benchmark:** [DalekCraft2/Shimeji-Desktop](https://github.com/DalekCraft2/Shimeji-Desktop)  
**Current architecture/parity benchmark:** [qingchenyouforcc/NeurolingsCE](https://github.com/qingchenyouforcc/NeurolingsCE)  
**NeurolingsCE current head inspected:** `3f3ec7221cbc7c597b17d77e0da5082256af75ed`  
**NeurolingsCE migration baseline:** Rust + Flutter rewrite of the maintainer's earlier C++/Qt line, targeting behavioral/API parity with C++/Qt `v0.5.3`

## Purpose

Shimeji Desktop is the desktop mascot runtime track. Its defining requirement is compatibility with real Shimeji/Shimeji-ee behavior rather than merely playing sprite animations. Modernization must preserve action/behavior XML graphs, image-set rules, drag/throw/fall behavior, window/edge interactions, DPI behavior, pack compatibility, runtime control semantics, and restart persistence.

## Current source boundary

The current connected GitHub environment still does not expose a verified user-owned standalone Shimeji Desktop repository. Therefore this page does **not** claim that either public upstream implementation below is the user's canonical project source.

The current GameSync Shimeji parser/browser-runtime documentation still references preserved Shimeji-ee source lineage, which remains useful compatibility evidence, but it is not proof of the current standalone desktop build.

The first implementation step remains source identity resolution, not starting a replacement application.

## Current Java compatibility benchmark

Checked 2026-08-21. [DalekCraft2/Shimeji-Desktop](https://github.com/DalekCraft2/Shimeji-Desktop) remains a useful active Java-era compatibility reference. It explicitly attempts backward compatibility while modernizing Shimeji-ee.

Its current documentation records:

- migration from JRE 6-era assumptions to JDK 25;
- Maven instead of Ant;
- Launch4j Maven packaging;
- DPI scaling work;
- Windows, macOS, and Linux support;
- fixes to default action/behavior XML;
- updated dependencies and logging/documentation improvements;
- continued use of configurable XML action and behavior files.

Use this benchmark primarily for Java/Shimeji-ee pack semantics, XML behavior, DPI, packaging, and cross-platform regression comparison.

## Current architecture/parity benchmark: NeurolingsCE Rust + Flutter

[NeurolingsCE](https://github.com/qingchenyouforcc/NeurolingsCE) has evolved materially since the first Rust-rewrite checkpoint documented here. The current repository is the Rust + Flutter rewrite, while the maintainer's earlier C++/Qt implementation is preserved separately as the migration source.

The repository's rewrite plan states that the new implementation targets full behavioral and external-contract parity with the earlier C++/Qt `v0.5.3` line, while separating the runtime, engine, pack layer, platform backends, CLI, store/client code, and Flutter manager.

### Current source layout

The current README/rewrite plan document this architecture:

```text
manager/                       Flutter fluent_ui manager
crates/
  neurolings-engine            Shimeji-ee parser/behavior/physics engine
  neurolings-pack              .mascot + legacy archive handling/validation
  neurolings-platform          transparent windows, IPC, autostart, platform services
  neurolings-runtime           runtime daemon, tick/render, HTTP/IPC, tray, bubbles
  neurolings-cli               CLI contract and runtime control
  neurolings-store             store/index/download/login/submission/update client
  neurolings-common            shared contracts/constants/serialization
xtask/                         build/run task support
packaging/                     release assembly and platform packaging
mascot_pack/                   deterministic compatibility fixtures
```

### Engine and pack compatibility

The rewrite plan records a full Shimeji-ee behavior engine port rather than a generic sprite player. Current project-owned upstream evidence includes:

- parser and Japanese compatibility translation;
- 22 action types;
- behavior manager, environment, physics, and broadcast interaction;
- QuickJS condition scripting with bounded execution protection;
- deterministic `Math.random` support for reproducible tests;
- `.mascot` package handling;
- legacy Shimeji archive analysis/import;
- SafePath/path-traversal protection;
- inspect/validate/extract/write/install flows;
- deterministic fixture packs used for replay/smoke testing.

The rewrite plan explicitly uses golden-state/deterministic tick replay as the core defense against behavior drift.

### Runtime and native window architecture

Current source evidence documents:

- one native transparent always-on-top pet window per mascot;
- Windows layered windows using `UpdateLayeredWindow` with per-pixel alpha and hit-through behavior;
- Linux X11 ARGB windows with XFixes input-shape handling and work-area awareness;
- macOS AppKit/NSView hit-testing and frame drawing;
- drag, right-click, hotspot, fall-through, frame caching, mirrored poses, and premultiplied BGRA rendering;
- tray behavior;
- multi-monitor handling;
- local IPC plus optional HTTP control;
- headless smoke mode for CI.

Linux and macOS backends have cross-compilation coverage in the rewrite plan, but the maintainer still records real-machine visual validation as an open requirement. Wayland remains the highest-risk platform boundary and should be qualified independently from X11.

### CLI, IPC, and HTTP contracts

The runtime/CLI boundary is intentionally treated as a compatibility contract rather than incidental tooling.

Current examples remain:

```powershell
.\target\release\NeurolingsCE.exe
.\target\release\NeurolingsCE-cli.exe --json --mascot list
.\target\release\NeurolingsCE-cli.exe --json --summon mascot --name Default 1
.\target\release\NeurolingsCE-cli.exe --json --list
.\target\release\NeurolingsCE-cli.exe --json --stop
```

HTTP is opt-in through `NEUROLINGSCE_HTTP=1` and uses the preserved `/shijima/api/v1` route family, for example:

```powershell
curl http://127.0.0.1:32456/shijima/api/v1/ping
```

The rewrite plan records runtime commands for ping/list/spawn/alter/dismiss/stop/labels/preview and a local IPC transport that preserves the earlier endpoint/JSON-line contract.

### Flutter manager

The Flutter manager is no longer merely a proposed shell. The rewrite plan records Windows build success and progressive connection of its seven-page navigation model.

Current page families include:

- Home;
- Create;
- Store;
- Combinations;
- Codex;
- Settings;
- About.

The initial manager milestone established live runtime status, installed-template summon controls, running-pet close controls, archive import, language switching, runtime/CLI discovery, and manager/runtime E2E wiring.

Later project commits and rewrite-plan checkpoints add or harden:

- store browsing/search/filter/install/status behavior;
- combinations save/restore/list/delete behavior;
- Codex integration surfaces;
- complete settings controls;
- manager navigation ordering and page structure;
- About/Inspector/Create refinements;
- install progress and streamed download retry behavior;
- dynamic tray refresh and cross-platform tray placeholders.

### Store, login, submission, and updater boundaries

The current `neurolings-store` layer records:

- versioned store index models;
- filtering/search;
- ETag/Last-Modified-aware cache behavior;
- atomic index/previous/meta rotation;
- SHA-256-verified downloads;
- GitHub Device Flow client support;
- credential-storage abstraction;
- two-stage HMAC submission session flow;
- idempotency handling;
- updater manifest validation and minimum-supported-version decisions.

Do not overstate deployment completeness. The rewrite plan still records maintainer-side infrastructure requirements for the submission service, GitHub App, Pages deployment, and some account-backed UI flows.

### Composition, bubble, Codex, and startup behavior

The rewrite plan's M8 milestone records working implementation for:

- Codex configuration block install/uninstall and notification forwarding;
- mascot speech/notification bubbles;
- mascot compositions with atomic `combinations.json` persistence;
- save/restore/list/delete composition operations;
- Windows Registry Run autostart;
- Linux XDG autostart;
- sandbox/window mode;
- generic HTTP command passthrough;
- restore/rebuild of saved mascot compositions.

These are useful architecture references for the user project because they combine desktop behavior, external control, and restart persistence without flattening Shimeji semantics.

## NeurolingsCE milestone status checked 2026-08-21

The current `docs/REWRITE_PLAN.md` records **M0 through M9 complete**.

Key recorded verification checkpoints include:

- M1: deterministic engine replay/golden tests and seven pack smoke coverage;
- M3: stable Windows GUI smoke plus headless runtime smoke;
- M4: CLI + HTTP + IPC E2E coverage and clean clippy state;
- M5: Flutter manager build/widget verification and manager/runtime deployment test;
- M6: Linux/macOS cross-target compilation checks;
- M7: store-client tests;
- M8: composition/Codex/bubble/window/autostart E2E coverage;
- M9: updater/package gate with tests, `clippy -D warnings`, formatting, and smoke verification;
- later M7 UI wiring checkpoint: **76 tests green**, `clippy -D warnings` clean, `flutter analyze` clean, and `--smoke 150` passing.

Treat those as upstream benchmark evidence tied to the NeurolingsCE rewrite, not as validation of the unresolved user-owned Shimeji Desktop project.

## Post-M9 hardening on current head

Since the earlier inspected commit `00adb430efd13b70db8791af3566eae7b4e8aa17`, the upstream benchmark has continued active development. The current inspected head is `3f3ec7221cbc7c597b17d77e0da5082256af75ed`.

Recent project-owned commits include:

- P0 contract fixes for look-direction flipping, vertical movement bounds, store index/cache behavior, Codex hooks, and autostart arguments;
- Store page tag filtering, ID-aware search, detail dialog, install progress, and streamed-download retry improvements;
- additional manager settings/home/composition controls;
- Store/Combinations/Codex page completion work;
- manager About/Inspector/Create restructuring;
- manager navigation alignment/order fixes;
- dynamic tray refresh, cross-platform tray placeholders, and publication-workflow changes;
- About/analyzer warning fixes.

This makes the current benchmark materially stronger than the initial Rust-rewrite snapshot and justifies using current-head evidence rather than permanently pinning the architecture comparison to the August 14 first rewrite commit.

## Verified benchmark build and run commands

The current NeurolingsCE README documents:

```powershell
cargo build --release
cargo test --workspace
```

For the Flutter manager:

```powershell
cd manager
flutter pub get
flutter build windows --release
```

Runtime and smoke examples include:

```powershell
.\target\release\NeurolingsCE.exe
.\target\release\NeurolingsCE-cli.exe --json --mascot list
.\target\release\NeurolingsCE-cli.exe --json --summon mascot --name Default 1
.\target\release\NeurolingsCE-cli.exe --json --list
.\target\release\NeurolingsCE-cli.exe --json --stop
.\target\release\NeurolingsCE.exe --smoke 300
```

The rewrite plan currently records this development environment:

```text
Rust 1.97.1 / cargo 1.97.1
Flutter 3.44.8
Dart 3.12.2
Windows 11 x64 development host
```

Use those versions as evidence for reproducing the current benchmark checkout, not as automatic requirements for the unresolved user project.

## Why NeurolingsCE is a benchmark, not a replacement

The user-owned Shimeji Desktop source remains unresolved. Replacing the project wholesale before locating that source could discard custom packs, already-working desktop semantics, integrations, persistence, or project-specific UX.

Use NeurolingsCE as an architecture and parity benchmark for:

- engine/runtime separation;
- deterministic engine testing;
- native transparent-window backends;
- pack validation/import boundaries;
- CLI/API/IPC compatibility contracts;
- manager/runtime process separation;
- compositions and restart persistence;
- deterministic smoke/build/package workflows;
- store/update integrity;
- external-agent/tool control.

Adopt or transplant an idea only after differential proof against the real Shimeji Desktop baseline.

## Archived alternative: Shijima-Qt

[pixelomer/Shijima-Qt](https://github.com/pixelomer/Shijima-Qt) is archived/discontinued. It remains useful research for cross-platform desktop-pet architecture and libshijima behavior, but it should not become the new canonical modernization base.

Current maintenance state outweighs its architectural interest when selecting a future production base.

## Compatibility contract

A desktop modernization must preserve or explicitly test at least:

- `actions.xml` graph semantics;
- `behaviors.xml` graph semantics and weighted behavior choice;
- required `ChaseMouse`, `Fall`, `Dragged`, and `Thrown` action/behavior paths where applicable;
- nested Sequence/Select/reference behavior;
- image-set discovery and alternate per-pack configuration directories;
- pose image, anchor, duration, velocity, gravity/resistance, and movement fields;
- drag, throw, fall, get-up, wall/ceiling/edge behavior;
- window interaction and screen/work-area geometry;
- multi-monitor and DPI scaling;
- image-set selection and persisted settings;
- tray/context controls;
- composition/restart persistence when the user runtime supports it;
- existing pack compatibility and deterministic fixture behavior.

## Differential compatibility corpus

After canonical source resolution, use one representative corpus across the user runtime, the active Java benchmark, and the current NeurolingsCE architecture benchmark.

| Area | Evidence to capture |
| --- | --- |
| Parse/config | chosen config files, parse errors, missing references, aliases |
| Action/behavior | selected actions, weighted behavior decisions, conditions, Sequence/Select/reference semantics |
| Media/poses | image/frame identity, anchors, durations, velocity, gravity/resistance |
| Interaction | drag, throw, fall, get-up, pet/click behavior |
| Desktop geometry | edges, windows, work area, multi-monitor, DPI |
| Packaging | directory pack, `.mascot`, legacy ZIP behavior where supported |
| Runtime control | tray, CLI/API/IPC commands where applicable |
| Persistence | selected packs, settings, composition state after restart |
| Failure behavior | malformed packs, missing files, unsafe paths, invalid conditions |
| Performance | startup time, steady-state memory/CPU, input/render responsiveness |

### Minimum parity rule

Do not promote a newer architecture merely because its language or UI stack is newer. The accepted candidate must preserve the user's existing pack and behavior semantics and show a measured advantage in one or more relevant dimensions without regressing compatibility, user-visible behavior, quantity, fidelity, or recovery paths.

## Current Java direction

JDK 25 remains the long-term-support generation used by the active Java compatibility benchmark. There is no evidence-backed reason to move the user project to a newer Java feature release merely because one exists. Preserve JDK 25 as the Java comparison target until the canonical source is resolved and a newer runtime demonstrates a concrete benefit without breaking packaging or behavior.

Official JDK 25 reference: https://openjdk.org/projects/jdk/25/

## Exact current next action

1. Resolve the canonical user-owned Shimeji Desktop repository/worktree and establish a runnable baseline.
2. Preserve its current source/artifacts before changing anything.
3. Run the same pack/XML/window/DPI/persistence corpus against:
   - the user-owned runtime;
   - [DalekCraft2/Shimeji-Desktop](https://github.com/DalekCraft2/Shimeji-Desktop) for current Java/Shimeji-ee compatibility behavior;
   - [qingchenyouforcc/NeurolingsCE](https://github.com/qingchenyouforcc/NeurolingsCE) at a pinned current commit for Rust/native-window/runtime-service architecture.
4. Compare exact behavior, failure handling, persistence, packaging, startup, CPU/memory, and interaction responsiveness.
5. Choose a modernization path only after the differential evidence is captured.

## Maintenance

Update this wiki when the canonical user source is resolved, when the desktop runtime or packaging changes, when a pack-compatibility fixture catches a regression, or when either current benchmark materially changes its maintenance state, architecture, or verified parity evidence.
