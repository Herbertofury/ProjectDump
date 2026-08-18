# Master Desktop Pet Research Wiki

**Project Constellation ID:** `PRJ-020`
**Status:** RESEARCH BASE
**Confidence:** High
**Latest recovered lineage:** consolidated master containing v10, v14, v9 and v7 material

## Purpose

Master Desktop Pet Research is the durable research base for desktop-pet, screenmate, mascot, legacy-agent and adjacent interactive-character ecosystems. It is a research corpus and decision source, not a runtime application or library by itself.

The project exists to keep one consolidated body of verified ecosystem knowledge that downstream mascot projects can reuse without repeatedly rediscovering the same hosts, communities, character systems, historical branches, creator hubs and implementation references.

## Canonical master and lineage

Project Constellation preserves the canonical master name as:

`master desktop pet research.md`

The preserved primary consolidation date is **2026-04-01**. The recovered lineage says the master incorporates embedded v10 and v14 material plus retained v9 and v7 appendices.

The durable rule remains: **append future verified research to this master instead of creating drifting numbered copies**, unless a snapshot is intentionally versioned for archival reasons.

## Recovered content map

The preserved master is described as containing:

- an exhaustive ecosystem catalogue;
- a host map;
- creator, Linktree and hub research;
- a Discord/community map;
- a Microsoft Agent / ACS / Bonzi / Peedy / Clippy / Windows XP Search branch;
- a KinitoPET addendum;
- embedded v10 and v14 research passes;
- retained v9 and v7 appendices.

This wiki preserves those categories without inventing missing entries from a master file whose current bytes have not yet been recovered through the connected durable sources.

## Current evidence boundary

The active Project Constellation lineage still identifies PRJ-020 as a **RESEARCH BASE** and points to the consolidated v10/v14/v9/v7 master. The older cross-chat database independently preserves the same canonical master name, consolidation date and content categories.

The exact current bytes of `master desktop pet research.md` still have not been located in the connected ProjectDump tree or Drive evidence used for this pass. Therefore this page does not claim a current SHA-256, exact line count, complete link inventory or byte-for-byte verification of the master itself.

That is a source-recovery boundary, not a reason to split or recreate the research into a new master.

## How this research is meant to be used

A useful PRJ-020 research item should answer:

1. **What exists?** Identify a desktop pet, screenmate, agent, runtime, creator hub, community, preservation project or interaction model.
2. **Where does it run?** Record the verified desktop, browser, web, native or legacy host context.
3. **What behavior is distinctive?** Record the behavior, animation, interaction, state, speech, physics, community-content or compatibility idea that matters.
4. **How current is the evidence?** Record checked date, release/tag/commit when available, activity state and evidence class.
5. **What downstream project does it inform?** Link the finding to a mascot, Shimeji, ACS, Petz or other tracked implementation.

Research does not become an implementation claim merely because it appears in this master.

## Current downstream implementation lines

Use the project-specific wikis for runtime truth:

- [[Mascot / Screenmate Platform|PRJ-005-mascot-screenmate-platform]]
- [[ACS Agent Parity Runtime|PRJ-006-acs-agent-parity-runtime]]
- [[PF Magic Petz Runtime Integration|PRJ-007-pf-magic-petz-runtime-integration]]
- [[Shimeji Desktop|PCX-037-shimeji-desktop]]
- [[Shimeji Browser Extension|PCX-038-shimeji-browser-extension]]
- [[Webmeji|PCX-039-webmeji]]
- [[ACS Voice / Speech Runtime|PCX-060-acs-voice-speech-runtime]]
- [[Petz Shared Core|PCX-061-petz-shared-core]]

Downstream pages supersede PRJ-020 whenever they contain newer verified project-owned runtime evidence.

## Current Java/Shimeji compatibility benchmark

