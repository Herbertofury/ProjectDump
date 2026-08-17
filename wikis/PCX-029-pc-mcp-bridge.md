# PC Bridge / MCP Bridge Wiki

**Project Constellation ID:** `PCX-029`  
**Status:** ACTIVE / TRACKED  
**Confidence:** Medium  
**Canonical source repository:** unresolved in connected evidence

## Purpose

PC Bridge / MCP Bridge exists to expose authorized local-PC capabilities as truthful Model Context Protocol tools. The bridge must preserve tool identity, capability discovery, authorization state, observable results, and real end-to-end execution. A successful transport handshake is never sufficient proof that a local capability works.

## Current verified Project Constellation contract

The durable project record requires:

- truthful capability discovery;
- preserved tool identity;
- preserved authentication/authorization state;
- real tool-call verification rather than handshake-only success.

Current Drive searches also show multiple Feature Foundry bridge artifacts, but they are not sufficient to establish that any one of them is the canonical standalone PC Bridge implementation. Project identity remains intentionally unresolved until direct project-owned source is found.

## Current stop point

The standalone bridge's canonical repository, current protocol version, implemented tool set, and runtime verification evidence are unresolved.

## Exact next action

Resolve the actual bridge source and protocol version, then build a compatibility matrix against MCP `2026-07-28` before changing transport behavior.

## Current technology research

### MCP specification 2026-07-28

The official [Model Context Protocol](https://github.com/modelcontextprotocol/modelcontextprotocol) project released specification **2026-07-28** with major transport and authorization changes:

- a stateless protocol core;
- retirement of the protocol-level `initialize` / `initialized` exchange and `Mcp-Session-Id`;
- optional `server/discover` for capability discovery;
- `Mcp-Method` and `Mcp-Name` request headers for routing/authorization;
- Multi Round-Trip Requests for interactions that previously required server-initiated requests;
- cache hints and deterministic ordering for list/read responses;
- formal extensions including Tasks;
- authorization hardening and migration away from Dynamic Client Registration toward Client ID Metadata Documents;
- a twelve-month minimum deprecation window for deprecated protocol features.

**Proposal:** implement a versioned transport adapter instead of rewriting the bridge wholesale. Preserve old-client compatibility where currently required, then add a `2026-07-28` path with stateless requests, explicit discovery, header routing, current authorization handling, and conformance fixtures.

**Why it fits:** a PC capability bridge can scale and recover more cleanly when transport state is not hidden in a long-lived protocol session, while explicit capability metadata makes truthful discovery easier to test.

**Integration cost:** high if the current bridge depends on sessions or server-initiated streaming; low to medium if transport is already isolated behind an adapter.

**Risks:** protocol migration can create fake compatibility if the bridge accepts calls but drops identity, authorization, cancellation, progress, or multi-round user input semantics. Legacy clients must not silently break.

**Small experiment:** expose three low-risk fixture tools through both current and `2026-07-28` adapters: capability echo, read-only filesystem metadata, and a bounded local command that returns deterministic fixture output. Record headers, authorization context, tool identity, result, failure behavior, and restart behavior.

**Acceptance test:** current supported clients continue to work; the new client discovers and calls the exact intended tools; authorization is enforced; repeated/restarted calls are stateless at the MCP transport layer; multi-round requests resume correctly where supported; and observed local results prove the real capability executed.

## Capability truth model

Each exposed tool should record:

- stable tool ID/name
- protocol version(s)
- local implementation owner
- required authorization/capability
- input schema
- output schema
- side-effect class
- timeout/cancellation behavior
- restart/persistence behavior
- last real verification timestamp
- implementation/build identity

## Anti-degradation contract

- Never advertise a tool before its implementation is callable.
- Never return success before the local operation succeeds.
- Never downgrade authorization to simplify MCP compatibility.
- Never replace exact tool destinations with generic shell/homepage behavior.
- Never count handshake/discovery success as end-to-end tool proof.

## Documentation gaps

- Canonical standalone source unresolved.
- Current implemented tool inventory unresolved.
- Current protocol version and legacy-client matrix unresolved.
- Current authentication provider/runtime unresolved.

## Wiki maintenance

Update this page when the canonical bridge source is found, protocol versions change, tool inventory changes, authorization changes, or real local tool flows are verified. Preserve compatibility/migration evidence instead of deleting the old transport story.