# Scout Slices

Use this after `agent-workflow` is already active and the problem is still open-ended enough that implementation would be premature.

## When to scout first

Scout before implementation when:

- the likely root cause is still unclear
- you need multiple orthogonal explanations before choosing a direction
- a direct implementation attempt would pollute the main conversation with too much exploratory output

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
- stop after consecutive dry rounds when new scouts are no longer producing materially new evidence
