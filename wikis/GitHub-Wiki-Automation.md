# GitHub Wiki Automation

ProjectDump now has a verified two-layer GitHub Wiki automation path that covers both the one-time first-page bootstrap and ongoing page creation, editing, deletion, full synchronization, and machine-readable publication proof.

## Architecture

GitHub Wikis are separate Git repositories at `OWNER/REPO.wiki.git`. The normal repository contents API does not expose wiki pages as ordinary files, and GitHub does not create the wiki Git remote until a first page exists.

The automation therefore uses two complementary layers:

1. **Ferrum first-page bootstrap** for a repository whose wiki Git remote does not exist yet.
2. **Source-controlled wiki sync** for all ongoing page management after the wiki Git remote exists.

## ProjectDump ongoing wiki source

The canonical ProjectDump wiki source is the repository directory:

`wikis/`

The publisher is:

`tools/github-wiki/wiki-sync.sh`

The GitHub Actions workflow is:

`.github/workflows/sync-github-wiki.yml`

A source file maps to a real GitHub Wiki page. Therefore:

- creating a source file creates a page;
- changing a source file edits that page;
- deleting a source file deletes that page;
- assets placed in the source directory are mirrored with the page set;
- the publisher mirrors the complete source directory rather than leaving stale remote pages behind.

After every publish, the script fresh-clones the real `.wiki.git` repository and byte-compares it to the source directory. A workflow success therefore proves that the remote wiki matches the intended source, including deletions.

## Machine-verifiable publication proof

The workflow now persists a traditional GitHub commit status named:

`wiki-publication`

It is written **only after** `wiki-sync.sh` completes successfully, which means the publisher has already:

1. mirrored the complete `wikis/` tree into `ProjectDump.wiki.git`;
2. pushed any changed Wiki commit;
3. fresh-cloned the remote Wiki after publication;
4. run the complete byte comparison against the source tree;
5. resolved the remote Wiki `master` commit.

The success status is attached to the exact source commit that triggered the workflow. Its description records the full 40-character published Wiki master commit, and its target URL points to the exact GitHub Actions run. If publication or fresh-clone verification fails, the workflow records a failure status when possible.

This closes an important verification gap for automated maintainers: a later run can query the triggering source commit, read `wiki-publication`, follow its exact Actions run, and inspect the job logs without relying on a manually copied run ID.

### Verified proof checkpoint

The proof mechanism itself was first verified on source commit:

`60bb4e8bee1afdc20369432bc0e0b8231d1cb240`

The `Sync GitHub Wiki` run was:

`32083124479`

The run concluded successfully. Its publisher reported that the Wiki already matched the source, fresh-cloned the remote Wiki, completed the byte comparison, and resolved published Wiki master commit:

`912305b14458ea5ac5340ed0ed1f3432fd9b97d3`

The workflow then wrote `wiki-publication=success` back to source commit `60bb4e8bee1afdc20369432bc0e0b8231d1cb240` with the run URL as the status target.

## Ferrum first-page bootstrap

Ferrum repository:

https://github.com/Herbertofury/Ferrum-Browser

Ferrum provides:

```bash
npx ferrum github-wiki probe OWNER/REPO
npx ferrum github-wiki bootstrap OWNER/REPO --space github
```

The matching MCP tools are:

- `ferrum_github_wiki_probe`
- `ferrum_github_wiki_bootstrap`

`probe` checks the separate GitHub Wiki smart-HTTP Git endpoint without mutating the repository.

`bootstrap` is idempotent. If the wiki Git remote already exists, it reports `already-initialized` and does not create a page. If the wiki is genuinely empty, Ferrum opens a real persistent Chromium Space, reaches GitHub's first-page editor, fills and saves the first page, captures evidence, and then verifies that the `.wiki.git` remote becomes available.

## Authentication

Ferrum Spaces preserve authenticated browser state. The default wiki Space is `github`.

If GitHub requires login and the Space is not yet authenticated, run bootstrap headed once and complete GitHub authentication in that browser. Later bootstrap operations can reuse the same persistent Space.

Git probing automatically uses `GH_TOKEN` or `GITHUB_TOKEN` when one is available. The token is used only for Git transport authentication and is not written into Ferrum evidence.

The ProjectDump sync workflow uses the repository-scoped Actions token. Its required permissions are `contents: write` for Wiki Git publication and `statuses: write` for the `wiki-publication` proof status.

## Private-repository safety

A private repository can make an unauthenticated `.wiki.git` probe return HTTP 404 even when the wiki already exists. Ferrum does not treat every unauthenticated 404 as permission to create a page.

When a token is available, Ferrum uses an authenticated Git probe. Without a token, Ferrum inspects the authenticated wiki root first. It only opens the first-page editor when the browser proves that the wiki is in the first-page state. Existing wiki content causes a non-mutating `already-initialized` result.

A dedicated browser regression test simulates the private false-404 case and verifies zero visits to the new-page editor and zero save submissions.

## Verified ProjectDump lifecycle

ProjectDump's initial wiki page was created once through GitHub. The automated publisher was then rerun against the real repository and succeeded.

The first successful complete ProjectDump synchronization fresh-cloned and byte-verified the real wiki after publishing the complete source set.

A temporary lifecycle page was subsequently exercised through all three mutations:

1. create page;
2. edit page with changed content;
3. delete page.

Every lifecycle workflow completed successfully with the same fresh-clone remote verification. The temporary page was removed after the deletion test.

## Verified Ferrum checkpoint

Ferrum code commit:

`71faada1cd13214fc4444fc11034c891f80c2708`

GitHub Actions run:

`32050699041`

The run completed successfully across all five jobs. The GitHub Wiki first-page browser smoke passed on both Ubuntu and Windows. The Linux lane also performed a live non-mutating probe of `Herbertofury/ProjectDump` and confirmed its real wiki Git remote is initialized.

The same exact Ferrum head also passed its existing unit, syntax, MCP, web, browser-matrix, MV3, workload-pack, dashboard, Electron, desktop, packaged-desktop, Lightpanda, and real Android/Appium gates.

## Future repository workflow

For another repository:

1. confirm the repository has GitHub Wikis enabled;
2. run `ferrum github-wiki probe OWNER/REPO`;
3. if the wiki is uninitialized, run `ferrum github-wiki bootstrap OWNER/REPO --space github`;
4. establish a source wiki directory in the normal repository;
5. install or reuse the verified wiki-sync publisher workflow with a write-capable GitHub token;
6. if automated verification needs to be queryable later, grant `statuses: write` and record a success status only after the fresh-clone byte comparison passes;
7. manage wiki pages by creating, editing, renaming, or deleting source files;
8. require the exact source commit's `wiki-publication` status, Actions run, published Wiki master commit, and fresh-clone comparison before treating the wiki update as complete.

This makes the browser-only first-page operation a one-time bootstrap detail while keeping normal wiki maintenance source-controlled, reviewable, repeatable, and independently verifiable.
