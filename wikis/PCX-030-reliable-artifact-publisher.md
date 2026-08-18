# Reliable Artifact Publisher Wiki

**Project Constellation ID:** `PCX-030`  
**Status:** ACTIVE / TRACKED  
**Confidence:** High for recovered hash evidence and current ProjectDump publication proof; canonical standalone publisher source/toolkit bytes unresolved in connected search

## Purpose

Reliable Artifact Publisher is the deterministic packaging and publication track for complete project artifacts. Its core contract is that an upload acknowledgement is not publication proof. A release becomes durable only after local identity is known and the remote object is independently verified by trustworthy digest/size or complete re-download and hashing.

## Current verified durable evidence

The connected Drive file `Reliable-Artifact-Publisher-SHA256.txt` records two artifact identities:

- `skill.zip` SHA-256: `deeb0cc67b1e4af532e7f9de0a8fb3ed31f906eeee332f3722ddfbdcc4a1bd37`
- `Reliable-Artifact-Publisher-Toolkit.zip` SHA-256: `e5c9be08f8f8cea79ed40f3a7e13badd9e7619a6ecdb3e88145e41089989901a`

Drive hash-manifest ID: `1Zi4ZlHhhQr0G1u8Qf0zBX9PqAoB5wDLo`

The toolkit ZIP itself was not rediscovered by the connected Drive search in this pass, so the hash manifest is verified continuity evidence but not sufficient to claim the current toolkit bytes are available.

## Verified ProjectDump publication implementation, checked 2026-08-17

Project Constellation now has a real source-controlled example of the core Reliable Artifact Publisher proof model in the ProjectDump GitHub Wiki publisher.

The `Sync GitHub Wiki` path writes a commit status named **`wiki-publication` only after** its publisher has:

1. mirrored the complete source `wikis/` tree to the separate `ProjectDump.wiki.git` repository;
2. pushed any changed Wiki commit;
3. fresh-cloned the remote Wiki after publication;
4. byte-compared that complete clone against the intended source tree;
5. resolved the exact published remote Wiki master commit.

The status is attached to the exact source commit that triggered publication and points to the exact GitHub Actions run. This creates a machine-queryable chain from source identity to publication job to independently re-read remote state.

The latest verified Wiki-content publication proof recorded by Project Constellation is:

- source commit `9bb798006e34c1122e40eae1037144a1247f2001`;
- Actions run `32083218948`;
- run conclusion `success`;
- `wiki-publication = success`;
- published Wiki master `31c2cc1347f86669ce45710963d1c2a970e93223`;
- complete fresh-clone byte comparison passed.

The immediately preceding proof checkpoint was source commit `60bb4e8bee1afdc20369432bc0e0b8231d1cb240`, Actions run `32083124479`, and Wiki master `912305b14458ea5ac5340ed0ed1f3432fd9b97d3`. That run demonstrated that the proof status remains meaningful even when the remote Wiki already matches the source.

This is not yet proof that the standalone Reliable Artifact Publisher toolkit is recovered. It is verified product-owned evidence that the publication model can be implemented and queried end to end.

## Current stop point

Artifact identity/hash evidence survives, and ProjectDump now proves one real publication-verification pattern, but the current canonical standalone Reliable Artifact Publisher source/package and its latest runnable toolkit are still not resolved from the connected GitHub/Drive surfaces.

## Exact next action

Resolve the toolkit/source bytes matching the recorded hash or a newer verified lineage, then reproduce the ProjectDump publication-proof pattern against a disposable generic artifact: local digest -> upload -> remote re-read/digest -> immutable remote identity -> optional attestation -> durable receipt.

## Current technology research

### GitHub artifact attestations

GitHub supports build provenance attestations and verification with GitHub CLI. Attestations are useful only when consumers verify them; they complement rather than replace byte-level artifact hashes.

### Sigstore Cosign provenance layer

