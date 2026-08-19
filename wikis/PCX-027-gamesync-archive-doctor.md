# GameSync Archive Doctor Wiki

**Project Constellation ID:** `PCX-027`  
**Status:** ACTIVE / TRACKED  
**Confidence:** High for recovered release/checkpoint behavior and support-tool identity; standalone source repository unresolved  
**Current verified integration boundary:** Archive Doctor is proven as a GameSync release/checkpoint support system through the recovered GameSync V2-289 publication evidence. Its standalone source tree is still unresolved.

## Purpose

GameSync Archive Doctor diagnoses, verifies, reassembles, and recovers GameSync release archives without destructive rewriting. Recovery must preserve original bytes, multipart ordering, hashes, provenance, and a browser-accessible fallback when a desktop executable or command script cannot be used.

The strongest current evidence is no longer limited to the older 0.25.9 recovery bundle. Later GameSync publication evidence proves that the same Archive Doctor support tools remained part of the release/checkpoint system through the recovered **GameSync V2-289** checkpoint.

## Current verified support-tool identity

The recovered V2-289 final checkpoint records these exact support tools:

| Tool | SHA-256 | Size |
| --- | --- | ---: |
| `GameSync Archive Doctor.exe` | `d67702d30fc2e81470138bb40b2a309bb6c616137040ff1497fa5b2d87cf2f14` | 2,824,704 bytes |
| `GameSync Archive Doctor - Browser Fallback.html` | `e8c842356443cd2ab9dcffa74402315fb6f11c26f08b7da3d597e4fb6e0db1a5` | 15,693 bytes |

The same two hashes appear in the recovered GameSync 0.25.12 real-browser-launch release manifest, establishing byte-stable support-tool lineage across those later GameSync release/checkpoint records.

This does **not** prove that the standalone Archive Doctor implementation never changed outside those checkpoints. It proves that the exact executable and browser fallback bytes above were the support tools embedded in both verified publication records.

## Verified GameSync V2-289 checkpoint integration

The recovered `v289-final-checkpoint.log` records a complete multipart publication for:

`GameSync-V2-289-APP-EXTENSION-DRIVE-READY.zip`

Verified archive identity:

- archive SHA-256: `3ae361b2faae0551f1e8c4794f99718ace47958fd36e635cfe6136789818c536`
- archive size: `314,083,858` bytes
- source fingerprint SHA-256: `c3eb1edfe91a6c1f4a7997f1acb284e2dd5d2ff69996b745db574ae401d58d6a`
- source file count: `6,478`
- source bytes: `525,300,903`
- multipart count: `13`
- first twelve parts: `25,165,824` bytes each
- final part: `12,093,970` bytes
- archive-doctor manifest: `GameSync-V2-289-APP-EXTENSION-DRIVE-READY.zip.ARCHIVE-DOCTOR.json`
- complete-project flag: `true`

The same checkpoint records oracle-integrity proof for the preserved legacy `opera-extension` tree:

- oracle files: `5,543`
- missing: `0`
- extra: `0`
- mismatches: `0`

This is important because Archive Doctor is part of a larger publication-integrity contract, not merely a convenience unzipper.

## Verified checkpoint fixture behavior

The recovered V2-289 parity run includes two especially relevant fixtures.

### Agent-enforcer fixture

The fixture records successful checks for:

- deterministic archive generation;
- verified checkpoint bytes;
- support-tool tamper detection;
- Archive Doctor part-contract tamper detection;
- embedded oracle proof;
- exact oracle path/count preservation.

### Checkpoint fixture

The checkpoint fixture generates and verifies:

- a normal checkpoint manifest;
- an Archive Doctor manifest;
- a final readiness record;
- multipart archives;
- deep source hashes;
- published Archive Doctor support tools;
- oracle-integrity validation.

Its acceptance evidence also records:

- `atomicReadyLast: true` - readiness is written only after the publication inputs are complete;
- stale multipart cleanup;
- recursive checkpoint exclusion;
- transient gate exclusion;
- publication readback claims only after verification;
- failed oracle publication revokes readiness;
- republishing can change the part count while preserving the new authoritative archive identity.

The recovered fixture command names are:

```text
python tools/run-agent-enforcer-fixture.py
python tools/run-checkpoint-fixture.py
```

These commands belong to the recovered GameSync V2-289 source/checkpoint evidence. Do not assume they exist unchanged in an unrelated or newer repository checkout until that exact source tree is resolved.

## Browser fallback

A connected Drive artifact named **GameSync Archive Doctor - Browser Fallback.html** has been inspected directly. It is a standalone local HTML application designed to run in Chrome or Opera GX without CMD, PowerShell, installation, administrator access, or a network connection.

### What the browser fallback accepts

The source recognizes multipart filenames shaped like:

```text
<archive>.zip.part000
<archive>.zip.part001
<archive>.zip.part002
```

and also accepts `.bin` suffix variants. Its matcher also supports a generic `<name>.partNNN` form.

The UI asks the operator to select:

- every multipart archive part;
- a manifest JSON when available; or
- a SHA-256 text file as supporting evidence.

