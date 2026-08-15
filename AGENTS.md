# ProjectDump Durable Continuity Contract

This repository is a durable cross-project source of truth for Bert's project work and skills.

## Mandatory source priority for ALL projects and skills

1. **GitHub: `Herbertofury/ProjectDump`** is the primary versioned source for project state, project memory, manifests, catalogs, handoffs, policies, source snapshots, skill continuity, and other text/code continuity data.
2. **Connected Google Drive** is the primary durable source for release artifacts, archives, binaries, large files, recovery bundles, exported project brains, skill packages, and byte-verifiable backups.
3. **DO NOT USE CHATGPT FILE LIBRARY.** It is prohibited as a working, continuity, recovery, discovery, backup, or publication source unless Bert explicitly instructs the current task to use ChatGPT File Library.
4. Ephemeral sandbox/container files are working copies only and are never the sole durable checkpoint.

## Global working behavior

- This policy applies to **every project, repository, app, extension, plugin, document, research track, agent workflow, Project Constellation operation, and skill** unless Bert explicitly overrides it for the current task.
- Before continuing existing work, resolve the latest canonical state from GitHub and Google Drive first.
- Never search ChatGPT File Library merely because a file is missing locally. Search ProjectDump, the relevant GitHub repository, and Google Drive instead.
- Never make ChatGPT File Library a dependency of a project or skill workflow.
- Never publish a project's only durable copy to ChatGPT File Library.
- Compare version, commit/ref, SHA-256, artifact identity, and substantive content when multiple candidates exist. Do not choose by filename or timestamp alone.
- User edits and explicitly chosen canonical versions win over automation-generated copies.
- Never silently reconstruct, overwrite, reset, or downgrade a newer project state because an older local copy is easier to access.
- Keep project-specific durable memory in repository-owned `.agents-memory/` state when appropriate.
- Keep Project Constellation and cross-project catalogs synchronized after meaningful verified progress, version/artifact changes, blocker changes, recovery discoveries, or steering decisions.
- After meaningful implementation changes, commit/publish durable version-controlled state to GitHub.
- Publish complete release/build/recovery artifacts to Google Drive when they do not belong in Git.
- Verify important Drive publications by size and SHA-256 or complete re-download/hash before treating them as durable.
- For continuity-critical checkpoints, never finish with the only good copy in ChatGPT's sandbox or File Library.

## Project Constellation

Project Constellation continuity must use GitHub plus Google Drive as the durable recovery base. Preserve the 63-project lineage and all later user decisions/research deltas. Do not fabricate missing historical artifact bytes. Record missing bytes as unresolved while preserving the latest verified metadata and recovery evidence.

## Skills

Every skill and skill-driven workflow must follow this same storage rule. Skill state, governance, source, exports, packages, and continuity checkpoints belong in GitHub and/or Google Drive according to artifact type. ChatGPT File Library must not be consulted unless Bert explicitly requests it for that task.

## Default future instruction

Unless Bert explicitly overrides this for a specific task, work from **Google Drive + `Herbertofury/ProjectDump`** and any project-specific GitHub repository. **Never use ChatGPT File Library.**
