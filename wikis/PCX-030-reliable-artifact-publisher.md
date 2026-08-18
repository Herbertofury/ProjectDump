# Reliable Artifact Publisher Wiki

**Project Constellation ID:** `PCX-030`  
**Status:** ACTIVE / TRACKED  
**Confidence:** High for recovered hash evidence and current ProjectDump publication proof; canonical standalone publisher source/toolkit bytes remain unresolved in connected evidence

## Purpose

Reliable Artifact Publisher is the deterministic packaging and publication track for complete project artifacts. Its core contract is that an upload acknowledgement is not publication proof. A release becomes durable only after local identity is known and the remote object is independently verified by a trustworthy provider digest/size or by complete re-download and hashing.

The project now has several production-grade proof patterns inside ProjectDump and Project Constellation even though the standalone toolkit source is not yet recovered. Those patterns should be treated as executable reference behavior for the future standalone implementation, not merely as documentation examples.

## Current verified standalone-artifact continuity evidence

The connected Drive file `Reliable-Artifact-Publisher-SHA256.txt` records two historical artifact identities:

- `skill.zip` SHA-256: `deeb0cc67b1e4af532e7f9de0a8fb3ed31f906eeee332f3722ddfbdcc4a1bd37`
- `Reliable-Artifact-Publisher-Toolkit.zip` SHA-256: `e5c9be08f8f8cea79ed40f3a7e13badd9e7619a6ecdb3e88145e41089989901a`

Drive hash-manifest ID: `1Zi4ZlHhhQr0G1u8Qf0zBX9PqAoB5wDLo`.

The toolkit ZIP itself has not been rediscovered in the connected Drive/GitHub surfaces. The hash manifest is therefore verified continuity evidence, but it is not enough to claim that the current standalone toolkit bytes are available or runnable.

## Verified publication implementation: ProjectDump GitHub Wiki

ProjectDump contains a real implementation of the central Reliable Artifact Publisher proof model.

The source-controlled Wiki lives under `wikis/`, but publication is not considered complete there. `.github/workflows/sync-github-wiki.yml` invokes `tools/github-wiki/wiki-sync.sh`, which:

1. resolves the intended source tree;
2. clones `Herbertofury/ProjectDump.wiki.git` or bootstraps it when necessary;
3. mirrors the complete `wikis/` tree into the Wiki repository;
4. commits only when bytes actually changed;
5. pushes the Wiki `master` branch;
6. fresh-clones the remote Wiki after the push;
7. byte-compares the complete fresh clone against `wikis/`;
8. resolves the exact remote Wiki master commit.

Only after that publisher step succeeds does the workflow attach a `wiki-publication` commit status to the exact ProjectDump source commit. The status target points to the exact Actions run and its description records the verified Wiki master commit.

This provides a machine-queryable chain:

`source commit -> workflow run -> remote Wiki commit -> fresh-clone byte verification -> success status`

Historical verified examples retained for lineage:

- source commit `60bb4e8bee1afdc20369432bc0e0b8231d1cb240` -> Actions run `32083124479` -> Wiki master `912305b14458ea5ac5340ed0ed1f3432fd9b97d3`;
- source commit `9bb798006e34c1122e40eae1037144a1247f2001` -> Actions run `32083218948` -> Wiki master `31c2cc1347f86669ce45710963d1c2a970e93223`.

The no-change path is intentionally valid: if the remote Wiki already matches source, the publisher still fresh-clones and byte-compares before reporting success.

## Verified dual-publication receipt pattern, 2026-08-18

Later Project Constellation wiki-maintainer passes extended the publication model beyond a single GitHub target. The checkpoint `project-constellation/evolution/2026-08-18T1108Z-prj-023-pcx-027.json` records a complete dual-publication receipt for a material UltraDeck wiki update.

The receipt joins all of these identities in one machine-readable checkpoint:

