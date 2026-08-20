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
Current observed `main` head used for this wiki: `cd906ff0831bf7fc33b41fea31b6f0c004cc1562`
Extension V2 package version: **0.8.0**

GameSync Next is a workspace-based migration repository. The Extension V2 workspace is `apps/extension-v2`; it uses WXT, TypeScript, React, and shared GameSync packages. The generated Chromium Manifest V3 build is referenced by the repository's verification tools at:

`apps/extension-v2/.output/chrome-mv3`

This generated directory is a release/test input, not the canonical source tree.

The current GameSync Next head is two commits ahead of the previous release-factory documentation baseline `9e337c720f0180cffa577f140b181c699f0a1650`. The merged delta materially expands the extension release surface with Universal Game Tracker, Bounty, Animation Tracker, new import/export dependencies, background alarms/message routing, UI routes, parity-matrix changes, and substantially expanded Opera verification.

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

### Current `test:e2e-opera` boundary

`package.json` still declares:

```text
node opera-extension/app/tests/e2e.opera-gx.test.js
```

but that target file is absent at current main `cd906ff0831bf7fc33b41fea31b6f0c004cc1562`. Therefore `npm run test:e2e-opera` must **not** be represented as a currently working release gate until its entrypoint is repaired or intentionally redirected to a maintained equivalent.

For current Extension V2 release qualification, use the maintained `verify:extension-v2:opera` / `verify:opera` path and the Playwright extension lanes that resolve to present files. A missing legacy entrypoint is a release-factory defect to fix, not a reason to mark that check passed.

A single passing build is not a substitute for the affected regression and runtime checks.

## Current merged Extension V2 release surface

The current main merge `cd906ff0831bf7fc33b41fea31b6f0c004cc1562` materially broadens what an Extension V2 release must preserve compared with the previous wiki baseline.

### Universal Game Tracker

The merge adds a typed Game Tracker feature, Dexie-backed data model, UI routes, schema editor, record editor, relationship handling, and worker-owned import/export paths. Supported import/export code now includes DOCX, XLSX/XLS, CSV/TSV, JSON, Google Docs/Sheets export URLs, native Word dropdown extraction, and binary image handling.

Extension V2 now directly depends on additional portability libraries including:

- `docx` `^9.7.1`;
- `linkedom` `^0.18.12`;
- `mammoth` `^1.12.0`;
- SheetJS `xlsx` from the explicit `0.20.3` CDN tarball.

The lockfile changed with this merge. A release candidate must therefore be installed from the candidate lockfile and must not silently reuse a dependency tree from the earlier 9e337 baseline.

Project-owned merge evidence records a clean isolated Opera run that imported both the supplied 43 MB local DOCX and a live Google Doc path independently. Each produced 181 active records, 75 relationships, and 124 schema-bound images; the UI exposed imported dropdown options and persisted an inline edit; JSON, XLSX, DOCX, and CSV exports completed and passed content checks. Treat these as project-owned verification evidence for the merged source, not as tests executed by this wiki-maintenance pass.

### Bounty

The merge adds typed Bounty contracts, service/background routing, reminder alarms, UI routing, and persistence. Project-owned merge evidence records a clean isolated Opera synchronization of 107 live GamerPower records with a healthy source state and rendered calendar.

A release touching background bootstrap, alarms, runtime messaging, storage, or Bounty UI must preserve:

- `BOUNTY_*` message routing;
- reminder alarm creation and handling;
- persisted Bounty state;
- real source synchronization and visible failure state;
- the exact runtime route in the built extension.

### Animation Tracker

The merge adds creator and pack contracts, HTTPS source validation, version detection/comparison, polling state, alarm handling, UI routes, and persistence. Project-owned merge evidence records an exact HTTPS source poll, semantic-version detection, and an available installed-pack update rendered without remounting the React root.

A release touching the background bootstrap, route shell, storage, or network behavior must preserve the Animation Tracker alarm and polling lifecycle in addition to ordinary compilation.

### Release-factory consequence

The same merge modifies `apps/extension-v2/src/background/bootstrap.ts`, `App.tsx`, `docs/gamesync-parity-matrix.json`, the extension lockfile/dependency graph, and `scripts/verify-extension-v2-opera.js`. Release qualification for current main therefore needs to bind the candidate source SHA to all of the following rather than relying on an older 0.8.0 smoke result:

