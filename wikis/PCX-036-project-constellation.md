# Project Constellation Wiki

**Project ID:** PCX-036  
**Canonical state:** ACTIVE / NORMAL_OPERATION  
**Verified product line:** v0.5.0  
**Canonical repository:** `Herbertofury/ProjectDump`  
**Canonical repository path:** `project-constellation/`  
**Canonical Drive folder:** `Project Constellation`, folder ID `1mUSeFlumpIOBtVCmlwbhN11kChRsdblV`

## What Project Constellation is

Project Constellation is the human-facing cross-project continuity and resume surface. Its job is to keep the tracked project catalog, exact next actions, stop points, provenance, research decisions, user checkpoints, and presentation artifacts synchronized without losing user edits or silently replacing newer state with older recovery material.

The active v0.5.0 line contains exactly **63 tracked projects**. `Sports Group Hub` is deliberately absent and must stay absent unless Bert explicitly changes the catalog. The older 25-project database is historical evidence only and must not replace the current 63-project catalog.

## Canonical startup order

Use this order before modifying anything:

1. Read repository root `AGENTS.md`.
2. Read `project-constellation/AGENTS.md`.
3. Read `project-constellation/HANDOFF.md`.
4. Read `project-constellation/PROJECT.json` and `STATUS.json`.
5. Read `project-constellation/Project-Constellation-Automation-State.json`.
6. Read `project-constellation/ACTIVE-CHECKPOINT.json`.
7. Read the Drive-published `Project-Constellation-Project-Catalog.json`.
8. Locate same-named presentation artifacts in the canonical Drive folder and compare their current hashes against `lastAutomationHash` before editing.
9. If a newer user-edited artifact exists, use it as the merge base and preserve the user's state additively.
10. Continue normal operation. Missing sandbox/container files alone are not a recovery condition.

## Canonical state files

| File | Purpose |
| --- | --- |
| `AGENTS.md` | Repository-wide durable continuity contract. |
| `project-constellation/AGENTS.md` | Project Constellation-specific operating contract and hard invariants. |
| `project-constellation/HANDOFF.md` | Human-readable active handoff and current product summary. |
| `project-constellation/PROJECT.json` | Machine-readable project identity. |
| `project-constellation/STATUS.json` | Machine-readable current status. |
| `project-constellation/ACTIVE-CHECKPOINT.json` | Verified checkpoint, artifact hashes, publication IDs, and validation evidence. |
| `project-constellation/Project-Constellation-Automation-State.json` | Automation merge base, last automation hashes, research cursor, validation, and next-run contract. |
| Drive `Project-Constellation-Project-Catalog.json` | Canonical 63-record project catalog used by the presentation layer and automation. |

## Current v0.5.0 product behavior

The verified handoff records these v0.5.0 capabilities:

- 63 project records with Sports Group Hub absent.
- Quick Checkpoint support.
- Resume Capsules.
- Ideas & Research decisions.
- Snapshot export/import.
- Permanent zero-setup Quick View.
- Persistent Continuity Lenses.
- Today queue.
- Review Queue with reviewed/defer controls.
- Changed Since Last Visit.
- Legacy v0.4.x local-state migration.
- Research promotion that can set the exact next action.
- 63 standalone project wiki pages in the published Wiki Pack.
- A self-contained master continuity command center.

These capabilities are presentation/runtime behavior from the v0.5.0 artifact line. Do not remove them during documentation or catalog maintenance.

## Published presentation artifacts

The current automation state identifies these durable Drive artifacts:

| Artifact | Current Drive ID | Purpose |
| --- | --- | --- |
| `Bert_Project_Second_Brain_Website.zip` | `10mkzVaIjkHhDP5e93-UFqzjS57XEHiHC` | Packaged Project Constellation website/PWA. |
| `Bert_Project_Constellation_Quick_View.html` | `1up9K9DTdUVg_fnW-v8bHVAIbjEWX7l77` | Zero-setup single-file Quick View. |
| `Bert_Project_Constellation_Recovery_Command_Center_Full_Wiki.html` | `1yMbhEumf5-ie8Ack2Zj1dQpPvkrdlAbO` | Self-contained master continuity command center. |
| `Bert_Project_Wiki_Pack.zip` | `1AUEcHVMLFNePTXu2I_ZYDxccCqawAhSZ` | Pack containing the per-project HTML wiki pages and index. |

The automation state records full remote re-download/hash verification for these current durable copies.

## How to use Project Constellation

### Resume a project

