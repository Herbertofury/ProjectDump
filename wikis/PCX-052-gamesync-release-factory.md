# GameSync Release Factory Wiki

**Project ID:** PCX-052  
**Project Constellation goal:** Create reproducible GameSync application/extension release artifacts from canonical source.  
**Documentation status:** Current source-grounded release/build contract  
**Primary shipping repository:** `Herbertofury/Gamesync`  
**Primary migration repository:** `Herbertofury/GameSync-Next`

## Purpose

GameSync Release Factory is the release-discipline track around GameSync rather than a separate application repository. Its job is to turn the current canonical GameSync sources into reproducible build outputs, run the checks that protect extension identity and user state, exercise the generated extension in Opera GX where the verifier supports it, and keep generated artifacts distinct from editable source.

The most important rule is that a successful source edit is not itself a release. A release candidate must be built from the canonical source, checked using the repository's current validation paths, and identified by the exact source revision and generated artifact being tested.

## Current source baselines

### Shipping JavaScript extension

Repository: `Herbertofury/Gamesync`  
Current package version: **0.6.3**  
Current observed `main` head used for this wiki: `a8e37976eb0b3ee3c4ec5e802b02d3bfa1f41928`

The repository explicitly separates:

- `app/` - canonical editable extension source;
- `dist/` - generated production extension;
- `vite.config.ts` and `package.json` - build tooling;
- `scripts/`, `dev/`, `rust/`, `docs/`, and `reference/` - supporting development material.

`dist/` is the folder intended to be loaded unpacked in Opera GX. It is regenerated from `app/` by the build and must not be mistaken for the authoritative editable source.

### GameSync Next / Extension V2

Repository: `Herbertofury/GameSync-Next`  
Current observed `main` head used for this wiki: `9e337c720f0180cffa577f140b181c699f0a1650`  
Extension V2 package version: **0.8.0**

GameSync Next is a workspace-based migration repository. The Extension V2 workspace is `apps/extension-v2`; it uses WXT, TypeScript, React, and shared GameSync packages. The generated Chromium Manifest V3 build is referenced by the repository's verification tools at:

`apps/extension-v2/.output/chrome-mv3`

This generated directory is a release/test input, not the canonical source tree.

## Shipping extension build pipeline

Run from the shipping extension repository root used by its `package.json`:

```powershell
npm ci
npm run build
```

The build command is `vite build`.

The Vite configuration uses `app/` as its root, empties `dist/`, builds the popup, options, panel, full view, offscreen document, background service worker, and content entry points, then runs a runtime-closure plugin that copies required runtime directories and files that were not emitted by Rollup/Vite.

The runtime closure currently preserves entries including `_locales`, assets, background/content/full/panel/popup/options modules, packs, themes, third-party assets, the Shimeji Browser Engine, voice packs, WASM, templates, test assets, the manifest, `Mascot_Engine.js`, and other explicitly enumerated runtime files.

Because `dist/` is emptied and regenerated, release verification must be performed against the newly generated `dist/`, not an older unpacked directory left from a previous build.

## Shipping extension development and validation commands

The shipping repository currently exposes these commands:

```powershell
npm run dev
npm run build
npm run test:bounty
npm run benchmark:bounty
npm run build:wasm:legacy-accel
npm run preview
```

Their verified meanings from `package.json` are:

- `dev`: run Vite in development mode;
- `build`: generate the production extension with Vite;
- `test:bounty`: execute the Bounty Node test suite under `app/test/bounty/`;
- `benchmark:bounty`: run the Bounty benchmark script;
- `build:wasm:legacy-accel`: rebuild the legacy acceleration WASM package with `wasm-pack` into `app/wasm/gs-legacy-accel`;
- `preview`: run Vite preview.

Only run the WASM rebuild when that subsystem is actually part of the change; it requires the external Rust/wasm-pack toolchain in addition to npm dependencies.

## Shipping extension Opera install target

After `npm run build`, load this generated directory as the unpacked Opera GX extension:

```text
<clone-directory>\dist
```

The repository README states that this generated directory is the only folder intended to be loaded unpacked. Loading `app/` directly bypasses the production build contract and is not equivalent release evidence.