The JSON path specifically looks for an object containing an `archive` field plus a `parts` array.

### Verification workflow

1. Open the standalone HTML file in Chrome or Opera GX.
2. Select every archive part and the matching manifest/evidence file.
3. Click **Verify selected parts**.
4. Review the diagnosis table for part number, size, SHA-256, and status.
5. Resolve missing, duplicate, wrong-size, or hash-mismatched parts before reassembly.
6. Use **Reassemble + verify to disk** only after the selected part set passes the required checks.
7. Preserve the original parts after successful reassembly until the resulting archive identity has been independently recorded.

### Browser verification mechanics

The inspected source performs these operations locally in the browser:

- groups duplicate candidates by part index;
- sorts candidate filenames deterministically;
- detects missing part indexes;
- compares expected part size when the manifest provides it;
- computes SHA-256 incrementally from the selected file stream;
- compares expected part SHA-256 when available;
- retries transient read/hash failures up to five times;
- logs retry failures rather than silently accepting them;
- reports expected full-archive name and SHA-256 when present in the manifest;
- keeps a visible operation log and progress state.

The artifact is self-contained and does not rely on a network service for hashing or reconstruction.

Drive artifact ID for the inspected browser fallback: `1AxF4x0ts4XPjXP5iZ_QaYU6vAYpR4cY7`.

## Desktop executable boundary

The recovered browser fallback states that the full desktop edition adds:

- deep per-entry ZIP CRC testing;
- clean-entry salvage.

The V2-289 checkpoint proves the Windows executable's byte identity and inclusion as a support tool, but the executable source code has not been resolved in the connected GitHub surface. Therefore this wiki does not invent desktop CLI flags, build commands, internal archive-library details, or salvage semantics that cannot be verified from source.

Treat the desktop tool as a verified published binary with a recovered behavioral claim, not as a fully source-documented subsystem yet.

## Recovered 0.25.12 publication lineage

The `GameSync-0.25.12-REAL-BROWSER-LAUNCH-SHA256SUMS-FULL.txt` manifest records a later release that already used the same support-tool bytes:

- full release archive: `GameSync-0.25.12-REAL-BROWSER-LAUNCH-FINAL-FULL.zip`
- full archive SHA-256: `b13a417bb168560b5d2d25f06740edaf16f8f2504997ef14a0f9dd3317eda238`
- multipart parts: `part000` through `part003`
- Archive Doctor manifest SHA-256: `638764304c5a3867d7606ac1e05df98a00d47e9b9f8ff97055f946f98263d34a`
- Archive Doctor executable SHA-256: `d67702d30fc2e81470138bb40b2a309bb6c616137040ff1497fa5b2d87cf2f14`
- browser fallback SHA-256: `e8c842356443cd2ab9dcffa74402315fb6f11c26f08b7da3d597e4fb6e0db1a5`

Drive manifest ID: `147f0-A6wCjo5Sh8m1T7JuwS1-iPGNWHV`.

This is stronger continuity evidence than treating the older 0.25.9 bundle as the latest known use of Archive Doctor.

## Historical 0.25.9 recovery-system manifest

The older durable `GameSync-0.25.9-Archive-Doctor-Recovery-System-SHA256SUMS.txt` remains important immutable lineage evidence.

It records:

- full archive SHA-256: `003ffb12625fae420cc9677f43d8e78e0d77a43a0222a63c5ae926f03527f1ac`
- part000 SHA-256: `586f256086697f738704d05def84a670e7822d2c6864370387d1f70289672147`
- part001 SHA-256: `463662500f118665a5d5e381183315a043aa0b1da2475010018650c180a50cc9`
- part002 SHA-256: `9a1a9787199012e148b82cf716c31f28fc5bb09a617bda50414df036290a5607`
- Archive Doctor manifest SHA-256: `ee5c36c12ea0d89ea3f3e9c970be77fce1d8df96fbbb532c995a807d824279dc`

Drive manifest ID: `1OKQ0W6R3ph1E_WNZCVzWjHV0sjUgHnwK`.

Do not discard this older manifest merely because later release evidence exists.

## Recovery architecture contract

Archive Doctor should continue to preserve distinct phases:

1. **Inventory:** identify the intended archive and all candidate parts without modifying them.
2. **Part integrity:** verify size/hash for every part where authoritative values exist.
3. **Duplicate resolution:** compare duplicate copies by expected size/hash rather than filename timestamp alone.
4. **Ordering:** establish a deterministic part sequence from explicit indexes.
5. **Reassembly:** create a new output and never overwrite source parts.
6. **Whole-archive verification:** verify the expected final SHA-256 when known.
7. **Container validation:** inspect ZIP/archive structures and per-entry integrity when the desktop path supports it.
8. **Salvage:** write verified recoverable entries to a separate destination rather than editing the damaged source in place.
9. **Provenance:** record every source part/hash, manifest identity, output hash, and publication/checkpoint identity.
10. **Readiness:** publish a READY/complete claim only after the final remote or local artifact has been verified.

