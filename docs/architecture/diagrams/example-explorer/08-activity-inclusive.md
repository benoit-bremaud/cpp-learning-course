# Activity diagram — Apply an inclusive temperature threshold

## Context

This activity models the separate rule that the indicator activates at or above 30 °C. Source: [example explorer specification](../../specs/example-explorer.md) § P4. Requirements: [site-wide charter](../../../example-charter.md).

## Diagram

![08-activity-inclusive](08-activity-inclusive.svg)

## Notes

- Temperature 29 returns `false`; 30 and 31 return `true`.
- Equality is included because the requirement differs from the strict reference.
- Tests must follow the stated rule instead of preferring one comparison operator.
