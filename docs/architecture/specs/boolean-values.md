# First boolean values

Status: option A explicitly approved by the owner on 2026-10-13; implemented locally; verification is recorded in docs/validation.md.

## Need and scope

Represent a supplied yes/no fact with bool, true and false, using known initialization, assignment and value-copy mechanics. The statement is "a fault is reported", represented by fault_present. true confirms that statement; it does not mean a good outcome. false denies the statement in this scenario; it does not mean unknown. Do not infer physical equipment health from a manually assigned value.

Six independent fragments inside main, no stdout or hardware IO. New syntax is limited to bool and its literals. true/false are lowercase C++ values without quotes, not variables or translated keywords. Do not teach numeric conversions, storage size/one-bit assumptions, negation, comparisons, branches, loops, references or concurrency here. A missing/unknown observation cannot be represented by a third bool value; defer richer modeling.

## Scenarios and acceptance

| Case | Exact instructions | Checkpoints (fault_present, fault_snapshot if created) | Model |
| --- | --- | --- | --- |
| absent | bool fault_present = false; | false | 01-activity-absent |
| present | bool fault_present = true; | true | 02-activity-present |
| changes | bool fault_present = false; then assignments true, false | false → true → false | 03-activity-changes |
| copy | initialize false, initialize bool fault_snapshot from fault_present, assign true to fault_present | (false), (false,false), (true,false) | 04-activity-copy |
| refresh | same as copy, then fault_snapshot = fault_present; | (false), (false,false), (true,false), (true,true) | 05-activity-refresh |
| wrong | bool fault_present = true; despite required absence | actual true, expected false | 01-activity-absent (expected only) |

The present and wrong snippets are intentionally identical under different requirements. Explain that true is not inherently wrong: it is wrong only for the absence requirement. The faulty card must not imply the expected UML executes the faulty code.

## Delivery and tests

Add src/content/docs/notions/premiers-booleens.md with six code fences, immediate uniquely identified UML cards, expected behavior before code, conceptual mapping, and value traces. Render five authoritative PlantUML models and copy their SVGs unchanged into public/diagrams/examples. Reuse shared UI and no-JS disclosure. Update sidebar, previous lesson, roadmap, homepage and README availability and test command. Companion explorer content remains an explicit future authoring gap; no empty explorer.

Add tests/boolean-values.py: extract actual excerpts, compile C++17 with warnings as errors, assert bool types and every initialized-value checkpoint, prove preserved copy and explicit refresh, assert the wrong initial value differs from the requirement, check empty stdout/stderr and SVG provenance. Extend browser route/count, discrepancy and no-JS coverage. Record evidence, not unrun claims.

## Four-pass conception review

1. Requirements: two values, meaning determined by a clearly stated proposition, assignment versus detection, independent copy versus live binding, and correct language versus wrong requirement all have dedicated cases.
2. Dependencies/SOLID: new static content only; no additional UI, service, data schema or architectural boundary. Existing initialization/copy knowledge transfers from int to bool.
3. KISS/YAGNI/DRY: reuse five activities for six cases; one coherent fault context prevents terminology overload. No pattern or class is justified. Contrasted examples are deliberate teaching repetition rather than accidental duplication.
4. Pattern/anti-pattern risks: avoid speculative state machines for a straight sequence; no decision diamonds without code decisions, no automatic sensor truth, no equivalence between false and unknown, no invented one-bit guarantee.

## Alternatives

Judgment scores /5, not measured learner mastery. Weights: progressivity 40%, relevance 30%, readability 20%, simplicity 10%. A values/assignment/copy: 5/5/4/5 = 4.8. B add comparisons: 3/5/3/4 = 3.7. C also add if: 2/4/2/3 = 2.7. The owner's preference for small revisitable modules favors A. Actual comprehension is unmeasured.

## References

https://eel.is/c++draft/basic.fundamental#10 defines bool's two values; https://eel.is/c++draft/expr.assign defines assignment. These are current working-draft pages, not the published ISO C++17 edition. Executable checks target C++17. LearnCpp's boolean-values lesson provides a curriculum comparison; copying its numeric conversion/IO material would exceed this approved scope.
