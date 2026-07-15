---
name: design-codebase
description: Use when the user asks about codebase design, architecture, module interfaces, seams, adapters, deep modules, domain language, architecture options, hard-to-test modules, testability through interfaces, or throwaway prototypes for design questions, or when an implementation depends on a non-obvious architecture, ownership, interface, or dependency-boundary decision that existing patterns cannot safely settle.
---

# Design Codebase

Use architecture language to improve leverage, locality, and testability without turning ordinary implementation into a design ceremony.

## First Decision

- If existing patterns make the next safe edit clear, keep small fixes and ordinary implementation in the lightweight flow.
- If an implementation depends on a non-obvious architecture, ownership, interface, or dependency-boundary decision that existing patterns cannot safely settle, use this workflow to resolve that decision.
- If the user asks where an interface or seam should live, inspect the directly affected callers, dependencies, tests, and constraints first.
- If the user asks to improve architecture, identify the actual design pressure before choosing lenses such as shallow modules or leakage across seams.
- If runnable feedback is the fastest way to settle a design question, read [prototypes.md](references/prototypes.md) and apply its automatic-local versus approval-required gate.
- If the user asks for broad planning, use the planning workflow instead of duplicating it here.

## Design Runbook

When this skill is active, drive the design pass in this order:

1. Read the directly affected callers, dependencies, tests, operational constraints, and relevant docs before proposing structure; stop broadening once the decision is safe.
2. State the design decision and goal, derive only decision-relevant criteria, and identify the actual design pressure without assuming a seam, adapter, or module-depth problem.
3. When the choice is non-obvious, compare the smallest useful set of materially distinct options against those criteria; recommend one option with migration impact, verification, and out-of-scope work.

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

- Existing project architecture and explicit user constraints outrank this skill's vocabulary and heuristics.
- Treat deep-module, seam, adapter, and interface-leakage checks as lenses only when caller complexity, duplicated coordination, or a real dependency boundary demonstrates the pressure.
- Do not introduce an interface or adapter merely because this skill is active.


Use these checks to support the runbook rather than replace it:

- Deletion test: if deleting the module makes complexity vanish, it was probably shallow. If complexity spreads across callers, it was earning its interface.
- Interface test surface: callers and tests should cross the same seam.
- Real seam test: introduce a seam only when demonstrated variation, ownership, testability, operational isolation, or an external dependency boundary justifies it. Adapter count alone does not determine whether a seam is real.
- Dependency fit: pure or local-substitutable dependencies can usually sit behind the module; remote or external dependencies may need ports/adapters.
- Scope fit: improve only the architecture needed for the current goal; avoid unrelated broad refactors.

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

Do not automatically create glossary files, domain-context files, ADRs, architecture reports, HTML files, subagent workflows, or broad refactors. Follow [prototypes.md](references/prototypes.md) for the only automatic-prototype exception.

Only create durable design artifacts when the user asks, or when a hard-to-reverse and surprising trade-off has been explicitly chosen and the user agrees it should be recorded.
