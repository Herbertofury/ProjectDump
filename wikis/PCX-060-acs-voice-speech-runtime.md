# ACS Voice / Speech Runtime Wiki

**Project Constellation ID:** `PCX-060`  
**Status:** ACTIVE / TRACKED  
**Goal:** Preserve classic agent speech and voice interaction expectations in the modern mascot runtime using real speech/audio services, coordinated animation/state, interruption, cancellation, and truthful fallbacks.

## Purpose

This project covers the voice and speech layer associated with the ACS / Microsoft Agent compatibility track. Speech is not just text-to-audio. Classic agent behavior depends on request ordering, animation coordination, speech balloons, voice selection, interruption, cancellation, and state transitions.

A modern implementation must therefore preserve agent semantics while allowing real local or host speech engines behind explicit adapters.

## Recovered historical foundation

The durable ACS parity record preserves an existing foundation that included:

- ACS parsing;
- ACS-to-runtime conversion;
- spritesheet and audio export;
- `pack.acsAgent` metadata;
- state and return maps;
- voice and balloon metadata;
- queued playback, movement, speech, dragging, and idle transitions;
- Shimeji compatibility.

The same record identifies important speech-related gaps:

- true `Think()` behavior;
- request objects and queue semantics such as Wait, Interrupt, StopAll, and Get;
- classic Commands / Voice Commands behavior;
- speech recognition and voice grammar;
- deeper state semantics;
- lip-sync and audio timing;
- local STT/TTS and voice switching;
- inspector/parity tooling.

These are historical continuity requirements. During this pass, current indexed GitHub source for the ACS voice runtime was not resolved well enough to claim that these gaps are now implemented.

## Current source boundary

The connected GameSync repositories remain important integration hosts for mascot systems, but GitHub code searches during this pass did not resolve a current authoritative ACS voice implementation from them. The standalone current ACS voice source/worktree therefore remains unresolved.

Do not create a replacement speech subsystem merely because modern TTS/STT libraries exist. Resolve the owning runtime first, then adapt current engines behind the existing agent/request model.

## Required speech state model

A complete speech request should be able to carry or derive:

- agent identity;
- request ID;
- text or phoneme input;
- speech versus thought mode;
- selected voice/provider;
- rate/pitch/volume when supported;
- balloon behavior;
- animation/state to enter before or during speech;
- audio start/end timing;
- viseme/phoneme timing when available;
- completion/error/cancel status;
- interruptibility and priority;
- queued predecessor/dependency;
- return/idle state.

The queue is part of the product behavior. Swapping TTS engines must not change Wait/Interrupt/StopAll semantics.

## Current local speech-engine research

### Piper TTS

The current `OHF-Voice/piper1-gpl` release is **v1.7.0**, published 2026-08-15. The project provides local neural text-to-speech and release wheels for Windows, Linux, and macOS. Release assets expose SHA-256 digests, which makes exact engine/package identity verifiable.

Primary source: https://github.com/OHF-Voice/piper1-gpl

**Fit:** strong candidate for an offline/local TTS adapter where license/deployment and voice-model requirements fit the host.

**Boundary:** adopting Piper must not replace ACS request/state semantics, balloon behavior, or animation timing. It is a speech provider, not the agent runtime.

### whisper.cpp

`ggerganov/whisper.cpp` remains an actively maintained local speech-to-text implementation suitable for evaluating offline recognition and voice-command input.

Primary source: https://github.com/ggml-org/whisper.cpp

**Fit:** candidate recognition adapter for local speech recognition / command grammar experiments.

**Boundary:** free-form transcription is not equivalent to classic command grammar. Recognition results must flow through an explicit grammar/intent layer and must never trigger hidden actions without the same authorization/command rules as other inputs.

## Adapter architecture

Speech providers should sit behind a narrow capability contract instead of leaking provider-specific APIs into agent behavior.

Suggested TTS capabilities:

- enumerate voices;
- synthesize/play text;
- stop/cancel request;
- pause/resume if supported;
- return duration/timing metadata;
- expose phoneme/viseme timing if supported;
- report offline/online status;
- report deterministic provider/version identity.

Suggested STT capabilities:

- start/stop recognition;
- partial/final transcript;
- confidence;
- language/model identity;
- optional constrained grammar;
- cancellation;
- explicit microphone/error state.

Unsupported capabilities should remain explicit rather than emulated with fake success.

## Queue and interruption contract

At minimum the runtime must prove:

1. two speech requests preserve queue order;
2. Wait blocks until the referenced request completes;
3. Interrupt terminates or supersedes the correct request and produces the correct state transition;
4. StopAll cancels speech/audio/related queued work without leaving stale talking animation or balloon state;
5. cancellation propagates to the actual provider, not only the UI;
6. provider failure resolves the request truthfully and returns the agent to a valid state;
7. drag/move or explicit agent commands interact with queued speech according to the compatibility contract.

## Animation, lip-sync, and balloons

Speech must coordinate with visual state rather than playing as detached audio.

A testable implementation should track:

- talking-state entry before audible output;
- balloon visibility and text lifetime;
- audio start/end;
- viseme or mouth-frame timing where the provider/runtime supports it;
- transition back to idle/return state;
- cancellation cleanup;
- thought balloon path distinct from audible speech.

When precise viseme timing is unavailable, fallback animation must be labeled as approximate rather than presented as true lip-sync parity.

## Local-first and privacy behavior

A modern voice runtime should be able to run locally when configured for local engines. Cloud providers can remain optional adapters, but secrets/tokens must not be stored in project-brain exports, logs, or portable mascot packs.

Microphone use must be explicit and observable. Speech recognition should fail visibly when permission/device/model state prevents operation.

## Proposed engine-matrix experiment

Once the canonical ACS voice runtime is resolved, run one fixed request/animation fixture against:

- the current existing speech provider;
- Piper v1.7.0 as a local TTS candidate;
- whisper.cpp as a local STT candidate when recognition is in scope.

The fixture should measure:

- time to first audio;
- completion/cancellation latency;
- exact request ordering;
- interrupt/StopAll correctness;
- balloon cleanup;
- talking/idle animation transitions;
- provider failure behavior;
- voice switching;
- restart persistence of voice configuration;
- offline behavior.

Do not adopt an engine merely because synthesis quality is higher if queue/state correctness regresses.

## Anti-degradation rules

- Never replace ACS request semantics with direct `speak(text)` calls.
- Never report approximate lip-sync as classic parity.
- Never leave an agent in talking state after cancellation or provider failure.
- Never make a cloud credential mandatory for baseline speech when a local path is intended.
- Never let recognition trigger commands outside the explicit command/authorization model.
- Never flatten `Think()` into audible speech.
- Never claim voice parity until the real mascot runtime is exercised end to end.

## Acceptance test

A speech-runtime upgrade is ready only when the real owning runtime proves:

- queue ordering;
- Wait/Interrupt/StopAll behavior;
- cancellation reaches the actual audio provider;
- speech and thought paths remain distinct;
- balloons clean up correctly;
- agent animation/state returns correctly;
- configured voice survives restart when stateful;
- provider failure is visible and recoverable;
- local/offline mode works when selected;
- any STT grammar/commands are verified through the actual command path;
- no previously working mascot/ACS behavior regresses.

## Exact current next action

Resolve the canonical ACS voice/speech source and existing request queue first. Then prototype Piper v1.7.0 and whisper.cpp only as provider adapters behind that contract, with a deterministic queue/interruption/animation/restart fixture before any migration claim.
