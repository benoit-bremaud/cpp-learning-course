# Repeat a decision until a limit is reached

Status: option A and the completed conception approved by the owner on 2026-10-20; implemented locally, with verification evidence recorded in `docs/validation.md` after the final checks.

## Need and learning boundary

Continue directly from the approved guarded-increment lesson. The learner already knows initialization, integer comparison, explicit assignment, `if`/`else`, console output and an upper limit. Introduce one new language mechanism: a `while` statement re-evaluates its condition before every possible iteration.

The lesson answers one question: how can the same bounded update be repeated until no further update is permitted? It does not teach keyboard input, sensors, `++`, `for`, `do`/`while`, functions, `break`, logical operators, containers, delays, hardware IO or concurrency. Programs use supplied nonnegative `int` values no greater than 20, a positive fixed limit, ordinary C++17 console output and arithmetic values far from overflow.

For the correct programs, the invariant is `initial_count <= count <= limit`. Every iteration increases `count` by exactly one, so the nonnegative variant `limit - count` decreases strictly and termination follows for the stated finite inputs. When the initial count already equals or exceeds the limit, the body executes zero times. The loop refuses further additions but does not repair an already excessive initial value.

The lesson must distinguish:

- evaluating a condition from storing a `bool` snapshot;
- zero iterations from one or several iterations;
- the back edge to the decision from parallel execution;
- termination of the loop from termination of the program;
- a correct bounded loop from code that merely compiles;
- the modeled count from acquisition of a physical measurement or insertion of an object.

## Acceptance criteria

1. Seven independent complete C++17 programs are presented in the approved order below.
2. Every program has an explicit requirement, expected output or non-termination warning, a value trace and an authoritative UML activity card.
3. Correct examples compile with `-Wall -Wextra -Wpedantic -Werror`, terminate with status 0, write exact stdout and leave stderr empty.
4. Tests exercise zero, one and multiple iterations and confirm that inputs and limits retain their specified roles.
5. The missing-update program is compiled but never run without a deterministic external guard; its infinite execution is established by trace and a bounded test harness.
6. The inclusive-condition error is executed and shown to finish one unit above the limit.
7. Public SVG snapshots are byte-identical to the rendered authoritative PlantUML sources.
8. Existing UML-card behavior is reused without shared UI changes.
9. Navigation, availability counts, previous/next links, the design map and validation evidence are updated during implementation.

## MCDA decision

Scores use a 0–5 ordinal scale. They are editorial judgments rather than measured learning outcomes. Non-compensable requirements are one principal new language mechanism, bounded correct examples, exact UML/code correspondence and deterministic verification.

| Criterion | Weight | Why it matters here |
| --- | ---: | --- |
| Continuity with guarded increment | 30% | Reuse the learner's accepted comparison and update model. |
| Isolation of one new concept | 25% | Keep the small-module contract. |
| Embedded relevance | 20% | Repeated polling and bounded state updates recur in firmware. |
| UML and test clarity | 15% | Make every evaluation and back edge observable. |
| Reading load | 10% | Avoid introducing several syntactic roles at once. |

| Option | Continuity | Isolation | Embedded relevance | UML/tests | Reading load | Weighted |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| A: bounded `while` with seven focused cases | 5 | 5 | 5 | 5 | 3.75 | **4.88** |
| B: repeat several `if` statements manually | 4 | 2 | 2 | 4 | 4 | 3.10 |
| C: introduce `for` directly | 4 | 3 | 4 | 4 | 2.5 | 3.60 |
| D: extract an addition function first | 3 | 3 | 4 | 4 | 3 | 3.40 |

Option A wins because it changes only the control structure while reusing the already accepted condition and assignment. B duplicates a fixed number of decisions and cannot express “until”. C combines initialization, continuation and iteration syntax before those roles have been separated. D improves naming but postpones the requested repeated decision and introduces function mechanics.

Sensitivity: A remains first if any single weight moves by 10 percentage points to another criterion. C is the recorded fallback at 3.60/5. Activate it only if evidence shows that a compact counted-loop header is easier for this learner than a visible pre-test/back-edge model; adopting it would require new diagrams and examples rather than a drop-in wording change.

## Approved example sequence

### 1. Multiple iterations

Start `measurement_count` at 1 with `measurement_limit` 3. The loop prints the value after each update, producing `2`, then `3`. Trace: decision true → update to 2 → back edge → decision true → update to 3 → back edge → decision false → final message. This establishes repeated re-evaluation.

### 2. One iteration

Start at 2 with limit 3. The same source structure runs its body once and finishes at 3. This contrasts behavior without introducing different syntax.

### 3. Zero iterations at the limit

Start at 3 with limit 3. The first evaluation is false, so the body is skipped and the final value remains 3. This makes the pre-test property explicit.

