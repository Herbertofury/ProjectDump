# Sims4CreatorStudio Wiki

**Project Constellation ID:** `PCX-033`  
**Status:** ACTIVE / TRACKED  
**Connected repository:** [Herbertofury/Sims4CreatorStudio](https://github.com/Herbertofury/Sims4CreatorStudio)

## Purpose

Sims4CreatorStudio is tracked as a project to build a verified Sims 4 creator studio from preserved alpha/source lineage while retaining repository identity, source assets, and real creator workflows.

## Current repository state

The connected repository still acts partly as a durable recovery/transfer point rather than a fully published production source tree. It contains a minimal visible top-level surface plus bootstrap/payload state, including:

- `.s4cs-bootstrap/`;
- `.s4cs-payload/`;
- `.s4cs-payload-v5/`;
- `.github/workflows/s4cs-drive-recover-alpha11.yml`.

The newest repository commit observed in this pass is `a810bdba98bd5ca8dfd879f48776ce3f7a8add0e`, whose only source change retriggers the verified Alpha11 Drive recovery workflow. That does **not** prove the Alpha11 source has been published to `main` yet.

## Preferred verified recovery path, checked 2026-08-18

The repository now contains a materially stronger recovery route than the older small-chunk transfer. The workflow `.github/workflows/s4cs-drive-recover-alpha11.yml` records an exact verified Git bundle in Google Drive and defines the complete recovery/publication contract.

Pinned recovery evidence:

- target source commit: `aa011d208d65dca1ad38bd83302fa05364e51800`;
- release tag: `v0.1.0-alpha.11`;
- Drive Git bundle ID: `1YiwAclxwY4VHAuIsff12GrW4_Xa8MPYw`;
- expected bundle size: **6,374,056 bytes**;
- expected bundle SHA-256: `3b3a7cccf44caa42a645e0aa6c6ef2bf7309fc156ad9ec79377e95cab4be6b41`.

The workflow is designed to:

1. download that exact Drive bundle;
2. verify byte size and SHA-256;
3. run `git bundle verify`;
4. recover exact commit `aa011d208d65dca1ad38bd83302fa05364e51800` and the Alpha11 tag;
5. verify that the recovered tree contains **248 files**;
6. verify `package.json` reports version `0.1.0-alpha.11`;
7. verify **14** Markdown wiki pages exist in the recovered source;
8. create a detached worktree from the exact source commit;
9. run `npm run build`;
10. run `npm test`;
11. run `npm run corruption`;
12. run `npm run stress`;
13. publish that exact source commit to `main` and the release tag;
14. verify the remote branch and tag resolve to the expected source SHA.

### Current publication boundary

At this checkpoint, repository `main` still resolves to the recovery/staging line rather than `aa011d208d65dca1ad38bd83302fa05364e51800`, and an API read of that target SHA does not yet resolve as a repository commit. Therefore the exact Alpha11 publication workflow is the **current preferred recovery path but not yet a completed publication**.

Do not claim recovered source, build success, test success, or release publication until the workflow's final remote-SHA checks actually pass.

## Legacy payload checkpoint

The older `.s4cs-payload-v5` small-commit transfer remains valuable recovery history and must be preserved, but it is no longer the preferred first recovery route while the verified Drive Git bundle exists.

The current legacy markers still show:

- `CHUNK-STATUS-08.txt` says Part 08 is the next durable payload checkpoint;
- `PAYLOAD-CHECKPOINT-08.txt` says the next required binary payload fragment is `part08.b64`;
- `PARTS_EXPECTED.txt` records expected payload fragments from `part00.b64` through `part19.b64`;
- expected decoded XZ payload size: **289,296 bytes**;
- expected decoded XZ SHA-256: `9da7f27544d79293a01752ccf9c00553f26030e285b8b7148052d7a24c8cb015`.

Treat this chunked route as fallback/recovery evidence. Do not delete it after the Git bundle succeeds unless a later explicit cleanup is proven safe and preserves lineage.

## Current exact next action

**Run or observe the existing verified Alpha11 Drive recovery workflow to completion, then verify that repository `main` and tag `v0.1.0-alpha.11` both resolve to `aa011d208d65dca1ad38bd83302fa05364e51800`. Only after that remote identity proof should the reconstructed production source be treated as canonical and its real application architecture/build/use workflow be documented.**

If the workflow cannot complete, preserve its exact failure evidence and continue from the chunked Part 08 route rather than restarting the project.

## Recovery and source-preservation rules

- Treat the current repository as durable lineage evidence.
- Preserve existing payload fragments, checkpoint markers, recovery workflow, and exact bundle identity.
- Do not initialize a fresh unrelated studio because the visible top-level repository is sparse.
- Do not treat a transfer marker, workflow file, or upload acknowledgement as application source.
- Prefer the exact hash-verified Git bundle path while it remains available.
- Verify recovered bytes and Git identity before promoting them as canonical.
- Preserve any newer user-edited source if discovered during reconciliation.
- Never overwrite a newer verified source tree with the older fragment reconstruction.

## Installation / build status

A truthful end-user install guide still cannot be finalized from the currently published `main` tree because the exact Alpha11 source has not yet been proven present there.

The recovery workflow does provide verified **qualification commands for the recovered source**:

```bash
npm run build
npm test
npm run corruption
npm run stress
```

These are recovery acceptance commands, not a claim that this documentation pass executed them successfully. Once the exact source commit is actually published and re-read, this wiki should be expanded from project-owned source with:

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

## Required verification after recovery

After Alpha11 source is fully recovered:

1. Verify the Drive Git bundle size and SHA-256.
2. Verify the bundle with `git bundle verify`.
3. Verify source SHA `aa011d208d65dca1ad38bd83302fa05364e51800`.
4. Verify 248 files, Alpha11 package version, and 14 wiki Markdown pages.
5. Build from a fresh detached worktree.
6. Run the project-owned test, corruption, and stress suites.
7. Verify the published `main` and release tag point to the exact tested source.
8. Inventory manifests, source roots, dependencies, assets, tests, and docs.
9. Resolve the real app entry point.
10. Launch the real creator studio.
11. Exercise each visible workspace/control relevant to the current project state.
12. Verify save/reopen persistence.
13. Verify Sims 4 import/export/package behavior where implemented.
14. Record exact artifact/version/hash and current stop point.

If the Git-bundle path fails and the chunked fallback is used instead, also verify the reconstructed legacy payload against `9da7f27544d79293a01752ccf9c00553f26030e285b8b7148052d7a24c8cb015` before using it.

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

Do not restart the project. Check the Alpha11 recovery workflow and exact Drive bundle identity first, then inspect hidden payload/bootstrap directories as fallback evidence.

### Alpha11 workflow does not publish the target SHA

Capture the failed workflow step. Verify Drive bundle availability, exact byte size, SHA-256, `git bundle verify`, and source SHA before changing the recovery mechanism. Do not weaken the hash or test gates to make publication pass.

### A legacy payload part is missing

Continue from the current recorded Part 08 checkpoint. Preserve already transferred parts and checkpoint files.

### Reconstructed legacy archive/payload hash does not match

Do not promote it as canonical. Re-check fragment ordering/completeness and compare against the expected decoded size/hash.

### A newer complete source copy is found elsewhere

Compare project identity, version, substantive content, Git ancestry, and hashes. Preserve both lineages until the newer canonical state is proven.

## Wiki maintenance

Update this page immediately when the Alpha11 workflow publishes the exact target commit, the release tag is remotely verified, the chunk fallback advances, a newer source supersedes Alpha11, the canonical runtime/build is identified, or creator workflows become verifiable. The current primary blocker is **verified source publication to canonical `main`**, not project identity and not absence of a recoverable source bundle.
