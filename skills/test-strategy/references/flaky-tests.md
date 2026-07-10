# Flaky Tests

Use when tests pass sometimes, fail under load, depend on timing, or contain guessed sleeps.

## Rule

Wait for the condition that proves progress, not a guessed duration.

## Replace Sleeps With Conditions

| Waiting For | Better Signal |
| --- | --- |
| Async state | state equals expected value |
| Event | event appears in stream |
| Queue/batch | count reaches expected size |
| File/process | file exists, process exits, port responds |
| UI | element visible/enabled or network call complete |

## Helper Shape

Use existing framework helpers first, such as Playwright assertions, Testing Library `findBy*`, or repo-specific wait utilities.

If no project or framework helper exists, implement a small polling helper with:

- a meaningful condition
- a deadline appropriate to the system
- a useful timeout message
- the last observed state or error when diagnostic value justifies it

Fixed sleeps are acceptable only when testing real timing behavior such as debounce, throttle, retry backoff, or polling intervals. First wait for the triggering condition, then document why the duration matters.
