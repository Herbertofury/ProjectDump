# ProjectDump Durable Continuity Contract

This repository is the durable cross-project source of truth for project work and skills.

## Source priority

1. GitHub `Herbertofury/ProjectDump` for versioned project state, memory, manifests, catalogs, handoffs, policies, and text/code continuity.
2. Connected Google Drive for complete release artifacts, archives, binaries, exported project brains, and byte-verifiable backups.
3. ChatGPT File Library is not a normal continuity source unless the user explicitly asks to use it.
4. Sandbox/container files are ephemeral working copies only.

## Global behavior

Resolve current canonical state from GitHub and Drive before mutating ongoing work. Preserve user edits and version lineage. Never promote a candidate by filename or timestamp alone. Never reconstruct or downgrade a newer state merely because an older copy is easier to access. Checkpoint meaningful versionable state to GitHub and publish appropriate complete artifacts to Drive.

## Tooling support

For project work, if an additional development tool, runtime, profiler, renderer, editor, decompiler, test harness, launcher, SDK, or other utility would materially improve correctness, speed, fidelity, compatibility, or verification, ask the user for that tool instead of silently accepting a weaker workflow. For Minecraft projects, reusable development utilities created by ChatGPT belong in the canonical Google Drive `Minecraft Dev Kit` folder, preferably under `AI Dev Tools`; project-specific outputs stay with their project. Never request account secrets, launcher tokens, browser cookies, or credentials as tooling inputs.

## Project Constellation

Project Constellation is **ACTIVE** and runs in **NORMAL_OPERATION**. Its durable control state lives under `project-constellation/` in this repository plus current artifacts in Google Drive. Missing sandbox files never trigger recovery or restoration mode. Recovery/restoration is fallback-only after an actual verified integrity failure. Preserve exactly **63 tracked projects** unless the user explicitly changes the list. The older 25-project database is historical source detail only and cannot replace the current 63-project catalogue. Future passes read `project-constellation/HANDOFF.md` and machine-readable state first, compare artifact hashes against `lastAutomationHash`, preserve newer user edits, then continue normal research and product improvement.

## Skills

Every skill and skill-driven workflow follows the same durable-source rule. Keep versionable continuity state in GitHub and appropriate complete artifacts in Google Drive. Do not make ephemeral sandbox copies the sole checkpoint.
