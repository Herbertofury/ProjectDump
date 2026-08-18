# Profit Nova Wiki

**Project Constellation ID:** `PCX-032`
**Status:** ACTIVE / TRACKED
**Current source boundary:** direct strict master-plan artifacts are present in the durable project evidence; no canonical production GitHub application repository has yet been resolved.

## Purpose

Profit Nova is an agent-first money operations station: a navigable, room-based application that discovers real income opportunities, scores them, turns them into executable offers/assets/workflows, routes work through specialized agents, and preserves durable operational state.

The project is not a generic chatbot wrapper or idea generator. Its core contract is to convert messy market signals into ranked, inspectable, executable money missions with visible agent coordination, review gates, rollback, persistent memory, and real output.

## Current master-spec lineage

The newest directly recovered plan is:

- `money_app_plan_v39_strict_master_spec.md`.

Important predecessor evidence remains relevant:

- `money_app_plan_v38_no_meta_prompts.md`;
- `money_app_plan_v36_hermes_agent_full_use.md`;
- earlier v34+ migration/donor planning.

The v39 strict edition explicitly converts soft planning language into binding implementation instructions and says a subsystem is not complete until its acceptance criteria are satisfied.

Some older sections still use the historical working title **Money Rooms**. The Project Constellation project identity remains **Profit Nova**, and later plan directives lock the product into the Profit Nova / money-operations-station identity. Preserve the naming lineage rather than treating the old working title as a separate project.

## Product contract

Profit Nova must visibly combine a command center with a game-like facility.

Core behavior:

- discover real opportunities across marketplaces and demand-signal sources;
- score them by speed, effort, competition, repeatability, automation fit, reach, margin, and risk;
- generate the assets required to execute an opportunity;
- route jobs through specialized agents/rooms;
- expose approvals, logs, state, evidence, and outputs;
- turn repeated service work into reusable products/offers;
- preserve durable money/mission/account/memory state.

The strict plan prioritizes actual executable money paths over broad feature theater.

## Current product identity and world model

The recovered plan evolves the UI beyond a dashboard into a navigable money operations station.

The facility model includes:

- a visually dominant command/orchestrator room;
- specialized discovery, forge, offer/mint, factory, outreach, market, audit, memory, and operations rooms;
- visible workers in rooms;
- facility overview and walkable-room modes;
- a player/avatar that can move between departments;
- explicit room/component sizing;
- room activity, agent-to-agent messages, mission/job movement, and operational feedback.

This navigable facility is functional product architecture, not decoration. Entering a room must expose that room's real domain workflow and state.

## Hard acceptance boundaries

The recovered strict plan requires full end-to-end behavior before completion claims.

Important persistent systems must not be cut merely to simplify implementation, including the plan's user-facing room/workflow architecture, review/approval ladder, memory system, account/control surfaces, money/ledger control plane, inbox/communications flow, rollback/recovery behavior, and core monetization rooms.

Every visible room/control remains a promise. A room that only animates, changes a highlight, or displays generated placeholder text without running its real workflow is incomplete.

## Current architecture lineage

The later recovered plan family moves toward a native hybrid architecture rather than preserving every early web-stack suggestion literally.

Current planning evidence includes:

- Tauri 2 shell;
- Bevy world/facility runtime;
- Rapier 2D physics where appropriate;
- room manifests/contracts;
- durable local state;
- explicit command/service/event/permission/memory contracts;
- donor implementations adapted behind Profit Nova-owned boundaries rather than copied as product architecture.

Early Next.js/LangGraph/n8n guidance remains useful historical research for service/API/agent patterns, but later native architecture directives supersede it where they conflict.

## Hermes Agent integration contract

The recovered v36 plan makes [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) a first-class operational donor/integration layer for areas such as:

- agent runtime patterns;
- messaging/gateway behavior;
- skills;
- schedules/cron;
- delegation/subagents;
- memory patterns;
- terminal/TUI operation;
- MCP/tool connectivity;
- remote execution.

Hermes must **not** replace Profit Nova's:

- Bevy facility/world rendering;
- Tauri application shell;
- room manifests;
- review/approval ladder;
- Memory Atlas routing;
- economic/money control-plane rules;
- project-owned event/service/permission contracts.

### Hermes freshness, checked 2026-08-18

The current verified Hermes release checkpoint is **v0.20.3 / v2026.8.16.2**, published by release commit `7339f5f160db5c96657a3bab60151227cc61f66c`. This supersedes the prior wiki statement that v0.20.2 was current.

Upstream main is already moving beyond that release. Commit `22f0f22298cc322c095b6c93a648e809e80443b6` fixes cron/manual-run media-delivery parity by surfacing attachment failures and applying the same media-policy bridge outside the gateway process, with eight new regression tests. That is useful donor evidence, but it is also a strong reason **not** to bind Profit Nova directly to moving Hermes main.

### Hermes donor decision

Use **v0.20.3 as the current donor comparison baseline**, and keep all Hermes integration behind Profit Nova-owned adapters. Evaluate post-release commits individually when they solve a demonstrated Profit Nova problem, then pin the adopted commit/release with its exact behavior and tests.

Do not silently follow Hermes main. A donor update is accepted only when Profit Nova's room, review, memory, permission, economic, and recovery contracts remain intact.

