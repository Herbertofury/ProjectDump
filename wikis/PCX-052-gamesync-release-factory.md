# GameSync Release Factory Wiki

**Project ID:** PCX-052  
**Project Constellation goal:** Create reproducible GameSync application and extension release artifacts from canonical source.  
**Documentation status:** Current source-grounded release/build contract  
**Primary shipping repository:** `Herbertofury/Gamesync`  
**Primary migration repository:** `Herbertofury/GameSync-Next`

## Purpose

GameSync Release Factory is the release-discipline track around GameSync rather than a separate product repository. Its job is to turn canonical GameSync source into reproducible build outputs, prove that the candidate being tested is the candidate being packaged, exercise the actual browser/application workflows that matter, preserve extension identity and user state, keep generated artifacts separate from editable source, and publish the final tested bytes durably.

A successful source edit is **not** a release. A release candidate is complete only when the exact source revision, dependency state, generated output, runtime verification, final packaged artifact, and remote publication can be tied together with evidence.

## Current production authorities

### Shipping JavaScript extension

Repository: `Herbertofury/Gamesync`  
Current `main`: `a8e37976eb0b3ee3c4ec5e802b02d3bfa1f41928`  
Current package version: **0.6.3**

The shipping repository separates:

- `app/` - canonical editable extension source;
- `dist/` - generated production extension;
- `vite.config.ts` and `package.json` - build tooling;
- `scripts/`, `dev/`, `rust/`, `docs/`, and `reference/` - supporting development material.

`dist/` is the unpacked Opera GX runtime target. It is generated from `app/` and must not be treated as the editable source of truth.

### GameSync Next / Extension V2

Repository: `Herbertofury/GameSync-Next`  
Current `main`: `cd906ff0831bf7fc33b41fea31b6f0c004cc1562`  
Extension V2 package version: **0.8.0**

The migration repository is workspace-based. Extension V2 lives under `apps/extension-v2` and uses WXT, TypeScript, React, and shared GameSync packages. The generated Chromium Manifest V3 build used by current verification lives at:

```text
apps/extension-v2/.output/chrome-mv3
```

That generated directory is a test/release input, not canonical source.

Current `main` includes the verified Universal Game Tracker, Bounty, and Animation Tracker recovery merge and therefore has a materially broader release surface than the earlier `9e337c720f0180cffa577f140b181c699f0a1650` baseline.

## Source versus generated output

Release work must preserve this separation:

| Lane | Canonical source | Generated runtime/output |
| --- | --- | --- |
| Shipping extension | `Gamesync/app/` | `Gamesync/dist/` |
| Extension V2 | `GameSync-Next/apps/extension-v2/` plus shared packages | `apps/extension-v2/.output/chrome-mv3` |
| Extension V2 packaged artifact | same source as above | output from `wxt zip` |
| Desktop/server | their workspace source | built workspace artifacts |

Never repair a release by editing a generated folder directly. Fix the source/build configuration, rebuild, and re-verify the regenerated product.

## Shipping GameSync build and validation

From the shipping repository root:

```powershell
npm ci
npm run build
```

`npm run build` executes `vite build`. The Vite configuration uses `app/` as the root, clears `dist/`, builds the popup/options/panel/full/offscreen/background/content entry points, and runs the repository runtime-closure logic that copies required non-bundled runtime material.

The runtime closure includes the manifest, locales, packs, themes, extension surfaces, mascot/shimeji assets, voice/WASM/template/test assets, and other explicitly enumerated runtime files. Because `dist/` is cleared first, release validation must target the newly generated `dist/`, not a stale unpacked copy.

Current shipping commands include:

```powershell
npm run dev
npm run build
npm run test:bounty
npm run benchmark:bounty
npm run build:wasm:legacy-accel
npm run preview
```

`build:wasm:legacy-accel` additionally requires the Rust/`wasm-pack` toolchain and should be run only when that subsystem is actually part of the change.

