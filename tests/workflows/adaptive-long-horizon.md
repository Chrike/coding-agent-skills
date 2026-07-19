# Adaptive Workflow Contracts

These checks maintain adaptive Workflow state and gate ownership. They are not routing rules.

## `adaptive-long-horizon`

- accepts a structured task, acceptance criteria, target paths, optional method capsule, declared evidenceVersion, and bounded limits;
- owns round, agent budget, question IDs, candidate evidence, active hypothesis, completed scopes, failed or ruled-out paths, contradictions, and supported criteria;
- selects the read-only investigator and completion verifier roles when the host supports the saved Agent selector, with built-in read-only `Explore` fallback when selector resolution is unavailable;
- treats selector-resolution fallback separately from worker execution, schema, permission, or tool failures;
- keeps candidate evidence provisional until the fresh verifier returns verified evidence;
- blocks unknown paths, changed references, unsupported polarity, missing criteria, unresolved contradictions, malformed evidence, invalid line ranges, mismatched evidenceVersion, and verifier mismatch/blocker results;
- stops after bounded rounds/agents or repeated inspectable no-progress;
- does not write files, run commands, create durable state, commit, push, publish, or create nested controllers; saved-selector failure uses read-only `Explore` rather than a generic worker.

## Verification boundary

The Workflow owns dynamic schemas, validators, and the final completion gate. Agent files own only stable role identity and tool/side-effect boundaries. A selector is not a security boundary, and a saved Agent does not replace Workflow validation.

## Adaptive-specific cases

- A nested-controller request is returned to the active Workflow unless an explicitly bounded controller is authorized; the flat pilot does not create another agent tree.
- A later round receives only accepted evidence, active hypothesis, ruled-out paths, unresolved contradictions, and completed scopes that constrain its next question.
- Candidate evidence stays provisional until the completion verifier returns verified evidence; mismatch and blocker results stop completion.

## Required regressions

- An exact `agent({agentType}): agent type '...' not found.` message may use the read-only `Explore` fallback; a worker, permission, schema, or tool error that merely embeds that text must propagate instead of falling back.
- Candidate evidence with `lines:0` or a reversed range such as `lines:20-10` blocks before completion.
- Candidate evidence must use the caller-declared `evidenceVersion`; abbreviated, mutable, or mismatched versions block, while the Workflow documents that SHA existence still requires caller/repository verification.
