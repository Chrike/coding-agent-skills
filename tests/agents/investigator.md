# Investigator Agent Contract

The investigator is a read-only leaf for one bounded evidence question. It reads only the supplied scope, returns structured candidate evidence plus a conclusion/blocker/next question, and never edits, runs commands, creates artifacts, delegates, or expands the task. Dynamic acceptance criteria, round state, candidate registry, schemas, and validation remain with `adaptive-long-horizon`.
