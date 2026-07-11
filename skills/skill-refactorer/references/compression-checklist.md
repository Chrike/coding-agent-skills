# Compression Checklist

Use this only after `skill-refactorer` is already active and the main file still feels too procedural.

## Good candidates for compression

- repeated reminders already covered by always-on instructions
- long step lists that only restate an obvious maintenance flow
- duplicated trigger language already present in frontmatter
- warnings that do not add a distinct safety or routing boundary
- stale caveats tied to removed files, old host behavior, or superseded migration phases

## Keep in the main skill file

- the real trigger boundary
- the main preserve-vs-remove distinction
- active safety and permission boundaries
- the relationship to adjacent workflows

## Move out of the main skill file

- optional cleanup heuristics
- extended examples of duplicated text patterns
- maintenance nudges that help but are not required for every invocation
- longer before-and-after style reminders

## Final check

- Do not compress a procedure merely because the host has a generic capability with a similar name.
- If the rewritten main file still reads like a maintenance essay instead of a narrow workflow boundary, compress again.
