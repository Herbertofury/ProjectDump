# Reliable Artifact Publisher Wiki

**Project Constellation ID:** `PCX-030`  
**Status:** ACTIVE / TRACKED  
**Confidence:** High for recovered hash evidence; canonical source/toolkit bytes unresolved in connected search

## Purpose

Reliable Artifact Publisher is the deterministic packaging and publication track for complete project artifacts. Its core contract is that an upload acknowledgement is not publication proof. A release becomes durable only after local identity is known and the remote object is independently verified by trustworthy digest/size or complete re-download and hashing.

## Current verified durable evidence

The connected Drive file `Reliable-Artifact-Publisher-SHA256.txt` records two artifact identities:

- `skill.zip` SHA-256: `deeb0cc67b1e4af532e7f9de0a8fb3ed31f906eeee332f3722ddfbdcc4a1bd37`
- `Reliable-Artifact-Publisher-Toolkit.zip` SHA-256: `e5c9be08f8f8cea79ed40f3a7e13badd9e7619a6ecdb3e88145e41089989901a`

Drive hash-manifest ID: `1Zi4ZlHhhQr0G1u8Qf0zBX9PqAoB5wDLo`

The toolkit ZIP itself was not rediscovered by the connected Drive search in this pass, so the hash manifest is verified continuity evidence but not sufficient to claim the current toolkit bytes are available.

## Current stop point

Artifact identity/hash evidence survives, but the current canonical Reliable Artifact Publisher source/package and its latest runnable toolkit are not resolved from the connected GitHub/Drive surfaces.

## Exact next action

Resolve the toolkit/source bytes matching the recorded hash or a newer verified lineage, then run an end-to-end publish/re-download/hash fixture against a disposable test artifact before changing the publisher workflow.

## Current technology research

### GitHub artifact attestations

GitHub supports build provenance attestations and verification with GitHub CLI. Attestations are useful only when consumers verify them; they complement rather than replace byte-level artifact hashes.

### Sigstore Cosign 3.1.3

The official [Sigstore Cosign](https://github.com/sigstore/cosign) project published **v3.1.3** on 2026-08-06. Its release artifacts include Sigstore bundles alongside package artifacts.

**Proposal:** add an optional provenance layer after existing byte verification:

1. deterministically package artifact;
2. record local SHA-256/size;
3. upload;
4. independently verify remote bytes/hash;
5. optionally produce/verify a GitHub artifact attestation or Sigstore bundle;
6. record all evidence in a publication receipt.

The attestation step must never replace remote-byte verification.

**Why it fits:** hashes prove byte identity; attestations can additionally bind an artifact to a build/repository/workflow identity.

**Integration cost:** medium. CI identity, signing/attestation policy, verification commands, and offline/alternate-provider behavior must be defined.

**Risks:** a valid attestation for the wrong artifact/version is still wrong. Transparency/signing infrastructure can also be unavailable. Publication must degrade safely to verified hash/size evidence rather than becoming unverifiable.

**Small experiment:** publish a disposable fixture file to a test destination, re-download and hash it, then attach and verify an attestation/bundle. Deliberately alter one byte and verify both hash and provenance verification fail as expected.

**Acceptance test:** local and remote hashes match; provenance verification binds the exact artifact digest to the expected source/build identity; a tampered artifact fails; retry/resume does not create ambiguous duplicate releases; the receipt can be independently reread later.

## Publication receipt schema proposal

A durable publication receipt should include:

- project/artifact ID and version
- canonical source commit/tree hash
- build command/environment identity
- local path/name, size, SHA-256
- packaging manifest/hash
- destination/provider and remote object ID
- upload attempt/resume IDs
- remote provider digest/size
- full re-download SHA-256 when required
- attestation/SBOM/bundle identity when present
- verification timestamp
- final status
- rollback/recovery pointer

## Anti-degradation contract

- Never call upload acknowledgement "verified publication."
- Never delete the previous verified artifact before the replacement is remotely proven.
- Never weaken checks because the provider lacks a convenient digest; use complete re-download hashing.
- Never sign/attest an artifact whose local identity is unresolved.
- Never lose multipart ordering, resume state, or predecessor/successor lineage.

## Current Project Constellation relevance

Project Constellation currently has a real publication debt: regenerated candidate presentation artifacts passed static validation but were not promoted because the Drive connector blocked local-file egress. Reliable Artifact Publisher should eventually turn this class of blocked-but-verified candidate into explicit resumable publication state rather than an informal note.

## Documentation gaps

- Canonical publisher source/toolkit bytes unresolved.
- Exact current CLI/API and package version unresolved.
- Current attestation/SBOM support not proven implemented.

## Wiki maintenance

Update this page when the toolkit/source is resolved, publication receipt schema changes, provider adapters change, attestation support is implemented, or end-to-end remote verification changes. Preserve old receipts and hashes as release-lineage evidence.