## Troubleshooting

### A part is reported missing

Confirm that every `.partNNN` file was selected and that indexes are contiguous. Do not rename a different part into the missing index merely to satisfy the UI. Recover the correct source part or authoritative duplicate.

### Duplicate copies exist

The browser fallback groups candidates by part index. Prefer the candidate matching the authoritative expected size and SHA-256. A newer file timestamp is not proof of correctness.

### A part repeatedly fails hashing

The browser fallback already retries read/hash failures up to five times. Continued failure should be treated as a real input or storage problem, not bypassed. Preserve the failed file and obtain a second copy before replacing anything.

### The manifest is missing

The browser can still infer part indexes and archive naming from filenames, but authoritative expected sizes and hashes may be unavailable. In that state, reconstruction is weaker evidence. Locate the matching Archive Doctor/upload/SHA manifest before claiming a verified release.

### Reassembled ZIP opens but integrity is uncertain

Opening a ZIP is not sufficient. Compare the final SHA-256 against the authoritative release/checkpoint hash, then use the desktop per-entry verification path when available.

### Security software blocks the executable

Use the standalone browser fallback for part inventory, hashing, duplicate selection, and reassembly/whole-archive verification. Preserve the exact executable rather than replacing it with an unverified tool.

### Publication says READY but a later readback differs

Treat readiness as invalid. The recovered checkpoint fixture explicitly requires verified readback before a publication claim and records failure paths that revoke readiness.

## Current technology research

### libarchive 3.8.9

The official [libarchive](https://github.com/libarchive/libarchive) project published **3.8.9** on 2026-07-28 as a security, bugfix, and minor-feature release. The release includes a Windows `unzip` port and current signed release archives.

**Proposal:** evaluate libarchive 3.8.9 as an optional desktop/native verification backend for formats and per-entry validation that exceed the browser fallback's scope. Keep the browser fallback self-contained and dependency-free.

**Why it fits:** Archive Doctor needs trustworthy entry-level archive validation and recovery across damaged/multipart inputs without inventing custom parsers for every format.

**Integration cost:** medium. A native adapter, deterministic error mapping, fixed fixture corpus, and packaging for Windows are required.

**Risks:** changing archive engines can alter tolerance, filename encoding, timestamp, or extraction semantics. Recovery must never mutate the original source archive or silently repair bytes in place.

**Small experiment:** run libarchive against copies of known-good, truncated, wrong-order, duplicate-part, CRC-corrupt, and single-entry-corrupt fixtures, comparing diagnosis against the existing Archive Doctor manifest logic.

**Acceptance test:** correct archives verify byte-for-byte; corrupt fixtures fail deterministically; recoverable entries are copied to a separate destination with provenance; original inputs remain unchanged; browser fallback results remain available and consistent for overlapping cases.

## Anti-degradation contract

- Never overwrite source archives or parts.
- Never mark an archive repaired solely because it opens.
- Never skip missing-part, expected-size, or hash failures to get a successful result.
- Never remove the browser fallback when adding native capabilities.
- Never replace exact support-tool bytes inside a verified checkpoint without recording a new hash and compatibility result.
- Never weaken oracle/source completeness checks merely to publish a smaller artifact.
- Never write READY before the artifact and its required remote/local readback have been verified.
- Never trade complete integrity checks for faster superficial scans.

## Current stop point

The standalone Archive Doctor source repository and current desktop implementation source are still unresolved. However, the tool is now strongly grounded as a real part of the later GameSync publication/checkpoint pipeline through 0.25.12 and the recovered V2-289 checkpoint and parity fixtures.

The next documentation/source-resolution task is therefore narrower than before: locate the implementation source that produced the exact `d677...` executable and `e8c842...` browser fallback, then map that source to the recovered checkpoint-fixture contract without replacing the verified binaries first.

## Exact next action

1. Resolve the project-owned source that produced the verified support-tool hashes.
2. Recreate the V2 checkpoint fixture from that source with known-good, missing-part, duplicate-part, wrong-order, part-tamper, support-tool-tamper, CRC-corrupt, and single-entry-corrupt cases.
3. Prove browser and desktop paths agree on overlapping integrity failures.
4. Preserve deep source hashes, oracle integrity, atomic readiness, stale-part cleanup, and readback-before-ready behavior.
5. Only after exact parity is established, evaluate a newer native archive backend such as libarchive.

## Documentation gaps

- Standalone source repository for the verified support-tool bytes is unresolved.
- Exact desktop build command/toolchain remains unresolved.
- Desktop per-entry salvage behavior is claimed by the browser artifact but not yet verified from source.
- The precise repository commit corresponding to the recovered V2-289 checkpoint source snapshot is unresolved.

## Wiki maintenance

Update this page when the standalone source identity is resolved, support-tool hashes change, a new GameSync checkpoint uses a newer Archive Doctor build, checkpoint/readback semantics change, recovery fixtures expand, archive backends change, or desktop salvage behavior becomes source-verified. Preserve historical 0.25.9 and 0.25.12 manifests as immutable lineage evidence.