1. Open Quick View or the master command center.
2. Find the project by ID/name.
3. Read its goal, requirements, latest/version evidence, exact next action, stop point, blocker, and continuity history.
4. Prefer newer project-owned evidence over the catalog summary when the two differ.
5. Preserve user notes/checkpoints and prior completed work when refining the record.
6. When the project materially changes, update its exact next action and stop point rather than replacing the entire history.

### Triage work

Use Continuity Lenses, Today, Review Queue, and Changed Since Last Visit to narrow the 63-project catalog to the projects that actually need attention. Review/defer state is part of the useful continuity state and should be preserved across artifact updates.

### Promote research into work

Research suggestions are not implementation facts. Promote a suggestion only when it is accepted, then set the exact next action to the accepted experiment/work item. Preserve dismissed and deferred research decisions so they are not repeatedly re-proposed without new evidence.

### Move state between environments

Use the snapshot export/import flow for portable state. Repository/Drive continuity remains the durable source of truth; ephemeral sandbox copies are working copies only.

## How to modify Project Constellation safely

### Catalog edits

When changing a project record:

1. Resolve the current Drive catalog and compare its hash/version with `lastAutomationHash`.
2. Confirm whether a newer user-edited artifact exists.
3. Merge additively from the newest valid state.
4. Preserve the 63-project invariant unless Bert explicitly changed the tracked-project list.
5. Keep Sports Group Hub excluded unless Bert explicitly reverses that decision.
6. Preserve project IDs whenever identity is stable.
7. Preserve user notes, checkpoints, exact stop points, research decisions, and completed-work history.
8. Clearly label unresolved or reconstructed metadata rather than presenting it as verified implementation fact.

### Presentation edits

Do not treat the Quick View, master command center, website ZIP, or Wiki Pack as disposable generated output. If presentation behavior changes, preserve the v0.5.0 functionality listed above unless the change is intentional and verified.

### Documentation edits

Project wikis should separate:

- verified current source/runtime facts;
- durable historical continuity evidence;
- unresolved identity/source gaps;
- current exact next action;
- known blockers;
- modification/build/test instructions only when they are verified from the project source.

Never invent build commands or architecture details simply to make a page appear complete.

## Verification before publication

The current checkpoint records successful static validation for:

- exactly 63 records;
- Sports Group Hub absence;
- JavaScript syntax;
- JSON parsing;
- goal/requirements/history presence;
- research contract rendering data;
- local wiki links;
- artifact hash agreement;
- ZIP integrity;
- full remote Drive re-download/hash agreement.

Browser interaction was attempted with Chromium, but the run timed out after D-Bus initialization failures and produced no DOM. Therefore browser interaction success is **not** part of the verified v0.5.0 evidence.

## Publication workflow

For a material update:

1. Update the versionable state in `Herbertofury/ProjectDump`.
2. Build/update only the presentation artifacts that materially changed.
3. Publish the canonical same-name artifacts to the dedicated Drive folder.
4. Re-download or otherwise obtain trustworthy remote bytes and verify SHA-256/size.
5. Update `lastAutomationHash`, publication IDs, validation evidence, research cursor, and checkpoint metadata only after remote verification succeeds.
6. Keep historical recovery evidence classified as historical. Do not promote the historical recovery checksum as the active checkpoint.

## Troubleshooting

### A sandbox file is missing

Do not enter recovery mode automatically. Read GitHub `project-constellation/` and the canonical Drive folder first. Recovery is fallback-only after an actual integrity failure.

### The Drive artifact hash differs from `lastAutomationHash`

Treat the mismatch as potential newer user work until proven otherwise. Compare version, modified evidence, content, and lineage. Merge from the newer valid artifact instead of overwriting it.

### The catalog suddenly contains 25 projects

That is the historical database, not the active catalog. The current catalog must retain 63 records unless Bert explicitly changes the list.

### Sports Group Hub appears again

Treat that as a regression unless Bert explicitly requested its return.

### Browser smoke testing fails in the automation environment

Record the failure boundary accurately. Static and byte-level validation can still be reported, but do not claim interactive browser success without a working browser/runtime test.

## Known unresolved verification boundary

The current durable checkpoint proves static correctness, archive integrity, and Drive byte agreement. It does not prove that the v0.5.0 Quick View was successfully interacted with in Chromium during the recorded automation pass because that browser attempt failed before DOM output.

## Maintenance rule

Update this wiki when Project Constellation's version, canonical files, artifact IDs/hashes, project-count invariant, presentation features, publication workflow, validation evidence, or user-visible operating model materially changes. Avoid timestamp-only edits.