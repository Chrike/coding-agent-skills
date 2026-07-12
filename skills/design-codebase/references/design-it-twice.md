# Design It Twice

Use this when the first interface idea feels plausible but the trade-off is important enough to compare alternatives.

## Lightweight Version

Produce only the materially distinct options needed to expose the real trade-off. Do not target a fixed option count. Use only lenses that create real alternatives for the current decision, such as:

- **Minimal caller surface**: hide behavior behind the smallest useful interface.
- **Known variation**: support demonstrated variation without exposing internals.
- **Common-path optimization**: optimize the frequent caller while isolating rare cases.
- **Migration safety**, **operational simplicity**, **performance**, or **future change cost**.

For each option, show only the decision-relevant details:

- Caller/interface shape and seam impact when those are part of the decision.
- Dependency strategy or adapters when a real dependency boundary exists.
- Operational, performance, migration, ownership, reversibility, locality, testability, or other derived trade-offs that distinguish the options.

Finish with a recommendation. Be opinionated; do not leave the user with an unranked menu.

## Full Version

If the user explicitly asks for independent exploration or a larger architecture comparison, use separate agents or sessions only when available and worthwhile. Give each pass a different design constraint, then compare results against the decision-derived criteria; use depth, locality, or seam only when they apply.

Do not spawn agents, create branches, or write durable reports by default.