- project: `PRJ-025` / UltraDeck;
- canonical project repository: `Herbertofury/UltraDeck`;
- current project source commit: `e1da516a7aad9a254443e4a3e48830b98a1c772b`;
- ProjectDump wiki-source commit: `4495b34d0d44ae4b9fe92387751ee54dc0c61124`;
- GitHub Wiki workflow run: `32130161996`;
- verified Wiki master commit: `58f62221836b6101c62e5a6650ac5ddd52bfefe1`;
- Wiki publication result: fresh-clone byte-verified;
- reader-facing Wiki URL: `https://github.com/Herbertofury/ProjectDump/wiki/PRJ-025-ultradeck`;
- durable Drive wiki document ID: `1DqCCTuM3Ax8rjmNYN09xd5zuY1NDE8oztateaOmPN3M`;
- re-exported Drive Markdown size: `18502` bytes;
- re-exported Drive Markdown SHA-256: `9cf732dfc9b2474ccd3023c43d363da9f322664215812bf5eac23e0bcecbe4da`.

The same checkpoint also records a separate Project Constellation checkpoint document:

- Drive checkpoint document ID: `1B5FqKxLti3-4nZhNjvPcK3ZLgNbffGqE5gJToQmqaj8`;
- round-trip read: pass;
- exported Markdown size: `4350` bytes;
- exported Markdown SHA-256: `399a7b2e303fae082027085dd1b67a178ded03f9d6a33937ef1be5248485c2ae`.

This is stronger than an upload log. It records the intended source identity, the GitHub publication proof, the separate Drive publication identity, and a re-read/re-export hash for the Drive copy.

### Operational conclusion

A generic Reliable Artifact Publisher should model multi-target publication as one logical transaction with independent target verification. A GitHub target can be verified while a Drive target is still pending, and vice versa. The aggregate publication state remains incomplete until every required target reaches its own verified terminal state.

## Verified catalog-integrity receipt pattern

Project Constellation now also stores `project-constellation/Project-Constellation-Catalog-Integrity.json`, created by commit `ab071e23eecb9c658ad6b50f62c9c2b73b3a4c68`.

That receipt records a canonical catalog publication with:

- repository path: `project-constellation/Project-Constellation-Project-Catalog.json`;
- Drive file ID: `1-ks_2aRKgKQ-O7Y9LHte7w_Xk5t16egq`;
- byte size: `116771`;
- SHA-256: `79c8dd524b866ab1fe2dc011820f010d7ab5c8f4b0f42d31ad3e6ca8db82e8be`;
- Git blob SHA: `d417e516449f7c2d4ec9a16accdedfebc5cb590f`;
- GitHub restore commit: `eb99a193c08b9f2ca370dbcf85c75c2f997eafa6`;
- GitHub state: `RESTORED_AND_FETCH_VERIFIED`;
- Google Drive state: `SOURCE_REDOWNLOADED_AND_SHA256_VERIFIED`.

It also records semantic invariants separately from byte identity: 63 unique project IDs, required project fields present, and the removed Sports Group Hub absent.

That separation matters. Raw SHA-256 is the exact byte identity. Semantic invariants answer whether the artifact is structurally acceptable. A future publisher should preserve both rather than normalizing bytes and then pretending the original digest still applies.

## What the current evidence proves

Verified now:

- deterministic publication can be tied to an exact source commit;
- a remote Git repository can be re-cloned after publication and byte-compared against intended source;
- a commit status can represent a verified remote publication rather than a mere workflow completion;
- Google Drive artifacts can be independently re-read/re-exported and hash-verified;
- one machine-readable receipt can join GitHub and Drive publication identities;
- byte identity and semantic invariants can be recorded separately;
- a no-change publication can still be healthy when the remote bytes are independently revalidated;
- publication checkpoints can preserve exact retry/resume state without regenerating unchanged artifacts.

Not yet proven for the standalone Reliable Artifact Publisher toolkit:

- current toolkit CLI/API commands;
- recovered standalone source tree and package version;
- generic provider adapters beyond the observed ProjectDump/Drive workflows;
- standalone multipart upload/resume implementation;
- standalone attestation/SBOM implementation;
- a generic transaction coordinator that enforces all required targets before aggregate success.

## Current Project Constellation publication debt

`project-constellation/Project-Constellation-Publication-Debt.json` intentionally preserves a separate unresolved presentation-artifact candidate instead of silently promoting it.