## Current stack freshness, checked 2026-08-18

### Bevy

The plan family references Bevy 0.18, while [Bevy 0.19](https://bevy.org/news/bevy-0-19/) was released June 19, 2026.

Relevant 0.19 additions include:

- next-generation scenes / BSN;
- large-scene rendering improvements;
- text input;
- app settings;
- built-in transform gizmo;
- continued editor tooling work.

These are directly relevant to a room/facility authoring runtime, but Bevy 0.19 is still an **upgrade candidate**, not an automatic migration. The canonical Profit Nova source must first be found and its actual Bevy integration/build baseline measured.

### Tauri

The later plan family targets Tauri 2. Current 2.11-line evidence should be treated as a migration input rather than a blind upgrade target. Once the real source is recovered, read the exact manifests/lockfile and current Tauri release notes before changing windowing, IPC, storage, updater, packaging, or restart behavior.

### Temporal as an optional durable-workflow experiment

[Temporal TypeScript SDK v1.21.1](https://github.com/temporalio/sdk-typescript/releases/tag/v1.21.1) remains the current release line identified in this pass. v1.21.0 also added experimental agent-oriented integrations and stricter payload-limit handling.

Profit Nova should **not** replace its room manifests, event bus, review ladder, or project-owned state machine with Temporal simply because durable workflows are attractive.

A bounded experiment is justified for one genuinely long-running money workflow where durable retries/resume/timeout semantics are valuable, for example:

`approved mission -> asset generation -> external publish/export -> verification -> retry/rollback`

Acceptance requires idempotent activity boundaries, truthful operator-visible state, restart recovery, and no duplication of a publish/payment action.

## Donor architecture rule

External repositories and agent frameworks are donors, not owners of Profit Nova's product contract.

For every donor subsystem, record:

- source repository and exact version/commit;
- behavior being borrowed;
- Profit Nova-owned service/event/permission/memory boundary;
- data migration/adapter;
- failure behavior;
- rollback plan;
- verification proving the donor does not take ownership of unrelated product state.

This prevents donor churn from fragmenting the product.

## Opportunity and execution model

The recovered plan prioritizes service/lead-generation work first, then digital products/templates, then short-form distribution/content systems.

Each opportunity should retain structured evidence including:

- channel/source;
- demand evidence;
- opportunity type;
- buyer intent;
- setup time;
- fulfillment time;
- expected sale-value range;
- gross-margin estimate;
- repeatability;
- automation coverage;
- saturation;
- dispute/refund risk;
- human-taste requirement;
- supporting sources;
- recommended execution path.

Generated outputs should carry size/type/cost/time metadata where applicable rather than appearing as opaque blobs.

## Agent/room workflow

A representative pipeline remains:

1. Scout discovers opportunities.
2. Analyst scores and compares them.
3. Orchestrator selects or presents approval choices.
4. Offer/Mint packages the mission.
5. Asset/Factory workers create deliverables.
6. Publisher/Market formats or exports channel-specific output.
7. Audit verifies quality, profitability, evidence, and failure risk.
8. Optimizer feeds results back into the next iteration.

The operator must be able to inspect the handoff and result at each stage.

## Memory, review, and control plane

Profit Nova needs durable state for:

- opportunity evidence;
- missions/runs;
- assets and provenance;
- agent tasks;
- room state;
- approvals and rejections;
- account/provider state;
- publication/export state;
- economic/ledger state;
- recovery/checkpoints;
- learning that is explicitly promoted rather than silently hallucinated into future runs.

A successful automation must never be inferred merely from a visual room animation or generated success toast.

## Current source problem

No production Profit Nova GitHub repository has been resolved from the connected repository set in this pass. Durable project evidence contains a substantial v39 strict spec and supporting lineage, but that is not runtime proof.

Do not initialize a new replacement app or treat a prototype as canonical merely because the production source path is unresolved.

## Smallest useful current experiment

After resolving the canonical source:

1. identify actual Tauri/Bevy/Hermes/runtime versions from manifests and lockfiles;
2. launch the current build and record its loaded identity;
3. exercise one existing money mission end to end;
4. compare actual implementation to the v39 room/event/memory/review contract;
5. separately evaluate Bevy 0.19 and Hermes v0.20.3 behind adapters;
6. inspect post-v0.20.3 Hermes fixes only when they map to a demonstrated Profit Nova failure;
7. run one bounded Temporal durable-workflow experiment only if the existing orchestration path has a demonstrated resume/retry gap.

## Exact current next action

Locate the canonical Profit Nova repository/worktree and reconcile it against `money_app_plan_v39_strict_master_spec.md` plus the Hermes integration lineage. Establish the real Tauri/Bevy/agent baseline before adopting Bevy 0.19, Hermes v0.20.3 APIs, Temporal, or any other stack migration. Keep Hermes behind a release-pinned adapter boundary so upstream churn cannot silently mutate Profit Nova state.

## Wiki maintenance

Update this page when the production repository is resolved, a room/workflow becomes runtime-proven, provider/account/publish behavior is verified, a donor version is promoted, the Bevy/Tauri/Hermes baseline changes, money-state persistence is proven, or the strict master plan is superseded by newer explicit user direction.
