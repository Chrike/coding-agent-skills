# Design Questions

Use these only when the request is too vague to plan safely. Ask one question at a time and prefer assumptions when the answer will not change implementation.

## Clarify

- What outcome should be true when this is done?
- Who or what uses the changed behavior?
- Is backward compatibility required?
- Are there data migration, permissions, performance, or reliability constraints?
- Which existing pattern should this follow?

## Compare

When real alternatives exist, compare the smallest useful set of materially different approaches. Show only the criteria that distinguish them, such as:

- compatibility and migration cost
- implementation and operational complexity
- reversibility
- performance
- verification strength
- future change cost

Recommend one option in project terms. Do not invent an alternative or compatibility bridge merely to fill a fixed option count.

## Stop Conditions

Stop planning and ask before implementation when:

- Requirements conflict.
- The safest approach depends on product intent the code cannot reveal.
- The work would require destructive data changes, broad dependency changes, or system/global setup.
- The user explicitly asked for plan-only output.