## GameSync Next build pipeline

At the GameSync Next repository root, the workspace package exposes a broad build graph. The main aggregate build is:

```powershell
npm ci
npm run build
```

The root `build` script first builds shared packages and then builds the server and desktop workspaces. `build:packages` currently builds schema, shared, engine, core, Pixi game, and UI packages in sequence.

Feature Foundry and HyperBowl have separate build commands and should not be treated as automatically covered by the root build unless their named command is run.

### Extension V2 build

Build Extension V2 directly with:

```powershell
npm --workspace apps/extension-v2 run build
```

The workspace `build` script runs:

1. `wxt build`;
2. `verify:offscreen-runtime`.

A release candidate that bypasses the second step is not equivalent to the repository's declared Extension V2 build.

### Extension V2 ZIP packaging

The Extension V2 workspace exposes:

```powershell
npm --workspace apps/extension-v2 run zip
```

This delegates to `wxt zip`. Treat the ZIP generated by that command as a packaging artifact. Do not infer a stable filename or publish destination unless the actual current output is inspected in the build environment.

## Extension V2 manifest and identity contract

Extension V2 is currently Manifest V3 and declares version **0.8.0**. Its WXT configuration embeds a public extension identity key and provides a dedicated same-ID upgrade verifier.

The release factory must preserve identity deliberately because changing the extension ID can sever access to existing browser-managed extension data.

The repository's same-ID verifier expects extension ID:

`piihebkkniekgkehlpkjdmhnhndccaai`

The verifier tests an upgrade from the current JavaScript extension to the generated V2 build using a dedicated Opera GX profile. It writes sentinels into:

- `chrome.storage.local`;
- `chrome.storage.sync`;
- IndexedDB.

It then loads the V2 build, verifies that the extension ID is unchanged, verifies V2 reports version 0.8.0, confirms all three sentinel stores survived the upgrade, restarts Opera with the V2 build, and confirms identity/version again after restart.

Run it with:

```powershell
npm --workspace apps/extension-v2 run verify:same-id-upgrade
```

The script locates the legacy JavaScript extension from supported sibling/workspace layouts or from `GAMESYNC_LEGACY_EXTENSION_PATH`. It uses `OPERA_GX_PATH` when the default Opera GX executable cannot be resolved.

A successful build without this test does not prove migration safety.

## Extension V2 Opera verification

The repository exposes two related commands:

```powershell
npm run verify:extension-v2:opera
npm --workspace apps/extension-v2 run verify:opera
```

The root command first rebuilds Extension V2 and then executes `scripts/verify-extension-v2-opera.js`. The workspace command invokes that verifier directly and therefore assumes a suitable generated build already exists.

The verifier is explicitly tied to the generated path:

`apps/extension-v2/.output/chrome-mv3`

It can launch Opera GX, stage a smoke-specific copy of the generated extension, connect through Chrome DevTools Protocol, exercise extension/runtime surfaces, and write reports/traces under the repository `output` area.

Important environment controls currently include:

- `OPERA_GX_EXE` - Opera GX executable path;
- `GAMESYNC_V2_TARGET_URL` - target site for the smoke flow;
- `GAMESYNC_V2_EXTENSION_ID` - use a configured installed extension identity/profile path;
- `GAMESYNC_V2_OPERA_PROFILE` - override the profile used by verification;
- `GAMESYNC_V2_ARTIFACT_DIR` - verification artifact directory;
- `GAMESYNC_V2_REPORT` - JSON report path;
- `GAMESYNC_V2_TRACE` - Playwright trace path;
- `GAMESYNC_V2_OPERA_DEBUG_PORT` - CDP port;
- `GAMESYNC_VERIFY_TRANSFORMERS` - enable deeper transformer/WASM smoke validation;
- `GAMESYNC_V2_PRESERVE_PROFILE` - preserve the verification profile;
- `GAMESYNC_V2_USE_LOAD_EXTENSION_FLAGS` - control whether a staged unpacked extension is loaded with browser flags.

