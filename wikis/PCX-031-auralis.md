# Auralis Wiki

**Project Constellation ID:** `PCX-031`
**Status:** ACTIVE / TRACKED
**Current source boundary:** production build artifacts and implementation directives are recovered in durable project evidence; a canonical GitHub application repository has not yet been resolved.

## Purpose

Auralis is a production-grade Windows 11 spatial-audio application. The product goal is real per-application audio capture, routing, spatialization, recovery, and verification, not a simulated mixer or visual-only prototype.

The recovered master build directive requires the application to preserve the supplied Auralis UI while making every control functional and routing real applications such as Spotify, Opera GX, Discord, VLC, and games through a low-latency Windows audio engine.

## Current authoritative implementation contract

The newest directly recovered Auralis build directive specifies this recovery baseline:

- stable Rust **1.97.1**, edition 2024;
- Slint **1.17.0**;
- `windows` / windows-rs **0.62.2**;
- Rubato **4.0**;
- event-driven WASAPI;
- process-tree loopback capture through `ActivateAudioInterfaceAsync`;
- Microsoft Spatial Sound through `ISpatialAudioClient`;
- preallocated lock-free real-time buffers;
- a fail-open signed virtual endpoint or isolated WDK bridge for transparent per-application routing.

Recovered authoritative artifacts include:

- `MASTER_BUILD_PROMPT.md`;
- `IMPLEMENTATION.md`;
- `Auralis-Interactive-Preview.html`.

The preview is a visual/interaction reference. Its simulated process list, meters, CPU, and latency values are not runtime evidence.

## Current stack freshness, checked 2026-08-22

The recovered Auralis stack is already close to current and should **not** be churned merely to look newer. Qualification must preserve a known-good recovery baseline and change one toolchain axis at a time.

