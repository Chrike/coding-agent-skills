# Prototypes

Build a prototype only when a design question needs runnable feedback. Prototype code is temporary and exists to answer one question.

## Logic Prototype

Use for business logic, state transitions, or data shape.

- State the question at the top of the prototype.
- Use the project's existing language and task runner.
- Keep state in memory unless persistence is the question.
- Keep the core experiment easy to inspect; introduce a reusable interface only when reuse or interface shape is the question being tested. Keep terminal/browser shell throwaway.
- Surface the full relevant state after each action.
- Provide one project-local command to run it.

## UI Prototype

Use when the question is visual structure or interaction shape.

- Prefer variants inside an existing page or route.
- Use `?variant=` or the project's equivalent to switch options.
- Create the smallest number of variants needed to answer the design question. Use multiple variants only when they represent materially different unresolved directions.
- Keep real data fetching when useful, but avoid real mutations.
- Remove losing variants and any switcher when a direction is chosen.

## Cleanup

When the question is answered, either delete the prototype or fold the validated decision into real code. Capture only the answer and why it mattered.

Do not add tests, production polish, broad abstractions, new runtimes, or persistent infrastructure to a prototype unless that is the specific question being tested.
