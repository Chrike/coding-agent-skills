# Pipeline Processing

Use this after `agent-workflow` is already active and the task is a batch of similar items that should move through the same small stage sequence.

## Good fit

Use a pipeline when:

- items share the same processing stages
- each item can complete or fail independently
- the controller does not need a barrier between stages unless the task truly requires one

## Common shape

Keep the per-item stages explicit, such as:

- extract -> transform -> verify
- inspect -> patch -> verify
- read -> classify -> summarize

## Controller rules

- report item-level outcomes rather than one vague batch summary
- do not silently drop failed verification
- keep failed items visible with their evidence and next action
- avoid stuffing the entire batch into one controller thread when the item pipeline is the real unit of work