Its contract is important to Reliable Artifact Publisher:

- exact candidate hashes and sizes are retained;
- unchanged candidates are not ceremonially regenerated;
- a failed or unavailable publication path leaves `lastAutomationHash` unchanged;
- remote bytes must be replaced and then re-read/re-downloaded before promotion;
- if source data changes before publication, old candidate hashes are invalidated and a coherent new candidate set must be generated;
- if source data did not change, retry the exact candidate bytes rather than creating an ambiguous near-duplicate release.

This is the correct behavior for resumable publication debt: preserve the known candidate, preserve why it is blocked, and distinguish `candidate built` from `published and verified`.

## Recommended publication state machine

A generic publisher should use explicit per-target and aggregate states rather than a single boolean.

Suggested artifact lifecycle:

1. `SOURCE_RESOLVED`
2. `BUILT`
3. `LOCAL_IDENTITY_VERIFIED`
4. `UPLOAD_PENDING`
5. `UPLOADED_UNVERIFIED`
6. `REMOTE_IDENTITY_VERIFIED`
7. `PROVENANCE_VERIFIED` or `PROVENANCE_NOT_APPLICABLE`
8. `TARGET_COMPLETE`
9. `ALL_REQUIRED_TARGETS_COMPLETE`

Useful failure/debt states:

- `REMOTE_MISMATCH`
- `UPLOAD_INTERRUPTED`
- `REMOTE_READ_UNAVAILABLE`
- `PROVENANCE_MISSING`
- `PROVENANCE_FAILED`
- `SOURCE_CHANGED_REBUILD_REQUIRED`
- `BYTE_VERIFIED_PROVENANCE_MISSING`

A retry must resume from the earliest invalid state, not replay successful stages automatically.

## Publication evidence join

One durable receipt should connect, where applicable:

- project/artifact/version;
- canonical source repository, branch, commit/tree/blob identity;
- build command and relevant environment/toolchain identity;
- local artifact name/path, size, and SHA-256;
- packaging manifest/hash;
- required publication targets;
- upload attempt/resume identifiers;
- provider-specific immutable object/version IDs;
- provider-reported digest/size when trustworthy;
- complete remote re-download/re-export SHA-256 when required;
- exact verification workflow/run/job identity;
- published Git/Wiki commit identity where applicable;
- optional signature/attestation/SBOM identity and verification result;
- semantic invariants checked after retrieval;
- predecessor/successor release lineage;
- final per-target status;
- aggregate status;
- rollback/recovery pointer.

The receipt itself should also be durable and re-readable. A receipt that exists only in an ephemeral runner log is not sufficient continuity evidence.

## Retry, resume, and idempotency contract

A reliable publisher must make retries boring and unambiguous.

Required behavior:

- retain the previous verified release until the replacement is independently proven;
- reuse the exact local artifact when source and build inputs are unchanged;
- never silently replace a failed candidate with newly generated bytes under the same identity;
- preserve multipart ordering and completed-part state;
- detect an existing matching remote object and verify it before uploading a duplicate;
- use immutable remote IDs or version IDs when the provider supports them;
- make publish actions idempotent where possible;
- record whether cleanup of temporary/failed remote objects happened and whether it was safe;
- preserve enough state to continue after process restart or runner loss.

For multi-target publication, retries should operate target-by-target. A verified GitHub target should not be republished simply because Drive needs a retry unless source identity changed.

## Current technology research

### GitHub artifact attestations

GitHub supports build provenance attestations and verification with GitHub CLI. Attestations are useful only when consumers verify them. They complement rather than replace byte-level remote verification.

### Sigstore Cosign provenance layer

