# [Reports] CSV export crashes when result set is empty

Users report that exporting a CSV from Reports crashes when the selected report returns zero rows.

## Reproduction

Reported but not fully provided.

Known trigger:

- Export CSV from reports when the result set is empty.

Missing:

- Exact navigation path
- Filter or report setup
- Screenshot or log attachment

## Expected Behavior

The export flow should handle an empty result set without crashing.

Open question:

- Should the product download an empty or header-only CSV, or show an empty-state message?

## Actual Behavior

The export crashes when the result set is empty.

## Evidence

- User reports mention logs and screenshots.
- Logs and screenshots were not provided.
- No stack trace is available yet.

## Environment

- App version: TODO
- Browser/OS: TODO
- Report type: TODO
- Export format: CSV

## Additional Context

This appears specific to empty result sets. CSV export behavior with non-empty result sets needs confirmation.
