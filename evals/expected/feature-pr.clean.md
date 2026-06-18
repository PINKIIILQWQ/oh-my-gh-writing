## Summary

Adds CSV export for the Reports page.

## Motivation

Users need a downloadable report format for offline review and sharing.

## Changes

- Adds an export action to the Reports page.
- Generates CSV output from the visible report rows.
- Surfaces export errors to the user instead of failing silently.

## Testing

Not run (not provided).

## Risk

- CSV formatting and large report sizes need confirmation.
- Browser download behavior may vary by environment.
