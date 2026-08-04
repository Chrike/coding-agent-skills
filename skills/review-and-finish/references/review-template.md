# Review Template

Use when the user asks for a code review, PR review, branch review, or review since a ref.

## Process

1. Confirm the scope selected by `SKILL.md`. Review only that scope and directly affected contracts. Do not silently expand to unrelated files or repository-wide debt.
2. Read the relevant code and requirements if available.
3. Prioritize bugs, regressions, missing requirements, data loss, security, and test gaps.
4. Determine whether each finding was introduced or exposed by the reviewed change. Report unrelated pre-existing debt separately.
5. Group findings that share one root cause instead of reporting the same issue at every affected call site.
6. Avoid style nits unless they affect correctness, maintainability, or documented standards.

## Optional Review Lenses

Use these lenses only when they clarify the reviewed change; they do not create a mandatory gate or a second review owner.

### Context And Tests First

- State the intended behavior and relevant requirements before judging the implementation.
- Read relevant tests before the implementation when they exist; use them as evidence of intended behavior and regression coverage.
- Treat missing tests as a finding only when the acceptance context or risk requires that evidence. Do not require tests for every change by default.

### Structural Remedy

When a finding is structural, propose the narrowest concrete remedy instead of only naming complexity. Depending on the evidence, consider replacing repeated conditionals with an explicit model or dispatcher, separating orchestration from domain logic, moving feature logic to its owning layer, reusing a canonical helper, making a type boundary explicit, or deleting a pass-through wrapper.

These are review recommendations, not automatic refactoring instructions. Do not edit code, delete dead code, run branch actions, or broaden the review scope merely because a remedy is suggested.

## Output

Lead with findings:

```md
Findings
- [Severity] File:line - Issue. Why it matters. Suggested fix.

Open Questions
- ...

Summary
- ...
```

Severity guidance:

| Severity | Use For |
| --- | --- |
| Critical | Credible paths to severe data loss, authentication or authorization bypass, serious security compromise, irreversible destructive behavior, or widespread service failure. |
| Important | User-visible incorrect behavior, missing requirements, likely regressions, unsafe error handling, or serious test gaps. |
| Minor | Maintainability problems, confusing code, or low-risk edge cases. |

Assign severity from reachable impact and likelihood, not from category labels alone.

If no issues are found, say that clearly and mention only concrete remaining verification gaps against the stated acceptance context, if any.
