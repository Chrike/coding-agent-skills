# Evidence Loop Principles

Read this reference when a task needs bounded candidate-evidence collection followed by fresh-context verification. `agent-workflow` remains the owner of decomposition, worker contracts, and integration; this reference supplies only reusable evidence-loop principles.

- Treat candidate evidence as provisional. Keep its path, version, location, scope, polarity, and producer provenance attached.
- Let a separate fresh-context verifier produce verified evidence by checking the supplied candidate set; the verifier verifies and does not become a second investigator.
- Carry forward only the minimal material carry-forward state needed for the next decision: the active hypothesis, accepted evidence, failed or ruled-out paths, unresolved contradictions, completed scopes, and supported criteria.
- Keep contradictions visible until a later result explicitly resolves them. Do not silently overwrite conflicting evidence.
- Bound rounds, investigators, verifiers, and no-progress retries with an explicit bounded stop condition. Stop when the evidence contract is satisfied or the bounded budget is exhausted.
- Keep leaf workers within their assigned scope. Shared, out-of-scope, or delegation-worthy questions return to the controller instead of creating sibling orchestration.
- A completion claim requires direct evidence for every acceptance criterion and must preserve evidence gaps as blockers rather than infer support.
