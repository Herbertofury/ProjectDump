# PRJ-009 - Bert's Skill Atlas / Skill Guide

**Project Constellation ID:** `PRJ-009`  
**Status:** ACTIVE RuneLite project  
**Source status:** canonical current repository/ZIP not yet re-resolved  
**Preserved latest lineage:** QA Cockpit after Unified Cockpit

## Purpose

Bert's Skill Atlas / Skill Guide is the broader RuneLite plugin family behind the later QA Cockpit. Its recovered purpose is a data-driven RuneLite sidebar guide spanning all skills, multiple routes/steps, money-making data, contextual highlights, and direct Wiki/Prices actions.

## Preserved lineage

1. `Bert's Skill Guide Master`
2. `bert-skill-guide-master.zip`
3. `bert-skill-atlas-ultra.zip`
4. `bert-skill-atlas-unified-cockpit.zip`
5. `bert-skill-atlas-qa-cockpit.zip`

Earlier source evidence records a sidebar guide covering all 24 current skills including Sailing, route/step data, money-making tabs, object/NPC/tile/inventory/bank/equipment highlights, Wiki and Prices actions, and a data-driven `GuideRepository.java` model.

Prior continuity records described the Unified Cockpit as preserving 24 skills, 144 routes, 404 money-makers, 211 quest entries, and 4,877 quest steps. Re-derive those counts from the recovered source before treating them as current runtime facts.

## Current official RuneLite development baseline

RuneLite's current Plugin Hub guidance recommends Java 11 for external plugin development, Gradle's `run` task for development, `runelite-plugin.properties`, commit-pinned Plugin Hub manifests, and `runeLiteVersion = 'latest.release'` for current-client tracking. Its review/build process also requires cryptographic Gradle dependency verification for non-transitive third-party dependencies.

Current RuneLite developer guidance recommends Plugin Hub work for most external plugins and looking first at current core plugins for correct API usage.

## Preservation contract

Do not rebuild the Skill Atlas as a generic static webpage or discard its data model. Preserve:

- stable skill/route/step identity;
- guide ordering and prerequisites;
- overlay target identity;
- money-maker records;
- quest data and step ordering;
- Wiki/Prices contextual destinations;
- plugin configuration and persistence;
- source data separate from rendering code;
- previous artifact/version lineage.

## Recovery workflow

When the latest ZIP or repository is found:

1. hash the original bytes and preserve them;
2. extract to a fresh directory;
3. inspect Gradle/plugin manifests and source/data layout;
4. identify `GuideRepository` or its successor and derive current content counts;
5. run project-owned tests/build;
6. launch the real RuneLite development client;
7. exercise every top-level Atlas/Cockpit workspace;
8. verify exact overlay and contextual-link targets;
9. restart and verify settings/state persistence;
10. record the loaded build/version/hash in Project Constellation.

## Relationship to PCX-062

`PCX-062 RuneLite QA Cockpit` is the QA-focused current continuation of this family. PRJ-009 preserves the wider product lineage and content corpus; PCX-062 tracks the verification cockpit and current QA acceptance surface. Avoid duplicating the same content into two independent implementations.

## Current research decision

Framework migration is deferred until source recovery. The current RuneLite Plugin Hub contract remains the compatibility target. Once source is available, add stronger generated data-integrity tests around route identity, quest-step ordering, overlay targets, links, and serialization before adding new features.

## Exact current next action

Find the newest Skill Atlas/QA Cockpit ZIP or canonical repository, record its SHA-256 and build identity, then run its Gradle build/tests and real RuneLite development-client workflow.

## Blocker

Exact Drive searches and the current Herbertofury GitHub repository list used in this pass did not surface the canonical current Skill Atlas source or QA Cockpit archive.

## Wiki maintenance

Update when the actual repository/archive is recovered, content counts are re-derived, RuneLite compatibility is proven, or the current version/stop point changes.