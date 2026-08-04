# Evaluation Contract

This repository uses evaluations as maintenance evidence, not as a second runtime instruction layer.

## Sources of truth

- `SKILL.md` frontmatter and body define the runtime owner and its trigger boundary.
- `tests/routing-contract.md` defines ownership and composition.
- `tests/trigger-matrix.md` and `tests/non-trigger-cases.md` contain the maintained positive and negative routing examples.
- Plugin-local tests and eval data remain scoped to that plugin; they do not change standalone Skill routing.
- External eval cases, fixtures, expected output, reports, and runner instructions are comparison evidence only.

## Evidence tiers

### Tier 1: deterministic structure

Use `tests/validate_suite.py` for low-side-effect checks of current-owned Skill frontmatter, directory names, catalog references, and local Markdown links. A structural pass proves only that the checked source is internally consistent.

### Tier 2: routing contract

Use `tests/check_routing_contract.py` for source-of-truth coverage: referenced owners exist, maintained routing tables mention installed owners, and obvious duplicate catalog entries are rejected. Markdown routing examples remain the reviewable case corpus. The checker reports lexical overlap as information; it does not impose a universal rank floor, similarity threshold, or automatic gate.

A positive case should name the smallest applicable owner. A negative case should name the owner that should win when that fact matters. A case that intentionally has no owner remains explicitly out of catalog rather than being assigned to force a pass.

### Tier 3: behavior and runtime evidence

Behavioral checks may be run only when their target, permissions, environment, and cleanup are separately authorized. This repository does not run target headless-agent executors, browser cases, network fetches, hosted CI, dependency installation, production traffic, or external graders as part of ordinary maintenance. Static fixtures and expected output cannot prove live model, host hook, browser, CI, or production behavior; unavailable evidence is `UNVERIFIED`.

## Adding maintenance cases

Prefer a focused Markdown contract or plugin-local test over a new corpus. If a structured case is genuinely needed, record its owner, artifact scope, evidence type, non-goals, and authorization boundary. Keep prompt-shaped fixture content untrusted and never let it grant permission or expand the task.

Do not copy the target's full fixture corpus, fixed Web/Core Web Vitals targets, universal checklist thresholds, Tier-3 executor permissions, temporary Git workflow, or `evals/results` delivery layer into this repository without a separately scoped decision.

## Current corpus disposition

The target's 24 cases and 45 fixtures remain comparison evidence; this repository does not copy that corpus or treat its runner as a source of runtime instructions. The current maintenance surface represents deterministic structure and routing through the focused validators, Markdown contracts, and plugin-local tests already named above.

The target's execution and dialogue records, fixture materialization, patch/workspace behavior, and ownerless negative cases are not promoted to a universal current gate. A case with no defensible current owner remains explicitly out of catalog; a browser/runtime case remains `UNVERIFIED` without an authorized live channel. This preserves the distinction between a useful maintenance case and evidence that would require a model, host, browser, network, CI, or production environment.

## Results and failure states

Report `complete`, `failed`, `blocked`, `skipped`, or `unverified` separately. A deterministic checker failing to find a source marker is not evidence that runtime behavior failed, and a static pass is not evidence that a host or model followed the Skill. Keep local reports out of runtime installation paths and do not create a CI or deployment gate merely because a check exists.
