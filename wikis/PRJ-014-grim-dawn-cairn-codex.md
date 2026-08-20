# PRJ-014 - Grim Dawn Cairn Codex

**Project Constellation ID:** `PRJ-014`  
**Tracked state:** ARTIFACT PRESENT / SOURCE RECOVERY REQUIRED  
**Confidence:** Medium  
**Historical latest artifact:** `Grim_Dawn_Cairn_Codex_Ultimate_v6_1.html`  
**Current source boundary:** Project Constellation preserves the v6.1 artifact identity, but the exact HTML bytes have not been recovered from the currently connected GitHub or Google Drive evidence.  
**Current official game baseline checked:** 2026-08-20  
**Latest official Grim Dawn patch line resolved:** `v1.3.0.6`, published by Crate Entertainment on 2026-08-07.

## Purpose

Grim Dawn Cairn Codex is a standalone HTML knowledge and guide surface for Grim Dawn. Its continuity requirement is stronger than merely keeping an old HTML file loadable. The Codex must preserve working navigation, filters, saved state, migrations, links, notes, and complete guide data while keeping version-sensitive game facts aligned with the current Grim Dawn release.

The current task is therefore **recovery plus evidence-backed freshness reconciliation**, not a speculative rewrite.

## Authority and evidence order

Use this order when deciding what is current:

1. exact recovered Cairn Codex artifact bytes and embedded version/schema data;
2. any project-owned validation report tied to those exact bytes;
3. current official Grim Dawn patch notes and expansion information from Crate Entertainment;
4. current live reference utilities such as GrimTools, only after their displayed game version is verified;
5. older Project Constellation continuity summaries and historical filenames.

A filename such as `v6_1` is useful lineage evidence but does not prove current game-data compatibility.

## Current Grim Dawn baseline

### Latest verified official patch line

As of 2026-08-20, the official Crate Entertainment patch-notes stream identifies **Grim Dawn v1.3.0.6** as the newest published game patch. Crate published it on 2026-08-07. The prior `v1.3.0.4 + v1.3.0.5` topic remains important predecessor evidence because several Codex-relevant bugs were fixed there, but it is no longer the current baseline.

Primary sources:

- [Current Grim Dawn Patch Notes index](https://forums.crateentertainment.com/c/grimdawn/patch-notes/28)
- [Grim Dawn v1.3.0.6 patch notes](https://forums.crateentertainment.com/t/grim-dawn-version-1-3-0-6/157907/1)
- [Grim Dawn v1.3.0.4 + v1.3.0.5 patch notes](https://forums.crateentertainment.com/t/grim-dawn-version-v1-3-0-4-hotfixes/157189/1)
- [Grim Dawn v1.3.0.0 + hotfixes](https://forums.crateentertainment.com/t/grim-dawn-version-v1-3-0-0-hotfixes/155979/1)
- [Official Grim Dawn site](https://www.grimdawn.com/)

### Why the 1.3 line is a major Codex freshness boundary

The official v1.3.0.0 notes describe a major backend update for **Fangs of Asterkarn**, a complete UI visual overhaul, stash and inventory changes, accessibility/control changes, and broad game, itemization, mastery/skill, devotion, modding, and content updates.

The later v1.3.0.4 patch includes additional balancing and Fangs of Asterkarn adjustments. The v1.3.0.5 hotfix records fixes for:

- a critical Frostveil Highlands crash;
- several text-tag issues;
- a broken bounty for **Yura Voideye**;
- a missing cauldron in **Ugdenbog**;
- inconsistent spawning of Aetherial and Aetherial Vanguard Nemeses.

The newer v1.3.0.6 patch adds further Codex-relevant changes:

- fixes a rare Shattered Realm infinite-loading case;
- fixes Crucible score progression that could block the score-based loot chest;
- changes several Crucible encounter behaviors;
- changes rendering/performance behavior for skill FX on Medium settings or lower and fixes additional shader/target-outline issues;
- lets **The Secrets of Ugdenbog** and **Cleansing Fire of a Forgotten God** complete retroactively for eligible veteran characters using Difficulty Merits or Multiplayer;
- increases monster and treasure density in multiple Fangs of Asterkarn areas, especially **Frostveil Highlands**;
- significantly increases the spawn rate of **Frozen Aster**;
- changes **Noktukari's bounty** reputation rewards by difficulty;
- resets **A Dreadful Encounter** so it can appear again on Ascendant difficulty and complete again by speaking to the remnant;
- fixes Fangs of Asterkarn breadcrumb/intro and questline start problems for multiplayer clients;
- fixes **Kurn Solutions** not unlocking Alteration for all eligible multiplayer players;
- fixes missing Lore Notes that could not spawn;
- changes Soul Echo/Soul Fragment multiplayer drop behavior and multiple Ascension Altar values/loot-bias rules;
- updates several item and mastery/skill behaviors, including summon templates and Berserker Onslaught/Endless Rage behavior.

These are not merely engine-level changes. They can affect Codex domains such as locations, bounties, named enemies, encounter troubleshooting, quest progression, multiplayer notes, loot/crafting guidance, skill descriptions, labels, and route guidance. A historical Codex that predates the 1.3 line therefore cannot be described as current without a domain-by-domain audit.

## Current artifact recovery status

Connected evidence currently resolves the historical artifact name:

`Grim_Dawn_Cairn_Codex_Ultimate_v6_1.html`

The exact v6.1 file bytes are still unresolved. Current connected Drive searches return Project Constellation continuity/checkpoint material rather than a retrievable canonical v6.1 HTML artifact. No canonical project repository containing the Codex implementation has been resolved in connected GitHub state.

Until the exact artifact is recovered, do not claim:

- a current SHA-256 or byte size;
- a verified embedded Codex version marker;
- a successful browser launch;
- a complete navigation or filter pass;
- current localStorage schema behavior;
- current game-patch compatibility;
- Fangs of Asterkarn coverage;
- current GrimTools compatibility;
- working import/export or migration behavior.

## Historical behavior and continuity requirements

Project Constellation preserves the Codex as a standalone HTML guide/codex with:

- quest and area data;
- browser-local persistent state;
- a localStorage schema associated with Cairn Codex Ultimate v5;
- legacy v4/v3 migration awareness;
- versioned historical artifact lineage.

Those characteristics are recovery requirements, not proof that every historical behavior still exists in v6.1. Once the file is recovered, verify them directly rather than reconstructing them from memory.

## Recovery procedure

### 1. Recover without overwriting history

Locate every plausible Cairn Codex artifact by:

- exact filename;
- close filename variants;
- embedded title/version text;
- HTML `<title>` and visible heading text;
- known localStorage keys;
- known v3/v4/v5 migration markers;
- upload/recovery date;
- content hash.

Preserve every distinct candidate until lineage is reconciled. Do not replace an older file merely because another file has a newer timestamp.

### 2. Record exact artifact identity

For each candidate record:

- filename;
- byte size;
- SHA-256;
- source location;
- recovered date;
- embedded version/build markers;
- predecessor/successor relationship if proven;
- whether it launches;
- whether it contains migration code;
- whether its data scope can be tied to a Grim Dawn game version.

### 3. Preserve an immutable original

Before editing recovered HTML:

- keep the original bytes read-only;
- create a working copy with a new explicit version only after the baseline is proven;
- never silently rewrite the only surviving v6.1 copy;
- preserve old localStorage migration logic until replacement migrations are proven.

## Browser baseline verification

A recovered candidate is not considered usable solely because the HTML opens. Run a real browser pass against the exact file.

### Identity proof

Record:

- absolute file path or served URL;
- SHA-256 and size;
- browser family/version;
- loaded Codex version marker;
- console state;
- localStorage keys before and after use.

### Navigation inventory

Exercise every top-level navigation target and any nested tabs or panels. For each destination confirm:

- the promised section opens;
- the correct content becomes visible;
- URL/hash/history state behaves correctly if used;
- reload returns to the intended state when supported;
- no section is an empty shell or dead control.

### Search and filter behavior

Exercise every searchable/filterable data surface with:

- exact match;
- partial match;
- mixed case;
- no-result search;
- reset/clear;
- multiple filters if supported;
- repeated use after navigation;
- reload after an active filter when persistence is intended.

Do not reduce the dataset or hide off-screen entries to make filtering appear faster.

### Stateful controls

Inventory and test all controls that mutate user state, such as:

- favorites/bookmarks;
- completed quest/checklist state;
- notes;
- filters/preferences;
- selected tabs or expansion scope;
- import/export;
- reset/clear actions.

For every stateful control verify mutation, visible feedback, reload persistence, browser restart persistence when intended, and truthful failure handling.

## LocalStorage and migration audit

The durable history references v3/v4/v5 migration behavior. Recovery must identify the actual keys and migration code before any schema change.

Create a migration matrix with at least:

| Source state | Expected result |
| --- | --- |
| clean profile / no prior data | safe defaults without errors |
| valid v6.1 data | lossless reload |
| valid v5 data | migrated once, preserving user state |
| valid v4 data | migrated through the supported path |
| valid v3 data | migrated through the supported path |
| partially missing fields | defaults only for missing fields |
| malformed JSON/value | recoverable error path without app lockout |
| unknown future schema | preserve bytes and fail safely rather than destructive downgrade |

Before changing migration code, export representative legacy fixtures so the regression suite does not depend on hand-created browser state.

## Content Freshness Manifest

After recovering v6.1, add a read-only **Content Freshness Manifest** before rewriting guide data. The manifest should expose which data is actually proven current.

Recommended record fields:

```text
domain
sourceProvider
sourceUrl
supportedGameVersion
expansionScope
checkedAt
embeddedCountOrHash
validationResult
freshnessStatus
notes
```

Recommended statuses:

- `VERIFIED_CURRENT`
- `STALE`
- `UNKNOWN`
- `NOT_APPLICABLE`

Unknown data must remain visible and searchable. Do not hide a domain merely because its freshness is unresolved.

## Required freshness domains

### Game/UI baseline

Audit:

- supported Grim Dawn game version;
- classic versus current UI terminology;
- accessibility/control instructions;
- stash/inventory instructions;
- screenshots or UI-location guidance.

### Expansions and world content

Audit separately:

- base game;
- Ashes of Malmouth;
- Forgotten Gods;
- Fangs of Asterkarn;
- any expansion-specific quest, faction, area, shrine, bounty, boss, mastery, item, and crafting data.

### Quests and bounties

Verify:

- quest names;
- quest giver and turn-in location;
- prerequisites;
- branching outcomes where relevant;
- bounty targets;
- bounty availability and broken/fixed state;
- exact world and local-area references;
- multiplayer and Difficulty Merit progression behavior where the guide mentions it.

Concrete current audit cases now include:

- the v1.3.0.5 **Yura Voideye bounty** fix;
- v1.3.0.6 retroactive completion for **The Secrets of Ugdenbog** and **Cleansing Fire of a Forgotten God**;
- v1.3.0.6 difficulty-scaled **Noktukari bounty** reputation;
- v1.3.0.6 **A Dreadful Encounter** reset/recompletion behavior;
- v1.3.0.6 fixes for Fangs of Asterkarn multiplayer breadcrumb/questline start and **Kurn Solutions** Alteration unlock.

If the recovered Codex contains those records, confirm its descriptions and troubleshooting notes match current behavior.

### Areas, maps, and route guidance

Verify:

- area names;
- entrances/exits;
- riftgates;
- dungeon/interior relationships;
- quest-object locations;
- current expansion areas;
- route text after UI/map changes;
- density/spawn advice that can become stale after content patches.

Concrete current checks include the v1.3.0.5 Frostveil Highlands crash fix, the v1.3.0.6 Frostveil Highlands density increase, and the v1.3.0.6 **Frozen Aster** spawn-rate increase.

### Monsters and bosses

Verify:

- names;
- factions;
- spawn conditions;
- nemesis identity/spawning;
- major boss locations;
- expansion-specific enemies;
- difficulty-sensitive notes.

The v1.3.0.5 Aetherial/Aetherial Vanguard Nemesis spawning fix and v1.3.0.6 Frozen Aster spawn change should be checked against any Codex encounter guidance.

### Items, crafting, and interactables

Verify:

- item names and categories;
- crafting materials;
- set/item references;
- quest items;
- interactable locations;
- crafting/stash terminology;
- Ascension Altar and multiplayer-drop guidance where present.

Current concrete cases include the v1.3.0.5 Ugdenbog cauldron fix plus v1.3.0.6 changes to Soul Echo/Soul Fragment instanced drops, Ascension Altar drop-chance and Nemesis-count bonuses, Ascended Affix reroll scaling, Legendary Helm blueprint behavior under loot bias, and Lightning bias behavior.

### Masteries, skills, and devotions

Verify:

- mastery roster including Fangs of Asterkarn additions where applicable;
- skill names and mechanics used by the Codex;
- devotion names and references;
- any numerical values shown to users.

The v1.3.0.6 baseline changes summon templates for Occultist Familiar/Hellhound and Shaman Briarthorn and changes Berserker Onslaught/Endless Rage behavior, plus Wereraven conversion visuals and Primal Strike animation timing. Treat any matching Codex skill guidance as version-sensitive.

Do not copy balance numbers from old guides without source/version provenance.

## External reference integration

### GrimTools

[GrimTools](https://www.grimtools.com/) remains a useful community reference surface for the build calculator, world map, checklist, item database, and monster data.

Before using GrimTools as an import/reference provider:

1. confirm the live tool's displayed Grim Dawn version;
2. record the checked date;
3. distinguish GrimTools-derived data from Crate primary-source patch facts;
4. preserve source URLs or stable identifiers where available;
5. do not assume a search-engine cache represents the live tool.

### Crate forum utilities and resources

Use the official [Utilities and Resources](https://forums.crateentertainment.com/c/grimdawn/utilities-and-resources/29) area to discover maintained community tools, but verify each candidate directly before adding a dependency or import path.

## Data-diff strategy

Do not rewrite the complete Codex from patch notes. Instead:

1. parse or inventory the recovered v6.1 embedded data;
2. assign each record to a freshness domain;
3. identify the version-sensitive records;
4. compare those records to current primary or version-verified reference evidence;
5. generate a change ledger;
6. review high-risk changes manually;
7. update only verified stale records;
8. rerun the complete browser and persistence regression suite.

The ledger should preserve:

- record identity;
- old value/source;
- proposed new value/source;
- reason for change;
- game-version boundary;
- verification result;
- migration impact if state keys reference the changed identity.

## Link validation

Every external link in the recovered Codex should be classified as:

- exact entity/deep link;
- provider home/search link;
- historical/archive link;
- broken/stale link.

A button such as `Open map`, `View quest`, or `Show item` must land on the exact intended destination when the provider supports it. A generic provider homepage is not equivalent to a working contextual action.

## Offline and standalone behavior

Because the Codex is historically a standalone HTML artifact, determine whether core use is expected to work offline.

If core data is embedded:

- opening the file offline should still expose the complete local guide dataset;
- failed optional external links/resources must not break navigation;
- state mutation must remain local and recoverable.

If a newer revision adds remote data:

- cache/provider failures must be visible;
- remote refresh must never delete the embedded last-known-good dataset without verified replacement;
- data-source version must be displayed.

## Performance rules

Large guide datasets must remain fully available. Do not use viewport-only loading, culling, virtualization, hidden records, truncated search indexes, or reduced data quantity to manufacture responsiveness.

Performance work should instead measure and improve:

- initial parse/index cost;
- search-index construction;
- filter recomputation;
- DOM update size while preserving the full underlying dataset;
- persistence serialization;
- localStorage migration cost;
- external-link resolution.

Any optimization must preserve the same search/filter results and state semantics.

## Troubleshooting

### The HTML opens but controls do nothing

Check browser console errors, script load order, CSP/browser restrictions for local files, duplicate element IDs, and stale event binding. Confirm the browser actually loaded the intended file hash rather than another copy with the same name.

### Saved state disappeared

Inspect the exact localStorage keys and migration path before resetting anything. Export current storage first. Compare the stored schema/version to the migration code and verify the app did not silently switch origin by moving from `file://` to a hosted URL or different path.

### A quest/location appears wrong

Record the current Grim Dawn version, expansion, difficulty, quest state, and exact Codex record. Check Crate primary evidence first, then a version-verified current map/reference provider. Do not edit the record from memory.

### A bounty or enemy behavior differs from the Codex

Check whether the behavior changed anywhere in the current 1.3 patch line. The v1.3.0.5 Yura Voideye bounty/Aetherial Nemesis fixes and the v1.3.0.6 Noktukari/Frozen Aster/Fangs progression changes are explicit examples of game behavior changing after the historical Codex line.

### Multiplayer quest progression differs from the Codex

Check v1.3.0.6 before changing guide logic. That patch specifically adjusts retroactive quest completion, Fangs breadcrumb/intro starts, Fangs questline starts for clients, and Kurn Solutions Alteration unlock in multiplayer.

### A map or item link opens a generic page

Treat this as an incomplete contextual action. Recover or generate the exact supported deep link or add a selected/highlighted in-app destination rather than leaving the user to search manually.

### Old saves fail after a content refresh

Do not discard them. Preserve the original storage payload, identify whether record IDs/names changed, add a one-way versioned migration with a rollback/export path, and test fixtures from every supported historical schema.

## Release qualification for a refreshed Codex

A new Codex release should not be described as current until all applicable gates pass.

### Artifact gate

- source artifact identity recorded;
- new artifact identity recorded;
- SHA-256 and size recorded;
- old artifact preserved;
- HTML/resources are complete and uncorrupted.

### Browser gate

- all top-level navigation routes tested;
- all user-facing controls in scope exercised;
- search/filter matrix passed;
- no relevant console errors;
- exact loaded build identity proven.

### Persistence gate

- clean profile works;
- current save reload works;
- v3/v4/v5 migration fixtures pass when those paths exist;
- malformed state fails safely;
- browser restart preserves intended state;
- export/import round trip passes if supported.

### Data gate

- every major domain has a freshness status;
- current official game baseline is recorded;
- Fangs of Asterkarn scope is explicit;
- version-sensitive changes have source provenance;
- no known stale record is silently labeled current.

### Link gate

- contextual links reach exact supported destinations;
- broken links are fixed or truthfully marked;
- offline/core standalone behavior remains functional where intended.

### Regression gate

- older expansion content is preserved;
- saved user state is preserved or migrated;
- search result completeness is unchanged or improved;
- no hidden/capped data path is introduced;
- representative before/after workflows are retained as evidence.

## Smallest useful next experiment

Recover the exact v6.1 HTML and add the **Content Freshness Manifest** without changing user-facing guide data.

Classify every major data domain against the current official **v1.3.0.6** baseline as `VERIFIED_CURRENT`, `STALE`, `UNKNOWN`, or `NOT_APPLICABLE`. Then run the unchanged v6.1 browser workflow to prove the classification layer did not alter navigation, filtering, state, or data quantity.

### Acceptance

- original v6.1 bytes and SHA-256 are preserved;
- every major domain has explicit source/version status;
- current baseline is recorded as v1.3.0.6 unless a later official patch supersedes it before execution;
- no content is deleted during freshness classification;
- Fangs of Asterkarn gaps become explicit;
- the v1.3.0.5 Yura Voideye/Frostveil/Ugdenbog/Aetherial-Nemesis cases and the v1.3.0.6 quest, bounty, Frozen Aster, Fangs multiplayer, lore-note, Ascension Altar, and mastery/skill changes are checked if present in the recovered dataset;
- browser navigation/state behavior remains unchanged until a separately verified content migration is ready.

## Exact current next action

Recover `Grim_Dawn_Cairn_Codex_Ultimate_v6_1.html`, preserve and hash the original bytes, browser-test the exact artifact, then run the domain freshness audit against Grim Dawn **v1.3.0.6** and Fangs of Asterkarn before changing guide content.

If the file still cannot be recovered, continue searching by embedded titles, localStorage keys, prior version markers, and content fingerprints rather than scaffolding a replacement Codex.

## Wiki maintenance

Update this page when:

- the historical artifact or canonical source is recovered;
- the artifact hash/browser status is proven;
- Crate publishes a newer patch than v1.3.0.6;
- current-game data is reconciled;
- a new Codex artifact supersedes v6.1;
- persistence/migration behavior is verified or repaired;
- a contextual link/provider integration changes.

Preserve the current verified game baseline date so later maintainers can distinguish a deliberate freshness check from an undated claim.