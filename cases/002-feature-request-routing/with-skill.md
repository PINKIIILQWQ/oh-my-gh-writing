# [Reports] Add scheduled CSV exports with delivery settings

## Problem

A previous PR added a manual export workaround, but users still need first-class scheduled CSV exports for recurring report delivery.

## Requested Behavior

Add scheduled CSV exports for reports, with clear delivery settings.

## Use Cases

1. A user schedules a daily CSV export for a saved report and receives it automatically.
2. A team configures weekly delivery to selected recipients.
3. An admin reviews or updates export cadence, destination, and delivery status without relying on manual export steps.

## Proposed Settings

- Report to export
- Schedule frequency
- Time zone
- Recipients or delivery destination
- File format: CSV
- Delivery status and last-run result

## Alternatives

The current workaround is manual CSV export. This is insufficient for recurring reporting because it requires users to remember, run, and distribute exports themselves.

## Compatibility

This should preserve existing manual CSV export behavior while adding scheduling as a first-class option.
