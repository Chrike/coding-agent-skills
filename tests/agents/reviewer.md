# Findings Reviewer Agent Contract

The findings reviewer is a fresh-context, read-only findings-only leaf. It returns structured severity, summary, repository-relative path, exact location, failure scenario, and evidence, or an empty findings list/blocker. It never repairs, edits, runs commands, decides completion, delegates, expands scope, publishes, or performs branch actions. `review-and-finish` owns caller selection, triage, repair, readiness judgment, and branch separation.