Do not report Opera verification as passed unless the verifier actually completes successfully and its generated evidence corresponds to the exact candidate being released.

## Parity gate between shipping GameSync and GameSync Next

GameSync Next contains an executable parity audit:

```powershell
npm run audit:gamesync-parity
```

The migration repository's recent history includes a fix specifically making the parity audit rebuild Extension V2 before examining generated manifest output in a clean checkout. This is important release-factory behavior: parity checks must not accidentally read stale generated output.

The root README also identifies `docs/gamesync-parity-matrix.json` as the machine-readable parity contract and `scripts/audit-gamesync-parity.mjs` as the executable parity audit.

For a V2 migration release, treat parity as a distinct gate from compilation. A V2 build can compile while still omitting shipping-extension behavior.

## Regression and browser test commands in GameSync Next

Available current commands include:

```powershell
npm run lint
npm run lint:oxc
npm run pw:list
npm run pw:test
npm run pw:test:web
npm run pw:test:extension
npm run pw:test:opera-extension
npm run test:mo2-regression
npm run test:intel-regression
npm run test:intel-ui-smoke
npm run test:e2e-opera
npm run test:extension-regression
```

Use the checks relevant to the changed release surface. For broad extension changes, `test:extension-regression` combines the current MO2 and intelligence regression groups; the root package also exposes Playwright web, Chromium-extension, and Opera-extension smoke paths.

A single passing build is not a substitute for the affected regression and runtime checks.

## Secret scanning and credential boundary

The shipping repository currently has a GitHub Actions `Secret scan` workflow that runs on push, pull request, and manual dispatch. It checks out full history and runs Gitleaks using `.gitleaks.toml`.

The repository README also states that Steam, Nexus Mods, Twitch, and other user-provided credentials are stored at runtime in browser-managed extension storage and are not bundled into `app/` or `dist/`.

The public manifest `key` is extension identity material, not a private signing key. Private signing keys, local environment files, credential exports, registry authentication, and local browser profiles must remain outside release artifacts.

Before publication, inspect the exact candidate archive/directory rather than assuming `.gitignore` or CI alone guarantees that no local material was packaged.

## Recommended release ledger

For every candidate, record at least:

| Field | Required evidence |
| --- | --- |
| Project lane | shipping GameSync, Extension V2, desktop/server, or another named workspace |
| Repository | exact `owner/name` |
| Source revision | full commit SHA |
| Declared version | exact package/manifest version |
| Build command | exact command actually executed |
| Generated output | exact path/file tested |
| Build result | observed exit/result |
| Regression checks | exact suites and results |
| Runtime check | exact Opera/browser/app workflow and result |
| Identity check | extension ID/version and migration result when applicable |
| Packaging command | exact command used |
| Artifact digest | SHA-256 of the final publishable file when a file artifact exists |
| Artifact size | final byte size |
| Publication destination | exact release/Drive/repository object |
| Remote verification | remote size/digest or complete re-download/hash |
| Known exclusions | tests/workspaces not exercised |

This prevents a source commit, generated folder, ZIP, and remotely published artifact from being conflated as though they were the same thing.

## Release procedure: shipping GameSync extension

1. Resolve the canonical `Herbertofury/Gamesync` `main` revision and confirm the intended version in `package.json`/manifest.
2. Install dependencies with the lockfile-compatible npm workflow, normally `npm ci`.
3. Run the regression or feature-specific tests relevant to the change.
4. Run `npm run build`.
5. Confirm `dist/` was freshly regenerated and contains the expected manifest/runtime closure.
6. Load the generated `dist/` into the real target Opera GX environment for the affected workflow when release confidence depends on browser behavior.
7. Inspect console/service-worker/runtime errors relevant to the changed feature.
8. Package the tested generated output using the project's actual chosen release packaging procedure. Do not substitute an untested source archive for the tested runtime.
9. Hash the final publishable file when packaging produces one.
10. Publish to the intended durable destination and verify the remote object before recording the release complete.

## Release procedure: Extension V2

