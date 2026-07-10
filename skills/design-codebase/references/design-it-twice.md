# Design It Twice

Use this when the first interface idea feels plausible but the trade-off is important enough to compare alternatives.

## Lightweight Version

Produce the smallest useful set of genuinely different interface options:

1. **Minimal interface**: smallest caller surface, maximum hidden behavior.
2. **Flexible interface**: supports known variation without exposing internals.
3. **Common-path interface**: optimizes the most frequent caller and pushes rare cases behind options or adapters.

For each option, show:

- Interface shape and caller example.
- What implementation details move behind the seam.
- Dependency strategy and adapters, if any.
- Trade-offs in depth, locality, migration cost, and testability.

Finish with a recommendation. Be opinionated; do not leave the user with an unranked menu.

## Full Version

If the user explicitly asks for independent exploration or a larger architecture comparison, use separate agents or sessions only when available and worthwhile. Give each pass a different design constraint, then compare results using the same depth/locality/seam criteria.

Do not spawn agents, create branches, or write durable reports by default.
