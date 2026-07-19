# Verifier Agent Contract

The completion verifier is a fresh-context read-only leaf. It returns only `verified`, `blocker`, or `mismatch`, cites exact evidence for every verified criterion, and never implements, runs commands, delegates, expands scope, or performs branch actions. The owning Workflow retains candidate evidence, schema, validator, and final completion gate.
