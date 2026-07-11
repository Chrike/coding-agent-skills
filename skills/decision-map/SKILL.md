---
name: decision-map
description: Use when the user clearly asks for a multi-session decision map, tracked decision frontier, or durable map of unresolved long-running direction. Keep ordinary planning and one-session design comparison in lighter flows.
---

# Decision Map

Turn long-running uncertainty into a compact frontier map when the user clearly asks for a decision map, tracked frontier, or durable multi-session direction artifact. Requests like “make a decision map for this,” “track the open frontier,” or “set up a multi-session decision map” count.

## First Decision

- Do not use this for ordinary implementation plans, small refactors, or one-session approach comparison.
- Use this only when the user clearly wants a durable multi-session decision workflow, decision map, or resume-by-ticket artifact.
- If the path is already clear after discussion, skip the decision map and use `plan-work` or direct implementation instead.
- Keep the map compact because the whole artifact may need to be reread in later sessions.
- Update a user-named or repository-standard map when one exists. If no authoritative path exists, propose the map and suggested path in chat before creating a durable file. Do not invent a new decision directory or duplicate map without explicit agreement; ask which map is authoritative when multiple plausible maps exist.

## What The Map Tracks

Each map should capture:

1. The current decision frontier.
2. Open tickets that must be resolved before downstream choices become clear.
3. Dependencies between tickets.
4. A short answer or outcome for each resolved ticket.
5. Links to supporting artifacts instead of copying large notes into the map.

Use small, numbered tickets. Size each ticket as one coherent decision question with a clear evidence and output contract. Do not size tickets according to a fixed model, context window, or session capacity.

## Ticket Types

| Type | Use It For | Output |
| --- | --- | --- |
| Research | reading docs, APIs, or external or local references to answer an open question | short linked note or summary |
| Prototype | testing a design or behavior hypothesis in code | throwaway prototype artifact and short conclusion |
| Discuss | resolving uncertainty through focused analysis with the user | concise decision note in the map |

Prefer research, code inspection, or existing evidence when they can resolve the uncertainty. Propose a reversible prototype when it would discriminate between options, and build it only when the user asks or agrees. Use `Discuss` when the remaining choice depends on product intent, value judgment, taste, policy, or other user-only information.

## Workflow

1. Restate the loose idea or decision space in one sentence.
2. Identify the true open questions, not implementation tasks.
3. Resolve trivial decisions inline instead of turning everything into tickets.
4. Create only the frontier tickets needed to move the decision forward.
5. Record blockers or dependencies between tickets.
6. If the user asks to progress or resolve the frontier, continue through newly unblocked tickets until the frontier is resolved, a user-only decision is reached, or a real blocker appears. Otherwise stop after creating or updating the map.

When resuming:

1. Read the whole map first.
2. Resolve the named ticket or the current frontier item.
3. Record the answer compactly.
4. Add, update, or delete downstream tickets if the frontier changed.
5. If the user asked to progress or resolve the frontier, continue through newly unblocked tickets until the frontier is resolved, a user-only decision is reached, or a real blocker appears. Otherwise stop after the ticket update.

## Boundaries

Do not turn implementation tasks, issue breakdowns, or ordinary design questions into a decision map just because work spans multiple files or feels somewhat ambiguous.

Do not automatically create PRDs, issue tracker items, ADRs, subagents, or broad prototype trees from this skill.

Do not duplicate large research notes in the map. Link to supporting files instead.

Use:

- `plan-work` for ordinary implementation planning
- `design-codebase` for architecture and seam decisions that fit in a normal design discussion
- `issue-workflow` for PRDs, issue breakdown, or tracker-ready work items
- `memory-handoff` when the user wants compression-safe handoff state rather than a decision frontier