### Shipping Opera target

After a successful build, load:

```text
<clone-directory>\dist
```

as the unpacked Opera GX extension. Loading `app/` directly bypasses the production build contract and does not prove the shipping artifact works.

## GameSync Next build pipeline

At repository root:

```powershell
npm ci
npm run build
```

The root build covers the shared package graph and the named application workspaces included by that script. Feature Foundry, HyperBowl, Extension V2, or another independently named workspace must not be assumed covered unless its command actually runs.

### Extension V2 build

```powershell
npm --workspace apps/extension-v2 run build
```

The workspace build runs:

1. `wxt build`;
2. `verify:offscreen-runtime`.

A candidate that skips the second step is not equivalent to the repository-declared build.

### Extension V2 ZIP

```powershell
npm --workspace apps/extension-v2 run zip
```

This delegates to `wxt zip`. Record the actual produced filename, byte size, and digest from the environment that created it rather than assuming a historical filename.

## Extension identity and upgrade safety

Extension V2 is Manifest V3 and currently declares version **0.8.0**. The current same-ID verifier expects extension ID:

```text
piihebkkniekgkehlpkjdmhnhndccaai
```

Run:

```powershell
npm --workspace apps/extension-v2 run verify:same-id-upgrade
```

The verifier writes sentinels into `chrome.storage.local`, `chrome.storage.sync`, and IndexedDB under the legacy extension, loads the V2 build, verifies the same extension ID and expected version, confirms those stores survived the upgrade, restarts Opera, and checks identity/version again.

A clean build without this test does not prove upgrade safety.

Useful environment input includes `GAMESYNC_LEGACY_EXTENSION_PATH` when the shipping source is not in a supported sibling layout and `OPERA_GX_PATH` when Opera GX is not discoverable automatically.

## Current Opera verification

GameSync Next exposes:

```powershell
npm run verify:extension-v2:opera
npm --workspace apps/extension-v2 run verify:opera
```

The root command rebuilds Extension V2 before calling `scripts/verify-extension-v2-opera.js`. The workspace command invokes the verifier directly and therefore assumes a suitable generated build already exists.

The verifier targets:

```text
apps/extension-v2/.output/chrome-mv3
```

and can launch Opera GX, stage a smoke copy, connect through Chrome DevTools Protocol, exercise extension/runtime surfaces, and preserve reports/traces.

Relevant environment controls include:

- `OPERA_GX_EXE`;
- `GAMESYNC_V2_TARGET_URL`;
- `GAMESYNC_V2_EXTENSION_ID`;
- `GAMESYNC_V2_OPERA_PROFILE`;
- `GAMESYNC_V2_ARTIFACT_DIR`;
- `GAMESYNC_V2_REPORT`;
- `GAMESYNC_V2_TRACE`;
- `GAMESYNC_V2_OPERA_DEBUG_PORT`;
- `GAMESYNC_VERIFY_TRANSFORMERS`;
- `GAMESYNC_V2_PRESERVE_PROFILE`;
- `GAMESYNC_V2_USE_LOAD_EXTENSION_FLAGS`.

Do not report Opera verification as passed unless the exact candidate completed the verifier and its evidence can be tied to the candidate source/build identity.

## Current `test:e2e-opera` compatibility defect

Current `main` still declares:

```text
node opera-extension/app/tests/e2e.opera-gx.test.js
```

for `test:e2e-opera`, but that file is absent on current `main`. Therefore:

```powershell
npm run test:e2e-opera
```

must **not** be represented as a working release gate on current `main`.

Draft GameSync Next PR #15 stages a compatibility entrypoint that delegates to the maintained `verify:extension-v2:opera` path, but the PR remains unmerged and fail-closed pending exact-head execution. Until it is actually merged and reverified, use the maintained verifier and present Playwright lanes for real evidence and record the legacy entrypoint as unresolved.

## Parity gate

