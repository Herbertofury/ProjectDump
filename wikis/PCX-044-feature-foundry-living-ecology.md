# Feature Foundry Living Ecology Wiki

**Project Constellation ID:** `PCX-044`
**Status:** ACTIVE / TRACKED
**Current strongest verified ecology artifact:** `Feature Foundry V33 - Recovered Ecology`

## Purpose

Living Ecology is the Feature Foundry subsystem for worlds that behave like coherent systems rather than decorative backgrounds. It governs theme-native object behavior, world signals, reactions, memory, weather/time/audio context, presentation tiers, motion/accessibility equivalence, and host-adapter behavior.

## Current verified V33 ecology state

The durable `V33 FINAL_READY` checkpoint records a rebuild from the verified V25 runnable base plus V30/V31 verification lineage and the V32 interaction/ecology specification. It explicitly preserves non-regression and no-artificial-caps guarantees.

Verified V33 ecology-facing capabilities include:

- Theme-aware Library Ecology Lab;
- Ecology Director world modes and transition depth 0-5;
- causal world-signal bus and replay history;
- chronological, interaction, and authored-world memory channels;
- Efficient/Balanced/High/Ultra/Cinematic presentation tiers with content parity;
- advanced optical/spatial depth composition;
- soundtrack/provider mapping hub with six provider mappings;
- five host adapters;
- persistent state;
- reduced-motion/performance equivalence.

The checkpoint records 101/101 V33 runtime assertions, 117/117 legacy runtime assertions, 22/22 V33 static assertions, 59 legacy controls with zero missing handlers, zero console/page errors, fresh extraction success, and remote byte verification of the V33 ZIP.

## Ecology behavior contract

Living-world behavior should remain causal and inspectable. A useful event path is:

`user/system input -> world signal -> affected entities/objects -> bounded reaction -> persisted/replayable evidence`

Distinct interaction categories such as press, drag, collision, recovery, time/weather change, soundtrack change, and authored transitions should remain distinct paths rather than collapsing into generic animation toggles.

## No-degradation requirements

- No viewport-only admission, virtualization, hidden entity caps, or reduced world content in lower performance tiers.
- Presentation tiers may reduce cost, effects, or sampling strategy only when the same authored world content, state, and interaction semantics remain available.
- Reduced-motion mode must preserve functionality and state transitions while changing presentation behavior.
- Recovery must not silently discard world history or authored state.
- Host adapters must preserve world identity and state semantics rather than implementing separate divergent mini-engines.

## Current technology research

PixiJS `8.18.1` is the current stable PixiJS release and remains a strong 2D rendering candidate where Feature Foundry uses or evaluates Pixi-backed surfaces.

Rapier's JavaScript package line is still `0.19.3`, but the dedicated `dimforge/rapier.js` repository was archived in July 2026 while the Rust `dimforge/rapier` repository remains active. Treat that as a maintenance signal: do not deepen coupling to the archived JS repository without a deliberate ownership strategy. If deterministic physics is needed for replayable ecology, evaluate the deterministic Rapier package behavior behind an adapter and verify cross-host replay rather than binding ecology semantics directly to a physics engine API.

## Exact next experiment

Create a fixed V33 ecology replay fixture covering at least press, drag, collision, recovery, a world-mode transition, a presentation-tier change, reduced motion, persistence/reload, and one host-adapter round trip. Record identical semantic state/results across supported presentation tiers and fail the test if any tier drops authored entities or changes causal outcomes unexpectedly.

## Acceptance test

- same authored entity/object count across tiers;
- same persisted semantic state across tiers;
- bounded, deterministic-enough replay for authored interactions;
- no dead controls;
- no hidden/off-screen content loss;
- reduced-motion behavior remains functional;
- reload/restart restores the expected world state;
- host adapter preserves identity/state;
- runtime logs contain no new material errors.

## Wiki maintenance

Update this page when the verified ecology checkpoint changes, the event/signal model changes, host adapters change, rendering/physics ownership changes, or new anti-regression evidence supersedes the V33 matrix.