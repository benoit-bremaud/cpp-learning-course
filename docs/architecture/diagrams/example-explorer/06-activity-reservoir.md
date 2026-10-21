# Activity diagram — Detect a low reservoir level

## Context

This activity models a strict lower-bound decision for an already valid percentage. Source: [example explorer specification](../../specs/example-explorer.md) § P3. Requirements: [site-wide charter](../../../example-charter.md).

## Diagram

![06-activity-reservoir](06-activity-reservoir.svg)

## Notes

- Levels 0 and 19 return `true`; 20, 21 and 100 return `false`.
- Equality belongs to the false branch because the requirement is strictly below 20.
- Measurement acquisition and invalid-input handling remain outside this function.