GameSync Next contains an executable shipping-to-V2 parity audit:

```powershell
npm run audit:gamesync-parity
```

The current audit rebuilds Extension V2 before reading generated manifest output in a clean checkout. The machine-readable parity contract is `docs/gamesync-parity-matrix.json`.

Treat parity as a distinct release gate. Compilation does not prove feature parity, and structural audit success must not be confused with every runtime capability being fully equivalent.

## Current merged Extension V2 release surface

Current `main` materially expands the release surface with three verified feature groups.

### Universal Game Tracker

The merge adds typed tracker records, Dexie persistence, schema/record editors, relationships, worker-owned import/export, DOCX/XLSX/XLS/CSV/TSV/JSON handling, Google Docs/Sheets export-URL handling, Word dropdown extraction, and binary image handling.

Current direct portability dependencies include:

- `docx` `^9.7.1`;
- `linkedom` `^0.18.12`;
- `mammoth` `^1.12.0`;
- SheetJS `xlsx` from the explicit `0.20.3` CDN tarball.

Project-owned merge evidence records isolated Opera imports from both a 43 MB local DOCX and a live Google Doc path, each producing 181 active records, 75 relationships, and 124 schema-bound images, with editable state and JSON/XLSX/DOCX/CSV export checks. Preserve those results as project-owned evidence, not as tests rerun by this wiki-maintenance pass.

### Bounty

The merge adds typed Bounty contracts, service/background routing, reminder alarms, UI routing, and persistence. Project-owned evidence records a clean isolated Opera synchronization of 107 live GamerPower records with a rendered calendar and healthy source state.

A release touching shared background/bootstrap/storage code must re-qualify Bounty message routing, alarms, persisted state, source failure visibility, and the built route.

### Animation Tracker

The merge adds creator/pack contracts, HTTPS source validation, version detection/comparison, polling state, alarm handling, UI routes, and persistence. Project-owned evidence records a real HTTPS poll, semantic-version detection, and an available update rendered without remounting the React root.

A release touching shared background/bootstrap/storage code must re-qualify the Animation Tracker polling/alarm/persistence lifecycle.

## Current package-manager security proposal: npm 12

A new coordinated release-engineering proposal appeared after the previous Release Factory checkpoint. It is **draft, branch-only, and unmerged**; it is not current production behavior.

### GameSync Next proposal

PR: `Herbertofury/GameSync-Next#23`  
Base: current `main` `cd906ff0831bf7fc33b41fea31b6f0c004cc1562`  
Exact proposal head observed for this wiki: `14d35f4f7dea811af2b3e7a4056a676e217f0072`  
Proposed npm: **12.0.2**

The proposal deliberately treats npm 12 as a security-policy migration, not a version-only bump. It stages:

- `engines.npm = 12.0.2`;
- fail-closed `devEngines` for npm 12.0.2 and Node `^24.15.0 || >=26.0.0`;
- root-workspace `allowScripts` as the single project policy;
- exact install-script approvals derived from the committed lockfile;
- `.npmrc` with `strict-allow-scripts=true`;
- `allow-git=none`;
- `allow-remote=root` because Extension V2 directly declares the reviewed SheetJS CE tarball URL;
- verification that rejects missing, stale, overbroad, or unexpected install-script/remote-source permissions.

The current proposal lists only lockfile identities requiring install-script approval, including Playwright browser Chromium, BabylonJS, better-sqlite3, optional canvas, esbuild, fsevents, onnxruntime-node, protobufjs, nested sharp, and wasm-pack identities present in that graph.

### Shipping GameSync paired proposal

PR: `Herbertofury/Gamesync#5`  
Base: current shipping `main` `a8e37976eb0b3ee3c4ec5e802b02d3bfa1f41928`  
Exact proposal head observed for this wiki: `2990dad9134d066bcc5593ee0f9c10751a8e4a97`  
Proposed npm: **12.0.2**

