# Activity diagram — Copy an integer value

## Context

This activity shows that two ordinary integer variables become independent after value copying. Source: [example explorer specification](../../specs/example-explorer.md) § P2. Requirements: [site-wide charter](../../../example-charter.md).

## Diagram

![05-activity-copy](05-activity-copy.svg)

## Notes

- `snapshot_count` receives the current value 12, not a live connection to `component_count`.
- The final values are 11 for `component_count` and 12 for `snapshot_count`.
- References, pointers and shared state remain outside this example.