The [Sigstore Cosign verification documentation](https://docs.sigstore.dev/cosign/verifying/verify/) states that normal signature payloads include the artifact/container digest and that verification checks the digest against the target.

A useful failure lesson is preserved in official [Cosign issue #4818](https://github.com/sigstore/cosign/issues/4818): Cosign container images `v3.0.3` through `v3.0.6` were reported without the expected signatures, causing documented verification commands to fail. That reinforces a core Reliable Artifact Publisher rule: the provenance mechanism itself must be verified for the exact artifact. The existence of a signing feature, SBOM, release tag, or attestation workflow does not prove that the expected signature/bundle exists and verifies.

### Provenance integration proposal

Add provenance only after byte verification:

1. deterministically package artifact;
2. record local SHA-256/size;
3. upload;
4. independently verify remote bytes/hash;
5. record immutable provider object/version identity;
6. optionally produce and verify a GitHub artifact attestation or Sigstore bundle against the exact digest;
7. record all evidence in the publication receipt.

The attestation step must never replace remote-byte verification.

**Integration cost:** medium. CI identity, signing/attestation policy, verification commands, provider-specific immutable IDs, alternate-provider behavior, and retry semantics must be defined.

**Risks:** a valid attestation for the wrong artifact/version is still wrong. A release can be missing an expected signature even when the project normally signs releases. Transparency/signing infrastructure can be unavailable. Publication must degrade truthfully to verified hash/size evidence rather than silently calling provenance complete.

**Small experiment:** publish a disposable fixture to two destinations, for example one GitHub-backed target and one Drive target. Re-download/re-export and hash both, record their immutable IDs, then attach and verify provenance where supported. Alter one byte and verify remote identity fails. Omit the attestation and verify the receipt reports `BYTE_VERIFIED_PROVENANCE_MISSING` instead of full provenance success.

**Acceptance test:** both required targets independently match the intended bytes; immutable remote identities can be reopened later; provenance binds the exact digest when present; tampering fails; missing provenance is reported truthfully; retry/resume creates no ambiguous duplicate release; and the receipt itself can be independently reread later.

## Anti-degradation contract

- Never call upload acknowledgement "verified publication."
- Never delete the previous verified artifact before the replacement is remotely proven.
- Never weaken checks because a provider lacks a convenient digest; use complete re-download/re-export hashing.
- Never sign or attest an artifact whose local identity is unresolved.
- Never lose multipart ordering, resume state, predecessor/successor lineage, or target-specific completion state.
- Never infer that a signature or attestation exists merely because the release process normally creates one.
- Never treat workflow success as sufficient unless that workflow emits success only after the remote verification step it claims to represent.
- Never treat one successful destination as aggregate success when another required destination is stale, missing, or unverifiable.
- Never regenerate unchanged artifact bytes merely to create activity.
- Never promote a new source/catalog hash while known publication debt still refers to older candidate bytes without explicitly invalidating that debt.

## Current stop point

The standalone Reliable Artifact Publisher source/toolkit remains unresolved, but the repository now contains substantially stronger product-owned reference evidence than the earlier hash manifest alone:

- verified GitHub Wiki publication with fresh-clone byte comparison;
- verified Drive re-read/re-export hashing;
- dual-target wiki publication receipts;
- catalog-integrity receipts joining GitHub and Drive identity;
- explicit preserved publication-debt state for blocked candidates.

## Exact next action

Resolve the toolkit/source bytes matching the recorded standalone hash or a newer verified lineage. Then reproduce the now-proven ProjectDump patterns with a disposable generic artifact through a real standalone publisher command:

`source identity -> deterministic build -> local hash -> two required targets -> independent remote verification -> optional provenance -> durable joined receipt -> restart/resume verification`

The acceptance gate is not that the command exits zero. Both target copies and the receipt must survive independent reread after the publisher process exits.

## Documentation gaps

- Canonical standalone publisher source/toolkit bytes unresolved.
- Exact current standalone CLI/API and package version unresolved.
- Generic provider adapters are not yet proven from recovered standalone source.
- Standalone multipart/resume behavior remains unproven.
- Standalone attestation/SBOM support remains unproven.
- No recovered standalone transaction coordinator yet proves required-target aggregate completion.

## Wiki maintenance

Update this page when the toolkit/source is resolved, provider adapters change, publication receipt/state-machine behavior changes, standalone multipart/resume becomes verified, attestation support is implemented, or new project-owned publication evidence proves a stronger end-to-end contract. Preserve old hashes, receipts, and blocked candidate identities as release-lineage evidence.