[DalekCraft2/Shimeji-Desktop](https://github.com/DalekCraft2/Shimeji-Desktop) remains a useful maintained modern-Java reference. The previously verified Project Constellation pass observed its main line at `dea89528c10c066626a09609f0e742cbe6405a8d`, with JDK 25 modernization, DPI work, cross-platform packaging and backward-compatibility goals.

Treat it as a compatibility benchmark, not as the user's canonical PRJ-020 master or the canonical implementation for every mascot host.

## New current architecture benchmark: NeurolingsCE Rust + Flutter

A materially newer ecosystem reference appeared in August 2026: [qingchenyouforcc/NeurolingsCE](https://github.com/qingchenyouforcc/NeurolingsCE). The repository was created on 2026-08-14 as a Rust + Flutter rewrite of the maintainer's earlier C++/Qt desktop-pet application.

The current source describes this architecture:

- Flutter `fluent_ui` manager;
- Rust crates for the Shimeji behavior engine, package handling, platform integration, runtime daemon, CLI, store and common contracts;
- QuickJS-backed conditions and **22 action types** in the behavior engine;
- `.mascot` plus legacy ZIP import and path-safety handling;
- native transparent desktop windows using `UpdateLayeredWindow` on Windows, X11/XFixes on Linux and AppKit hit-testing on macOS;
- HTTP plus local IPC between manager/runtime surfaces;
- CLI/HTTP/IPC contract compatibility goals with the preceding C++ implementation;
- `cargo test --workspace`, a headless smoke mode, deterministic packaging and SHA-256-oriented release handling.

The predecessor [NeurolingsCE-Qt](https://github.com/qingchenyouforcc/NeurolingsCE-Qt) documents v0.5.3 as a cross-platform C++17/Qt6 Shimeji-compatible line with package import/conversion, saved mascot compositions, autostart restoration, CLI, REST API, update integrity checks and multi-platform packages. Its README explicitly announces migration away from the Qt repository toward Rust.

### Evidence boundary

The Rust rewrite is fresh. Its README states that Linux/macOS window backends have cross-compile checks but still need real-machine visual validation, and that store/submission server plus GitHub App deployment remain external deployment work. It is therefore a **high-value architecture/parity benchmark**, not a drop-in authority for the user's mascot runtime.

### Smallest useful differential experiment

Build one representative compatibility corpus and run it against both the mature Qt v0.5.3 line and the Rust rewrite:

1. load the same Shimeji-ee resource packs;
2. compare all represented action/behavior selections and condition semantics;
3. compare `.mascot` and legacy ZIP import results;
4. compare drag, hit-testing, transparent-window behavior and multi-monitor placement on Windows;
5. compare CLI, HTTP and local IPC outputs field-for-field;
6. exercise startup/restart composition restoration;
7. compare failure behavior for malformed paths, invalid packs and unavailable assets;
8. preserve platform-specific behavior rather than normalizing away useful differences.

Acceptance requires parity for the chosen corpus before borrowing architecture, plus explicit regression tests for any behavior the user's existing mascot engines already support beyond NeurolingsCE.

## Research-entry schema

When the canonical master is recovered, new entries should use a consistent evidence shape:

| Field | What to record |
| --- | --- |
| Name | Exact project, product, creator, host or community name. |
| Category | Desktop pet, Shimeji, Microsoft Agent/ACS, Petz, web mascot, creator hub, community, preservation source, game/experience or other verified category. |
| Source | Direct primary URL when available. |
| Checked | Exact date the source was revalidated. |
| Version / commit | Release, tag, build, commit or other stable identity when exposed. |
| Host / platform | Verified runtime or host context. |
| Distinct capability | Behavior or idea that matters downstream. |
| Evidence class | Sourced fact, user-observed evidence, inference, proposal or historical note. |
| Maintenance state | Active, maintained, dormant, archived, historical, inaccessible or unresolved. |
| Downstream fit | Which tracked project should consume the finding. |
| Follow-up | Smallest useful verification or implementation experiment. |

Do not promote an inference into a sourced fact during consolidation.

## Maintenance workflow

1. **Resolve the real master before editing.** Search durable sources for the canonical filename and same-content variants. Compare embedded lineage, section coverage, hashes and substantive content, not timestamp alone.
2. **Preserve all prior passes.** New work extends the existing sections or adds a dated appendix. Older verified research remains historical evidence when superseded.
3. **Revalidate only load-bearing claims.** Recheck primary sources when an old claim affects a current decision.
4. **Keep source hierarchy explicit.** Prefer official repositories, releases, specs and maintainer sources for technical/current claims.
5. **Promote only implementation-relevant findings downstream.** PRJ-020 stays the broad research map; downstream projects own runtime decisions.
6. **Checkpoint the master, not another numbered fork.** Publish the same-name master, record its hash, and update Project Constellation after material additions.

## Quality and anti-drift gates

Before treating a research update as complete, verify that:

- the update was applied to the recovered canonical master rather than a convenient duplicate;
- prior v10/v14/v9/v7 material remains present unless a change is explicitly documented;
- new current claims have direct sources and checked dates;
- historical links are labeled rather than silently presented as current;
- source facts, user observations, inferences and proposals remain distinguishable;
- downstream implementation pages are linked when a finding has implementation consequences;
- no research-only item is described as shipping behavior without project-owned proof;
- the final master is stored durably with hash or equivalent byte-verification evidence.

## Troubleshooting and recovery

### Multiple master files exist

Do not select by modification time. Compare embedded versions, section inventory, v10/v14/v9/v7 coverage, unique research branches and hashes. Preserve unique material during reconciliation.

### A numbered v15/v16-style file appears

Treat it as a candidate snapshot until its unique material is reconciled into the canonical master.

### An old source link is dead

Preserve the original citation as historical evidence, then locate the project's official moved repository/site or trustworthy archive and record the replacement separately.

### A community claim conflicts with project source

Keep the community claim labeled as such and let current primary project evidence control technical/runtime claims.

### Research says a feature exists but a downstream runtime does not

The downstream project's actual runtime evidence wins. Keep the research item as inspiration/reference only.

## Exact next action

**Recover the exact `master desktop pet research.md` artifact, prove its lineage and hash, preserve the consolidated v10/v14/v9/v7 material, then append the NeurolingsCE Qt-to-Rust transition as a dated current architecture/parity case study. Run the differential mascot corpus before promoting any implementation idea into PRJ-005/006/007 or PCX-037/038/039/060/061.**