The shipping proposal applies the same Node/npm policy but deliberately uses:

```text
allow-git=none
allow-remote=none
strict-allow-scripts=true
```

because the current shipping direct graph does not require the GameSync Next SheetJS remote tarball. Its present install-script approval is limited to the exact `fsevents@2.3.3` identity in the committed graph.

### Why this matters to Release Factory

npm 12 changes release reproducibility and supply-chain acceptance. Current npm 12.0.2 documentation exposes `allowScripts`, `strict-allow-scripts`, `allow-git`, and `allow-remote` controls; `strict-allow-scripts=true` makes an unreviewed dependency install script a hard install failure instead of silently normalizing trust.

As of this checkpoint, Node **26.7.0 Current** still ships npm **11.19.0**, so selecting npm 12.0.2 is a deliberate project toolchain decision rather than merely inheriting the npm bundled with the newest Node binary.

If the proposal is eventually promoted, the release ledger must record all of the following separately:

1. exact Node version;
2. exact npm version;
3. exact lockfile digest;
4. exact `allowScripts` policy and zero pending approvals;
5. `allow-git` / `allow-remote` policy;
6. frozen `npm ci` result;
7. proof that `npm ci` did not mutate the committed lockfile;
8. security audit result;
9. affected builds/runtime gates;
10. exact final artifact digest and publication proof.

Do **not** use `dangerously-allow-all-scripts`, `allow-remote=all`, hand-edited lock metadata, skipped install scripts, or reduced browser/runtime coverage as a way to make a candidate pass.

### Required severe acceptance before promotion

The coordinated proposal requires npm 12.0.2 verification on Node 24.19.0 and Node 26.7.0, frozen install, zero pending script approvals, immutable lockfile, security audit, affected product builds, parity checks, exact-build Ferrum acceptance, and real Opera GX fresh/restart evidence. GameSync Next additionally covers its broader workspace build graph and fresh standalone parity audit.

Until those exact-head gates actually execute and the PRs merge, **current main remains npm-11-era production source** for release documentation purposes.

## Regression and browser commands in GameSync Next

