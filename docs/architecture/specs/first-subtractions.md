# First subtraction: calculating a remaining quantity

Status: owner-approved conception, implemented locally; validation recorded in docs/validation.md.

## Need, scope and acceptance

Continue roadmap stage 3 after first-expressions. Explain binary subtraction as subtracting the second operand from the first, with an explicit stock contract. Learner can compute remaining stock, explain unchanged inputs, interpret an exactly empty stock and identify reversed operands as a requirement error rather than a compilation error.

Valid examples use known initial stock and used quantities between 0 and 20, with used quantity no greater than initial stock. This is a stated precondition, not a check performed by the code. Keep int; do not introduce unsigned as a supposed validation mechanism. Explain the small negative counterexample as representable by int, without introducing integer representation or unary-minus syntax lessons.

No self-update, -=, decrement, comparisons, conditions, division, multiplication, precedence, hardware IO or new website interaction. Subtraction is the single new operator. Future lessons handle multiplication/grouping, then division with its own exact/truncated-result and nonzero-divisor requirements before self-update according to the roadmap.

## Exact proposed fragments

S1 — known quantities, result 7:
```cpp
int remaining_count = 12 - 5;
```
Purpose: change the operator from the previous addition lesson. Define remaining_count as stock after using five of twelve components; no physical withdrawal occurs in code.

S2 — named quantities, checkpoints initial_count=12, used_count=5, remaining_count=7:
```cpp
int initial_count = 12;
int used_count = 5;
int remaining_count = initial_count - used_count;
```
Purpose: distinguish the original quantity from a newly calculated result. The two inputs remain 12 and 5. Not an update of initial_count.

S3 — exactly empty stock, inputs both 12, remaining_count=0:
```cpp
int initial_count = 12;
int used_count = 12;
int remaining_count = initial_count - used_count;
```
Purpose: meaningful boundary. Zero is the correct computed result, not missing data. Use in the main page, adjacent to S2, changing only the used quantity.

S4 — deliberately wrong formula, valid C++, result -7:
```cpp
int initial_count = 12;
int used_count = 5;
int remaining_count = used_count - initial_count;
```
Purpose: operand positions matter. Expected stock remains 7 per S2; actual result is -7. Explain negative as below zero and representable by int. Not a compiler failure, undefined behavior, evidence of physical negative inventory or automatic input validation. Correction: restore initial_count - used_count. Do not suggest swapping data values, clamping or renaming as fixes.

All four are independent fragments inside main, with no output. Tables are explanatory observations. Introduce each requirement before its code, with a discreet UML card after every fence.

## UML and interaction

Three authoritative activity views: literal, named, exactly-empty. Use the named expected activity for the S4 discrepancy card and explicitly contrast expected 7 with actual -7. Do not label the expected diagram as S4's executed trace. Activities split conceptual calculation/storage, without implying machine instruction count or operand evaluation order; final node ends the fragment, not main by an implicit return.

Use the existing UML card and no-script fallback, no UI modification. Four purposeful readings in the main lesson; do not fabricate two complementary categories just to add an explorer. Further companion content remains an authoring opportunity, per the charter's ban on empty controls.

## Implementation after approval

- New src/content/docs/notions/premieres-soustractions.md: four excerpts and corresponding model mappings, input assumptions, outcome tables and short self-explanation prompts without grading.
- public/diagrams/examples/subtraction-{literal,named,empty}.svg: copies of the three authoritative renders.
- astro.config.mjs, previous lesson continuation, parcours.md and index.md: sidebar, availability and lesson count.
- tests/first-subtractions.py: extract all actual snippets, C++17 compilation and instrumented checkpoint assertions, including the wrong-but-valid -7 result and expected/actual distinction; source/public SVG equality.
- Extend browser route/control coverage to four cards, including the discrepancy label; existing structural/link checks and regression suite.
- README.md and docs/validation.md: validation command and actual outcomes.

## Four-pass conception review

1. Requirements and traceability: each snippet addresses a distinct question; same identifiers/values across code and expected diagrams. S4 is explicitly nonconforming to the expected stock model.
2. Dependencies and responsibilities: relies only on initialized int and expressions; no framework, IO or new abstraction. Separate original stock from result to defer self-update.
3. KISS/YAGNI/DRY: four short cases, three models with explicit expected-model reuse. No new explorer category, schema, automated translator or duplicate copy of existing lessons.
4. Pattern fit and risks: no design pattern is warranted. Mitigate conflation of legal negative integers with valid domain quantities, implication of checked preconditions, fabricated output, and treating wrong arithmetic as compiler rejection.

## Alternatives and internal scoring

Scores /5; weights: progressive prerequisites 40%, example contribution 30%, reading load 20%, implementation simplicity 10%. Internal design judgment, not empirical learning measurements.

A. Focused subtraction: 5,5,5,5 = 5.0.
B. Subtraction, multiplication, division and grouping in one lesson: 2,5,2,3 = 3.0.
C. Skip directly to self-updating counters: 3,4,3,5 = 3.5.

A serves the accepted small-module organization. B introduces division-specific rules before a simple single-operator case is consolidated. C is useful later but adds state-change reasoning and skips the currently promised arithmetic step.

## Sources

- https://eel.is/c++draft/expr.add — difference is the second operand subtracted from the first.
- https://eel.is/c++draft/basic.fundamental — int is a signed integer type; small negative values are representable.

Consulted public HTML working draft; not the published ISO C++17 edition. Conception examples target C++17 and their concrete numerical results must be checked in that mode. Published course prose will be original and French; identifiers remain English.
