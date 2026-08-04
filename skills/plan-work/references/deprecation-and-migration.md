# Deprecation And Migration

Read this reference only when the plan explicitly retires, replaces, migrates, or compatibility-transitions an API, system, feature, dependency, consumer, or data shape. It adds planning questions; it does not authorize notification, traffic changes, backfills, destructive schema work, deletion, deployment, or branch actions.

## Deprecation Decision

Record the smallest decision packet:

- **Scope and value:** what is being retired, what unique value it still provides, and why maintenance or risk now justifies change.
- **Consumers:** known direct and indirect consumers, owner or contact coverage, environments, versions, and any consumer that cannot be inventoried yet.
- **Replacement:** the replacement and the critical behaviors it covers, or an explicit no-replacement decision with its owner and risk acceptance.
- **Migration cost:** the work, compatibility window, notification or contract window, support needs, and residual exceptions for each consumer class.
- **Removal criteria:** the evidence that all active consumers have migrated, remaining usage is below an agreed boundary, exceptions have owners and expiry, and the old implementation can be removed safely.

Product or service owners decide whether deprecation is advisory or compulsory, the deadline, and accepted residual risk. A plan records that decision; it does not make it on their behalf.

## Consumer-First Slices

For each consumer group, keep the sequence observable and independently verifiable:

1. identify touchpoints and current usage;
2. define the compatibility contract, notification window, owner, and exception path;
3. build or validate the replacement against critical behavior;
4. migrate one consumer group or version at a time;
5. verify behavior, data semantics, and error handling;
6. recheck remaining usage before removing the old path.

Do not claim zero consumers from a static search alone. Usage, telemetry, deployment, and contact evidence may be unavailable; mark that gap `UNVERIFIED` and route runtime evidence to its applicable owner.

## Compatibility And Schema Transitions

Use an adapter, parallel path, feature flag, or other compatibility mechanism only when the project facts support it. For a data or schema transition where old and new code must coexist, consider an additive expand → compatible backfill or dual-write → read switch → late contract sequence. This is a conditional heuristic, not a universal rule: data ownership, consistency, downtime, rollback semantics, and the actual migration tool determine the safe shape.

- Keep destructive drops, renames, and removal after the evidence that no supported path still needs the old shape.
- State the rollback or forward-repair semantics for each step; a generic “run down” command is not proof of safe data reversal.
- Backfills, dual-writes, traffic changes, flag changes, and destructive cleanup are separate implementation or operational actions with their own authorization and verification.

## Handoffs

- Architecture, ownership, adapter, or interface decision → `design-codebase`.
- Compatibility test, fixture, regression seam, or data assertion → `test-strategy`.
- Unknown migration failure or unexplained regression → `debug-systematically`.
- Completed migration readiness → `review-and-finish`.
- Repository CI definition → `ci-cd-and-automation`.
- Commit, push, merge, deletion, or other Git action → `finish-branch`.
- Deployment, notification, traffic, backfill, flag, or publication → the explicitly named owner or host method; do not infer one.
