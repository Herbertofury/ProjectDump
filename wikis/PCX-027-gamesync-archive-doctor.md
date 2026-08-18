# GameSync Archive Doctor Wiki

**Project Constellation ID:** `PCX-027`
**Status:** ACTIVE / TRACKED
**Confidence:** High for recovered artifact lineage; canonical source repository unresolved

## Purpose

GameSync Archive Doctor exists to diagnose, verify, reassemble, and recover GameSync release archives without destructive rewriting. Recovery must preserve original bytes, multipart ordering, hashes, provenance, and a browser-accessible fallback when desktop tools or command execution are unavailable.

## Current verified durable artifacts

### Browser fallback

A current connected Drive artifact named **GameSync Archive Doctor - Browser Fallback.html** was verified in this pass. It is a standalone local HTML application designed to run in Chrome or Opera GX without CMD, PowerShell, installation, administrator access, or a network connection.

Verified behavior present in the artifact source includes:

- selecting multipart `.part000`, `.part001`, later parts, `.bin` variants, and manifest/SHA files;
- duplicate/index grouping and deterministic part ordering;
- expected-size and SHA-256 checks;
- five read/hash retry attempts for transient file-read failures;
- progress/status reporting;
- local reassembly and full-archive SHA-256 verification;
- browser-only recovery rather than a network service.

The artifact also states that the full desktop edition adds deep per-entry ZIP CRC testing and clean-entry salvage.

Drive artifact ID: `1AxF4x0ts4XPjXP5iZ_QaYU6vAYpR4cY7`

### Recovered v0.25.9 recovery-system hash manifest

The durable `GameSync-0.25.9-Archive-Doctor-Recovery-System-SHA256SUMS.txt` records:

- full archive SHA-256: `003ffb12625fae420cc9677f43d8e78e0d77a43a0222a63c5ae926f03527f1ac`
- part000 SHA-256: `586f256086697f738704d05def84a670e7822d2c6864370387d1f70289672147`
- part001 SHA-256: `463662500f118665a5d5e381183315a043aa0b1da2475010018650c180a50cc9`
- part002 SHA-256: `9a1a9787199012e148b82cf716c31f28fc5bb09a617bda50414df036290a5607`
- Archive Doctor manifest SHA-256: `ee5c36c12ea0d89ea3f3e9c970be77fce1d8df96fbbb532c995a807d824279dc`

Drive manifest ID: `1OKQ0W6R3ph1E_WNZCVzWjHV0sjUgHnwK`

## Current stop point

The recovery artifacts and browser fallback are durable, but the canonical source repository and current desktop implementation source have not yet been resolved from connected GitHub evidence. Do not reimplement or replace the recovered browser fallback merely because the source repository is missing.

## Exact next action

Resolve the newest source package/repository for Archive Doctor, then build a fixed corruption/partial-archive fixture suite that proves browser and desktop recovery paths preserve identical source bytes and report the same integrity failures.

## Current technology research

### libarchive 3.8.9

The official [libarchive](https://github.com/libarchive/libarchive) project published **3.8.9** on 2026-07-28 as a security, bugfix, and minor-feature release. The release includes a Windows `unzip` port and current signed release archives.

**Proposal:** evaluate libarchive 3.8.9 as an optional desktop/native verification backend for formats and per-entry validation that exceed the browser fallback's scope. Keep the browser fallback self-contained and dependency-free.

**Why it fits:** Archive Doctor needs trustworthy entry-level archive validation and recovery across damaged/multipart inputs without inventing custom parsers for every format.

**Integration cost:** medium. A native adapter, deterministic error mapping, fixed fixture corpus, and packaging for Windows are required.

**Risks:** switching archive engines can change tolerance, filename encoding, timestamp, or extraction semantics. Recovery must never mutate the original source archive or silently "repair" bytes in place.

**Small experiment:** run libarchive against copies of known-good, truncated, wrong-order, duplicate-part, CRC-corrupt, and single-entry-corrupt fixtures, comparing diagnosis against the existing Archive Doctor manifest logic.

**Acceptance test:** correct archives verify byte-for-byte; corrupt fixtures fail deterministically; recoverable entries are copied to a separate destination with provenance; original inputs remain unchanged; browser fallback results remain available and consistent for overlapping cases.

## Recovery architecture contract

Archive Doctor should maintain distinct phases:

1. **Inventory:** identify archive and parts without modifying them.
2. **Part integrity:** verify size/hash for every part.
3. **Ordering:** establish a deterministic part sequence.
4. **Reassembly:** create a new output, never overwrite source parts.
5. **Whole-archive verification:** verify expected full hash when known.
6. **Container validation:** inspect ZIP/archive structures and per-entry integrity.
7. **Salvage:** copy only verified recoverable entries to a separate tree.
8. **Provenance:** record every source part/hash and every output hash.

## Anti-degradation contract

- Never overwrite source archives or parts.
- Never mark an archive repaired solely because it opens.
- Never skip missing-part or hash failures to get a successful result.
- Never remove the browser fallback when adding native capabilities.
- Never trade complete integrity checks for faster superficial scans.

## Documentation gaps

- Canonical source repository and current desktop code are unresolved.
- Exact current desktop version/build commands are unresolved.
- The relationship between the v0.25.9 recovery-system bundle and later GameSync release lines needs a version/provenance ledger.

## Wiki maintenance

Update this page when source identity is resolved, a new Archive Doctor version is proven, recovery fixtures are added, archive backends change, or recovered/salvaged output behavior changes. Preserve old hash manifests as immutable lineage evidence.