1. Resolve the canonical `Herbertofury/GameSync-Next` revision.
2. Run `npm ci`.
3. Build required shared dependencies and the Extension V2 workspace as needed by the selected command path.
4. Run `npm --workspace apps/extension-v2 run build`.
5. Run lint/typecheck checks relevant to the extension surface.
6. Run `npm run audit:gamesync-parity` for migration/parity-sensitive releases.
7. Run `npm --workspace apps/extension-v2 run verify:same-id-upgrade` when claiming a safe upgrade from the shipping extension.
8. Run `npm run verify:extension-v2:opera` for the real Opera build/runtime lane when available.
9. Run relevant Playwright and extension regression suites.
10. If packaging a release ZIP, run `npm --workspace apps/extension-v2 run zip` only after the candidate build and checks correspond to the source revision being released.
11. Record the final artifact hash/size and verify the remote publication before declaring the release durable.

## Modifying the release factory

### Adding a release check

Prefer a deterministic command that can run from a clean checkout and fails with a non-zero status when the acceptance condition is not met. If the check consumes generated output, make the dependency explicit so stale output cannot create a false pass.

### Adding a generated artifact

Document:

- canonical source inputs;
- command that generates it;
- exact output location;
- whether the output is reproducible;
- runtime that consumes it;
- checks that validate it;
- whether it is source-controlled, ignored, or release-only.

### Changing extension identity

Treat any change to manifest identity material as a migration-sensitive release. Update and rerun same-ID/upgrade expectations deliberately. Never treat an accidental ID change as harmless packaging churn.

### Changing workspace versions

Update the package/manifest version and any verifier expectations that intentionally assert that version. The current same-ID verifier explicitly expects Extension V2 version 0.8.0; a future version bump requires the verifier to be updated together with the release contract.

## Troubleshooting

### `dist/` behaves differently from `app/`

This is expected to be possible because `dist/` is a generated production closure. Rebuild and debug the generated runtime. Do not ship `app/` as a workaround.

### Extension V2 Opera verifier cannot find Opera GX

Set the supported Opera executable environment variable used by the selected verifier. `verify-same-id-upgrade.mjs` uses `OPERA_GX_PATH`; `verify-extension-v2-opera.js` uses `OPERA_GX_EXE`.

### Same-ID verifier cannot find the legacy extension

Keep the shipping GameSync repository in one of the supported sibling layouts or set `GAMESYNC_LEGACY_EXTENSION_PATH` to the canonical legacy extension source containing its manifest.

### Same-ID validation loses storage

Treat this as a release blocker for an upgrade claim. Determine whether extension identity changed, the wrong profile/build was loaded, or migration behavior modified browser storage. Do not weaken the sentinel test.

### Parity audit fails only in a clean checkout

Treat that as a build-dependency defect rather than preserving generated output to make the test pass. The current repository history already hardened the audit to rebuild Extension V2 before reading generated manifest output.

### Secret scan fails

Inspect the finding and remove the sensitive material from the candidate/history as appropriate. Do not disable the Gitleaks release guard merely to publish.

### A ZIP exists but no tested generated directory can be tied to it

The ZIP is not sufficient release proof. Rebuild from a known source revision, test that exact candidate, then regenerate/package and hash the final artifact.

## Verification boundary for this wiki

This page documents the **current repository-declared release and verification mechanisms**. During this documentation pass, the repositories were inspected remotely; this pass did not execute npm builds, launch Opera GX, generate a new ZIP, or publish a GameSync product release. Commands above are included only when present in current project-owned source.

The two most recent source baselines inspected were shipping GameSync 0.6.3 at `a8e37976eb0b3ee3c4ec5e802b02d3bfa1f41928` and GameSync Next at `9e337c720f0180cffa577f140b181c699f0a1650`, with Extension V2 declaring version 0.8.0.

## Wiki maintenance triggers

Update this page when any of the following materially changes:

- shipping GameSync version or build layout;
- Extension V2 version, WXT layout, or output directory;
- extension identity or same-ID migration logic;
- build, ZIP, parity, lint, regression, Playwright, or Opera verification commands;
- release/publishing destination;
- generated artifact naming/layout;
- secret scanning or credential boundaries;
- desktop/server packaging flow;
- remote artifact verification procedure.
