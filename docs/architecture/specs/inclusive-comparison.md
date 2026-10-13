# Reaching a limit versus exceeding it

Status: option A explicitly approved by the owner on 2026-10-13; implemented and verified locally; validation evidence is recorded in docs/validation.md.

## Need and contract

Build on the strict-comparison lesson with one new operator, >=. Two questions share the same known numeric inputs: "strictly beyond the limit?" and "at least the limit?". limit_exceeded answers the first; limit_reached answers the second. Define the latter explicitly as reached OR exceeded, never as exactly equal or a previously latched historical event.

Keep measurement_limit at const int 3; supplied measurement_count values are 2,3,4. The same-type initialized ints are in 0..20. Both comparisons yield bool and leave their operands unchanged. Each example is independent inside main with no output. No sensor, storage allocation, stopping action, automatic enforcement or result update. No new if, ==, <, <=, logical operators, numeric conversion or arithmetic.

Introduce >= as one operator spelled with adjacent > then =, meaning greater than or equal to; do not describe it as an assignment following >. The mathematical phrase "or equal" does not introduce the C++ logical-or operator.

## Five proposed examples

The first three compare both predicates side by side, using known initialization/const/bool mechanics. At count three, only the inclusive predicate is true. At four both predicates are true, which prevents treating >= as equality alone.

### below

Result pair (limit_exceeded / limit_reached): false/false.

```cpp
const int measurement_limit = 3;
int measurement_count = 2;
bool limit_exceeded = measurement_count > measurement_limit;
bool limit_reached = measurement_count >= measurement_limit;
```

### equal

Result pair (limit_exceeded / limit_reached): false/true.

```cpp
const int measurement_limit = 3;
int measurement_count = 3;
bool limit_exceeded = measurement_count > measurement_limit;
bool limit_reached = measurement_count >= measurement_limit;
```

### above

Result pair (limit_exceeded / limit_reached): true/true.

```cpp
const int measurement_limit = 3;
int measurement_count = 4;
bool limit_exceeded = measurement_count > measurement_limit;
bool limit_reached = measurement_count >= measurement_limit;
```

### strict-for-inclusive

Result pair (limit_exceeded / limit_reached): false/false (expected false/true).

```cpp
const int measurement_limit = 3;
int measurement_count = 3;
bool limit_exceeded = measurement_count > measurement_limit;
bool limit_reached = measurement_count > measurement_limit;
```

### inclusive-for-strict

Result pair (limit_exceeded / limit_reached): true/true (expected false/true).

```cpp
const int measurement_limit = 3;
int measurement_count = 3;
bool limit_exceeded = measurement_count >= measurement_limit;
bool limit_reached = measurement_count >= measurement_limit;
```

## Deliberate discrepancies

strict-for-inclusive misses a reached threshold: it uses > for the second question, so the second answer is false at count three. Correct only that expression to >=.

inclusive-for-strict falsely claims a strict exceedance: it uses >= for the first question, so the first answer is true at count three. Correct only that expression to >.

Both snippets compile. Both retain the two original questions; changing a name or requirement is not the correction. The equal model supplies the expected pair false/true and must be labeled as intended behavior, not the faulty execution. Under count two or four, both faulty versions match the correct pair: those inputs alone mask the substitutions. Explain this with a small summary table, not another code block solely to inflate example count.

## Traceability and UML

| Case | Model | Contribution |
| --- | --- | --- |
| below | 01-activity-below | Both answers false below the boundary |
| equal | 02-activity-equal | Difference at the boundary: false/true |
| above | 03-activity-above | Both true beyond it; inclusive does not mean equal-only |
| strict-for-inclusive | 02-activity-equal, expected only | An overly strict test misses the reached limit |
| inclusive-for-strict | 02-activity-equal, expected only | An inclusive test incorrectly reports strict exceedance |

Use native activity actions, not decision diamonds: computing two answers does not branch. Preserve exact names and values. Calculation and storage are conceptual steps within each declaration, not extra variables. Four-row traces mark each variable as not yet created until its declaration. The first bool remains unchanged when calculating the second.

## Implementation scope after approval

- src/content/docs/notions/atteindre-ou-depasser.md: five code examples, visible conception before code, five immediate UML cards with two discrepancy labels, value traces and comprehension checks.
- public/diagrams/examples/inclusive-{below,equal,above}.svg: unchanged authoritative renders.
- Update sidebar, previous comparison lesson, roadmap, introductory count and README command.
- tests/inclusive-comparison.py: extract actual excerpts, compile C++17 with warnings as errors, check bool expression/result types, all initialized-value checkpoints and unchanged inputs; reuse actual expressions for counts 2/3/4 to verify boundary differences and masking. No output; verify SVG provenance.
- Extend browser route/count, discrepancy and no-JS coverage. Record actual validation evidence. Keep shared UI, deployment, practice publication and deferred quizzes/downloads unchanged.

Companion explorer sheets remain a future authoring gap; do not add empty category controls.

## Four-pass conception review

1. Requirements: the strict/inclusive distinction is motivated by different questions. Three boundary neighborhoods and both wrong operator substitutions cover distinct failure directions. No claim that one operator is universally better or safer.
2. Dependencies/SOLID: one new operator using the exact previous variables and known declarations; no new component, framework dependency or data structure.
3. KISS/YAGNI/DRY: three authoritative models cover five cases. Repeated four-line fragments make each independent; their contribution is the changed boundary or mistaken rule, not vocabulary changes. No recap of unrelated operations or redundant stale-result scenario.
4. Pattern fit: no pattern or state machine is justified. The wording avoids conflating the current comparison with a latched historical "has ever reached" flag, equality-only meaning, or actual limit enforcement.

## Alternatives and scores

Judgments /5, not measured learner outcomes. Weights: progressivity 35%, misconception coverage 35%, readability 20%, simplicity 10%.
A — paired > and >= at 2/3/4 plus two opposite errors: 5/5/4/5 = 4.8.
B — >= alone, refer back to the previous lesson for >: 5/3/5/5 = 4.3; shorter snippets but forces cross-page comparison at the critical distinction.
C — all six comparisons now: 2/4/2/3 = 2.8; broad coverage but overloads one step.
D — defer >= and apply > inside if first: 3/2/3/3 = 2.7; concrete branching but leaves the boundary distinction unresolved while introducing control flow.

A is preferred under the owner's progressive, example-rich priorities. B could be preferable if paired results overload the learner; the deliberate four-line size and named questions limit that risk. Comprehension remains unmeasured.

## Source

https://eel.is/c++draft/expr.rel specifies built-in comparison results (bool) and arithmetic relations. Current working draft, not the published ISO C++17 edition. Semantic claims will be checked in C++17 on the proposed examples before requesting implementation approval.


## Conception verification

All five proposed snippets were extracted from this specification and compiled in C++17 mode with -Wall -Wextra -Werror. Checks covered every initialized-value checkpoint and both result types; all passed with no stdout/stderr. Three PlantUML models rendered successfully and the equality diagram was visually inspected. This is proposal verification, not evidence of an implemented lesson or browser acceptance.
