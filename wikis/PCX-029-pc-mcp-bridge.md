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

The official [Model Context Protocol 2026-07-28 release announcement](https://blog.modelcontextprotocol.io/posts/2026-07-28/) and [specification](https://modelcontextprotocol.io/specification/2026-07-28) establish `2026-07-28` as the current released protocol revision. Major transport and authorization changes include:

- a stateless protocol core;
- retirement of the protocol-level `initialize` / `initialized` exchange and `Mcp-Session-Id` for the new revision;
- optional `server/discover` for capability/version discovery;
- `Mcp-Method` and `Mcp-Name` request headers for routing/authorization;
- Multi Round-Trip Requests for interactions that previously required server-initiated requests;
- cache hints and deterministic ordering for list/read responses;
- formal extensions including Tasks;
- authorization hardening and migration away from Dynamic Client Registration toward Client ID Metadata Documents;
- a twelve-month minimum deprecation window for deprecated protocol features.

The release announcement states that the TypeScript, Python, Go, and C# Tier 1 SDKs were updated for this revision.

### SDK compatibility evidence checked 2026-08-17

The official [Go SDK compatibility matrix](https://github.com/modelcontextprotocol/go-sdk/blob/main/README.md) records Go SDK **v1.7.0+** as supporting `2026-07-28` while retaining `2025-11-25`, `2025-06-18`, `2025-03-26`, and `2024-11-05` compatibility. Its protocol documentation explicitly supports both lifecycle eras: `server/discover`/per-request metadata for `2026-07-28`, and fallback to legacy `initialize` when the peer negotiates an older revision.

The Go SDK also documents an important transport boundary: Streamable HTTP accepts `2026-07-28` only in stateless mode. If a deployment keeps stateful Streamable HTTP sessions, it negotiates an older protocol revision instead of pretending to provide the new semantics.

The official [TypeScript SDK migration guide](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/migration/support-2026-07-28.md) requires explicit version-negotiation opt-in for existing v2 code paths. This is useful evidence that SDK presence alone is not proof that an existing bridge is speaking the new wire protocol.

### Transport migration implication

For PC Bridge, treat protocol revision as an explicit compatibility dimension rather than a global upgrade switch. A bridge that supports `2026-07-28` must prove the new stateless request model, discovery/version negotiation, authorization headers, cancellation/error behavior, and tool identity. A legacy client path must continue to negotiate and execute correctly until that compatibility is intentionally retired.

**Proposal:** implement a versioned transport adapter instead of rewriting the bridge wholesale. Preserve old-client compatibility where currently required, then add a `2026-07-28` path with stateless requests, explicit discovery, header routing, current authorization handling, and conformance fixtures.

**Why it fits:** a PC capability bridge can scale and recover more cleanly when transport state is not hidden in a long-lived protocol session, while explicit capability metadata makes truthful discovery easier to test.

**Integration cost:** high if the current bridge depends on sessions or server-initiated streaming; low to medium if transport is already isolated behind an adapter.

**Risks:** protocol migration can create fake compatibility if the bridge accepts calls but drops identity, authorization, cancellation, progress, or multi-round user input semantics. Legacy clients must not silently break. SDKs can also expose compatibility shims, so a successful library upgrade does not prove the intended wire revision was negotiated.

**Small experiment:** expose three low-risk fixture tools through both the current and `2026-07-28` adapters: capability echo, read-only filesystem metadata, and a bounded local command that returns deterministic fixture output. Run the same fixtures from one known `2025-11-25` client and one `2026-07-28` client, recording negotiated version, request headers/metadata, authorization context, tool identity, result, cancellation/error behavior, and restart behavior.

**Acceptance test:** current supported clients continue to work; the `2026-07-28` client discovers and calls the exact intended tools; each run records the actual negotiated revision; authorization is enforced; repeated/restarted new-protocol calls are stateless at the MCP transport layer; legacy fallback uses the legacy lifecycle rather than a mixed state; multi-round requests resume correctly where supported; and observed local results prove the real capability executed.

### Conformance candidate

The official [MCP conformance repository](https://github.com/modelcontextprotocol/conformance) has revision-aware SDK fixtures, including `--spec-version 2026-07-28` handling for stateless server configurations. Once the canonical bridge source is recovered, use the official conformance suite as an additive protocol check alongside bridge-owned end-to-end tool fixtures. Conformance must not replace proof that the local PC capability actually ran.

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
- Never claim `2026-07-28` compatibility merely because an SDK dependency supports it; record the negotiated wire revision from the actual fixture.
- Never remove a currently supported legacy MCP path until its retirement is explicit and replacement parity is verified.

## Documentation gaps

- Canonical standalone source unresolved.
- Current implemented tool inventory unresolved.
- Current protocol version and legacy-client matrix unresolved.
- Current authentication provider/runtime unresolved.

## Wiki maintenance

Update this page when the canonical bridge source is found, protocol versions change, tool inventory changes, authorization changes, or real local tool flows are verified. Preserve compatibility/migration evidence instead of deleting the old transport story.