1. fresh `npm ci` from the current lockfile;
2. fresh Extension V2 build plus offscreen-runtime verification;
3. current parity audit after generated output is rebuilt;
4. current Opera verifier against the generated `.output/chrome-mv3` candidate;
5. import/export round-trip evidence for Game Tracker when that surface is in scope;
6. Bounty source/alarm/persistence evidence when Bounty or shared background code is in scope;
7. Animation Tracker poll/alarm/persistence evidence when Animation or shared background code is in scope;
8. extension identity and same-ID upgrade proof for migration releases;
9. final ZIP hash/size and dual-destination remote byte verification when a release artifact is published.

## Secret scanning and credential boundary

The shipping repository currently has a GitHub Actions `Secret scan` workflow that runs on push, pull request, and manual dispatch. It checks out full history and runs Gitleaks using `.gitleaks.toml`.

GameSync Next current main also contains a `secret-scan.yml` workflow. Release bookkeeping should record which repository and exact source commit supplied the security scan evidence instead of treating a passing scan from the sibling repository as interchangeable.

The repository README also states that Steam, Nexus Mods, Twitch, and other user-provided credentials are stored at runtime in browser-managed extension storage and are not bundled into `app/` or `dist/`.

The public manifest `key` is extension identity material, not a private signing key. Private signing keys, local environment files, credential exports, registry authentication, and local browser profiles must remain outside release artifacts.

Before publication, inspect the exact candidate archive/directory rather than assuming `.gitignore` or CI alone guarantees that no local material was packaged.

## Signed build provenance and artifact attestations

GitHub's current artifact-attestation path can add cryptographically signed build provenance to GameSync release artifacts without replacing any existing release gate. GitHub Actions currently documents `actions/attest@v4` with `id-token: write`, `contents: read`, and `attestations: write`; the final publishable ZIP or binary is supplied as the attestation subject. GitHub also supports signed SPDX or CycloneDX SBOM attestations for the same artifact.

For public repositories, GitHub-backed attestations use the Sigstore Public Good Instance and are intended to let consumers verify where and how the artifact was built. The corresponding verification command is:

```text
gh attestation verify PATH/TO/ARTIFACT -R OWNER/REPOSITORY
```

This should be an **additive provenance layer**, not a substitute for SHA-256, exact source revision, reproducible build identity, same-ID upgrade verification, parity audit, Opera/runtime tests, remote Drive/GitHub byte verification, or regression suites. An attested artifact can still be functionally broken if the workflow built broken source, so runtime acceptance remains mandatory.

### Proposed attested-release experiment

For one Extension V2 release candidate after all existing build/runtime gates pass:

1. produce the final ZIP in GitHub Actions from the exact source commit under test;
2. compute and record its SHA-256 and byte size;
3. generate build provenance for that exact ZIP with `actions/attest@v4`;
4. optionally generate an SPDX or CycloneDX SBOM and attest it against the same ZIP;
5. download the workflow artifact into a fresh environment and run `gh attestation verify` against the owning repository;
6. compare the verified attestation subject digest to the release ledger SHA-256;
7. publish the exact same bytes to the intended GitHub release and Google Drive destination;
8. re-download both remote copies and verify their SHA-256/size still match the attested subject.

This ties source commit, workflow identity, final bytes, remote publication, and consumer verification together without weakening any existing GameSync acceptance gate.

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
| Attestation subject | exact subject path/name and SHA-256 digest when provenance is generated |
| Attestation verification | observed `gh attestation verify` result and owning repository |
| SBOM attestation | predicate/type and verification result when produced |
| Publication destination | exact release/Drive/repository object |
| Remote verification | remote size/digest or complete re-download/hash |
| Known exclusions | tests/workspaces not exercised |

This prevents a source commit, generated folder, ZIP, attestation, and remotely published artifact from being conflated as though they were the same thing.

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
10. When the candidate is built in GitHub Actions, generate and verify an artifact attestation for the exact final publishable file without replacing the existing runtime gates.
11. Publish the intended bytes to the durable destinations and verify each remote object before recording the release complete.

## Release procedure: Extension V2

