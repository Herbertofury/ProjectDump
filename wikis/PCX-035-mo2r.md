# MO2R Wiki

**Project Constellation ID:** `PCX-035`  
**Status:** ACTIVE / TRACKED  
**Connected repository:** [Herbertofury/MO2R](https://github.com/Herbertofury/MO2R)  
**Repository evidence boundary:** the connected repository currently contains only a minimal `# MO2R` README. The real implementation source/worktree has not yet been verified from that repository.

## Purpose

MO2R evolves Mod Organizer 2 workflows while preserving native MO2 behavior and data fidelity. The current feature line focuses on richer mod metadata, dependency/relationship intelligence, changelog/history visibility, exact source navigation, and coordinated plugin behavior without damaging drag/drop, compact rows, sorting/filtering, profile state, separators, or restart persistence.

MO2R features are not complete because a column header exists or because data structures compile. Every visible column/control must be backed by the real data pipeline and verified inside the real MO2 runtime.

## Current directly recovered implementation contract

The newest strong MO2R execution artifact recovered in this pass is:

- `MO2R_FINISH_CHANGELOG_THEN_UPGRADE_RELATIONSHIPS.md`

It defines one combined completion run for:

1. a fully implemented **Changelog** column;
2. a fully automatic, typed, evidence-backed **Relationship** column/pipeline.

The specification explicitly requires both features to work end to end in the actual MO2R mod list before completion.

## Current upstream host baseline, checked 2026-08-17

The official [Mod Organizer 2 releases](https://github.com/ModOrganizer2/modorganizer/releases) identify **MO2 v2.5.2** (`9c130cb`) as the current latest stable release.

Important v2.5.2 host facts for MO2R include:

- Qt / PyQt **6.7.1**;
- Python **3.12.3**;
- `libloot` 0.23.0;
- USVFS 0.5.0;
- Starfield Creation support changes;
- `IPluginPreview::supportsArchive()`;
- `IPluginPreview::genDataPreview()`;
- non-game third-party plugins can register custom mod content/checkers;
- `mobase.INVALID_HANDLE_VALUE` is exposed to Python plugins.

### Decision

Use v2.5.2 as the primary live compatibility target for current MO2R verification. Preserve older beta/release evidence as regression history, but do not treat an older beta as the current host baseline.

Do not exploit newer plugin APIs until the canonical MO2R source is resolved and the migration can be tested in the real host.

## Changelog column contract

The Changelog column must be a first-class MO2 mod-list column.

For each installed mod it should:

- show the newest verified changelog entry in a compact cell;
- retain complete history even when visible text is elided;
- bind to stable mod identity, never transient row index/display position;
- leave separator rows appropriately empty;
- present a truthful unavailable/empty state when no source exposes changelog data.

### Changelog normalized model

For each retained changelog entry preserve, when available:

- version/release identifier;
- release/update date;
- complete changelog text;
- provider/source;
- canonical source URL or stable source identity;
- acquisition type, such as API, page, release note, creator post, snapshot, or imported provenance;
- original source text;
- translated display text when translation is enabled;
- provenance/evidence.

Duplicate entries found through several providers should be deduplicated while retaining all supporting provenance. Conflicting reliable records should remain distinguishable rather than being silently merged.

### Changelog data-source rule

Use MO2R's existing provider/metadata architecture rather than building a disconnected changelog scraper.

Potential sources include:

- Nexus metadata/API;
- external provider adapters;
- GitHub/GitLab or other release APIs;
- release notes and history sections;
- source pages;
- creator posts;
- verified offline snapshots/cache;
- imported source/provenance already attached to the mod.

Network/browser parsing must occur through background metadata/source refresh, not because the pointer entered a Changelog cell.

## Changelog hover/history behavior

The exact mod's cached history popup must:

- open from already-cached data;
- show all known entries newest first;
- show complete text;
- show version/date/source when available;
- preserve useful headings/list structure;
- handle long history without an artificial count cap;
- scroll independently;
- behave correctly at monitor/screen edges;
- respect theme and DPI;
- expose the same complete data through keyboard/accessibility interaction.

Rapid hover must never show another mod's stale async result.

## Native column behavior

The new Changelog column must remain compatible with MO2's real column model:

- sortable;
- movable;
- resizable;
- hideable/showable;
- persisted across restart;
- compatible with filtering/sorting;
- compatible with separators;
- compatible with mod reordering and native drag/drop;
- compatible with compact row height;
- compatible with current themes/DPI.

Adding it must not reset existing column order/width/visibility, selection, scroll, separator state, or mod order.

Refresh only affected rows where practical rather than rebuilding the full list to update one mod.

## Relationship pipeline contract

The Relationship column's previous steady states such as `Not scanned`, `Unresolved`, `Refresh the canonical source`, or `No cached evidence` must not remain normal installed-mod outcomes.

Every normal installed mod should automatically enter relationship processing.

Allowed steady outcomes include:

- relationships found and summarized;
- completed scan with no relationships found;
- stale cached relationships being refreshed;
- a specific actionable processing/source error.

`Scanning...` is acceptable only while actual work is in progress.

## Event-driven invalidation and rescanning

Relationship work must connect to the real MO2R event flow rather than depending on hover/open/manual scan.

The recovered contract requires appropriate full or incremental processing after events including:

- first startup after migration;
- normal startup when cache is missing/stale/invalid;
- profile switch;
- mod install/reinstall/update/remove;
- mod enable/disable;
- plugin enable/disable;
- FOMOD selection/install change;
- metadata/source refresh;
- update checks;
- source-adapter refresh;
- relevant LOOT metadata change/import;
- relevant save selection/load change;
- generated-output creation/update/removal when provenance is known;
- explicit user-defined relationship change;
- older-cache migration/repair.

Do not replace this with constant background polling.

## Relationship evidence graph

Use all reliable evidence available through MO2R, including where applicable:

- plugin masters/light masters;
- installed file ownership and winning-file relationships;
- FOMOD conditions/selections;
- Nexus requirements/file metadata;
- external-site dependency metadata;
- LOOT metadata;
- official manifests;
- generated-output provenance from Nemesis, Pandora, FNIS, BodySlide, Synthesis, xEdit, DynDOLOD, TexGen, LODGen, and related tools;
- user-defined relationships;
- save/plugin references;
- source-page dependency information;
- patch/translation/compatibility/update evidence;
- verified archive/provenance evidence.

Preserve type, direction, and source. Do not collapse every edge into `required`.

Supported semantic categories should include when evidenced:

- required dependency;
- runtime required;
- dependent/reverse requirement;
- patch for;
- translation for;
- optional integration;
- conflict/incompatibility;
- generated from;
- update/replacement;
- related source/mirror where useful but distinct from dependency.

## Relationship cell and popup

The compact cell should summarize computed relationships deterministically, for example counts by meaningful type.

The popup should use the cached typed graph and show:

- relationship type;
- related mod/source;
- current installed/enabled state where relevant;
- evidence/source;
- exact navigation/action.

When an installed related mod exists, `Open`/`Show` must navigate directly to that exact mod. A generic mod-list landing page or source homepage does not satisfy the action.

## Performance and anti-degradation rules

Expensive relationship discovery belongs off the UI thread.

Required scheduling behavior:

- deduplicate duplicate requests;
- coalesce rapid event bursts;
- incrementally invalidate affected mods where possible;
- cache completed results;
- persist appropriate cache across restart;
- invalidate when source evidence changes;
- reject stale async writes for a different mod/version;
- keep scrolling, hover, selection, sorting, filtering, drag/drop, enable/disable, and profile switch responsive.

Hard prohibitions:

- no viewport-only scanning;
- no visible-row-only relationship processing;
- no mod-count cap;
- no reduced relationship data to make benchmarks look faster;
- no hover-triggered full scan on the UI thread;
- no stale source cache silently presented as current.

## Required Changelog verification

The recovered acceptance set includes real cases for:

- one entry;
- many entries;
- no version number;
- duplicate entries across providers;
- conflicting provider records;
- source offline with last-known-good cache;
- refresh adding a new release;
- no changelog available;
- rapid hover;
- very long text;
- large history;
- sort/filter/separators;
- drag/drop/reordering;
- move/resize/hide/show;
- restart layout/cache persistence;
- zero network/browser work caused solely by hover;
- no wrong-mod popup;
- no UI freeze during refresh.

## Required Relationship verification

The recovered acceptance set includes:

- fresh startup with many never-scanned mods;
- restart after initial scan;
- profile switch;
- install/update/reinstall/remove;
- mod enable/disable;
- plugin enable/disable;
- FOMOD change;
- update check;
- metadata/source refresh;
- dependency-evidence change;
- required/dependent/patch/translation/optional/conflict/generated relationships;
- true no-relationship result;
- failure then retry;
- rapid hover/movement during scans;
- sort/filter/reorder while work is active;
- restart persistence;
- exact related-mod/source navigation;
- full-list audit proving normal installed mods are not permanently left as `Not scanned`.

## Current source problem

The connected [Herbertofury/MO2R](https://github.com/Herbertofury/MO2R) repository currently exposes only the title `# MO2R`. It does not prove the real implementation source, plugin set, build commands, or current runtime artifact.

The direct File Library implementation directive is strong product evidence but does not identify the canonical build tree.

Do not create a replacement implementation in the placeholder repository until the real MO2R source/worktree is reconciled.

## Smallest useful current experiment

Once the canonical MO2R source is found:

1. record repository/worktree/branch and artifact hash;
2. launch current MO2R against upstream MO2 v2.5.2;
3. reproduce the persistent `Not scanned` relationship state;
4. baseline current column layout/drag-drop/row-height/profile behavior;
5. implement Changelog through the existing metadata/provider architecture;
6. implement event-driven relationship invalidation/processing;
7. run the full-list relationship audit;
8. restart the real host and verify layout/cache/navigation persistence;
9. test with the other installed MO2R/MO2 plugins to catch shared-column and drag/drop regressions.

## Exact current next action

Resolve the real MO2R implementation repository/worktree and run the Changelog + Relationship contract against current upstream **MO2 v2.5.2**. The connected placeholder repository is not enough to code safely.

## Wiki maintenance

Update this page when the canonical source is resolved, upstream MO2 changes, either column reaches real-runtime proof, provider/relationship evidence expands, drag/drop/layout behavior changes, or the current combined implementation directive is superseded.