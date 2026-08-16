# Sims4CreatorStudio Wiki

**Project Constellation ID:** `PCX-033`  
**Status:** ACTIVE / TRACKED  
**Connected repository:** [Herbertofury/Sims4CreatorStudio](https://github.com/Herbertofury/Sims4CreatorStudio)

## Purpose

Sims4CreatorStudio is tracked as a project to build a verified Sims 4 creator studio from preserved alpha/source lineage while retaining repository identity, source assets, and real creator workflows.

## Current repository state

The connected repository currently contains a minimal top-level `README.md` plus several hidden/bootstrap/payload directories, including:

- `.s4cs-bootstrap/`
- `.s4cs-payload/`
- `.s4cs-payload-v5/`

This means the repository currently acts partly as a durable recovery/transfer point rather than a fully documented production source tree.

## Current payload checkpoint

The current `.s4cs-payload-v5` markers show that the small-commit transfer is still incomplete:

- `CHUNK-STATUS-08.txt` says Part 08 is the next durable payload checkpoint.
- `PAYLOAD-CHECKPOINT-08.txt` says the next required binary payload fragment is `part08.b64`.
- `PARTS_EXPECTED.txt` records expected payload fragments from `part00.b64` through `part19.b64`.
- The expected decoded XZ payload size is **289,296 bytes**.
- The expected decoded XZ SHA-256 is `9da7f27544d79293a01752ccf9c00553f26030e285b8b7148052d7a24c8cb015`.

Do not present the source transfer as complete until all expected parts exist, the payload reconstructs, and the reconstructed bytes match the recorded hash.

## Current exact next action

Continue from the newest verified transfer checkpoint without restarting or replacing the repository. Complete the remaining payload transfer, reconstruct the intended source, verify the expected hash, then identify the actual application structure and runtime before documenting build/use instructions.

## Recovery and source-preservation rules

- Treat the current repository as durable lineage evidence.
- Preserve existing payload fragments and checkpoint markers.
- Do not initialize a fresh unrelated studio because the visible top-level repository is sparse.
- Do not treat a transfer marker as application source.
- Verify reconstructed payload bytes against the recorded SHA-256 before promoting them as canonical.
- Preserve any newer user-edited source if discovered during reconciliation.

## Installation / build status

A truthful install/build guide cannot yet be finalized from the currently verified repository surface because the application payload transfer is incomplete and the top-level repository does not expose the complete production source tree.

When the payload is complete, this wiki should be expanded with:

1. canonical source root;
2. language/framework/runtime;
3. dependency installation;
4. development launch command;
5. production build/package command;
6. required Sims 4 paths/assets;
7. configuration/storage layout;
8. creator workflows;
9. tests and validation commands;
10. release artifact format.

## Required verification after reconstruction

After the payload is fully reconstructed:

1. Verify SHA-256 against `9da7f27544d79293a01752ccf9c00553f26030e285b8b7148052d7a24c8cb015`.
2. Extract/open it in a fresh location.
3. Inventory manifests, source roots, dependencies, assets, tests, and docs.
4. Resolve the real app entry point.
5. Build the application using project-owned instructions.
6. Launch the real creator studio.
7. Exercise each visible workspace/control relevant to the current project state.
8. Verify save/reopen persistence.
9. Verify Sims 4 import/export/package behavior where implemented.
10. Record exact artifact/version/hash and current stop point.

## Documentation target

The completed wiki should allow another developer to understand and modify:

- project architecture;
- Sims 4 package/resource handling;
- asset/content pipelines;
- creator workspaces;
- persistence/database formats;
- preview/render systems;
- import/export behavior;
- plugin/extension points;
- build/test/release workflow;
- recovery and migration behavior;
- troubleshooting.

Only add these as verified implementation facts after the source is actually recovered and inspected.

## Troubleshooting

### Repository looks nearly empty

Do not restart the project. Check the hidden payload/bootstrap directories and current transfer checkpoint first.

### A payload part is missing

Continue from the current recorded part number. Preserve already transferred parts and checkpoint files.

### Reconstructed archive/payload hash does not match

Do not promote it as canonical. Re-check fragment ordering/completeness and compare against the expected decoded size/hash.

### A newer complete source copy is found elsewhere

Compare project identity, version, substantive content, and hashes. Preserve both lineages until the newer canonical state is proven.

## Wiki maintenance

This page should be updated immediately when the payload transfer advances, the complete source is reconstructed, the canonical build/runtime is identified, or creator workflows become verifiable. The current primary blocker is incomplete source transfer, not lack of project identity.