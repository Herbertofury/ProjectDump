# Webmeji Wiki

**Project Constellation ID:** `PCX-039`  
**Status:** ACTIVE / TRACKED  
**Canonical user-owned standalone source:** unresolved in connected GitHub  
**Current external behavior reference:** [lars-rooij/webmeji](https://github.com/lars-rooij/webmeji)  
**Current GameSync integration evidence:** [Herbertofury/Gamesync](https://github.com/Herbertofury/Gamesync) at `a8e37976eb0b3ee3c4ec5e802b02d3bfa1f41928`

## Purpose

Webmeji is the lightweight website-embedded mascot runtime track. Its value is near-zero setup: a site owner should be able to add a companion directly to ordinary pages without turning the site into an application framework or breaking host-page input.

The intended project is related to Shimeji but is not interchangeable with the full Shimeji Desktop or browser-extension tracks. It should preserve web-native simplicity while borrowing only the behavior semantics that make sense for an embedded page companion.

## Current source boundary

The current connected GitHub environment does not expose a verified user-owned standalone Webmeji repository. Do not initialize a replacement project merely because the public reference is easy to find.

Two current evidence sources are useful:

1. `lars-rooij/webmeji`, a direct public embedded-Webmeji implementation;
2. the current GameSync mascot contract, which already contains explicit Webmeji settings and allowances.

The next implementation action is to resolve the user-owned source and reconcile those two references against it.

## External Webmeji reference

Checked 2026-08-17. [lars-rooij/webmeji](https://github.com/lars-rooij/webmeji) describes itself as a Shimeji embedded directly into a website. Its source README was last updated 2026-01-27.

Its basic embed consists of only:

- `webmeji.css`
- `config.js`
- `webmeji.js`

No package manager or build step is required by that source tree.

Verified reference behavior includes:

- walking along the bottom edge;
- idle/sit/dance/trip actions;
- jumping to side/top edges;
- hanging/climbing/falling from edges;
- hover pet interaction;
- mouse and touch dragging;
- requestAnimationFrame movement;
- multiple instances and multiple skins;
- configurable allowances, movement speeds, animation frames, intervals, and loop counts.

The upstream roadmap mentions momentum while dragging/falling, collision-based edge clinging, jumping between edges, arbitrary edges, and a client-side behavior menu. Treat those as ideas, not as already-implemented facts.

## Current GameSync Webmeji contract

The current GameSync mascot contract contains explicit Webmeji controls rather than treating Webmeji as an unnamed generic sprite mode.

Current defaults include:

- `webmejiCanvasRenderer: false`
- `webmejiEnabled: false`
- `webmejiSpawnCount: 3`
- `webmejiJumpChance: 0.08`
- `webmejiWalkSpeed: 50`
- `webmejiFallSpeed: 200`
- `webmejiJumpSpeed: 150`
- `webmejiGetUpMs: 2000`
- pet, drag, bottom, top, left, and right allowances enabled.

This is evidence that GameSync already treats Webmeji behavior as a first-class compatibility surface. Preserve that contract when reconciling standalone and integrated implementations.

## Experimental comparison source

[pixelomer/Shijima-Web](https://github.com/pixelomer/Shijima-Web) is an experimental JavaScript web version of Shijima. It is not archived, but its source has not been pushed since January 2026 and its adoption is small.

Use it only as a differential implementation reference. It is not mature enough to replace the current Webmeji reference or any user-owned source.

## Recommended architecture boundary

Keep the embeddable core small and host-neutral:

- configuration and sprite/animation data;
- creature state machine;
- page-edge/element-edge geometry;
- pointer/touch interaction;
- animation/movement scheduler;
- deterministic optional RNG for tests;
- explicit cleanup/dispose path.

Host-specific adapters can then provide:

- plain-script embed;
- GameSync integration;
- browser-extension integration;
- future Feature Foundry preview/runtime integration.

Avoid coupling the core to extension APIs, React, a specific bundler, or a single host page.

## Current improvement experiment

Prototype two optional behaviors without changing the default three-file embed contract:

1. momentum on drag release/falling;
2. arbitrary element-edge attachment so a Webmeji can treat selected page elements as climb/hang surfaces.

The experiment must be capability/config driven and disabled by default until verified.

### Acceptance gate

- existing bottom/top/left/right behavior stays identical when new options are off;
- pet, drag, jump, fall, get-up, and multi-instance behavior still works;
- mouse and touch remain supported;
- host-page clicks, text selection, scrolling, links, forms, and navigation are not intercepted incorrectly;
- element-edge attachment updates correctly as layout/scroll changes;
- cleanup removes listeners/animation work;
- no viewport culling or quantity cap is introduced as a performance shortcut.

## Exact current next action

Resolve the canonical user-owned Webmeji source. Compare its behavior/configuration with `lars-rooij/webmeji` and the current GameSync Webmeji contract, then implement the smallest evidence-backed compatibility or element-edge improvement in the real source and verify it on ordinary desktop and touch pages.

## Maintenance

Update this page when the canonical source is resolved, the embedded API/config schema changes, GameSync Webmeji settings change, or a current external implementation materially advances the state of the art.
