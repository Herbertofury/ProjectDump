# ProjectDump Durable Continuity Contract

This repository is a durable cross-project source of truth for Bert's project work.

## Canonical source priority

1. **GitHub: `Herbertofury/ProjectDump`** is the primary versioned source for project state, project memory, manifests, catalogs, handoffs, policies, source snapshots that belong in Git, and other text/code continuity data.
2. **Connected Google Drive** is the primary durable source for release artifacts, archives, binaries, large files, recovery bundles, exported project brains, and byte-verifiable backups.
3. **ChatGPT File Library is tertiary recovery-only storage.** Do not use it as the normal working source when the same state is available from GitHub or Google Drive.
4. Ephemeral sandbox/container files are working copies only and are never the sole durable checkpoint.

## Required working behavior

- Before continuing an existing project, resolve the latest canonical state from GitHub and Google Drive first.
- Compare version, commit/ref, SHA-256, artifact identity, and substantive content when multiple candidates exist. Do not choose by filename or timestamp alone.
- User edits and explicitly chosen canonical versions win over automation-generated copies.
- Never silently reconstruct, overwrite, reset, or downgrade a newer project state because an older local or Library copy is easier to access.
- Keep project-specific durable memory in repository-owned `.agents-memory/` state when appropriate.
- Keep Project Constellation and cross-project catalogs synchronized after meaningful verified progress, version/artifact changes, blocker changes, recovery discoveries, or steering decisions.
- After meaningful implementation changes, commit/publish the durable project state to GitHub when it belongs in version control.
- Publish complete release/build/recovery artifacts to Google Drive when they do not belong in Git.
- Verify important Drive publications by size and SHA-256 or complete re-download/hash before treating them as durable.
- For continuity-critical checkpoints, never finish with the only good copy in ChatGPT's sandbox or File Library.

## Project Constellation

Project Constellation continuity must use GitHub plus Google Drive as the durable recovery base. Preserve the 63-project lineage and all later user decisions/research deltas. Do not fabricate missing historical artifact bytes. Record missing bytes as unresolved while preserving the latest verified metadata and recovery evidence.

## Default future instruction

Unless Bert explicitly overrides this for a specific task, work from **Google Drive + `Herbertofury/ProjectDump`** first and treat ChatGPT File Library as a last-resort recovery source only.
