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

Current connected Drive searches still expose Feature Foundry bridge artifacts and prior PCX-029 wiki/checkpoint material, but they do not establish a canonical standalone PC Bridge implementation. Connected GitHub repository search likewise did not resolve a standalone bridge repository in this pass. Project identity therefore remains intentionally unresolved until direct project-owned source is found.

## Current stop point

The standalone bridge's canonical repository, current implemented tool inventory, current protocol revision, authentication provider, and runtime verification evidence remain unresolved.

## Exact next action

Resolve the actual bridge source and negotiated protocol behavior, then build a compatibility matrix against MCP `2026-07-28` before changing transport behavior.

## Current protocol authority

The released [Model Context Protocol 2026-07-28 specification](https://modelcontextprotocol.io/specification/2026-07-28) and its authoritative schema identify `2026-07-28` as the current protocol revision.

The current specification makes an important distinction that this wiki previously described too loosely:

- **Servers MUST implement `server/discover`.** This is the modern discovery endpoint for supported protocol versions, server capabilities, and server identity.
- **Clients are not required to call `server/discover` before every request.** A client may send an RPC directly and handle `UnsupportedProtocolVersionError` if the requested revision is unsupported.
- A client supporting both modern and legacy behavior over **stdio SHOULD call `server/discover` first** so it can distinguish the modern per-request model from the older `initialize` lifecycle.
- `serverInfo` returned by discovery is self-reported metadata. Clients should not use it as an authorization or security decision signal.

Canonical discovery source: [MCP `server/discover` specification](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2026-07-28/server/discover.mdx)

This server-mandatory/client-optional distinction is now part of PCX-029's protocol acceptance contract. A bridge cannot claim complete `2026-07-28` server compatibility while omitting `server/discover`, even if direct tool calls happen to work.

## MCP specification 2026-07-28

The official [2026-07-28 release announcement](https://blog.modelcontextprotocol.io/posts/2026-07-28/) and [specification](https://modelcontextprotocol.io/specification/2026-07-28) establish `2026-07-28` as the current released protocol revision. Major transport and authorization changes include:

- a stateless protocol core;
- retirement of the protocol-level `initialize` / `initialized` exchange and `Mcp-Session-Id` for the new revision;
- mandatory server support for `server/discover`, with client invocation optional except where compatibility probing requires it;
- `Mcp-Method` and `Mcp-Name` request headers for routing/authorization;
- Multi Round-Trip Requests for interactions that previously required server-initiated requests;
- cache hints and deterministic ordering for list/read responses;
- formal extensions including Tasks;
- authorization hardening and migration away from Dynamic Client Registration toward Client ID Metadata Documents;
- a twelve-month minimum deprecation window for deprecated protocol features.

The release announcement states that the TypeScript, Python, Go, and C# Tier 1 SDKs were updated for this revision.

## Streamable HTTP behavior in 2026-07-28

The current [Streamable HTTP specification](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2026-07-28/basic/transports/streamable-http.mdx) removes the protocol-level GET stream and protocol-level sessions for the modern revision.

For a PC Bridge implementation, that means:

- the server exposes one MCP HTTP endpoint;
- each JSON-RPC request or notification is sent as its own HTTP POST;
- a request may receive either one JSON response or a request-scoped SSE response;
- the transport must not quietly depend on `Mcp-Session-Id` for modern requests;
- per-request version/capability metadata must survive routing and authorization;
- cancellation and termination behavior must be verified in the actual transport rather than inferred from an SDK version.

If the recovered bridge currently depends on stateful Streamable HTTP sessions, preserve that behavior behind a legacy adapter until the modern path is independently qualified.

## SDK compatibility evidence

### TypeScript SDK

The official [TypeScript SDK 2026-07-28 migration guide](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/migration/support-2026-07-28.md) makes an important compatibility point: upgrading to the v2 package line does not automatically place `2026-07-28` traffic on the wire. Existing hand-constructed clients and servers remain on the 2025-era lifecycle unless the modern revision is explicitly enabled.

For clients, `versionNegotiation` can explicitly select legacy, automatic discovery/fallback, or a pinned modern revision. In automatic mode the SDK probes with `server/discover` and can fall back to the legacy `initialize` path when policy and transport conditions allow it.

For servers, the modern HTTP path is served through the current per-request handler API, while stdio uses a connection-era serving entrypoint so modern and legacy behavior are not accidentally mixed.

This is direct evidence that **SDK dependency version is not wire-protocol proof**. PCX-029 must record the revision negotiated or pinned by the actual fixture.

### Go SDK

The official [Go SDK](https://github.com/modelcontextprotocol/go-sdk) documents modern and legacy protocol compatibility and is a useful second implementation for interoperability fixtures. It should be used as an independent client/server counterparty when the recovered bridge's implementation language differs.

## Transport migration implication

For PC Bridge, treat protocol revision as an explicit compatibility dimension rather than a global upgrade switch. A bridge that supports `2026-07-28` must prove the new stateless request model, required server discovery, version selection, authorization metadata, cancellation/error behavior, and tool identity. A legacy client path must continue to negotiate and execute correctly until that compatibility is intentionally retired.

**Proposal:** implement a versioned transport adapter instead of rewriting the bridge wholesale. Preserve old-client compatibility where currently required, then add a `2026-07-28` path with stateless requests, mandatory server discovery support, per-request metadata, current authorization handling, and conformance fixtures.

**Why it fits:** a PC capability bridge can scale and recover more cleanly when transport state is not hidden in a long-lived protocol session, while explicit capability/version metadata makes truthful discovery easier to test.

**Integration cost:** high if the current bridge depends on sessions or server-initiated streaming; low to medium if transport is already isolated behind an adapter.

**Risks:** protocol migration can create fake compatibility if the bridge accepts calls but drops identity, authorization, cancellation, progress, or multi-round user input semantics. Legacy clients must not silently break. SDKs can also expose compatibility shims, so a successful package upgrade does not prove the intended wire revision was negotiated.

## Small compatibility experiment

Once the canonical bridge source is recovered, expose three low-risk fixture tools through both the current and `2026-07-28` adapters:

1. capability echo;
2. read-only filesystem metadata against a deterministic fixture path;
3. a bounded local command that returns deterministic fixture output.

Run the same fixtures from one known `2025-11-25` client and one `2026-07-28` client. Record:

- requested and negotiated protocol revision;
- whether `server/discover` is implemented and what it reports;
- whether the client called discovery or used direct inline RPC;
- request `_meta` and applicable routing/authorization headers;
- authorization context;
- stable tool identity;
- input/output schema identity;
- local implementation/build identity;
- observable result;
- cancellation/error behavior;
- restart behavior.

### Acceptance test

A compatibility pass requires all of the following:

- current supported legacy clients continue to work;
- the modern server implements `server/discover` and reports the expected supported revision/capabilities;
- a modern client can either discover first or make an allowed direct call and receive correct version handling;
- stdio dual-era clients use the required discovery/fallback behavior rather than mixing lifecycles;
- each run records the actual revision used, not merely the installed SDK version;
- authorization is enforced before privileged local work executes;
- repeated/restarted new-protocol calls do not rely on hidden MCP protocol session state;
- legacy fallback uses the legacy lifecycle rather than a mixed state;
- multi-round requests resume correctly where supported;
- cancellation reaches the real operation;
- observed local results prove the intended PC capability actually executed.

## Conformance candidate

The official [MCP conformance repository](https://github.com/modelcontextprotocol/conformance) contains revision-aware fixtures. Once the canonical bridge source is recovered, use the official conformance suite as an additive protocol check alongside bridge-owned end-to-end tool fixtures.

Conformance is not enough by itself. A bridge can pass protocol framing while exposing a dead, misrouted, unauthorized, or fake local capability. Every advertised tool still needs real end-to-end execution evidence.

## Capability truth model

Each exposed tool should record:

- stable tool ID/name;
- protocol version(s);
- local implementation owner;
- required authorization/capability;
- input schema;
- output schema;
- side-effect class;
- timeout/cancellation behavior;
- restart/persistence behavior;
- last real verification timestamp;
- implementation/build identity.

Discovery evidence should separately record:

- supported protocol revisions returned by `server/discover`;
- advertised capabilities;
- server implementation identity;
- cache/TTL metadata when present;
- whether the client actually used discovery for that run;
- the revision ultimately used for the real tool call.

## Anti-degradation contract

- Never advertise a tool before its implementation is callable.
- Never return success before the local operation succeeds.
- Never downgrade authorization to simplify MCP compatibility.
- Never replace exact tool destinations with generic shell/homepage behavior.
- Never count handshake or discovery success as end-to-end tool proof.
- Never claim `2026-07-28` compatibility merely because an SDK dependency supports it; record the actual wire behavior from the fixture.
- Never claim complete `2026-07-28` server compatibility if `server/discover` is absent.
- Never treat self-reported `serverInfo` as an authorization/security signal.
- Never remove a currently supported legacy MCP path until its retirement is explicit and replacement parity is verified.

## Troubleshooting

### Modern client cannot discover the bridge

Verify that the server actually implements `server/discover`. For `2026-07-28`, this is a server requirement. Check the discovery response's supported versions and capabilities before debugging individual tools.

### Direct tool call works but discovery is missing

Treat this as incomplete modern-server compatibility, not as a successful full migration. Direct calls are allowed for clients, but the server is still required to expose discovery.

### Legacy stdio client/server stops working after a modern upgrade

Inspect era negotiation and lifecycle separation. A dual-era stdio client should probe with discovery and fall back to the older `initialize` path when appropriate. Do not send a hybrid sequence on one connection.

### HTTP implementation still depends on `Mcp-Session-Id`

Keep that path explicitly legacy. The modern `2026-07-28` Streamable HTTP path is per request and must not pretend the old session header is part of the new protocol.

### Discovery shows the right tool but the tool does nothing

Discovery proves advertisement only. Trace the tool call through authorization, local implementation dispatch, observable side effect/result, cancellation path, and returned output before marking the capability verified.

### SDK says it supports 2026-07-28 but traffic still looks legacy

Inspect the SDK's explicit version-negotiation/serving configuration and record the actual request sequence. Current TypeScript SDK documentation explicitly warns that package upgrade alone does not switch existing code to the modern revision.

## Documentation gaps

- Canonical standalone source unresolved.
- Current implemented tool inventory unresolved.
- Current protocol revision and legacy-client matrix unresolved.
- Current authentication provider/runtime unresolved.
- No project-owned runtime fixture currently proves local PC capability execution through the bridge.

## Wiki maintenance

Update this page when the canonical bridge source is found, protocol revisions change, tool inventory changes, authorization changes, or real local tool flows are verified. Preserve compatibility/migration evidence instead of deleting the old transport story. Revalidate protocol claims against the released MCP specification and schema, not only SDK migration prose.