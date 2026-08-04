# Vertical Slices

Use vertical slices when a feature, refactor, or PRD is too large to implement safely in one pass.

## Slice Rules

- Each slice delivers a narrow but complete path through the needed layers.
- A finished slice is demoable, testable, or otherwise verifiable on its own.
- Prefer user-visible or behavior-visible outcomes over layer-only tasks.
- Put enabling refactors first only when they make the feature easier or safer.
- Keep dependencies explicit; avoid slices that can only be understood after every other slice is done.

## Good Slice Shape

```markdown
1. Add the minimal data path for <one behavior>
   - Touches: schema/model/API/UI as needed
   - Proves: user can complete the narrow path
   - Verification: focused test, request, or UI flow
   - Blocked by: none

2. Add <next behavior or variant>
   - Builds on: slice 1
   - Proves:
   - Verification:
```

## Choose The Next Slice

- Use contract-first slicing when independently developed consumers need a shared interface; settle the observable contract before splitting implementation work across sides of the boundary.
- Use risk-first slicing when one uncertainty could invalidate the rest of the approach; prove that uncertainty with the smallest safe slice before building on it.
- Before expanding a slice, check its stated acceptance result and the evidence that supports it. A passing check does not by itself prove unrelated acceptance criteria.
- Keep increments narrow and easy to revert by avoiding unrelated cleanup or speculative abstractions. Branch actions remain separately authorized.

## Avoid

- "Build backend", then "build frontend", then "write tests" as separate horizontal slices.
- Large infrastructure work before any behavior is proven.
- Tracker-specific issue publishing unless the user asks for issue workflow.
- Splitting so finely that no slice can be reviewed or verified alone.
