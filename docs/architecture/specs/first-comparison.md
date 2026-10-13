# First comparison: has a fixed limit been exceeded?

Status: proposed conception; implementation awaits explicit owner validation. Prepared on 2026-10-13.

## Need and prerequisites

Connect CPP-09's constant limit, current integer values, and the previous bool lesson. Compute a boolean answer to "does measurement_count strictly exceed measurement_limit?" rather than supplying true/false manually. The fictional limit is three measurements. Reaching it is not exceeding it. Comparing does not prevent, clamp or repair a count beyond the limit.

Use initialized local ints in 0..20 and const int measurement_limit = 3. Supply known counts; no sensor, actual measurement acquisition, storage allocation, IO, loops or automatic updates. Introduce only built-in >. No if, >=, <, ==, logical combinations or numeric conversions in teaching snippets. Standalone > returns bool; it is not a guard that changes control flow. Prerequisites: CPP-01, CPP-09 and first boolean values. Counter update is useful reinforcement but no arithmetic is required here.

## Five independent snippets

### below — evaluate below the limit

Expected limit 3, count 2, answer false; numeric inputs remain unchanged.

```cpp
const int measurement_limit = 3;
int measurement_count = 2;
bool limit_exceeded = measurement_count > measurement_limit;
```

Read the expression as "measurement count is strictly greater than measurement limit". The comparison itself yields bool; declaring a bool does not create the truth rule. The declaration creates and initializes a result, not a permanent relation between variables.

### equal — distinguish reached from exceeded

Expected false at the exact limit. This is a boundary case, not an error or unknown observation.

```cpp
const int measurement_limit = 3;
int measurement_count = 3;
bool limit_exceeded = measurement_count > measurement_limit;
```

### above — obtain a true result without enforcing the limit

Expected true with count still four and limit still three. Do not claim measurements have been rejected or the count reset.

```cpp
const int measurement_limit = 3;
int measurement_count = 4;
bool limit_exceeded = measurement_count > measurement_limit;
```

### reversed — compile successfully but ask the wrong question

Keep the above requirement: four exceeds three, so the expected answer is true. Swap operands while retaining the same operator. Actual false; expected activity is above, explicitly labeled as the intended model rather than execution of faulty code.

```cpp
const int measurement_limit = 3;
int measurement_count = 4;
bool limit_exceeded = measurement_limit > measurement_count;
```

Correction restores count > limit. Inverting operands asks if the limit exceeds the count. At equal operands both expressions yield false, so testing only equality would mask this mistake. Explain this in prose/table, without another duplicated code fragment.

### refresh — a stored answer does not recalculate itself

Expected answer initially false at count two, still false after assigning count four, then true after explicit recomputation. The stored answer is from the earlier observation; no undefined behavior or language error occurs when inputs later change.

```cpp
const int measurement_limit = 3;
int measurement_count = 2;
bool limit_exceeded = measurement_count > measurement_limit;
measurement_count = 4;
limit_exceeded = measurement_count > measurement_limit;
```

The five-row trace is essential: it shows the intermediate stale value as well as the final result. Reuse the original requirement with new data instead of introducing another context solely to increase snippet count.

## Conception and traceability

| Scenario | Authoritative activity | Expected observation |
| --- | --- | --- |
| below | 01-activity-below | 3,2,false |
| equal | 02-activity-equal | 3,3,false |
| above | 03-activity-above | 3,4,true |
| reversed | 03-activity-above, expected only | actual false instead of true |
| refresh | 04-activity-refresh | stored false remains after count changes, explicit update yields true |

Each result has a concrete role, not a general "good/bad" meaning. Use activity actions for calculation and storage, not conditional branches or a state-machine pattern. No invented temporaries, automatic watchers or hardware actions.

## Planned delivery after approval

- src/content/docs/notions/premiere-comparaison.md: five independent snippets, essential visible UML before code, five immediate cards (one discrepancy), requirement/mapping/traces, short comprehension check.
- public/diagrams/examples/comparison-{below,equal,above,refresh}.svg: unchanged rendered snapshots.
- astro.config.mjs, previous bool lesson, roadmap, homepage availability and README test command.
- tests/first-comparison.py: extract actual snippets, compile C++17 with warnings as errors, check every initialized-value checkpoint and unchanged inputs, bool expression/result types, reversed-operand failure, equality masking and no output. Verify SVG provenance.
- Browser checks: route, five card controls including discrepancy, desktop/mobile/no-JS; document validation evidence.

No shared UI change, practice publication, deployment, graded exercises or downloads. Missing companion explorer content remains an authoring gap rather than an empty control.

## Four-pass review

1. Requirements: three boundary neighborhoods, operand roles, calculated versus assigned literal answer, and stored versus recomputed result are covered. Most important risk: mistaking observation for enforcement.
2. Dependencies/SOLID: only known int/const/bool declarations and assignments plus one operator; reuse static rendering/cards. No new runtime responsibility or architectural layer.
3. KISS/YAGNI/DRY: five purposeful examples with four models; a separate stale-only snippet would duplicate refresh's intermediate trace. No compulsory fixed count of examples. The longer final snippet remains five lines with explicit checkpoints.
4. Pattern fit: none justified; no decision diagram branching when code only computes a value. No pattern for a few local variables.

## Alternatives and scoring

Decision judgments /5, not empirical learner outcomes. Weights: progressivity 40%, misconception coverage 30%, readability 20%, simplicity 10%.
A — single > with boundaries, operand error and recalculation: 5/5/4/5 = 4.8.
B — strict/inclusive pair > and >= together: 4/5/3/4 = 4.1; coherent follow-up but introduces a second rule before the first is established.
C — catalog of all six comparisons plus if: 2/4/2/2 = 2.6; broad reference but too many new elements for this progression.
D — defer comparisons and expand bool syntax first: 3/2/4/4 = 3.0; simple but postpones answering questions from actual numeric values.

A best fits the owner's small progressive modules. B would become preferable if strict comparison were already mastered; no evidence of that mastery is available. Broad reference tables can follow the worked sequence. Scores are sensitive to the pedagogical priorities, not proof of superiority.

## Sources and verification limits

https://eel.is/c++draft/expr.rel specifies bool results and arithmetic operand relations. Current working draft, not the published C++17 edition. https://www.learncpp.com/cpp-tutorial/relational-operators-and-floating-point-comparisons/ is an authored curriculum comparison; its six-operator, input/output and floating-point scope is intentionally not copied into this first step. Proposed snippets can be checked in C++17 before implementation; successful execution does not establish learner comprehension.


## Conception verification

Before requesting implementation approval, all five proposed snippets were extracted from this specification and compiled with g++ in C++17 mode (-Wall -Wextra -Werror). Every initialized-value checkpoint and the bool comparison-expression type were checked; execution produced no output. All four PlantUML models rendered successfully; the refresh diagram was visually inspected. These checks validate the proposal, not an implemented course page or its browser behavior.
