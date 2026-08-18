# Project Constellation Wiki

**Project Constellation ID:** `PCX-036`  
**Status:** ACTIVE / NORMAL_OPERATION  
**Canonical repository:** [Herbertofury/ProjectDump](https://github.com/Herbertofury/ProjectDump)  
**Canonical repository path:** `project-constellation/`  
**Canonical Drive folder ID:** `1mUSeFlumpIOBtVCmlwbhN11kChRsdblV`  
**Current reviewed main base:** `4335d671d238bb9a85bfc6e1c4472e75bb4ffc8c`  
**Tracked-project invariant:** exactly 63 projects.

## Purpose

Project Constellation is the human-facing continuity and second-brain control plane over the user's project portfolio. It answers two immediate questions without discarding the deeper evidence behind them:

1. Where did work stop?
2. What exact action happens next?

It is not a replacement for project-owned source, `.agents-memory`, Project Compass, release artifacts, or runtime proof. It is the fast synchronized mirror that points back to those authorities.

## Current durable architecture

The current control plane is distributed deliberately across several durable surfaces.

### GitHub

`Herbertofury/ProjectDump` stores versioned continuity state, machine-readable checkpoints, wikis, governance, and research/evidence records. Current important files under `project-constellation/` include:

- `Project-Constellation-Automation-State.json`
- `Project-Constellation-Evidence-Coverage.json`
- `Project-Constellation-Publication-Debt.json`
- `Project-Constellation-Technology-Radar.json`
- `Project-Constellation-Project-Catalog.json`
- `Project-Constellation-Research-Suggestions.json`
- timestamped evolution checkpoints

The project wiki directory contains detailed project-specific documentation and should increasingly replace vague catalogue summaries with source-backed evidence.

### Google Drive

The dedicated Project Constellation Drive folder stores the byte-oriented continuity artifacts and the ACTIVE CHECKPOINT. The active checkpoint explicitly classifies Project Constellation as `ACTIVE`, `NORMAL_OPERATION`, and not in recovery mode.

The four permanent presentation/recovery surfaces remain first-class artifacts:

- `Bert_Project_Constellation_Quick_View.html`
- `Bert_Project_Constellation_Recovery_Command_Center_Full_Wiki.html`
- `Bert_Project_Second_Brain_Website.zip`
- `Bert_Project_Wiki_Pack.zip`

### Presentation model

The Quick View remains a zero-setup single HTML surface with local state, continuity lenses, search, Today/Review behavior, change tracking, research display, and snapshot import/export.

The full master/recovery HTML retains the deeper project history and lineage needed when a compact card is not enough.

The PWA/website line may add richer storage and workflows, but it must never become a reason to remove the permanent single-file Quick View.

## Authority order

When sources disagree, use this order:

1. current explicit user correction or edit;
2. current canonical project repository/runtime evidence;
3. project-owned durable memory and Compass evidence;
4. current Project Constellation machine record;
5. older handoffs, exports, presentation snapshots, and historical summaries.

A newer timestamp or larger filename is not enough to supersede a known-good state.

## Anti-degradation contract

Project Constellation must never improve its UI or speed by losing project content. In particular:

- keep all 63 projects available;
- preserve user edits, project history, requirements, blockers, research, artifact hashes, and source lineage;
- never use viewport culling, virtualization, hidden caps, or incomplete datasets as a shortcut;
- never regenerate presentation artifacts from an older source if doing so would discard later evidence;
- never promote a new `lastAutomationHash` until remote publication is byte-verified.

## Current publication-debt state

The current byte-verified Drive presentation artifacts remain trustworthy, but they predate later hourly evidence merges. A prior regenerated candidate line was not durably available to the current runtime. Because rebuilding directly from the older Drive presentation bytes would lose later evidence, Project Constellation correctly kept that debt open rather than promoting a degraded replacement.

This pass materializes a current 63-record machine-readable catalog and current technology/research radar as a stronger regeneration source. Presentation debt remains open until the complete presentation line is regenerated from this no-data-loss source, published, and remotely verified.

## Current technology research

### Optional SQLite WASM / OPFS PWA mirror

Checked 2026-08-17. The current [`@sqlite.org/sqlite-wasm`](https://www.npmjs.com/package/@sqlite.org/sqlite-wasm) release is `3.53.0-build1`. SQLite's current WASM persistence documentation describes OPFS-backed VFS choices including `opfs`, `opfs-sahpool`, and `opfs-wl`, with different concurrency, header, and portability tradeoffs. The package also documents the older Worker1/Promiser1 APIs as deprecated.

**Proposal:** test SQLite WASM only as an optional PWA persistence adapter. Keep the single-file Quick View dependency-free and keep localStorage plus snapshot import/export as the universal baseline.

**Why it may help:** a PWA-only SQLite/OPFS mirror could provide indexed project/research history, schema migrations, and durable local querying without compromising the permanent HTML recovery surface.

**Acceptance gate:** all 63 records and user state round-trip exactly, multi-tab behavior is explicit, unavailable OPFS falls back safely, and the Quick View continues to work unchanged without WASM.

Current SQLite OPFS documentation: https://sqlite.org/wasm/doc/trunk/persistence.md

## Exact current next action

Use the newly materialized 63-record machine catalog plus current project wikis/evidence as the source for the next coherent presentation regeneration. Regenerate all presentation/catalog artifacts together, compare against user edits, validate the 63-project and no-loss invariants, publish to GitHub and Drive, and promote hashes only after remote byte verification.

## Verification checklist

Before claiming a Project Constellation evolution is complete:

- canonical GitHub main and Drive ACTIVE CHECKPOINT were reread;
- exactly 63 project records are present;
- current project-owned evidence supersedes stale summary fields;
- JSON parses;
- generated HTML JavaScript parses;
- every project retains goal, requirements, stop point, next action, and history;
- wiki links resolve;
- ZIP integrity passes;
- real browser behavior is exercised when a presentation build is promoted;
- Drive/GitHub publication is reread or redownloaded and byte-verified;
- `lastAutomationHash` changes only after that proof.

## Maintenance

Update this wiki when the machine schema, canonical storage model, presentation line, evidence authority rules, research/evolution workflow, or publication verification process changes. Preserve prior checkpoints as history rather than rewriting them away.