Current root commands include:

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
npm run test:extension-regression
npm run verify:extension-v2:opera
```

Use the checks relevant to the changed release surface. A single green build is not a substitute for affected regression, parity, restart, persistence, or real-browser checks.

## Security and credential boundary

The shipping repository and GameSync Next both carry secret-scanning workflows. Record the exact repository and exact source revision that supplied security evidence; a sibling repository's passing scan is not interchangeable proof.

Steam, Nexus Mods, Twitch, and other user credentials belong in browser-managed/runtime storage and must not be bundled into source or generated release artifacts. The public Manifest key is extension identity material, not a private signing credential.

Before publication, inspect the exact archive/directory being shipped rather than assuming `.gitignore` or CI alone prevents local material from entering the artifact.

## Artifact attestations and provenance

GitHub artifact attestations can be an additive release layer for final GameSync ZIPs/binaries. When used, bind the attestation to the exact final publishable file and keep its subject digest in the release ledger.

A suitable workflow can:

1. build the final artifact from the exact source revision;
2. compute SHA-256 and byte size;
3. generate GitHub build provenance for that exact file;
4. optionally generate and attest SPDX/CycloneDX SBOM data;
5. download the artifact in a fresh environment;
6. run `gh attestation verify` against the owning repository;
7. compare the verified subject digest to the release ledger;
8. publish the same bytes to GitHub and Drive;
9. re-download/hash both remote copies.

Attestation does not replace functional browser/application acceptance. A cryptographically proven broken build is still broken.

## Required release ledger

Record at least:

| Field | Required evidence |
| --- | --- |
| Project lane | shipping GameSync, Extension V2, desktop/server, or named workspace |
| Repository | exact `owner/name` |
| Source revision | full commit SHA |
| Declared version | exact package/manifest version |
| Node version | exact runtime used by the candidate |
| npm version | exact package manager used by the candidate |
| Lockfile identity | digest and no-mutation/frozen-install evidence |
| Install-script policy | exact `allowScripts` and pending-approval result when applicable |
| Remote-source policy | exact `allow-git` and `allow-remote` policy when applicable |
| Build command | exact command actually executed |
| Generated output | exact path/file tested |
| Build result | observed result |
| Regression checks | exact suites/results |
| Runtime check | exact Opera/browser/app workflow/result |
| Identity check | extension ID/version and migration result where applicable |
| Packaging command | exact command used |
| Artifact digest | SHA-256 of final publishable file |
| Artifact size | final bytes |
| Attestation | subject digest/verification result when used |
| Publication destination | exact GitHub/Drive/release object |
| Remote verification | provider digest/size or complete re-download/hash |
| Known exclusions | relevant gates not exercised |

This prevents source, lockfile, generated folder, ZIP, attestation, and remote publication from being conflated.

## Release procedure: shipping GameSync

1. Resolve current canonical `Gamesync/main` and intended version.
2. Resolve the project's declared Node/npm policy for that exact source revision; do not apply a draft npm 12 branch policy to current `main` by assumption.
3. Install from the candidate lockfile using the exact supported package manager, normally frozen `npm ci`.
4. Run affected regression/security checks.
5. Run `npm run build`.
6. Confirm `dist/` was freshly regenerated and contains the expected runtime closure.
7. Load the new `dist/` in the real target Opera GX environment for the affected workflow.
8. Inspect service-worker/content/page console/runtime failures relevant to the change.
9. Package the tested generated product using the project's real release path.
10. Record final file size/SHA-256.
11. Generate/verify provenance when using the attested GitHub Actions lane.
12. Publish the same tested bytes to the intended durable destinations.
13. Re-download or provider-verify both destinations before recording publication complete.

## Release procedure: Extension V2

1. Resolve current canonical `GameSync-Next/main`.
2. Resolve the exact Node/npm/lockfile policy for that source revision.
3. Run the supported frozen install.
4. Build affected shared packages/workspaces.
5. Run `npm --workspace apps/extension-v2 run build`.
6. Run relevant lint/type/regression suites.
7. Run `npm run audit:gamesync-parity` for migration/parity-sensitive releases.
8. Run `verify:same-id-upgrade` when claiming a safe legacy-to-V2 upgrade.
9. Run `npm run verify:extension-v2:opera` and relevant Playwright extension lanes.
10. Do not count the current missing-file `test:e2e-opera` compatibility path as passing until its repair is actually merged and verified.
11. Add current feature-specific Game Tracker/Bounty/Animation qualification when shared background/UI/storage or those features are affected.
12. Run `npm --workspace apps/extension-v2 run zip` only after the candidate being packaged matches the candidate tested.
13. Hash the final ZIP and record bytes.
14. Generate/verify provenance when used.
15. Publish the exact tested bytes to GitHub and Drive.
16. Re-download/hash both remote copies before declaring the release durable.

## Modifying the release factory

### Add a release check

Prefer a deterministic command that runs from a clean checkout, fails non-zero when the acceptance condition is unmet, and either produces evidence itself or points to a machine-readable result. If it consumes generated output, make the build dependency explicit so stale artifacts cannot create false passes.

### Add a generated artifact

Document its canonical inputs, generator command, output location, reproducibility expectations, consumer runtime, validation checks, source-control status, packaging role, and final publication identity.

### Change extension identity

Treat any manifest identity change as migration-sensitive. Update and rerun same-ID expectations deliberately. Never dismiss an accidental extension-ID change as packaging noise.

### Change workspace version

Update package/manifest versions together with verifier expectations that intentionally assert them. The current same-ID verifier expects V2 version 0.8.0.

### Change package manager

Treat it as release infrastructure and supply-chain behavior, not cosmetic tooling. Version, engine policy, lockfile format/identity, install-script approvals, remote-source policy, CI images, developer instructions, security gates, and generated product qualification must move coherently.

## Troubleshooting

### `dist/` differs from `app/`

Expected: `dist/` is generated. Fix source/build closure and rebuild; do not ship `app/` as a workaround.

### Opera GX is not found

Use the environment variable expected by the selected verifier: same-ID uses `OPERA_GX_PATH`; the maintained Extension V2 verifier uses `OPERA_GX_EXE`.

### Same-ID verification loses storage

Block the upgrade claim. Check extension identity, loaded profile/build, and migration/storage behavior. Do not weaken sentinel checks.

### Parity only fails in a clean checkout

Treat that as a build dependency/stale-generated-output defect. The parity audit should rebuild what it consumes rather than relying on old generated files.

### `npm run test:e2e-opera` reports a missing file

That is a known current-main compatibility defect. Use the maintained verifier for actual evidence and keep PR #15 fail-closed until its compatibility entrypoint is merged and proven.

### `npm ci` fails after npm 12 policy is adopted

Do not bypass policy globally. Identify the exact dependency/source that is blocked, confirm it is required and reviewed, add the narrowest identity-scoped approval, regenerate authoritative lock/policy state with the real package manager, and rerun the full severe matrix.

### Game Tracker works before packaging but fails after packaging

Verify exact lockfile/dependency identity, generated worker/runtime closure, and the exact `.output/chrome-mv3` build loaded. The current merge adds document/spreadsheet parser/export dependencies that stale installs or stale output can omit.

### Bounty/Animation works only before service-worker restart

Check background bootstrap routing, alarm listeners, alarms, and persisted state. Initial-worker-only success is incomplete release evidence.

### Secret scan fails

Investigate and remove the sensitive material appropriately. Do not disable the release guard to publish.

### Attestation verification fails

Treat attested provenance as failed until artifact bytes, subject digest, repository ownership, and tested/downloaded object identity agree.

### A ZIP exists but cannot be tied to the tested generated build

Rebuild from a known revision, test that candidate, regenerate the package, and re-hash. The existence of a ZIP is not release proof.

## Verification boundary for this wiki

This page documents the current repository-declared release mechanisms, current merged Extension V2 release surface, the new coordinated npm 12.0.2 security-policy proposals, and current upstream npm/Node behavior relevant to that proposal.

This wiki-maintenance pass did **not** merge either npm 12 proposal, execute a GameSync product build, launch Opera GX, publish a GameSync product release, or create a new GameSync artifact attestation. Draft proposal evidence is therefore kept separate from current-main product authority.

Current main authorities remain:

- shipping GameSync `a8e37976eb0b3ee3c4ec5e802b02d3bfa1f41928`, version 0.6.3;
- GameSync Next `cd906ff0831bf7fc33b41fea31b6f0c004cc1562`, Extension V2 version 0.8.0.

Current draft package-manager proposal heads observed for this checkpoint are:

- `Gamesync#5`: `2990dad9134d066bcc5593ee0f9c10751a8e4a97`;
- `GameSync-Next#23`: `14d35f4f7dea811af2b3e7a4056a676e217f0072`.

Re-read active PRs before executing from a recorded SHA because proposal heads can advance.

## Wiki maintenance triggers

Update this page when any of the following materially changes:

- shipping GameSync source/version/build layout;
- GameSync Next current `main`, Extension V2 version, WXT layout, output directory, or release-critical feature surface;
- Node/npm/package-manager policy, lockfile format, install-script approval model, or remote dependency policy;
- paired release/security proposal state or exact head when it materially changes the release contract;
- extension identity or same-ID migration logic;
- build, ZIP, parity, lint, regression, Playwright, Opera, or compatibility-entrypoint commands;
- artifact attestation/SBOM/provenance policy;
- security scanning or credential boundaries;
- desktop/server packaging flow;
- remote publication and byte-verification procedure.
