# Fresh Findings Review Workflow Contract

These checks maintain the explicit, read-only `fresh-findings-review` Workflow. They are not routing instructions.

## Input and output

- accepts a non-empty `task`, optional `context`, and optional repository-relative `targetPaths` array;
- returns `reviewed` with a findings array and empty blocker, or `blocked` with a concrete blocker;
- each finding has severity, summary, repository-relative path, exact symbol/section/line location, failure scenario, and supporting evidence;
- validates target paths and returned finding locations before returning findings, including positive and non-reversed line ranges.

## Ownership and safety

- selects `fresh-findings-reviewer` when the host supports the saved Agent selector;
- falls back only on the exact selector-resolution error; worker, schema, permission, and tool failures are not retried as inline work;
- the reviewer is read-only and findings-only; it does not repair, decide completion, publish, commit, push, or perform branch actions;
- `review-and-finish` owns caller selection, findings triage, repair, completion/readiness judgment, and `finish-branch` separation;
- the Workflow does not create durable state, nested controllers, or concurrent writes.

## Required regressions

- a valid bounded README review returns an empty findings list when no grounded issue exists;
- an invalid or out-of-bound target boundary blocks without findings;
- a selector-resolution error reaches the built-in read-only `Explore` fallback, while other worker errors propagate;
- a worker, permission, schema, or tool error that merely embeds the selector-not-found text does not trigger fallback;
- the fallback uses built-in `Explore`, which exposes read/search tools only and does not expose Write, Edit, or Agent;
- a finding with `lines:0` or a reversed range such as `lines:20-10` blocks without findings;
