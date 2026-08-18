# Project Governance Wiki

**Project Constellation ID:** `PCX-026`
**Status:** ACTIVE / TRACKED
**Confidence:** Medium
**Durable governance repository:** [Herbertofury/ProjectDump](https://github.com/Herbertofury/ProjectDump)

## Purpose

Project Governance is the policy and execution-contract track that keeps project work consistent across repositories, agents, tools, releases, and continuity surfaces. Its job is not to add ceremony. Its job is to make requirements enforceable, preserve user steering, prevent silent scope reduction, and ensure that completion claims are tied to real verification.

## Current verified durable evidence

The current `Herbertofury/ProjectDump` root `AGENTS.md` is the strongest connected governance source verified in this pass. It establishes the durable source priority and current Project Constellation invariants:

- GitHub holds versioned project state, memory, manifests, catalogs, handoffs, policies, and text/code continuity.
- Google Drive holds complete release artifacts, archives, binaries, exported project brains, and byte-verifiable backups.
- Canonical state must be resolved before mutating ongoing work.
- User edits and version lineage must be preserved.
- Project Constellation remains ACTIVE / NORMAL_OPERATION with exactly 63 tracked projects.
- Missing sandbox files are not a recovery trigger.

Canonical evidence: [ProjectDump AGENTS.md](https://github.com/Herbertofury/ProjectDump/blob/main/AGENTS.md)

## Current stop point

The governance contract is durable and active, but this tracked project does not yet have a separately resolved project-owned repository or machine-enforced policy package that can be identified as the canonical standalone implementation. The ProjectDump governance text is therefore the current verified operating source, while a standalone Project Governance implementation remains unresolved.

## Exact next action

Create a machine-checkable, non-destructive governance validation layer that audits repository/project state against the existing human-readable contract without replacing user authority or rewriting policy automatically.

## Current technology research

### Open Policy Agent

The official [Open Policy Agent](https://github.com/open-policy-agent/opa) project published **v1.19.0** on 2026-07-30. OPA provides policy-as-code evaluation and is a strong candidate for validating structured project invariants when those invariants can be represented as data.

**Proposal:** test OPA only as an optional audit engine behind Project Governance. Start with read-only checks for invariants such as canonical repository identity, required verification evidence, forbidden scope reductions, and the exactly-63 Project Constellation count. Human-readable AGENTS rules and explicit user corrections remain authoritative.

**Why it fits:** the governance problem is not a lack of prose. It is the gap between prose requirements and repeatable machine checks.

**Integration cost:** medium. Existing policies must first be represented in a small stable JSON schema, and every machine-enforced rule needs fixtures proving that it does not reject valid project-specific exceptions.

**Risks:** policy engines can create false confidence or over-constrain projects if prose is translated mechanically. Never auto-rewrite user policy from OPA results.

**Small experiment:** define four read-only invariants from the existing ProjectDump contract and run them against synthetic pass/fail fixtures plus the real Project Constellation state.

**Acceptance test:** every fixture produces the expected result, current valid state passes, intentionally broken state fails with an actionable explanation, and disabling the policy engine does not alter project data or execution behavior.

## Governance data model proposal

A future machine-readable governance package should separate:

- `ruleId`
- source document/path and source hash
- human-readable rule text
- machine-checkable predicate where appropriate
- scope and exemptions
- severity
- evidence required
- last reviewed date
- supersedes/superseded-by relationship
- user override history

Never treat a machine predicate as the canonical rule when the source human policy or explicit user correction says otherwise.

## Anti-degradation contract

Governance work must never make projects easier to "pass" by weakening tests, reducing supported targets, removing user-visible capabilities, lowering data fidelity, hiding failures, or redefining completion. A governance change itself requires versioned source, regression fixtures, and proof that existing valid project workflows are still accepted.

## Verification ladder

1. Parse/validate governance schema.
2. Run rule-unit fixtures.
3. Run repository/project-state fixtures.
4. Run against current Project Constellation state.
5. Verify explicit user override precedence.
6. Verify stale/superseded policy detection.
7. Verify no project data is modified in audit mode.
8. Re-read the published policy and confirm source hash/lineage.

## Documentation gaps

- Standalone Project Governance repository/implementation identity is unresolved.
- Existing governance rules are primarily human-readable rather than structured policy objects.
- No current evidence proves OPA or any other policy engine is already integrated.

## Wiki maintenance

Update this page when the canonical Project Governance implementation is resolved, the durable AGENTS contract changes, machine-enforced policy is introduced, or a policy engine/tool is actually integrated and verified. Preserve superseded rules and user override lineage rather than silently rewriting history.
