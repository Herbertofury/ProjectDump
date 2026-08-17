# PRJ-014 - Grim Dawn Cairn Codex

**Project Constellation ID:** `PRJ-014`  
**Historical state:** artifact present, runtime unverified  
**Historical latest artifact:** `Grim_Dawn_Cairn_Codex_Ultimate_v6_1.html`  
**Current source boundary:** the historical database proves the v6.1 artifact name, but exact current bytes were not recovered from connected GitHub/Drive searches in this pass.

## Purpose

Grim Dawn Cairn Codex is a standalone HTML knowledge/guide surface for Grim Dawn. Its continuity requirement is stronger than simply keeping the old page loadable: navigation, filters, saved state, migrations, links, and game-content facts must stay correct for the current game.

## Major freshness event, checked 2026-08-17

The historical v6.1 Codex predates a major Grim Dawn change. Crate Entertainment released **Grim Dawn v1.3.0.0** with Fangs of Asterkarn support in July 2026, followed by hotfixes including **v1.3.0.2**. The official Grim Dawn site also states that Fangs of Asterkarn is available alongside the free v1.3 update.

Primary sources:

- https://forums.crateentertainment.com/t/grim-dawn-version-v1-3-0-0-hotfixes/155979/1
- https://www.grimdawn.com/

The v1.3 line includes broad UI, stash/inventory, gameplay, itemization, class/skill, modding, and expansion-content changes. Therefore the old Codex cannot be treated as current merely because its JavaScript still runs.

## Current data-freshness risk

The inspected Drive/GitHub state did not expose the actual `Grim_Dawn_Cairn_Codex_Ultimate_v6_1.html` bytes, so this pass cannot truthfully verify:

- what game patch/expansion the embedded data targets;
- whether Fangs of Asterkarn content is represented;
- whether new v1.3 systems/items/mastery changes are represented;
- whether external links still land on exact intended entities;
- whether localStorage/state schemas survive current browser/runtime behavior.

Recover the artifact before modifying or regenerating it.

## Current external reference landscape

GrimTools remains an important community data/reference surface for build calculator, world map, checklist, item database, and monster data. However search-index snapshots can lag current game patches, so Project Constellation must not infer GrimTools freshness from a cached search result alone.

Before importing any GrimTools-backed data, verify the live tool's displayed game version against the current Crate patch line.

Community utility index:

- https://www.grimtools.com/
- https://forums.crateentertainment.com/c/grimdawn/utilities-and-resources/29

## Proposed Codex freshness architecture

After recovering the v6.1 HTML, add a read-only **Content Freshness Manifest** rather than immediately rewriting the entire app.

For each major data domain record:

- source/provider;
- game version or expansion scope;
- checked date;
- source URL;
- embedded-data hash or count where possible;
- last successful validation;
- stale/unknown flag.

Suggested domains include classes/masteries, skills, devotions, items/sets, factions, quests, world/locations, shrines/checklists, bosses/monsters, expansion-specific content, build links, and external reference links.

The manifest must not hide stale entries. Unknown freshness should be visible and searchable.

## Recovery and validation workflow

1. Recover a hashable copy of `Grim_Dawn_Cairn_Codex_Ultimate_v6_1.html`.
2. Preserve the original bytes read-only and record SHA-256/size.
3. Open it in a real browser and record the loaded build identity.
4. Exercise every top-level navigation route and filter.
5. Test search, favorites/bookmarks, any checklists, import/export, links, and state mutation controls.
6. Reload and restart the browser to verify persistence/migration behavior.
7. Inspect console errors and broken network/external-link paths.
8. Inventory embedded game-content version assumptions.
9. Compare each data domain to current Grim Dawn v1.3.0.x/Fangs of Asterkarn primary evidence.
10. Update only stale domains, then rerun the exact same regression suite.

## Anti-regression gate

A v1.3 content refresh must not remove working v6.1 navigation, filters, saved state, older expansion content, notes, or external references simply because a data schema changes. Add migrations and versioned provenance instead of replacing the artifact wholesale.

Do not use a smaller subset of items/classes/quests as a temporary performance shortcut. Complete data availability remains part of correctness.

## Smallest useful experiment

Recover v6.1 and add the Content Freshness Manifest without changing user-facing data. Mark every domain as `VERIFIED_CURRENT`, `STALE`, or `UNKNOWN` against v1.3.0.x.

### Acceptance

- original v6.1 bytes and hash are preserved;
- every major domain has a source/version status;
- no content is deleted during freshness classification;
- current v1.3/Fangs of Asterkarn gaps become explicit;
- browser navigation/state behavior remains unchanged until a separately verified content migration is ready.

## Exact current next action

Recover the exact v6.1 HTML bytes, hash and browser-test them, then run a v1.3.0.x/Fangs of Asterkarn freshness audit before any content rewrite.

## Wiki maintenance

Update when the artifact is recovered, its hash/browser status is proven, current-game data is reconciled, or a newer Codex artifact supersedes v6.1.