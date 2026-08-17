# PRJ-001 - Project Compass Orchestrator / Project Second Brain

**Project Constellation ID:** `PRJ-001`  
**Status:** ACTIVE continuity system  
**Historical recovered release:** Skill v3.3.0, Artifact Library and Storage Manager  
**Current source boundary:** the historical project-brain contract is preserved in the durable cross-chat database, while the exact current installable skill/bundle bytes are not presently resolved as a canonical GitHub or Drive artifact.

## Purpose

Project Compass Orchestrator is the project-brain and execution-governance lineage that preserves project identity, progress, research, artifact provenance, recovery state, and agent execution rules across chats and tools. Its key requirement is continuity without pretending that ephemeral session memory is durable state.

The historical v3.3.0 record remains useful lineage, but it must not be treated as proof that the currently installed project-brain skill is still byte-identical to that release. Current ProjectDump/Drive control-plane evidence has evolved beyond the old snapshot and now provides stronger durability mechanisms.

## Preserved historical contract

The recovered v3.3.0 line includes:

- project-owned `.agents-memory/` state;
- a durable cross-project catalog and Markdown database;
- artifact-library cataloging and project bundles;
- hash-proven duplicate handling and reversible quarantine;
- identity checks and handoffs;
- research memory and artifact reconciliation;
- controlled learning and anti-poisoning rules;
- portable AGENTS exports;
- `skill.zip`, `AGENTS-workflow-bundle.zip`, `AGENTS-all-in-one.md`, `AGENTS-modular.md`, `Feature-Foundry-Project-Brain.zip`, `USER-PROJECTS-DATABASE.md`, project catalogs, and library catalogs as known lineage artifacts.

Historical preservation rules remain valid: installed skill packages do not silently update themselves, repository memory is separate from an installed skill, cross-chat durability requires a real durable store, and same-name artifacts retain lineage rather than being overwritten by timestamp alone.

## Current durable control plane

Current Project Constellation operation resolves two durable authorities:

1. `Herbertofury/ProjectDump` for source-controlled project state, wikis, checkpoints, manifests, and automation state.
2. The dedicated Project Constellation Google Drive folder for byte-verifiable presentation artifacts, archives, and active checkpoints.

The current Drive `PROJECT-CONTINUITY-SOURCE-OF-TRUTH.md` explicitly establishes GitHub plus Drive as the default working source of truth and treats sandbox/container files as ephemeral working copies.

## New verified wiki durability path

ProjectDump now has a verified source-controlled GitHub Wiki publication path.

Current user-authored source documents:

- `wikis/` is the canonical wiki source directory;
- `tools/github-wiki/wiki-sync.sh` publishes the complete wiki source set;
- `.github/workflows/sync-github-wiki.yml` automates publication;
- Ferrum supplies the one-time first-page bootstrap when a `.wiki.git` remote is not initialized;
- after publication, the sync flow fresh-clones the real wiki Git repository and byte-compares it to the source tree.

The user also exercised create, edit, and delete lifecycle operations before documenting the workflow. This is a meaningful evolution of the project-brain contract because the human-readable wiki can now be a verified projection of source-controlled state instead of an independent hand-maintained copy.

## Anti-drift rule

ProjectDump `wikis/` is source; the GitHub Wiki is a published mirror. A successful page render is not sufficient proof. Publication should remain incomplete until the remote wiki is fresh-cloned and compared to source.

Drive remains a separate durability channel. Wiki sync does not replace the required Drive checkpoint/artifact path.

## Current gap

The exact newest installable Project Brain Orchestrator skill package and portable AGENTS bundle are not currently exposed as canonical GitHub/Drive bytes in the inspected state. Therefore:

- preserve v3.3.0 as historical lineage;
- do not claim it is the current installed version;
- do not regenerate a replacement package from memory;
- resolve the current installable package/bundle before a skill release or migration claim.

## Project Constellation improvement derived from this pass

Add a read-only **Mirror Health** lens that reports, for each durable projection:

- source authority;
- last source commit/hash;
- last publish result;
- remote verification method;
- verified remote commit/hash when available;
- stale/missing status;
- exact recovery action.

The lens must never mutate project content or turn a publish acknowledgement into verification. It should expose GitHub source, GitHub Wiki mirror, Drive checkpoint/artifact state, and presentation-publication debt separately.

## Acceptance for the Mirror Health experiment

- ProjectDump source and GitHub Wiki mirror can be compared without editing either.
- A source-only change is visibly marked as unpublished until wiki verification completes.
- A GitHub-only checkpoint is not shown as fully durable when its Drive copy is missing or stale.
- All 63 tracked projects remain available; Sports Group Hub remains absent.
- User edits always outrank generated mirror state.

## Exact current next action

Resolve the newest installable Project Brain Orchestrator/AGENTS bundle bytes and record their version/hash/source lineage. Until then, keep the v3.3.0 record as historical evidence while using the current GitHub + Drive control plane and verified wiki-sync path for durable continuity.

## Wiki maintenance

Update when the current skill/bundle is resolved, the AGENTS policy package changes, the project catalog format changes, wiki publication verification changes, or the GitHub/Drive durability contract changes.