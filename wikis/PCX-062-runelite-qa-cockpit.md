# PCX-062 - RuneLite QA Cockpit

**Project Constellation ID:** `PCX-062`  
**Status:** ACTIVE / TRACKED  
**Source status:** canonical user-owned plugin repository/ZIP not yet re-resolved  
**Preserved latest lineage:** `bert-skill-atlas-qa-cockpit.zip` after the Unified Cockpit line

## Purpose

RuneLite QA Cockpit is the verification-focused continuation of Bert's Skill Atlas / Skill Guide: one working cockpit for guide content, preparation, map/location assistance, money-making, settings, and True Content QA. Do not restart it from an empty template merely because the current source location is unresolved.

## Preserved lineage

Durable Project Constellation evidence records:

1. `Bert's Skill Guide Master`
2. `bert-skill-guide-master.zip`
3. `bert-skill-atlas-ultra.zip`
4. `bert-skill-atlas-unified-cockpit.zip`
5. `bert-skill-atlas-qa-cockpit.zip`

The Unified Cockpit was previously described as preserving 24 skills including Sailing, 144 routes, 404 money-makers, 211 quest entries, and 4,877 quest steps. These are continuity counts only until re-derived from the recovered QA Cockpit source.

## Current official RuneLite baseline

Current RuneLite Plugin Hub guidance remains the authoritative external-plugin workflow. It recommends Java 11, the Gradle `run` task for development, `runelite-plugin.properties`, commit-pinned Plugin Hub manifests, and `runeLiteVersion = 'latest.release'` when following the current RuneLite client. Third-party dependencies require Gradle dependency-verification hashes.

Official RuneLite developer guidance recommends Plugin Hub development for most third-party plugins and current core plugins as the first reference for correct API usage.

## Recovery-first workflow

When the QA Cockpit ZIP or a newer verified successor is found:

1. Record source, size, SHA-256, embedded version, and modification evidence.
2. Extract to a fresh directory without overwriting another checkout.
3. Inventory Gradle files, wrapper, plugin properties, source/resources, tests, and content data.
4. Re-count skills, routes, money-makers, quests, and quest steps from source.
5. Run project-owned Gradle build/tests.
6. Launch the real development client using the project's run path.
7. Prove the loaded plugin identity.
8. Exercise guide, prep, map, money, settings, overlays, links, and True Content QA.
9. Restart and verify persistence where promised.

## QA contract

A rendered sidebar is insufficient. Verify distinct top-level workspaces, correct route/step context, exact object/NPC/tile/inventory/bank/equipment overlay targets, exact Wiki/Prices destinations, quest-step ordering, money-maker identity, truthful malformed-data failures, configuration persistence, and QA reporting that surfaces bad records instead of silently dropping them.

## Current research decision

Do not migrate frameworks before source recovery. First align the recovered build with current RuneLite Plugin Hub requirements. The highest-value improvement is stronger generated content-QA invariants. Current `fast-check` v4.9.0 demonstrates modern shrinkable property-based testing, but do not force a JavaScript dependency into this Java plugin. Use the property-based strategy with a Java-native test library compatible with the recovered Gradle build: generate route/step/ID combinations and prove stable identity, no orphan steps, valid destinations, and deterministic content serialization.

## Exact current next action

Locate the newest QA Cockpit ZIP or canonical repository, record its SHA-256/source identity, extract it cleanly, and run its real Gradle build/tests before implementation or migration work.

## Blocker

The current connected GitHub repositories and exact Drive searches used in this pass did not expose the canonical QA Cockpit bytes. Historical continuity proves the lineage, not a current runnable build.

## Wiki maintenance

Update immediately when source is re-resolved, counts are re-derived, current RuneLite compatibility is proven, or runtime/restart verification changes the stop point.