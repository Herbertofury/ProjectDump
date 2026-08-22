# PCX-062 - RuneLite QA Cockpit

**Project Constellation ID:** `PCX-062`  
**Status:** ACTIVE / TRACKED  
**Source status:** canonical user-owned QA Cockpit repository/ZIP still not re-resolved  
**Preserved latest lineage:** `bert-skill-atlas-qa-cockpit.zip` after the Unified Cockpit line  
**Related project:** [PRJ-009 - Bert's Skill Atlas / Skill Guide](PRJ-009-berts-skill-atlas.md)

## Purpose

RuneLite QA Cockpit is the verification-focused continuation of Bert's Skill Atlas / Skill Guide: one working RuneLite cockpit for guide content, preparation, map/location assistance, money-making, settings, overlays, links, and **True Content QA**.

The project must not be restarted from an empty template merely because the newest plugin bytes are currently unresolved. Recovery, identity proof, content validation, current RuneLite compatibility, and real user-driven in-game verification come before broad framework or feature rewrites.

This page is intentionally split into two kinds of evidence:

1. **Preserved project continuity** - what earlier project records say the QA Cockpit lineage contained.
2. **Current RuneLite qualification authority** - the current external-plugin build/review/runtime rules a recovered QA Cockpit must satisfy now.

Do not allow either source to impersonate the other. Historical counts do not prove current source bytes, and a clean modern template does not prove the user's original cockpit content.

---

## Preserved project lineage

Durable Project Constellation evidence records this sequence:

1. `Bert's Skill Guide Master`
2. `bert-skill-guide-master.zip`
3. `bert-skill-atlas-ultra.zip`
4. `bert-skill-atlas-unified-cockpit.zip`
5. `bert-skill-atlas-qa-cockpit.zip`

The Unified Cockpit was previously described as preserving:

- 24 skills including Sailing;
- 144 routes;
- 404 money-makers;
- 211 quest entries;
- 4,877 quest steps.

These are **continuity counts only** until they are re-derived from the recovered QA Cockpit source. Never copy them into a new database merely to make a replacement build match a historical number.

### Intended product surface

Preserved project evidence describes one integrated RuneLite experience covering:

- skill guides and route planning;
- preparation requirements;
- map/location assistance;
- money-making data;
- quest/step content;
- object/NPC/tile/inventory/bank/equipment overlays;
- Wiki and Prices actions;
- settings;
- True Content QA for malformed, missing, conflicting, or unreachable content.

A sidebar that simply renders tabs is not sufficient. Each visible workspace must execute its real workflow end-to-end.

---

## Current RuneLite compatibility baseline - 2026-08-22

The canonical QA Cockpit source is still missing, but the **current external-plugin qualification target is not ambiguous**.

### RuneLite Plugin Hub baseline

Current official `runelite/plugin-hub` state inspected for this pass:

- Plugin Hub `runelite.version`: **`1.12.36`**
- Plugin Hub master head at inspection: `e39910dc2f8ec6549b4e30163403a9e667fbd4d5`
- Official Plugin Hub repository: https://github.com/runelite/plugin-hub
- Official current external-plugin template: https://github.com/runelite/example-plugin

Treat `1.12.36` as the **current compatibility checkpoint observed in this documentation pass**, not a permanent hard-coded version. On every actual recovery/build pass, reread `runelite/plugin-hub/runelite.version` and the current template first.

### Current example-plugin baseline

The current official `runelite/example-plugin` master head inspected for this pass is:

`5370caa0f5f6a5bba4fbb42931722ca535ad3fd5`

Its current build contract includes:

- Java 11 source compatibility;
- `runeLiteVersion = 'latest.release'`;
- the Gradle `run` task launching the development client with developer/debug mode;
- Gradle wrapper **8.10**;
- wrapper distribution SHA-256 verification;
- `compileOnly` RuneLite client dependency;
- JUnit test dependency;
- no assumption that Plugin Hub resources are unpacked as ordinary files.

The official example template is a **compatibility reference**, not a replacement for the recovered QA Cockpit repository.

---

## Current Plugin Hub development and review rules

A recovered QA Cockpit should be reconciled against current official RuneLite Plugin Hub guidance before feature work.

### Build and language

Current Plugin Hub guidance requires/recommends:

- **Java 11** for Plugin Hub plugins;
- IntelliJ IDEA Community Edition plus Eclipse Temurin Java 11 as the standard development environment;
- the Gradle `run` task for external-plugin development;
- `runelite-plugin.properties` with current plugin metadata;
- `build=standard` when the plugin needs no custom dependencies/build steps, or `build=gradle` when it genuinely does;
- `runeLiteVersion = 'latest.release'` when tracking the latest normal RuneLite release.

Do not migrate the recovered plugin to Kotlin, Scala, JNI/JNA, or another native/runtime layer simply because a modern stack exists. Plugin Hub reviewability is part of the product contract.

### Dependency integrity

Plugin Hub requires cryptographic verification for third-party dependencies that are not already RuneLite-client transitives.

For a recovered QA Cockpit:

1. inventory every declared dependency;
2. remove unnecessary direct declarations of RuneLite transitive libraries;
3. identify genuine third-party dependencies;
4. use Gradle dependency verification and SHA-256 metadata as required by Plugin Hub;
5. manually review dependency identity before accepting updated hashes;
6. prefer no extra dependency when equivalent functionality is already available from RuneLite or the JDK.

Dependency-version churn is not a feature improvement by itself.

### Threading and performance

Current RuneLite example-plugin guidance explicitly warns against expensive or blocking work on the client thread.

For QA Cockpit code:

- never use `Thread.sleep()` in client behavior;
- never block `startUp()` or `shutDown()` waiting for worker termination;
- cancel scheduled work explicitly on shutdown;
- avoid blocking disk or network I/O on the RuneLite client thread;
- use injected OkHttp asynchronously for network requests;
- return RuneLite API work to `clientThread.invoke(...)` when required;
- do not scan the entire scene every game tick/frame when spawn/despawn or state-change events can maintain a bounded working set;
- keep overlay rendering computation small and precompute data outside per-frame paint paths where possible.

A QA tool that makes the client hitch is not a successful QA tool.

### API, network, and persistence rules

Current example-plugin guidance establishes useful current defaults:

- prefer `net.runelite.api.gameval` constants over magic numeric IDs when an official constant exists;
- use `LinkBrowser` for opening links;
- use injected `OkHttpClient` and injected Gson rather than creating competing client stacks;
- keep plugin-owned file writes under RuneLite's `.runelite` directory, preferably in a project-specific subdirectory;
- use `JFileChooser` for explicit user-selected import/export locations;
- never silently rename a config key or config group without a migration;
- any optional feature that sends the user's IP to a third-party service must be opt-in and carry RuneLite's required warning.

For QA Cockpit this means content caches, exported QA reports, imported custom guide packs, and migration receipts need an explicit storage owner and versioned schema.

---

## Current forbidden/restricted implementation boundary

The 2026 RuneLite example-plugin agent guidelines and RuneLite's current rejected/rolled-back feature policy make several boundaries explicit.

Plugin Hub code must remain reviewable. Current guidance forbids or rejects patterns including:

- Java reflection;
- JNI or JNA;
- unsafe/native-memory tricks;
- launching external programs/processes;
- downloading or dynamically loading code at runtime;
- runtime code generation;
- Java object serialization;
- programmatic mouse/keyboard input injection;
- autotyping or modifying outgoing chat text;
- exposing player information over HTTP;
- crowdsourcing other players' location/gear/name data;
- direct credential-manager behavior;
- prohibited combat prediction/automation helpers;
- simulated game content that crosses current Jagex/RuneLite review policy.

Before re-enabling an old QA Cockpit feature, compare it against:

- https://github.com/runelite/example-plugin/blob/master/AGENTS.md
- https://github.com/runelite/runelite/wiki/Rejected-or-Rolled-Back-Features
- https://secure.runescape.com/m=news/third-party-client-guidelines?oldschool=1

A historical feature is not automatically acceptable simply because it worked in an older client.

### No automated in-game interaction for verification

Do **not** use browser automation, computer-use automation, synthetic mouse/keyboard injection, or a testing agent to play RuneScape in order to prove the plugin works.

Safe automated evidence includes:

- compilation;
- unit tests;
- pure content validators;
- serialization/deserialization tests for project-owned data formats;
- deterministic mapping tests;
- plugin startup in the development client without automated game input;
- static checks against current RuneLite API and Plugin Hub rules.

Final in-game behavior must be confirmed by the user in the real development client.

---

## Recovery-first source workflow

When `bert-skill-atlas-qa-cockpit.zip`, a canonical repository, or a newer verified successor is found, preserve it before changing it.

### 1. Record artifact identity

Capture at minimum:

```text
project ID: PCX-062
artifact/repository name:
source URL / Drive file ID / repository:
branch or archive filename:
embedded version:
file size:
SHA-256:
Git HEAD if applicable:
recovered timestamp:
predecessor / successor evidence:
```

Do not infer latest-good from filename number or Drive modification time alone.

### 2. Extract or clone cleanly

Never recover directly over another checkout.

For an archive:

1. preserve the original ZIP read-only;
2. verify ZIP integrity;
3. hash it;
4. extract to a fresh directory;
5. inventory files before running Gradle.

For a repository:

1. record remote URL and default branch;
2. record exact HEAD;
3. check for tags/releases;
4. inspect repository status before edits;
5. preserve any user-local changes.

### 3. Inventory build identity

Inspect before modifying:

```text
build.gradle
settings.gradle
gradlew
gradlew.bat
gradle/wrapper/gradle-wrapper.properties
runelite-plugin.properties
src/main/java/
src/main/resources/
src/test/java/
content/data directories
README / changelog / validation reports
```

If a Gradle wrapper exists, use the project wrapper first. Do not silently replace it with the current example-plugin wrapper until a compatibility migration is intentionally chosen and tested.

### 4. Re-derive project counts

Recompute from source rather than trusting historical summaries:

- skills;
- routes;
- money-makers;
- quest records;
- quest steps;
- overlay definitions;
- map/location targets;
- settings/config keys;
- external links;
- content QA rules.

Record old count, recovered count, reason for each difference, and whether the difference is intentional or a recovery defect.

---

## Build normalization after source recovery

The first goal is to make the **recovered source** build correctly, not to recreate the plugin around a fresh template.

### Preferred first pass

On Windows:

```powershell
.\gradlew.bat clean test
.\gradlew.bat run
```

On Linux/macOS:

```bash
./gradlew clean test
./gradlew run
```

The exact available tasks must come from the recovered build; these commands are only appropriate if its Gradle structure matches the current Plugin Hub-style project.

### If the recovered build is stale

Create a migration ledger comparing recovered build files against the current official example-plugin rather than copying the template wholesale.

Check specifically:

- Java release target;
- RuneLite dependency declaration;
- Gradle wrapper version/checksum;
- repository declarations;
- Lombok usage;
- test/runtime classpath;
- `pluginMainClass`;
- `runelite-plugin.properties` build type;
- third-party dependency verification;
- resource loading;
- forbidden APIs;
- config-key migrations.

Every change should preserve the QA Cockpit's project identity and content.

---

## Content architecture to preserve or reconstruct only from evidence

The exact current QA Cockpit source is unresolved, so the architecture below is an **acceptance model**, not a claim about class names in missing source.

A maintainable recovered implementation should have clear separation between:

```text
content records
  -> stable IDs / schema
  -> repository or loader
  -> validation / QA
  -> workspace presentation
  -> context/overlay actions
  -> persistence/config
```

Avoid embedding thousands of content records directly inside Swing panel construction code when the recovered project already has or can preserve a data-driven content layer.

### Stable identity

Every durable route, quest, step, money-maker, location, or target should have stable project-owned identity that survives display-name corrections.

Do not use list position as durable identity.

### Provenance

When content is corrected, retain enough provenance to answer:

- what changed;
- why;
- which game/RuneLite baseline was used;
- which source or project artifact justified it;
- which validation rule now covers the correction.

---

## True Content QA contract

True Content QA should reject bad project data before it becomes a misleading in-game guide.

At minimum, automated validators should detect:

### Identity and graph integrity

- duplicate IDs;
- orphan steps;
- missing route parents;
- unreachable routes or quest sections;
- invalid predecessor/successor links;
- cycles where the content model forbids them;
- unstable ID generation.

### Game target integrity

Where source data references RuneLite/game entities:

- prefer current official gameval constants where applicable;
- flag unresolved or retired IDs;
- distinguish item, NPC, object, widget, tile/location, and inventory/equipment target types;
- never silently coerce an unknown target into a generic one.

### Link integrity

Validate Wiki, Prices, and other outbound links for:

- expected host;
- exact intended entity/slug where deterministic;
- malformed URLs;
- dead local route references;
- wrong project content identity.

Do not turn a validation pass into uncontrolled live scraping from the client thread.

### Content completeness

Examples of project-level invariants worth generating from the recovered schema:

- every route has at least one valid step;
- every step belongs to exactly one valid route/section unless the schema explicitly supports reuse;
- ordering keys are deterministic;
- every money-maker has a stable identity and required metadata;
- every top-level skill has a valid navigation target;
- every overlay action points to a resolvable target type;
- required preparation entries are not silently dropped;
- serialized content reloads to the same semantic records.

Property-based testing is useful for these invariants, but use a **Java-native** library compatible with the recovered Gradle build instead of adding a JavaScript testing stack to a RuneLite plugin.

---

## Functional acceptance matrix

A release candidate is not ready because its Gradle build is green.

### Sidebar and top-level navigation

For every visible top-level section:

- direct entry reaches the intended workspace;
- clicking changes the actual workspace, not only selection styling;
- selected skill/route/quest context is preserved where promised;
- Back/forward/history behavior is correct if the plugin implements it;
- reopening the panel does not lose state unexpectedly;
- config/profile changes are reflected after reload/restart as intended.

### Guide workspace

Verify:

- skill selection;
- route selection;
- step ordering;
- requirements/preparation;
- exact next/previous navigation;
- malformed-data surfacing;
- current target context.

### Preparation workspace

Verify required items/stats/conditions are tied to the correct route or quest and do not leak between unrelated selections.

### Map/location workspace

Verify the UI identifies the exact promised destination. A generic map open is not sufficient if the action promises a specific target.

### Money workspace

Verify each entry's identity, source content, links, sorting/filtering, and any displayed requirements. Do not display stale values as live values unless the project has a verified current-data source.

### Settings

Verify:

- every setting has a real runtime consumer;
- defaults are truthful;
- renamed keys migrate;
- reset restores documented defaults;
- state survives restart where promised;
- networked features are opt-in when required by Plugin Hub policy.

### Overlays and highlights

Verify exact context for object/NPC/tile/inventory/bank/equipment highlights without automating clicks or game actions. Overlay drawing should not perform heavy content discovery every frame.

### Wiki and Prices actions

Use RuneLite's supported link-opening path and prove the destination matches the selected content entity.

### True Content QA

The QA cockpit must surface bad records with enough detail to fix them. Silent omission is a failure.

---

## Verification ladder

Use progressively stronger evidence.

### Gate 1 - artifact/source identity

- hash/source/HEAD recorded;
- clean extraction/checkout;
- no accidental overwrite of prior versions.

### Gate 2 - static/build integrity

- Gradle wrapper/bootstrap succeeds;
- Java 11 compatibility;
- compile passes;
- tests pass;
- no forbidden dependencies/APIs;
- resource paths work from JAR/classpath assumptions.

### Gate 3 - content QA

- counts re-derived;
- schema parses;
- stable identities verified;
- graph/link/target invariants pass;
- malformed fixtures fail truthfully.

### Gate 4 - development client startup

Launch with the project's supported `run` task and prove the recovered plugin loads into a current development client.

Do not call this an in-game pass yet.

### Gate 5 - user-driven in-game workflow

The user logs in through the current supported Jagex-account development-client flow and manually verifies the changed workflows.

Do not automate gameplay input.

### Gate 6 - restart/persistence

Exit the development client, relaunch, and verify project settings/data state that promises persistence.

### Gate 7 - packaging / Plugin Hub readiness

If Plugin Hub publication is intended:

- public repository identity established;
- permissive license present;
- `runelite-plugin.properties` correct;
- exact commit selected;
- Plugin Hub marker references the exact commit;
- CI passes;
- dependency verification is complete;
- no prohibited feature is present.

---

## Current Plugin Hub submission model

Plugin Hub tracks plugins using small manifest files under its `plugins/` directory:

```text
repository=https://github.com/<owner>/<plugin>.git
commit=<40-character commit SHA>
```

This is useful for PCX-062 because it creates a clean release identity: the exact Plugin Hub marker commit must correspond to the exact plugin source that was qualified.

Do not document "latest main" as a release identity if Plugin Hub points to a different commit.

---

## Persistence and migration expectations

When recovered, inventory all persistent state before changing configuration.

Typical categories may include:

- RuneLite config values;
- plugin-owned files under `.runelite/<plugin>/`;
- imported/exported project content selected by the user;
- UI selection/navigation state if intentionally persistent;
- content-QA caches or reports.

For every persistent schema/key change:

1. define previous format;
2. define new format;
3. provide migration;
4. preserve unknown valid data where possible;
5. make corrupt-state handling explicit;
6. test restart after migration;
7. provide a safe reset path that does not delete unrelated RuneLite state.

---

## Troubleshooting

### The QA Cockpit source still cannot be found

Do not initialize a replacement project. Search for the preserved QA Cockpit archive/repository lineage, compare plausible copies by content and embedded metadata, and preserve all candidates until latest-good identity is resolved.

### `runeliteVersion` / API compilation errors after recovery

First reread current Plugin Hub `runelite.version` and current example-plugin. If the recovered plugin intentionally targets an older baseline, record that before changing it. Migrate API usage deliberately rather than changing random numeric IDs until compilation succeeds.

### Gradle wrapper fails

Inspect `gradle-wrapper.properties`, distribution URL, wrapper checksum, Java home, and the recovered repository's intended wrapper version. Do not blindly replace the wrapper because the current template happens to use Gradle 8.10.

### Client launches but the plugin is missing

Confirm the correct test main/plugin main class, external-plugin loading path, `runelite-plugin.properties`, current build output, and that the development client actually loaded the changed checkout rather than another copy.

### Plugin freezes or causes hitches

Inspect client-thread disk/network work, tick-wide scans, overlay-frame computation, blocking futures, and uncancelled scheduled tasks first.

### Links open the wrong destination

Verify the selected content identity and use RuneLite `LinkBrowser`. Do not build URLs from display text when a stable route/entity key exists.

### Settings reset after an update

Check whether a config group/key was renamed without migration. Treat silent config loss as a regression.

### QA reports different counts from the historical record

Do not force the recovered data to match 24/144/404/211/4,877. Produce a diff ledger and determine whether the difference is a valid later content change, a historical counting-method difference, or a recovery defect.

### A test wants to automate RuneScape input

Stop. Keep automation at code/content/startup verification and require user-driven in-game confirmation.

---

## Contribution workflow after recovery

A safe contribution should normally follow:

1. resolve canonical repository and exact base commit;
2. make one scoped content or implementation change;
3. add/update deterministic QA coverage;
4. run project-owned compile/tests;
5. run full content validators when content changes;
6. launch the development client;
7. have the user manually verify the affected in-game workflow;
8. restart when state/persistence changed;
9. record exact artifact/commit identity;
10. update Plugin Hub marker only after the exact commit is ready for review.

Avoid mixing broad formatting changes with feature/content fixes because it makes review and recovery comparisons harder.

---

## Current external qualification references

Use these as current references, not as substitutes for the missing project source:

- RuneLite Plugin Hub: https://github.com/runelite/plugin-hub
- Current Plugin Hub version file: https://github.com/runelite/plugin-hub/blob/master/runelite.version
- Official example plugin: https://github.com/runelite/example-plugin
- Current example-plugin agent/review rules: https://github.com/runelite/example-plugin/blob/master/AGENTS.md
- RuneLite build/development guide: https://github.com/runelite/runelite/wiki/Building-with-IntelliJ-IDEA
- RuneLite rejected/rolled-back features: https://github.com/runelite/runelite/wiki/Rejected-or-Rolled-Back-Features
- Jagex third-party client guidelines: https://secure.runescape.com/m=news/third-party-client-guidelines?oldschool=1
- Jagex-account development-client login: https://github.com/runelite/runelite/wiki/Using-Jagex-Accounts

---

## Exact current next action

**Recover the newest canonical QA Cockpit source bytes first.**

When found:

1. preserve and hash them;
2. re-derive project counts;
3. compare the recovered build contract against the current Plugin Hub `1.12.36` / Java-11 / example-plugin baseline;
4. run build and pure content QA;
5. launch the current development client;
6. perform user-driven guide/prep/map/money/settings/overlay/link/QA verification;
7. restart and verify persistent state;
8. only then decide whether a Plugin Hub or architecture migration is warranted.

## Current blocker

Fresh connected Drive/GitHub searches in this pass still did **not** expose `bert-skill-atlas-qa-cockpit.zip` or a canonical user-owned QA Cockpit repository. Current evidence therefore supports a stronger recovery/qualification contract, but not a runnable build claim.

## Wiki maintenance

Update this page immediately when:

- canonical QA Cockpit bytes are recovered;
- a newer verified successor is found;
- historical counts are re-derived;
- the RuneLite Plugin Hub baseline materially changes;
- Plugin Hub review/restriction rules change;
- build/runtime/restart verification changes the stop point;
- the project is actually published or installed against a current RuneLite release.
