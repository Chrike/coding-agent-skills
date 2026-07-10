---
name: design-codebase
description: Use when the user explicitly asks about codebase design, architecture, module interfaces, seams, adapters, deep modules, domain language, architecture options, hard-to-test modules, testability through interfaces, or throwaway prototypes for design questions.
---

# Design Codebase

Use architecture language to improve leverage, locality, and testability without turning ordinary implementation into a design ceremony.

## First Decision

- If the user asks for a small bug fix or ordinary implementation, stay in the lightweight development flow.
- If the user asks where an interface or seam should live, inspect the directly affected callers, dependencies, tests, and constraints first.
- If the user asks to improve architecture, look for shallow modules and leakage across seams before proposing changes.
- If the design question needs runnable feedback, suggest a throwaway prototype; build it only when the user asks or agrees.
- If the user asks for broad planning, use the planning workflow instead of duplicating it here.

## Design Runbook

When this skill is active, drive the design pass in this order:

1. Read the directly affected callers, dependencies, tests, constraints, and any directly relevant docs before proposing structure. Stop broadening the design read once the decision can be made safely.
2. State the design goal in one sentence.
3. Name the current seam, leak, shallow module, or interface pain that is making the work harder.
4. Compare the smallest useful set of concrete placements or interface shapes when the answer is non-obvious.
5. Recommend one option and explain why it improves leverage, locality, or testability for the current goal.
6. Call out migration impact, verification approach, and what should stay out of scope.

## Vocabulary

Use these terms consistently:

- **Module**: anything with an interface and implementation.
- **Interface**: everything callers must know to use the module correctly, including invariants, ordering, errors, configuration, and performance.
- **Implementation**: what lives behind the interface.
- **Seam**: the place where behavior can vary without editing callers.
- **Adapter**: a concrete implementation that satisfies an interface at a seam.
- **Depth**: leverage at the interface; deep modules hide useful behavior behind a small surface.
- **Locality**: changes, bugs, and tests concentrate in one place.

## Design Checks

- Existing project architecture and explicit user constraints outrank the vocabulary and heuristics in this skill.
- Treat deep-module, seam, and adapter checks as lenses, not mandatory design goals.


Use these checks to support the runbook rather than replace it:

- Deletion test: if deleting the module makes complexity vanish, it was probably shallow. If complexity spreads across callers, it was earning its interface.
- Interface test surface: callers and tests should cross the same seam.
- Real seam test: one adapter is usually hypothetical indirection; two justified adapters make a seam real.
- Dependency fit: pure or local-substitutable dependencies can usually sit behind the module; remote or external dependencies may need ports/adapters.
- Scope fit: improve the architecture needed for the current goal; avoid unrelated broad refactors.

## References

- Deep module vocabulary and design checks: [deep-modules.md](references/deep-modules.md)
- Deepening shallow clusters: [deepening.md](references/deepening.md)
- Comparing alternative interfaces: [design-it-twice.md](references/design-it-twice.md)
- Domain language and ADR guidance: [domain-modeling.md](references/domain-modeling.md)
- Throwaway design feedback: [prototypes.md](references/prototypes.md)

## Exit To Implementation

- Once the design choice is settled and the user asks to implement it, exit this workflow and continue in the base implementation flow.
- Do not keep comparing architecture alternatives during implementation unless the selected design becomes concretely invalid.
- Verify the implementation against the settled interface and invariants rather than reopening the design discussion.

## Boundaries

Do not automatically create glossary files, domain-context files, ADRs, architecture reports, HTML files, prototypes, subagent workflows, or broad refactors.

Only create durable design artifacts when the user asks, or when a hard-to-reverse and surprising trade-off has been explicitly chosen and the user agrees it should be recorded.
