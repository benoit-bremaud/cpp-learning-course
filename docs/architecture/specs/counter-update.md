# Update a counter from its current value

Status: option A explicitly approved by the owner on 2026-10-13; implementation follows this conception.

## Need and acceptance criteria

Explain how an initialized mutable int supplies the value used to calculate its replacement. Readers already know initialization, assignment, addition and subtraction. Each snippet is independent inside main, with no output or hardware IO. A counter does not detect an event. Two written assignments do not introduce a loop.

Six cases: single 0→1; repeated 0→1→2; resumed 5→6→7; faulty reset 0→1→1 versus required 0→1→2; batch stock 5 plus added_count 3 becomes 8; withdrawal stock 8 minus used_count 2 becomes 6. Other operands stay unchanged. Every initialized variable is observed after each instruction.

Inputs and intermediate results are in 0..20, withdrawals do not exceed stock. These are teaching preconditions, not guards. Do not imply int is unbounded, saturating or hardware-atomic. No arithmetic overflow demonstration. No new syntax +=, ++, loops, comparisons, functions or hardware API. No pattern has a present justification.

## Models and traceability

| Case | Model | Verification |
| --- | --- | --- |
| single | 01-activity-single | checkpoints 0,1 |
| repeated | 02-activity-repeated | checkpoints 0,1,2 |
| resumed | 03-activity-resumed | checkpoints 5,6,7 |
| reset (deliberate error) | 02-activity-repeated, expected behavior only | actual 0,1,1; differs at second update |
| batch | 04-activity-batch | stock 5,5,8; added quantity remains 3 |
| withdrawal | 05-activity-withdrawal | stock 8,8,6; used quantity remains 2 |

Native activity diagrams explain value calculation followed by storage without introducing code temporaries. The faulty snippet explicitly diverges from the expected model; do not pass that model off as its execution trace. Explain the masking first update from zero: reset-to-one happens to match increment once.

## Delivery

Author src/content/docs/notions/mise-a-jour-compteur.md, retain shared UML cards and no-JS disclosures, publish five unchanged SVG snapshots for six snippets. Update sidebar, preceding division lesson, roadmap and homepage availability. Add tests/counter-update.py extracting actual snippets, compiling C++17 and checking each checkpoint, preserved operands, zero/full-withdrawal alternate cases, no stdout/stderr and SVG provenance. Extend existing browser route coverage and README command; record actual validation results.

Practice repositories, deployment, new UI, downloads and graded assessments are out of scope. Do not claim a new practice repository is available.

## Four-pass conception review

1. Requirements: one new mental model, existing syntax; every case resolves a different misconception or transfers the same rule. Contrast assignment with mathematical equality and retained versus replaced data.
2. Dependencies/SOLID: static authored content reuses existing UI. No new software boundary, runtime service or data model. Tests use real snippets rather than mocks.
3. KISS/YAGNI/DRY: five diagrams cover six cases because the error references the repeated case's intended model. Avoid another explorer with empty categories or repeated filler examples.
4. Pattern fit: none warranted. Prevent invented hardware actions, loops, automatic detection, overflow guarantees and temporary variables in diagrams.

## Alternatives

Judgments /5, not measured learning outcomes. Weights: progressivity 40%, understanding 30%, readability 20%, simplicity 10%. A explicit update and contrasted examples: 5/5/4/5 = 4.8. B add += and ++: 3/4/3/4 = 3.4. C introduce an Arduino loop: 2/3/2/2 = 2.3. A wins under the owner's small-module priority; a prior mastery of loops would change the assumptions. Actual learner mastery remains unmeasured.

## Sources

The assignment rule is grounded in https://eel.is/c++draft/expr.assign (current draft, not the published C++17 edition). Snippets are checked in C++17 mode. LearnCpp's arithmetic-operators lesson introduces explicit self-update before compound assignment; this informs comparison, not a requirement to adopt its whole sequence.
