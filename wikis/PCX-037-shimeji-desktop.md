# Shimeji Desktop Wiki

**Project Constellation ID:** `PCX-037`
**Status:** ACTIVE / TRACKED
**Canonical user-owned source:** unresolved in connected GitHub
**Current Java compatibility benchmark:** [DalekCraft2/Shimeji-Desktop](https://github.com/DalekCraft2/Shimeji-Desktop)
**Current architecture/parity benchmark:** [qingchenyouforcc/NeurolingsCE](https://github.com/qingchenyouforcc/NeurolingsCE)
**NeurolingsCE commit inspected:** `00adb430efd13b70db8791af3566eae7b4e8aa17`

## Purpose

Shimeji Desktop is the desktop mascot runtime track. Its defining requirement is compatibility with real Shimeji/Shimeji-ee behavior rather than merely playing sprite animations. Modernization must preserve action/behavior XML graphs, image-set rules, drag/throw/fall behavior, window/edge interactions, DPI behavior, and existing packs.

## Current source boundary

The current connected GitHub environment does not expose a verified user-owned standalone Shimeji Desktop repository. Therefore this page does not claim that any public upstream implementation is the canonical project source.

The current GameSync Shimeji parser and browser-runtime documentation still reference a preserved `Reference/shimejieesrc` lineage, which is useful compatibility evidence, but it is not proof of the current standalone desktop build.

The first implementation step remains source identity resolution, not starting a replacement application.

## Current Java compatibility benchmark

Checked 2026-08-17. [DalekCraft2/Shimeji-Desktop](https://github.com/DalekCraft2/Shimeji-Desktop) remains a useful active compatibility reference. It explicitly attempts backward compatibility while modernizing Shimeji-ee.

Its current documentation records:

- JRE 6 to JDK 25 migration;
- Maven instead of Ant;
- Launch4j Maven packaging;
- DPI scaling work;
- Windows, macOS, and Linux support;
- fixes to default action/behavior XML;
- updated dependencies and logging/documentation improvements;
- continued use of configurable XML action and behavior files.

This remains valuable for Java-era pack behavior, XML semantics, DPI, packaging, and cross-platform regression comparison.

## New architecture/parity benchmark: NeurolingsCE Rust + Flutter

A materially newer ecosystem reference appeared in August 2026: [qingchenyouforcc/NeurolingsCE](https://github.com/qingchenyouforcc/NeurolingsCE). Its current repository was created as a Rust + Flutter rewrite of the maintainer's earlier C++/Qt desktop-pet application, [NeurolingsCE-Qt](https://github.com/qingchenyouforcc/NeurolingsCE-Qt).

The inspected current README and initial rewrite commit document this workspace:

```text
manager/ Flutter fluent_ui manager
crates/
 neurolings-engine Shimeji-ee behavior engine
 neurolings-pack.mascot and legacy ZIP handling
 neurolings-platform native transparent-window/platform layer
 neurolings-runtime runtime daemon, rendering, HTTP/IPC
 neurolings-cli command-line runtime control
 neurolings-store store/index/download/update surface
 neurolings-common shared contracts/constants
 xtask build/run task support
```

Source-verified architectural capabilities include:

- a Shimeji-ee behavior engine with QuickJS condition scripts and 22 action types;
- `.mascot` packages plus legacy ZIP import and path validation;
- Windows transparent windows using `UpdateLayeredWindow` with input hit-through behavior;
- Linux X11 ARGB/XFixes window/input handling;
- macOS AppKit/NSView hit-testing;
- a Rust runtime daemon with tick/render, gestures, bubbles, audio, tray behavior, HTTP and local IPC;
- a separate CLI intended to preserve the earlier external command/output contract;
- a Flutter `fluent_ui` manager;
- cargo workspace tests;
- a headless smoke mode;
- deterministic Windows packaging with SHA-256 output.

### Verified benchmark build and run commands

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

Runtime and CLI examples include:

```powershell
.\target\release\NeurolingsCE.exe
.\target\release\NeurolingsCE-cli.exe --json --mascot list
.\target\release\NeurolingsCE-cli.exe --json --summon mascot --name Default 1
.\target\release\NeurolingsCE-cli.exe --json --list
.\target\release\NeurolingsCE-cli.exe --json --stop
.\target\release\NeurolingsCE.exe --smoke 300
```

The HTTP API is opt-in through `NEUROLINGSCE_HTTP=1`; the README's ping example uses `http://127.0.0.1:32456/shijima/api/v1/ping`.

The benchmark README also states that Linux/macOS window backends have cross-compilation coverage but still need real-machine visual validation, while store/submission server and GitHub App deployment require maintainer-side infrastructure. Those boundaries must remain visible when comparing implementations.

### Why NeurolingsCE is a benchmark, not a replacement

The user-owned Shimeji Desktop source remains unresolved. The Rust rewrite is also very new. Replacing the project wholesale before resolving the user's canonical source would risk losing custom behavior, pack handling, integrations, or already-working desktop semantics.

Use NeurolingsCE as an architecture and parity benchmark for:

- engine/runtime separation;
- native transparent-window backends;
- pack validation/import boundaries;
- CLI and local service contracts;
- deterministic smoke/build/package workflows;
- manager/runtime process separation.

Adopt or transplant an idea only after differential proof against the real Shimeji Desktop baseline.

## Archived alternative: Shijima-Qt

[pixelomer/Shijima-Qt](https://github.com/pixelomer/Shijima-Qt) is archived/discontinued. It remains useful research for cross-platform desktop-pet architecture and libshijima behavior, but it should not become the new canonical modernization base.

This is an important change from earlier research where Shijima-Qt could appear to be the more modern C++/Qt choice. Current maintenance state now outweighs that architectural attraction.

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
- existing pack compatibility and deterministic fixture behavior.

## Differential compatibility corpus

After canonical source resolution, use one representative corpus across the user runtime, the active Java benchmark, and the newer NeurolingsCE architecture benchmark.

Record per pack/runtime:

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

JDK 25 remains the current long-term-support generation used by the active Java compatibility benchmark. There is no evidence-backed reason to move the user project to a newer Java feature release merely because one exists. Preserve JDK 25 as the Java comparison target until the canonical source is resolved and a newer runtime demonstrates a concrete benefit without breaking packaging or behavior.

Official JDK 25 reference: https://openjdk.org/projects/jdk/25/

## Exact current next action

Resolve the canonical user-owned Shimeji Desktop repository/worktree and establish a runnable baseline. Then run the same pack/XML/window/DPI/persistence compatibility corpus against:

1. the user-owned runtime;
2. [DalekCraft2/Shimeji-Desktop](https://github.com/DalekCraft2/Shimeji-Desktop) for current Java/Shimeji-ee compatibility behavior;
3. [qingchenyouforcc/NeurolingsCE](https://github.com/qingchenyouforcc/NeurolingsCE) for the Rust/native-window/runtime-service architecture.

Only after that differential pass should a modernization path be selected.

## Maintenance

Update this wiki when the canonical user source is resolved, when the desktop runtime or packaging changes, when a pack-compatibility fixture catches a regression, or when either current benchmark materially changes its maintenance state or architecture.
