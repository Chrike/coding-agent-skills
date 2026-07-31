# Capability Contracts

Every delegated task must have a narrow objective, explicit boundaries, a fixed return contract, and a stop condition. Delegation depth is one; leaf agents must not delegate further. The contracts in this file are the canonical contracts for the current project plugin.

`SubagentStop` checks the minimum headings below. Optional sections are useful only when they contain material evidence; do not emit empty placeholders.

## Context scout

Use for one open-ended or unfamiliar task where missing domain context may materially improve a named decision. Before
searching, the scout states the decision and the missing signal. A plausible material gap is enough to begin bounded
discovery; the scout does not need to prove in advance that search will improve the final result. A discovery response
must include:

```markdown
## Capability decision
- the decision, missing signal, and why bounded discovery is the best next action

## Context gaps
- material detail the request leaves implicit and why it matters

## Decision brief
- actionable domain, relationship, medium, composition, and failure-mode details

## Evidence
- source or repository location and what it supports

## Plan implications
- concrete changes the active controller should make before generation or implementation
```

When no plausible bounded source can supply useful task context, the scout returns only:

```markdown
## Capability decision
- direct route and why no bounded source can supply useful task context

## Skip reason
- the fixed constraint, sufficient local evidence, unavailable signal, or intrinsic capability limit
```

The scout may add `## Search path`, `## Noise excluded`, and `## Uncertainty`. It uses at most 3-5 focused direct, component,
and adjacent searches, does not copy an existing artifact, and does not choose or implement the final result. Verification
and evaluation are separate optional routes, not prerequisites for this contract. For an incomplete brief, return the
blocked-brief form below.

## Evidence researcher

Use for one bounded repository question or explicitly authorized current official or primary-source question. The complete response must include:

```markdown
## Findings
- concise finding

## Evidence
- source or project location, what it supports, and relevant version or date
```

The agent may add `## Applicability`, `## Limitations`, `## Uncertainty`, and `## Recommended action` when materially relevant. For an incomplete brief, return only:

```markdown
## Blocked brief
- missing item

## Required next input
- smallest input needed to proceed
```

The agent distinguishes facts, inferences, absence claims, and unresolved uncertainty; it does not modify files, broaden scope, or delegate.

## Independent brancher

Use for one materially different design, plan, optimization, or implementation approach. The complete response must include:

```markdown
## Approach
- concise name and thesis

## Assumptions
- assumptions required

## Plan
1. concrete step

## Strengths
- material advantage

## Failure conditions
- when this approach is wrong or inferior

## Validation
- checks that would confirm or reject it
```

The agent may add `## Evidence basis` when repository facts materially affected the approach. For an incomplete brief, return the blocked-brief form above. The controller owns comparison, selection, implementation, and integration; the brancher does not choose the final answer or create cosmetic variants.

## Execution verifier

Use for one claim that can be checked against an identified repository state, artifact, or environment. The complete response must include:

```markdown
## Verification target
- exact claim, cwd, worktree or checkout, revision or unversioned state, and artifact or environment identity

## Checks executed
- exact command, action, or observation; use None with a reason when no check ran

## Evidence result
- supports-claim, mismatch, no-issue-found, blocked, failed, stale, or unverified; include the relevant evidence
```

The agent may add `## Reproduction details` and `## Unverified areas`. It does not modify source files, repair defects, assign severity, recommend a fix, make a completion verdict, or delegate. A command that starts and errors is `failed`; a check blocked before starting is `blocked`; lack of reliable evidence is `unverified`.

## Skeptical evaluator

Use for supplied candidate artifacts or results when deterministic checks do not settle a material quality dimension. The complete response must include:

```markdown
## Hard-constraint verdict
- pass, fail, or unverified for each supplied hard constraint

## Comparative judgment
- candidate ordering or single-result quality judgment

## Decisive evidence
- checks, project facts, or sources supporting the judgment
```

The agent may add `## High-impact defects`, `## Regression risks`, and `## Recommendation`. For an incomplete brief, return the blocked-brief form above. The evaluator does not rewrite artifacts, create candidates, authorize side effects, or issue an overall ready/done verdict.

## Ownership and integration

The active controller and domain Skill own implementation, repair count, acceptance, and final integration. Harness workers return bounded evidence, candidates, verification, or evaluation. Preserve the strongest verified result seen so far and report unresolved uncertainty instead of hiding it.
