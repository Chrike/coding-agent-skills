---
name: decision-map
description: Use when the user clearly asks for a multi-session decision map, tracked decision frontier, or durable map of unresolved long-running direction. Keep ordinary planning and one-session design comparison in lighter flows.
---

# Decision Map

Turn long-running uncertainty into a compact frontier map when the user clearly asks for a decision map, tracked frontier, or durable multi-session direction artifact. Requests like “make a decision map for this,” “track the open frontier,” or “set up a multi-session decision map” count.

## First Decision

- Use this only for an unresolved, durable multi-session decision frontier; ordinary planning, design, and implementation stay with their owning workflows.
- Keep the map compact because the whole artifact may need to be reread in later sessions.
- Treat a user-named or repository-standard map as authoritative. If no authoritative path exists or multiple plausible maps exist, ask which map is authoritative and get agreement on the path before creating durable state; do not invent a decision directory or duplicate a map.

## What The Map Tracks

Each map should capture:

1. The current decision frontier.
2. Open tickets for unresolved decision questions or options, not implementation tasks.
3. Dependencies and blockers between tickets.
4. A concise answer or outcome for each resolved ticket.
5. Links to supporting artifacts instead of copied research notes.

Use small, numbered tickets. Size each ticket as one coherent decision question or option comparison with a clear evidence and output contract.

## Ticket Types

| Type | Use It For | Output |
| --- | --- | --- |
| Research | reading docs, APIs, or external or local references to answer an open question | short linked note or summary |
| Prototype | testing a design or behavior hypothesis in code | throwaway prototype artifact and short conclusion |
| Discuss | resolving uncertainty through focused analysis with the user | concise decision note in the map |

Use existing evidence when it resolves the question. A `Prototype` must be reversible and requires the user to ask or agree before it is built. The automatic local-prototype exception in `design-codebase` does not apply to a decision-map prototype ticket because this workflow updates a durable multi-session frontier. Use `Discuss` when the remaining choice depends on product intent, value judgment, taste, policy, or other user-only information.

## Frontier Loop

1. On resume, read the whole authoritative map first; otherwise establish the current frontier and its open questions or options.
2. Keep open questions and options separate from implementation tasks; create only the necessary small numbered tickets and record dependencies or blockers.
3. Resolve the named ticket or current frontier item; record the answer or outcome compactly with supporting links, and add, update, or delete downstream tickets when the frontier changes.
4. If the user asks to progress or resolve the frontier, continue through newly unblocked tickets until the frontier is resolved, a user-only decision is reached, or a real blocker appears. Otherwise stop after the map or ticket update.

## Boundaries

Do not use this for ordinary tasks or one-session planning, design, or implementation, and do not turn it into PRDs/issues, architecture or ADR artifacts, handoff/checkpoint state, or subagent workflows. Use `plan-work`, `design-codebase`, `issue-workflow`, or `memory-handoff` for those scopes. Keep supporting research linked rather than copied, and do not create duplicate maps or research content.
