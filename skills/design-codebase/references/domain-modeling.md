# Domain Modeling

Use this when architecture depends on precise domain language, or when the user explicitly asks to name concepts, define a glossary, or record an architectural decision.

## Language

- Prefer the project's existing domain terms when present.
- If a term is overloaded, ask which concept it names.
- If code and conversation disagree, surface the contradiction.
- Define domain terms by what they are, not by implementation details.

## Glossary Artifacts

Do not create or update glossary or domain-context artifacts during ordinary design work.

If the user asks to maintain a glossary, or a term is explicitly resolved and worth recording, use a compact glossary style:

```md
# <Context Name>

## Language

**Order**:
One or two sentences defining the concept.
_Avoid_: Purchase, transaction
```

Only include project-specific domain concepts, not general programming terms.

## ADRs

Offer an ADR only when all are true:

- The decision is hard to reverse.
- A future reader would find it surprising without context.
- Real alternatives were considered.

Keep ADRs short: title plus 1-3 sentences is often enough. Do not create ADRs without user agreement.

Before writing one, inspect the repository for an established ADR convention: location, extension, numbering or naming, headings, status vocabulary, and any tooling or configuration. Continue that convention rather than introducing a second scheme. If conventions conflict, surface the conflict. If none exists, propose the intended location and format in chat and wait for agreement; do not assume `docs/decisions/` or create a path merely because an ADR is useful.

Use a small decision record with context, decision, alternatives, and consequences when those details change future choices. Keep historical records: when a decision changes, write a successor that links to and supersedes the prior record instead of deleting or rewriting its rationale. `Proposed`, `Accepted`, `Superseded`, and `Deprecated` are examples, not a universal status vocabulary; match the repository's established terms.

## Verification / Exit

Before writing an ADR, verify:

- The decision is hard to reverse, would surprise a future reader without context, and has real alternatives.
- The repository's ADR location, format, naming, headings, status vocabulary, and tooling were inspected; conflicting conventions are surfaced.
- The user agreed to create the durable record.
- The record captures the context, decision, relevant alternatives, consequences, and a successor link when it replaces an earlier decision.

If any applicable check or user agreement is missing, exit without writing the ADR. Keep prior records unchanged and use a linked successor for a changed decision.