The [Sigstore Cosign verification documentation](https://docs.sigstore.dev/cosign/verifying/verify/) states that normal signature payloads include the container image digest and that verification checks that digest against the artifact. Sigstore's own examples sign and verify immutable image digests rather than relying only on mutable tags.

A useful failure lesson is preserved in official [Cosign issue #4818](https://github.com/sigstore/cosign/issues/4818): Cosign container images `v3.0.3` through `v3.0.6` were reported without the expected signatures, causing documented verification commands to fail. That incident reinforces a core Reliable Artifact Publisher rule: the provenance mechanism itself must be verified for the exact artifact. The existence of a signing feature, SBOM, release tag, or attestation workflow is not evidence that the expected signature/bundle actually exists and verifies.

**Proposal:** add an optional provenance layer after existing byte verification:

1. deterministically package artifact;
2. record local SHA-256/size;
3. upload;
4. independently verify remote bytes/hash;
5. record immutable provider object/version identity where available;
6. optionally produce and verify a GitHub artifact attestation or Sigstore bundle against the exact digest;
7. record all evidence in a publication receipt.

The attestation step must never replace remote-byte verification.

**Why it fits:** hashes prove byte identity; attestations can additionally bind an artifact to a build/repository/workflow identity. ProjectDump's `wiki-publication` status proves that source-commit-to-remote-state evidence can also be made machine-queryable.

**Integration cost:** medium. CI identity, signing/attestation policy, verification commands, provider-specific immutable IDs, offline/alternate-provider behavior, and retry semantics must be defined.

**Risks:** a valid attestation for the wrong artifact/version is still wrong. A release can also be missing an expected signature even when the project normally signs releases. Transparency/signing infrastructure can be unavailable. Publication must degrade safely to verified hash/size evidence rather than becoming unverifiable.

**Small experiment:** publish a disposable fixture file to a test destination, re-download and hash it, record the provider's immutable object/version identity, then attach and verify an attestation/bundle. Deliberately alter one byte and verify both hash and provenance checks fail. Deliberately omit the attestation and verify the receipt reports `BYTE_VERIFIED_PROVENANCE_MISSING` rather than incorrectly reporting full provenance success.

**Acceptance test:** local and remote hashes match; the immutable remote identity can be re-opened later; provenance verification binds the exact artifact digest to the expected source/build identity when present; a tampered artifact fails; a missing provenance object is reported truthfully; retry/resume does not create ambiguous duplicate releases; and the receipt can be independently reread later.

## Publication evidence join

A generic Reliable Artifact Publisher should join, rather than duplicate, the evidence Project Constellation now stores across publication systems. One read-only record should be able to connect:

- project/artifact/version;
- canonical source commit/tree identity;
- local artifact hash/size;
- upload attempt and destination;
- immutable remote object/version ID;
- remote provider digest/size or complete re-download hash;
- exact verification workflow/job/run when applicable;
- optional signature/attestation/SBOM identity and its verification result;
- final status and retry/recovery pointer.

For ProjectDump Wiki publication, the source commit -> `wiki-publication` status -> Actions run -> published Wiki master -> fresh-clone byte comparison is already one working example of this evidence join. For Project Constellation Drive checkpoints, the corresponding remote Drive file ID and independent re-read/re-download evidence should be joined into the same logical receipt rather than maintained as an unrelated success claim.

## Publication receipt schema proposal

A durable publication receipt should include:

- project/artifact ID and version
- canonical source commit/tree hash
- build command/environment identity
- local path/name, size, SHA-256
- packaging manifest/hash
- destination/provider and remote object ID/version
- upload attempt/resume IDs
- remote provider digest/size
- full re-download SHA-256 when required
- verification workflow/run/job/status identity when applicable
- attestation/SBOM/bundle identity when present
- explicit provenance status such as verified, missing, failed, or not-applicable
- verification timestamp
- final status
- rollback/recovery pointer

## Anti-degradation contract

- Never call upload acknowledgement "verified publication."
- Never delete the previous verified artifact before the replacement is remotely proven.
- Never weaken checks because the provider lacks a convenient digest; use complete re-download hashing.
- Never sign/attest an artifact whose local identity is unresolved.
- Never lose multipart ordering, resume state, or predecessor/successor lineage.
- Never infer that a signature or attestation exists merely because the release process normally creates one; verify the exact digest's provenance object.
- Never treat a successful workflow status as sufficient unless that status is emitted after the remote verification step it claims to represent.

## Current Project Constellation relevance

Project Constellation still has presentation-artifact publication debt: previously regenerated presentation candidates were not promoted because the available Drive path could not prove replacement bytes. That debt remains correctly unpromoted.

At the same time, the ProjectDump Wiki path has now closed a separate publication-proof gap by making verified remote Wiki publication machine-queryable through `wiki-publication`. Reliable Artifact Publisher should generalize that pattern so blocked candidates, successful uploads, Drive mirrors, GitHub releases, and provenance evidence all have explicit resumable states rather than informal notes.

## Documentation gaps

- Canonical standalone publisher source/toolkit bytes unresolved.
- Exact current standalone CLI/API and package version unresolved.
- Current standalone attestation/SBOM support not proven implemented.
- Generic provider adapters and receipt persistence are not yet proven from recovered standalone source.

## Wiki maintenance

Update this page when the toolkit/source is resolved, publication receipt schema changes, provider adapters change, attestation support is implemented, or end-to-end remote verification changes. Preserve old receipts and hashes as release-lineage evidence.