# First multiplication: equal-size component kits

Status: enriched option A approved by the owner and implemented locally; verification recorded in docs/validation.md.

## Need and acceptance criteria

After basic addition/subtraction, explain binary * through three identical kits with four components per kit. The learner can choose multiplication from the requirement, distinguish kit count from components per kit, calculate a total without changing inputs and interpret zero kits. All examples use known quantities in 0..10; products stay in 0..100, safely representable by int. These are example assumptions, not runtime input validation or general int limits.

One new difficulty: choosing and reading multiplication. No precedence, parentheses, loops, *=, pointers, arrays, hardware access, or class/pattern. * is introduced only between two integer operands. Explain 3 times 4 as three groups of four in prose; it does not imply a loop in the program or how the processor implements multiplication. The number of components per kit must be the same for every kit.

## Proposed exact examples

M1 — literal product, expected 12:
```cpp
int component_count = 3 * 4;
```
Question: how do three groups of four give twelve components? Explain * as the code spelling of multiplication, rather than the letter x.

M2 — named roles, expected kit_count=3, components_per_kit=4, component_count=12:
```cpp
int kit_count = 3;
int components_per_kit = 4;
int component_count = kit_count * components_per_kit;
```
Question: which number counts groups, and which describes one group? Both inputs retain their values. Units: kits times components per kit gives components. No automatic formula binding or physical kit assembly occurs.

M3 — zero kits, expected 0:
```cpp
int kit_count = 0;
int components_per_kit = 4;
int component_count = kit_count * components_per_kit;
```
Question: does four components per kit imply that four components exist even with no kits? No: the total is zero. This is a known absence of kits, not missing input.

M5 — one kit, expected 4 (read after M2, before M3):
```cpp
int kit_count = 1;
int components_per_kit = 4;
int component_count = kit_count * components_per_kit;
```
Question: must multiplication increase the per-kit quantity? No: one group retains the same quantity. Together with M3 this directly addresses an overgeneralization from 3 * 4. Keep stable IDs; reading order M1, M2, M5, M3, M4.

M4 — deliberate wrong operation, valid C++, actual 7 instead of required 12:
```cpp
int kit_count = 3;
int components_per_kit = 4;
int component_count = kit_count + components_per_kit;
```
Question: why does a familiar operator not solve every total? Adding a group count to a per-group quantity does not compute the required component total. C++ int values carry no unit checking here; compilation succeeds. Restore * without altering the two correct input values. Expected activity is the M2 model, explicitly labelled expected 12 versus actual 7 before the image.

Each fragment is independent inside main, with no stdout. Statements define initialized locals. Tables show successive values; do not invent console output. All five cases in the main reading, no fabricated explorer categories.

## UML and planned files

Four PlantUML activities: literal, named, zero-kits and one-kit. Calculation/storage separation is conceptual; it neither introduces a named temporary nor specifies processor steps or operand evaluation order. The final node ends a fragment, not an implicit return. M4 reuses the named expected model, never described as its actual execution.

Implementation after approval:
- src/content/docs/notions/premieres-multiplications.md with five snippets and UML cards using the unchanged shared UI.
- public/diagrams/examples/multiplication-{literal,named,zero,one}.svg snapshots from the authoritative models.
- astro.config.mjs, subtraction continuation, parcours.md and index.md for navigation and honest availability.
- tests/first-multiplications.py to extract snippets, assert checkpoints and unchanged inputs in C++17, discriminate expected 12 from actual 7 and verify source/public SVG provenance.
- Browser route coverage for five cards including the discrepancy label; existing structural/link checks, README.md command and docs/validation.md outcomes.

## Four-pass review

1. Requirements: same context, five distinct questions (operator, named units, one group, zero groups, wrong operator); exact names and values mapped to models. The requirement specifies equal-size groups.
2. Dependencies: initialized integers and expressions suffice; no new runtime, IO, framework component or abstraction. Self-update remains later.
3. KISS/YAGNI/DRY: use the existing card component; four authoritative diagrams, with explicit reuse for the faulty case. No redundant companion sheet or automatic UML translator.
4. Pattern fit: no design pattern justified. Prevent interpreting arithmetic grouping as execution sequencing, confusing totals with per-group quantities, or inferring that a successful build proves domain correctness.

## Revised alternatives and weighted recommendation

The previous perfect score for the four-example proposal overstated its completeness. The deeper review found an uncovered misconception (multiplication always makes the per-group quantity larger) and a test-data trap (2 * 2 equals 2 + 2). Add M5 and explain the trap after the deliberately wrong operator, in a small result table rather than another duplicated code block. The table compares products/sums for (3,4): 12/7 and (2,2): 4/4. This is analysis of the already-shown formulas with alternate inputs, not an additional approved algorithm. Matching one expected number does not establish a generally correct formula.

Explicitly limit kits to equal contents. A brief prose contrast can say that differing kit contents cannot be computed by multiplying by a single shared per-kit value. Do not introduce arrays, loops or an average. 4 + 4 + 4 may illustrate three equal groups as mathematical prose, without claiming the CPU executes repeated additions.

Internal judgment /5, not measured effectiveness. Revised weights reflect the uncovered risks: prerequisite progression 30%, distinctive misconception coverage 30%, reading load 25%, simplicity 15%.

A — Focused five-case lesson, one-kit contrast and discriminating test-data note: 5,5,4,4 = 4.60.
B — Original four-case lesson: 5,3,5,5 = 4.40.
C — Multiplication plus mixed-expression grouping: 3,5,3,4 = 3.75.
D — All remaining arithmetic including division: 2,5,2,3 = 3.05.
E — Defer multiplication and repeat addition/subtraction: 1,2,5,5 = 2.90.

A costs one short example/diagram more than B, but directly addresses a common-sense overgeneralization without any new language prerequisite. C/D fit a faster review but add independent difficulties. E is sensible only if learner feedback reveals an actual earlier difficulty; none has been reported. Reading order remains concrete situation, expected result, UML, code and observation. Avoid turning explanatory tables into a scored quiz.

Confidence: high for the checked numerical results and language behavior; moderate for relative learning effectiveness, which requires learner feedback. This design does not claim the book/reference sources prescribe our exact example count or order.

## Source

https://eel.is/c++draft/expr.mul — binary * denotes multiplication. Public HTML working-draft reference, not the published ISO C++17 edition. Concrete snippets target C++17 and are checked in that mode; no claim about arbitrary large products or integer representation is needed.

Additional references consulted during deeper review:
- https://eel.is/c++draft/expr.pre — expression semantics and representable-result constraints; no operand execution ordering claim follows from a teaching activity.
- https://www.stroustrup.com/programming.html — author presentation of PPP3, emphasizing fundamentals and self-study; a pedagogical orientation only, not evidence for our exact module scoring. PPP3 uses newer C++ editions; our fragments remain C++17.
