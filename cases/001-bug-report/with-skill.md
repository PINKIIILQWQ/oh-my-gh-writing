# [Reports] CSV export crashes when result set is empty

Users report that exporting a CSV from Reports crashes when the selected report returns zero rows.

## Reproduction

1. Open Reports.
2. Apply filters that produce an empty result set.
3. Select **Export CSV**.
4. Observe the export flow.

## Expected Behavior

The export should complete successfully and produce a valid CSV with headers and no data rows, or show a clear empty-state message.

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

This appears specific to empty result sets. CSV export behavior with non-empty result sets should be checked separately.
