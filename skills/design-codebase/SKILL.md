---
name: design-codebase
description: Use when the user asks about codebase design, architecture, module interfaces, seams, adapters, deep modules, domain language, architecture options, hard-to-test modules, testability through interfaces, or throwaway prototypes for design questions, or when an implementation depends on a non-obvious architecture, ownership, interface, or dependency-boundary decision that existing patterns cannot safely settle.
---

# Design Codebase

Use architecture language to improve leverage, locality, and testability without turning ordinary implementation into a design ceremony.

## First Decision

- If the user asks for a small bug fix or ordinary implementation and existing patterns make the next safe edit clear, stay in the lightweight development flow.
- If an implementation depends on a non-obvious architecture, ownership, interface, or dependency-boundary decision that existing patterns cannot safely settle, use this workflow to resolve that decision.
- If the user asks where an interface or seam should live, inspect the directly affected callers, dependencies, tests, and constraints first.
- If the user asks to improve architecture, identify the actual design pressure before choosing lenses such as shallow modules or leakage across seams.
- If the design question needs runnable feedback, suggest a throwaway prototype; build it only when the user asks or agrees.
- If the user asks for broad planning, use the planning workflow instead of duplicating it here.

## Design Runbook

When this skill is active, drive the design pass in this order:

1. Read the directly affected callers, dependencies, tests, operational constraints, and any directly relevant docs before proposing structure. Stop broadening the design read once the decision can be made safely.
2. State the exact design decision and goal in one sentence.
3. Derive only the criteria that matter for this decision, such as compatibility, locality, operational simplicity, performance, ownership, failure isolation, testability, migration cost, and reversibility.
4. Identify the current design pressure without assuming it is a seam, adapter, or module-depth problem.
5. Compare the smallest useful set of materially distinct options against the derived criteria when the answer is non-obvious.
6. Recommend one option that best fits the current project and change pressure, then call out migration impact, verification approach, and what should stay out of scope.

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
- Treat deep-module, seam, adapter, and interface-leakage checks as lenses only when caller complexity, duplicated coordination, or a real dependency boundary demonstrates that pressure.
- Do not introduce an interface or adapter merely because this skill is active.


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

- When a request includes implementation, treat design as a transient internal phase: once the design choice is settled, exit to implementation automatically unless user-only input, an irreversible trade-off, or a scope change remains.
- When the user asks only to design, do not implement until they ask.
- Do not keep comparing architecture alternatives during implementation unless the selected design becomes concretely invalid.
- Verify the implementation against the settled interface and invariants rather than reopening the design discussion.

## Boundaries

Do not automatically create glossary files, domain-context files, ADRs, architecture reports, HTML files, prototypes, subagent workflows, or broad refactors.

Only create durable design artifacts when the user asks, or when a hard-to-reverse and surprising trade-off has been explicitly chosen and the user agrees it should be recorded.
