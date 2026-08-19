# GitHub Wiki Publisher

This directory owns the verified publication bridge from the version-controlled `wikis/` source tree to the real reader-facing GitHub Wiki.

## Publication contract

The canonical source is `wikis/` on `Herbertofury/ProjectDump` `main`. The reader-facing destination is the separate Git repository `Herbertofury/ProjectDump.wiki.git` and the Wiki UI at `https://github.com/Herbertofury/ProjectDump/wiki`.

A source Markdown edit is not considered published merely because it exists under `wikis/`.

`.github/workflows/sync-github-wiki.yml` runs `tools/github-wiki/wiki-sync.sh` when `wikis/**`, this tool directory, or the workflow itself changes. The publisher must:

1. clone the existing Wiki repository, or initialize a Wiki worktree only for first-publication bootstrap;
2. mirror `wikis/` exactly into the Wiki worktree while preserving only the Wiki `.git` directory;
3. commit and push `master` only when source bytes differ;
4. fresh-clone `ProjectDump.wiki.git` after the push;
5. remove the verification clone's `.git` metadata;
6. run a recursive byte comparison between the complete `wikis/` source tree and the fresh remote clone;
7. resolve the published `refs/heads/master` commit and print `Wiki master commit: <sha>`;
8. let the workflow record the `wiki-publication` commit status only after that verification succeeds.

## Required environment

`wiki-sync.sh` requires `GH_TOKEN` with write access to the source repository and its Wiki Git remote. The workflow supplies `${{ github.token }}` with `contents: write` and `statuses: write` permissions.

Manual script shape:

```bash
GH_TOKEN=... bash tools/github-wiki/wiki-sync.sh Herbertofury/ProjectDump wikis https://github.com
```

Do not store the token in source, logs, durable checkpoints, or documentation.

## Successful output

A successful publisher run ends with both lines:

```text
Wiki sync verified: https://github.com/Herbertofury/ProjectDump/wiki
Wiki master commit: <40-hex-sha>
```

The workflow then records a `wiki-publication` success status on the exact source commit. Its description includes the fresh-clone byte-verified Wiki master commit and its target URL points to the exact Actions run.

## Failure handling

Treat these states differently:

- **No workflow/status for an eligible source push:** verify the push touched one of the workflow path filters, inspect Actions execution, and trigger a new meaningful eligible publication-path change rather than claiming publication from repository source alone.
- **Publisher push failure:** inspect Wiki Git authentication/bootstrap state. Do not mark the wiki current.
- **Fresh-clone comparison failure:** the remote page set differs from `wikis/`; repair the mismatch and rerun publication.
- **Missing Wiki master SHA:** fail closed. The workflow intentionally exits instead of producing an unverifiable success.
- **No source changes:** `wiki-sync.sh` may report that the Wiki already matches source, but it must still fresh-clone, byte-compare, and report the remote Wiki master commit before the workflow records success.

## Scope rule

`wikis/` documents projects tracked inside Project Constellation. Project Constellation itself is the control plane, not a normal recurring project-wiki target. The preserved PCX-036 page is a legacy continuity reference only.
