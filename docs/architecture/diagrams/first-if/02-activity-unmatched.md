# Activity — first if — unmatched

Source: [First if proposal](../../specs/first-if.md).

## Context

Owner-approved conception: inspect a stored bool, execute or skip a message, then continue with the common write and return. Both paths remain modeled for the concrete supplied initializer.

## Diagram

![Conditional message and common continuation](02-activity-unmatched.svg)

## Notes

Guard not is used here as a UML predicate; no negation is added to the teaching programs. Guards are complementary, so exactly one path is selected. The empty false path merges before the common write; no parallel execution or synchronization. This model is also the expected design for the misplaced-statement discrepancy.
