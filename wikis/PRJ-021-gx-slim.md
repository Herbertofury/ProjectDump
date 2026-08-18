# PRJ-021 - GX Slim

**Project Constellation ID:** `PRJ-021`
**Status:** UNRESOLVED IDENTITY
**Confidence:** Low
**Preserved artifact identity:** `GX-Slim-1.0.0-FULL.zip`
**Preserved SHA-256:** `5ad8aa6d13a898af1ead4d50b7922829ec94d427199475f17522b2ed1a4a9717`

## Purpose

GX Slim is a preserved Project Constellation project identity whose product purpose and canonical source are still unresolved. The durable record proves that a versioned archive and hash existed; it does not prove whether GX Slim is an Opera GX utility, GameSync derivative, Feature Foundry host, browser project, or something else.

## Current evidence

The strongest current evidence is the historical cross-chat project database and the byte identity recorded there:

- archive: `GX-Slim-1.0.0-FULL.zip`
- version marker: `1.0.0`
- SHA-256: `5ad8aa6d13a898af1ead4d50b7922829ec94d427199475f17522b2ed1a4a9717`
- historical status: recovered artifact, unresolved identity

Exact-name searches in the connected Drive and current Herbertofury GitHub repository surface did not recover the ZIP, a README, or a canonical source repository during this pass.

## Missing evidence

Before implementation, the project still needs:

1. the exact ZIP or a hash-matching copy;
2. root README/manifest/package metadata;
3. canonical source repository/worktree/branch, if one exists;
4. build/runtime instructions;
5. validation or test evidence;
6. relationship to GameSync, Opera GX, Feature Foundry, Ferrum, or any other tracked project.

## Anti-regression rule

Do not infer product identity from the name `GX Slim`. Do not initialize a replacement repository, merge it into GameSync, or recreate an app from guesses. A source/artifact match must be proven by the preserved hash, embedded identity, or stronger current project-owned evidence.

## Recovery procedure

When a candidate archive is found:

1. compute SHA-256 before extraction;
2. compare against the preserved hash;
3. preserve the original bytes read-only;
4. extract to a fresh directory;
5. inventory manifests, README, source roots, build files, assets, tests, and embedded version strings;
6. record the product name/purpose from project-owned files rather than guessing;
7. search Git history/repository remotes inside the extracted source when present;
8. build/test only after the canonical identity is resolved;
9. update Project Constellation with the exact stop point and next action.

## Research decision

External technology research is intentionally deferred until identity is resolved. Choosing a framework, browser API, build system, or replacement library before knowing what GX Slim actually is would create false continuity and could overwrite the real project direction.

## Exact current next action

Recover a hash-matching `GX-Slim-1.0.0-FULL.zip` or stronger project-owned source, inspect its README/manifests, and resolve purpose plus canonical repository before any coding.

## Wiki maintenance

Replace unresolved assumptions only with direct artifact/repository evidence. Preserve the 1.0.0 filename and SHA-256 lineage even if a newer successor is found.