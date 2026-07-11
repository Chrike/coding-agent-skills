# Scout Slices

Use this after `agent-workflow` is already active and the problem is still open-ended enough that implementation would be premature.

## When to scout first

Scout before implementation only after the active domain method or controller identifies two or more orthogonal investigation questions that can progress independently without one shared write scope.

Do not activate scouts merely because the root cause is still unclear. Use `debug-systematically` to establish the diagnostic method for an unclear shared-root failure first; scout only the distinct source, subsystem, or failure-path questions it identifies.

Do not use long exploratory output alone as the reason to fan out.

## Ownership Before Launch

- Use one Explore delegation for one focused search question.
- Use multiple scouts only when their primary questions are orthogonal.
- Give each scout a distinct question, subsystem, source boundary, failure path, or architecture option.
- Do not assign the same primary files, search terms, or evidence question to multiple scouts merely to increase confidence.
- Include already-checked paths and explicitly excluded paths in each brief.
- The controller must not search a scout's assigned scope while that scout is active.
- If overlap becomes apparent after launch, narrow or stop one scout instead of allowing both to finish the same investigation.

## How to split scout work

Split scouts by orthogonal lenses such as:

- failure path
- architecture option
- source type
- subsystem boundary

## Scout output contract

Require scouts to return:

- ranked sources or evidence paths
- concise conclusions
- source-backed facts
- working assumptions
- stale or version-sensitive material
- unresolved questions
- recommended next probes

## Controller rules

- dedupe overlapping findings before escalating into implementation work
- keep scout output to evidence, unresolved questions, and recommended next probes
- scouts do not write the final conclusion for the controller
- stop after two consecutive dry rounds with no materially new evidence
