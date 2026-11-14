---
name: checkpoint-reconciliation
description: Reconcile ProjectDump's durable cross-project checkpoints, source hashes, staged payloads and artifact lineage without overwriting newer work or treating verification branches as published products.
---

# Checkpoint reconciliation

Use for continuity recovery, source/artifact provenance, project handoffs and audit of competing checkpoints. Read root `AGENTS.md` first; preserve its durable source priority and Project Constellation rules. For a Minecraft implementation task, continue through `tools/minecraft-dev-kit/SKILL.md` rather than replacing its acceptance contract with this audit.

## Select the actual project state

1. Resolve the exact project path, current owner-authorized task, active branch/PR and last verified checkpoint. Read the narrow project handoff rather than bulk-enumerating every project or artifact store.
2. Inventory candidate identities: repository/ref/commit/tree, checkpoint date, source hash, artifact hash, toolchain, reported tests and their exact run IDs. A descriptive filename or recent timestamp is not proof of newer accepted source.
3. Distinguish source payload, reconstructed tree, compiled artifact, runtime-tested artifact and published release. Open verification PRs are not accepted product releases merely because a workflow or its description reports success.
4. Compare against current remote state before mutating. Preserve newer owner edits, private inputs and unrelated branches. Missing ephemeral workspace files do not establish an integrity failure and do not trigger restoration of older state.

## Verify recovery safely

Read the project's own reconstruction/manifest instructions; never concatenate arbitrary payload parts by guessed order. Verify each declared base, patch and complete archive digest at its appropriate boundary. Inspect archive paths before extracting into a fresh staging location and reject path traversal/unexpected links. Do not execute decoded scripts or binaries merely because they were stored in a checkpoint.

If the exact archive, mapping or permission is missing, record that specific gap and continue independent permitted work. Do not silently substitute a similarly named archive, downgrade to a convenient old release or erase failed evidence. Keep licensed/private payloads out of public commits.

## Reconcile rather than overwrite

For Project Constellation, inspect `project-constellation/HANDOFF.md` and its machine-readable state, then compare artifact identities against recorded automation hashes before any update. Preserve its documented 63-project scope unless the owner changes it; historical smaller datasets are not replacements. Respect active NORMAL_OPERATION rather than inventing disaster recovery.

For each update retain a before/after record: selected canonical identity and why, files changed, evidence preserved, verification commands/results, private/public boundary and exact next action. Keep project state in its own scope; reusable general behavior belongs in the shared core, not private or project-specific details.

## Delivery and claims

Verify exact remote blobs after authorized repository publication. For artifact delivery, verify the complete saved artifact with an independently read hash, not just an upload acknowledgement; preserve the canonical destination identity. Repo wiki mirrors and workflow logs are not proof of live wiki/release availability.

Do not dispatch unrelated bootstrap, build, release or recovery workflows to validate a documentation-only checkpoint change. Report implementation, tests, publication and native acceptance separately. Retain uncertain sends/actions as uncertain until observed, and do not duplicate them blindly.