1. Resolve the canonical `Herbertofury/GameSync-Next` revision.
2. Run `npm ci`.
3. Build required shared dependencies and the Extension V2 workspace as needed by the selected command path.
4. Run `npm --workspace apps/extension-v2 run build`.
5. Run lint/typecheck checks relevant to the extension surface.
6. Run `npm run audit:gamesync-parity` for migration/parity-sensitive releases.
7. Run `npm --workspace apps/extension-v2 run verify:same-id-upgrade` when claiming a safe upgrade from the shipping extension.
8. Run `npm run verify:extension-v2:opera` for the real Opera build/runtime lane when available.
9. Run relevant Playwright and extension regression suites. Do not count the currently broken `test:e2e-opera` legacy entrypoint as a pass.
10. For current main, add the Game Tracker/Bounty/Animation feature-specific qualification described above when the candidate touches those features or shared background/UI/storage code.
11. If packaging a release ZIP, run `npm --workspace apps/extension-v2 run zip` only after the candidate build and checks correspond to the source revision being released.
12. Record the final ZIP hash/size, generate and verify build provenance for those exact bytes when using the GitHub Actions release lane, and keep the attestation subject digest in the release ledger.
13. Publish the same verified bytes to the intended GitHub and Drive destinations and re-download/hash both before declaring the release durable.

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

### `npm run test:e2e-opera` fails with a missing file

At current main this is an expected repository defect because the declared `opera-extension/app/tests/e2e.opera-gx.test.js` entrypoint is absent. Use the maintained current verifier/Playwright paths for actual release evidence, record the legacy gate as unresolved, and repair the package script separately rather than suppressing the failure.

### Game Tracker import/export passes locally but fails after packaging

Verify that the candidate was installed from the exact current lockfile, that worker-owned portability modules are present in the generated extension, and that the build being loaded is the exact `.output/chrome-mv3` candidate. The current merge adds `docx`, `mammoth`, `linkedom`, and SheetJS dependencies plus worker-owned DOCX/spreadsheet/export paths, so stale dependency or generated-output reuse can create false local confidence.

### Bounty or Animation works until browser/service-worker restart

Check that the current build preserved background bootstrap message routing, alarm creation, alarm listeners, and persisted state. Treat a release that only works in the initial live service worker as incomplete.

### Secret scan fails

Inspect the finding and remove the sensitive material from the candidate/history as appropriate. Do not disable the Gitleaks release guard merely to publish.

### Attestation verification fails

Treat this as a release-provenance blocker for any release that claims attested provenance. Confirm the artifact bytes match the recorded subject digest, the expected repository owns the attestation, and the tested/downloaded artifact is the same object that the workflow attested. Do not regenerate an attestation over different bytes and present it as proof for the original candidate.

### A ZIP exists but no tested generated directory can be tied to it

The ZIP is not sufficient release proof. Rebuild from a known source revision, test that exact candidate, then regenerate/package and hash the final artifact.

## Verification boundary for this wiki

This page documents the **current repository-declared release and verification mechanisms**, current merged Extension V2 release-surface evidence, and a sourced GitHub artifact-attestation proposal. During this documentation pass, the repositories were inspected remotely and current GitHub documentation was revalidated; this pass did not execute npm builds, launch Opera GX, generate a new ZIP, create a GameSync artifact attestation, or publish a GameSync product release.

The two source baselines inspected were shipping GameSync 0.6.3 at `a8e37976eb0b3ee3c4ec5e802b02d3bfa1f41928` and GameSync Next at `cd906ff0831bf7fc33b41fea31b6f0c004cc1562`, with Extension V2 declaring version 0.8.0.

Project-owned commit evidence for `cd906ff0831bf7fc33b41fea31b6f0c004cc1562` records the Universal Game Tracker, Bounty, and Animation Tracker isolated-Opera acceptance summarized above. Those are retained as project evidence, not re-labeled as tests executed during this wiki-maintenance pass.

## Wiki maintenance triggers

Update this page when any of the following materially changes:

- shipping GameSync version or build layout;
- Extension V2 current main head, version, WXT layout, or output directory;
- Game Tracker, Bounty, Animation Tracker, or another release-critical feature changes the lockfile, background bootstrap, route shell, parity matrix, or Opera verifier;
- extension identity or same-ID migration logic;
- build, ZIP, parity, lint, regression, Playwright, legacy E2E, or Opera verification commands;
- artifact-attestation action/version, provenance policy, SBOM predicate, or verification workflow;
- release/publishing destination;
- generated artifact naming/layout;
- secret scanning or credential boundaries;
- desktop/server packaging flow;
- remote artifact verification procedure.