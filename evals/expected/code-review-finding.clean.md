## Findings

- Major: `src/export.ts` can throw before a CSV response is created when `rows` is empty.
  The code reads `rows[0].columns` without checking whether any rows were returned. Empty filtered reports would fail instead of producing an empty CSV. Add an empty-result branch before reading the first row.

## Open Questions

- Is an empty filtered report expected to download an empty CSV or show an in-app empty state?

## Test gaps

Behavior for empty rows cannot be verified from the provided diff alone.

## Change Summary

The diff changes CSV column selection in `buildCsv`.
