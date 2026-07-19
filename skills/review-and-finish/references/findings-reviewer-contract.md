# Findings-Only Reviewer Contract

Use `fresh-findings-reviewer` only for a bounded independent review pass when a fresh context materially reduces a concrete blind-spot risk.

## Input

Provide:

- the review scope and changed artifact;
- the acceptance or compatibility context;
- the exact paths the reviewer may inspect;
- any relevant current version or diff boundary;
- the expected structured result.

## Output

Return an object with:

```json
{
  "findings": [
    {
      "severity": "critical|high|medium|low",
      "summary": "...",
      "path": "repository-relative/path",
      "location": "symbol: Name|section: Name|lines:N-M",
      "failureScenario": "...",
      "evidence": "..."
    }
  ],
  "blocker": ""
}
```

Use an empty `findings` array when no grounded issue remains. Use `blocker` when the scope or evidence is insufficient to perform the bounded pass. The reviewer must not repair, edit, run commands, create artifacts, decide completion, or perform branch actions.

## Ownership

`review-and-finish` owns caller selection, feedback triage, repair decisions, completion/readiness judgment, and the separation from `finish-branch`. If the saved Agent cannot be selected, perform the same bounded check inline rather than treating selector availability as a security boundary.