- The recovered directive pins **Rust 1.97.1**, but the current stable compiler is [Rust 1.98.0](https://blog.rust-lang.org/2026/08/20/Rust-1.98.0/), released August 20, 2026. Treat 1.97.1 as the recovery/compiler baseline and 1.98.0 as a separate compiler-qualification candidate after the source is recovered and the baseline build passes.
- Rust 1.98.0 adds explicit algebraic floating-point methods such as `algebraic_add` and `algebraic_mul`. The Rust release notes state that these operations may be reordered and are non-deterministic. **Do not adopt them in Auralis DSP merely because the compiler exposes them.** Real-time audio code needs a deliberate numerical-quality experiment proving bounded gain, finite output, phase behavior, loudness/true-peak behavior, repeatability expectations, and measured CPU benefit before any algebraic/fast-math-style transformation is accepted.
- The recovered directive pins **Slint 1.17.0**, while the current stable patch release remains [Slint 1.17.1](https://github.com/slint-ui/slint/releases/tag/v1.17.1), released July 7, 2026. It fixes several startup/runtime crashes and UI correctness issues, including `TextEdit` cursor scrolling, conditional `Timer.restart()` panic, struct-field two-way binding crashes, and other rendering/windowing defects. Treat 1.17.1 as a patch-level qualification candidate after the baseline build is proven.
- [`windows` 0.62.2](https://docs.rs/crate/windows/latest) remains the current documented Rust-for-Windows crate line used by the recovered directive.
- [Rubato 4.0.0](https://github.com/HEnquist/rubato) remains the current major release and explicitly documents real-time-safe processing without allocations during processing.

### Qualification order

Do not combine compiler and UI-runtime upgrades into one unexplained rebuild. Use this sequence:

1. recover and build the exact Rust 1.97.1 + Slint 1.17.0 baseline;
2. hold Rust at 1.97.1 and qualify Slint 1.17.1;
3. return Slint to the chosen accepted state and qualify Rust 1.98.0 separately;
4. only then test a combined accepted toolchain;
5. record exact `rustc -Vv`, Cargo lockfile hash, Slint version, generated artifact hash, and runtime acceptance evidence for every lane.

This keeps a compiler regression distinguishable from a UI-runtime regression and prevents a fresh toolchain from silently becoming the recovery authority.

### Decision

Preserve Rust 1.97.1 / Slint 1.17.0 / windows-rs 0.62.2 / Rubato 4.0 as the **recovery baseline** until canonical source is found and built. Then qualify Slint 1.17.1 and Rust 1.98.0 as independent low-risk toolchain lanes. A successful newer build does not erase the recovered baseline.

Slint 1.17's MCP accessibility/input/screenshot capability remains a useful **test/debug adapter candidate**, not part of the audio signal path. If adopted, isolate it to development/verification surfaces and never require it for real-time audio operation.

## Capture and routing contract

Auralis must use real Windows audio/session APIs.

Required behavior:

- wrap `ActivateAudioInterfaceAsync` for process-loopback capture;
- treat a target process and relevant child/helper processes as one logical application where appropriate;
- enumerate active Core Audio render sessions;
- show active audio applications by default, with a separately controlled all-processes view;
- provide an **Auralis Input** virtual render endpoint and paired engine capture path when the chosen routing architecture requires it;
- preserve the prior endpoint for immediate rollback;
- fail open to the user's default output device when the Auralis engine, service, or helper fails;
- never duplicate the original audio stream during routing;
- recover after device changes, default-device changes, app relaunch, sleep/resume, format changes, or endpoint failure.

Microsoft's Windows audio APIs and the recovered project contract are the source of truth. Generic cross-platform audio abstractions may be used only where they do not hide session routing, process-loopback, endpoint-role, or Spatial Sound behavior Auralis depends on.

## Real-time engine contract

The production engine should use:

- event-driven shared-mode WASAPI as the normal path;
- an advanced exclusive-mode path only where explicitly supported and verified;
- one capture graph per selected logical application/process tree;
- one shared output graph per endpoint;
- preallocated SPSC buffers;
- immutable graph snapshots swapped atomically at safe buffer boundaries;
- source/sink clock-drift measurement;
- Rubato asynchronous resampling only when clock divergence requires it;
- device hot-plug and format renegotiation recovery;
- MMCSS `Pro Audio` scheduling with correct restoration on shutdown.

### Hard real-time rule

The audio callback must never allocate, lock, log, perform disk/network I/O, or wait on UI/service work. Any new library or feature that violates that rule is a regression regardless of convenience.

## DSP quality contract

The recovered production checklist requires replacement of starter/demo DSP with measured production behavior, including:

- phase-coherent stereo widening;
- energy-preserving 5.1 and 7.1 upmixing;
- 7.1.4 spatial beds;
- tested Linkwitz-Riley crossovers;
- center extraction;
- transient-aware surround decorrelation;
- bass management and LFE headroom;
- true-peak limiting with look-ahead/oversampling;
- EBU R128 loudness guard;
- SOFA HRTF loading, interpolation, and partitioned convolution;
- room simulation as a separate optional late-reverb bus;
- mono compatibility/correlation metering;
- loudness-matched A/B.

Every DSP block needs bounded-gain and finite-output tests. Subjective enhancement must not be confused with numerical correctness.

### Compiler-sensitive DSP gate

Any compiler upgrade, target-feature change, LTO change, SIMD rewrite, or use of algebraic floating-point operations must rerun the deterministic DSP fixture set. At minimum record:

- impulse response and channel-matrix outputs;
- silence/denormal behavior;
- finite-output and bounded-gain properties;
- true-peak and loudness deltas;
- phase/correlation metrics;
- resampler drift behavior;
- callback CPU distribution and underrun count;
- exact compiler and build flags.

Performance wins are accepted only if the audio-quality and recovery gates stay within defined tolerances. Do not trade determinism or numerical safety for an unmeasured compiler optimization.

## Microsoft Spatial Sound

Auralis should detect endpoint support through `ISpatialAudioClient` and expose spatial modes only when the selected system endpoint reports them.

The recovered contract calls for:

- static objects for a 7.1.4 bed;
- dynamic objects only when motion provides a real benefit;
- truthful presentation of Windows Sonic, Dolby Atmos, and DTS availability;
- no claim that Auralis itself performs licensed Dolby/DTS encoding when the corresponding system component is not active.

## UI contract

The recovered interactive preview establishes the intended visual baseline:

- left navigation for Live Mixer, Profiles, Devices, Acoustics, and Diagnostics;
- active-app mixer rows;
- per-app spatial mode and intensity;
- draggable soundstage sources;
- room/focus controls;
- Stereo / 7.1 / 7.1.4 quick modes;
- headphone calibration;
- master engine/bypass control.

The real product must preserve that visual identity while replacing every simulated value and placeholder behavior with real engine state.

Additional recovered requirements include:

- executable-hash rules and child-process inheritance;
- per-app presets/profile fallback;
- speaker layout/channel/phase tests;
- presets for music, movies, games, voice chat, browser video, and low-latency competitive use;
- expert controls behind an advanced surface;
- tray mixer;
- global bypass/profile/A-B hotkeys.

## Reliability, security, and recovery

Required safeguards:

- versioned atomic configuration with backup/migration;
- signed application, helper/service, endpoint package, and updater where applicable;
- UI process remains non-elevated;
- endpoint/driver installation lives in a narrowly scoped elevated helper;
- crash-safe bypass and watchdog recovery;
- privacy-safe diagnostics outside the callback;
- no microphone capture unless explicitly selected;
- no recording/transmission of captured application audio as an implicit side effect;
- clean uninstall restores routing and removes the virtual endpoint.

## Verification gate

Auralis is not complete because the preview renders or because the audio engine compiles.

Required proof includes:

1. unit tests for channel matrices, filters, limiter stability, denormals, and silence;
2. property tests for finite output and bounded gain;
3. measured loopback-impulse latency;
4. device-switch, default-device, sleep/resume, app-relaunch, and sample-rate recovery;
5. 24-hour stress testing;
6. real Spotify capture/routing/spatialization/bypass/restore;
7. real Opera GX and Chromium child-process-tree behavior;
8. real Discord and VLC behavior;
9. representative game behavior;
10. protected-media failure behavior where capture is restricted;
11. clean rollback/uninstall proof;
12. no duplicated audio, persistent glitches, or meaningful idle CPU use introduced by the engine;
13. compiler/toolchain qualification evidence when moving away from the recovered Rust 1.97.1 baseline.

## Smallest useful current experiment

Once the canonical source repository/worktree is resolved:

1. verify Rust/Slint/windows-rs/Rubato lockfile identity against this recovered directive;
2. build the recovered Rust 1.97.1 + Slint 1.17.0 baseline without changing dependencies;
3. enumerate active Core Audio sessions;
4. implement or verify one process-tree loopback capture path;
5. exercise default-device switching and process relaunch;
6. record latency, underruns, recovery time, exact build hash, and DSP fixture results;
7. hold Rust at 1.97.1 and qualify Slint 1.17.1;
8. qualify Rust 1.98.0 separately with the accepted Slint state and rerun compiler-sensitive DSP fixtures;
9. only then evaluate the virtual-endpoint routing layer.

This isolates the riskiest Windows audio fundamentals and prevents compiler/UI changes from being conflated before DSP or broader UI expansion.

## Current blocker

The production repository/worktree containing the executable Rust implementation has not yet been resolved from the connected GitHub surface. Durable project artifacts prove the implementation contract but are not enough to claim a runnable build exists.

Do not initialize a replacement Auralis repository merely because the connected source path is unresolved. Search and reconcile the project-owned source first.

## Exact next action

Resolve the canonical Auralis source repository/worktree and reconcile it against `MASTER_BUILD_PROMPT.md`, `IMPLEMENTATION.md`, and the interactive preview. Preserve Rust 1.97.1 + Slint 1.17.0 as the first build baseline. Then qualify Slint 1.17.1 and Rust 1.98.0 in separate lanes before considering any larger dependency, DSP, or architecture migration.

## Wiki maintenance

Update this page when the canonical source repository is located, the stable Rust/Slint/windows-rs/Rubato versions change, the virtual endpoint/WDK architecture is selected, real application routing becomes verified, DSP stages become measured, installer/signing behavior becomes proven, or a new latest-good runtime build is established. Recheck compiler-sensitive DSP qualification whenever the Rust toolchain changes.