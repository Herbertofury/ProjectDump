# Shimeji Desktop Wiki

**Project Constellation ID:** `PCX-037`  
**Status:** ACTIVE / TRACKED  
**Canonical user-owned source:** unresolved in connected GitHub  
**Current external compatibility benchmark:** [DalekCraft2/Shimeji-Desktop](https://github.com/DalekCraft2/Shimeji-Desktop)  
**Benchmark main inspected:** `dea89528c10c066626a09609f0e742cbe6405a8d`

## Purpose

Shimeji Desktop is the desktop mascot runtime track. Its defining requirement is compatibility with real Shimeji/Shimeji-ee behavior rather than merely playing sprite animations. Modernization must preserve action/behavior XML graphs, image-set rules, drag/throw/fall behavior, window/edge interactions, DPI behavior, and existing packs.

## Current source boundary

The current connected GitHub environment does not expose a verified user-owned standalone Shimeji Desktop repository. Therefore this page does not claim that any public upstream fork is the canonical project source.

The current GameSync Shimeji parser and browser-runtime documentation still reference a preserved `Reference/shimejieesrc` lineage, which is useful compatibility evidence, but it is not proof of the current standalone desktop build.

The first implementation step remains source identity resolution, not starting a replacement application.

## Current strongest upstream benchmark

Checked 2026-08-17. [DalekCraft2/Shimeji-Desktop](https://github.com/DalekCraft2/Shimeji-Desktop) is active and explicitly attempts backward compatibility while modernizing Shimeji-ee.

Its current README records:

- JRE 6 to JDK 25 migration;
- Maven instead of Ant;
- Launch4j Maven packaging;
- proper DPI scaling;
- Windows, macOS, and Linux support;
- fixes to default action/behavior XML;
- updated dependencies and logging/documentation improvements;
- continued use of configurable XML action and behavior files.

Recent July 2026 commits include settings reload work and dependency maintenance, so this is a useful current compatibility benchmark rather than only a historical fork.

### Why it is a benchmark, not an automatic replacement

The user-owned project may contain custom behavior, patches, pack handling, or integrations absent from the upstream fork. Replacing it wholesale before resolving the canonical source would violate the anti-degradation contract.

Use the upstream project to build differential tests and selectively transplant improvements only after the user-owned baseline is known.

## Archived alternative: Shijima-Qt

[pixelomer/Shijima-Qt](https://github.com/pixelomer/Shijima-Qt) is now archived/discontinued. It remains useful research for cross-platform desktop-pet architecture and libshijima behavior, but it should not become the new canonical modernization base.

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

## Proposed modernization experiment

After canonical source resolution, create one compatibility corpus containing representative old and new packs. Run the same corpus against the existing user runtime and the current JDK 25 benchmark.

Record per pack:

- parse success/failure;
- chosen config files;
- actions and behaviors resolved;
- missing references;
- animation/frame identity;
- drag/throw/fall result;
- edge/window interaction;
- DPI and multi-monitor result;
- startup time and memory;
- settings/restart persistence.

Only port a newer implementation detail when it solves a measured problem and the corpus proves no regression.

## Current Java direction

JDK 25 is the current long-term-support generation used by the active compatibility benchmark. There is no evidence-backed reason to move the user project to a newer feature release merely because it exists. Preserve the JDK 25 compatibility target until the real source is resolved and a newer runtime demonstrates a concrete benefit without breaking packaging or behavior.

Official JDK 25 reference: https://openjdk.org/projects/jdk/25/

## Exact current next action

Resolve the canonical user-owned Shimeji Desktop repository/worktree and establish a runnable baseline. Then run a pack/XML/window/DPI differential compatibility pass against DalekCraft2/Shimeji-Desktop before selecting any modernization path.

## Maintenance

Update this wiki when the canonical user source is resolved, when the desktop runtime or packaging changes, when a pack-compatibility fixture catches a regression, or when the external benchmark's maintenance state materially changes.
