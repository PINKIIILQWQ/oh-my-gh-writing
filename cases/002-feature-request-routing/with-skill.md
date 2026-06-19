# [Reports] Add scheduled CSV exports with delivery settings

## Problem

A previous PR added a manual export workaround, but users still need first-class scheduled CSV exports for recurring report delivery.

## Requested Behavior

Add scheduled CSV exports for reports, with clear delivery settings.

## Use Cases

TBD: confirm target users and delivery workflow.

Potential areas to clarify:

- Export cadence
- Delivery destination
- Recipient model
- Failure notification behavior

## Proposed Settings

- File format: CSV
- Schedule frequency: TBD
- Delivery destination: TBD
- Recipient model: TBD
- Delivery status or failure handling: TBD

## Alternatives

The current workaround is manual CSV export. This is insufficient for recurring reporting because it requires users to remember, run, and distribute exports themselves.

## Compatibility

This should preserve existing manual CSV export behavior while adding scheduling as a first-class option.
