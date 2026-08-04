# API and Interface Contracts

Use this reference when `design-codebase` is active and a decision depends on a consumer-visible API, service boundary, module interface, or component contract.

## Contract lens

1. Identify the real consumers and the boundary they cross. Include only behavior that a caller can observe and that matters to the current decision.
2. Describe the caller inputs, returned outputs, server-generated values, error modes, ordering or idempotency rules, and any performance or compatibility constraint that is actually load-bearing.
3. Separate the input model from the output model when the system adds identity, timestamps, defaults, or other server-owned data.
4. Put parsing and validation at untrusted boundaries: user input, configuration, and third-party responses. Do not duplicate checks between internal functions that already share a verified contract, and do not skip real authorization or persistence invariants.
5. Prefer an additive, compatible extension when it satisfies the goal. If a breaking change is necessary, record the affected consumers and the migration conditions instead of executing the migration in this design pass.

## Project fit

- Follow the project's existing protocol, naming, error, serialization, and versioning conventions. This reference does not require REST, GraphQL, TypeScript, a particular status-code table, an error envelope, pagination shape, or identifier representation.
- Add an interface, adapter, or seam only when demonstrated variation, an external boundary, ownership, testability, or operational isolation justifies it. Do not create one for a single speculative implementation.
- Keep the contract smaller than the implementation. Hide coordination, retries, translation, and other policy that callers should not need to know.
- Treat undocumented observable behavior as a compatibility consideration, not as a reason to freeze every implementation detail.

## Handoffs and verification

- `design-codebase` decides the boundary and contract. `test-strategy` chooses the narrowest behavioral seam, fixture, mock, timing, or acceptance proof for the remaining test question.
- Verify through the public endpoint, service boundary, or domain interface when that is the behavior consumers rely on. Avoid tests that assert private methods or incidental collaborator call order unless the order is part of the contract.
- If compatibility, consumer rollout, sequencing, or scope remains unresolved after the boundary is chosen, hand that decision to `plan-work`.
- Do not run commands, create migrations, update consumers, publish versions, or change remote state merely because the contract has been designed.

## Keep out

This reference does not authorize API implementation, consumer notification, adapter rollout, data backfill, deprecation, deployment, rollback, commit, or pull-request actions. Resolve those through their owning workflow and explicit action authorization.