### 4. Zero iterations above the limit

Start at 4 with limit 3. The body is skipped and the value remains 4. The mechanism prevents another increment; it is not validation, clamping or repair.

### 5. Transfer to a box

Start `item_count` at 5 with `box_capacity` 8. The same loop produces 6, 7 and 8. The names change while the control rule remains identical. Items are abstract identical units; the program does not manipulate physical objects.

### 6. Deliberate missing-update error

Start at 1 with limit 3 and omit the assignment from the body. The comparison remains true forever because neither operand changes. The actual activity returns to the same true decision after printing the unchanged value. The page must state that successful compilation does not prove termination. Tests compile the exact snippet and use an instrumented finite-step model to establish the repeated unchanged state; they must not leave a runaway process.

### 7. Deliberate inclusive-condition error

Start at 1 with limit 3 but use `measurement_count <= measurement_limit`. The trace reaches 3, evaluates true once more, updates to 4, then exits. This isolates the boundary error and connects it to the earlier strict/inclusive comparison lesson.

## Source shape for correct examples

The lesson varies only the supplied names and values around this structure:

```cpp
#include <iostream>

int main() {
    const int measurement_limit = 3;
    int measurement_count = 1;

    while (measurement_count < measurement_limit) {
        measurement_count = measurement_count + 1;
        std::cout << measurement_count;
        std::cout << "\n";
    }
    std::cout << "Loop finished\n";
    return 0;
}
```

Do not cache the condition in a `bool` outside the loop: that would preserve the previous lesson's snapshot and make a true initial answer stale. A direct condition is required here because re-evaluation is the concept being taught. Do not extract a helper: one flat `main` keeps the causal relation visible.

## UML contract

Each activity shows initialization, a decision with `[count < limit]` and `[not count < limit]` guards, the update, observable write, a back edge from the body to the decision, the neutral final write `Loop finished`, return 0 and final node. Neutral wording is required because leaving the loop also covers an initially excessive value; it must not falsely claim that such an input equals the limit. The missing-update diagram deliberately lacks a state-changing action on its true path. The inclusive-error diagram uses the actual `<=` guard and labels the resulting fourth update; its notes contrast actual execution with the strict requirement.

Only activity diagrams are warranted. There is one program, no actor goal requiring a use-case view, no multi-component collaboration requiring a sequence/component view, no domain types requiring a class diagram, and no independently persistent lifecycle requiring a state machine. Adding those views would be diagram ceremony without a design question.

## Traceability

| Requirement | UML realization | Planned lesson evidence | Planned verification |
| --- | --- | --- | --- |
| RD-R1: condition is re-evaluated | Multiple-iteration back edge | Examples 1, 2 and 5 | Exact value sequences and iteration counts |
| RD-R2: body may run zero times | Initial false path | Examples 3 and 4 | Count unchanged; no iteration output |
| RD-R3: correct loops terminate under assumptions | Decreasing distance to limit | Examples 1–5 | Bounded alternate inputs and status 0 |
| RD-R4: transfer preserves the rule | Box activity | Example 5 | Values 6, 7, 8; capacity unchanged |
| RD-R5: progress is required | Missing-update back edge | Example 6 | Exact snippet compiles; finite-step model repeats count 1 |
| RD-R6: boundary operator matters | Inclusive actual activity | Example 7 | Actual sequence 2, 3, 4 and final 4 |
| RD-R7: conception matches every excerpt | Seven activity cards | Mapping tables and traces | Source labels, SVG provenance and browser card checks |

## Architecture and pattern review

- Requirements/traceability: each acceptance criterion maps to an activity, lesson artifact or deterministic check; no orphan behavior is planned.
- Dependency/SOLID: each standalone program has one teaching responsibility and depends only on the standard console. Static-site content consumes existing UML-card behavior; no domain logic depends on Astro UI code.
- KISS/YAGNI/DRY: keep direct programs and intentionally repeat small excerpts for independent reading. A shared teaching abstraction would hide the one changed condition and violate the module goal.
- Pattern fit: no design pattern has a present force. Strategy, State, Command and Template Method would add indirection without runtime variation, multiple implementations or a test seam. The correct decision is direct structured control flow.
- Anti-pattern check: the deliberate missing-progress case is labeled as an error, never recommended. The correct examples avoid infinite loops, hidden mutable globals, deep nesting, speculative helpers and magic unnamed limits.

## Implementation boundary after approval

Implementation may add one French lesson page, seven source/snapshot/documentation diagram triplets, one C++ extraction harness, navigation and documentation updates, and validation evidence. It must not change shared UI, CI, deployment, the practice repository, assessment scoring, downloadable summaries or hardware content. If the exact snippets or modeled behavior change, update this specification and obtain conception validation before or with that change.
