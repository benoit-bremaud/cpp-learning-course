# First conditional execution: if and common continuation

Status: refined option A approved by the owner on 2026-10-13; implemented and verified locally; evidence is recorded in docs/validation.md.

## Need and recommended scope

Refine the initial suggestion of a first if/else lesson into two short modules. This module teaches one question: which instructions are executed when a known bool is true, and where does execution continue when it is false? The next module adds an explicit alternative with else, reusing the same scenario. Roadmap approval does not approve that future module's snippets.

Direct prerequisites already present: complete console program, iostream/cout, literal messages and newline, main braces and return 0; initialized int/const/bool and ==. Link both output lessons as optional refreshers alongside the equality lesson. Do not assume that the reader remembers output syntax merely because it was published.

Use complete C++17 console programs, no keyboard input. Inputs are supplied ints in 0..20, standard output is assumed working normally. Messages are observations, not hardware readiness, actual acquisition or authentication. target_matched means exact equality; avoid the ambiguous phrase target reached. Use a named bool before if to preserve the distinction between computing an answer and using it. A direct comparison inside if is deferred to the next module's design, not declared inferior or unsafe.

Explain if, its condition parentheses, braces around the controlled block, and the common statement after the closing brace. Use braces from the first example; indentation supports reading but does not determine the controlled statements. Do not claim braces are mandatory for a single C++ statement. Do not add a semicolon immediately after the if condition. A false condition skips this block, not the rest of main. This one passage does not wait for the value to change or keep checking it; loops come later.

Only one new execution mechanism. No else, !, &&, ||, implicit int-to-bool conversions, conditional declarations, nested if, early return, loops or branch-local variable declarations. No missing-brace, empty-statement or assignment-in-condition bug in this first module. A scope/lifetime lesson is unnecessary here because all variables are declared before the block.

## Proposed complete programs

### matched

Expected stdout:

```text
Target matched
Check finished
```

```cpp
#include <iostream>

int main() {
    const int measurement_target = 3;
    int measurement_count = 3;
    bool target_matched = measurement_count == measurement_target;

    if (target_matched) {
        std::cout << "Target matched\n";
    }
    std::cout << "Check finished\n";
    return 0;
}
```

### unmatched

Expected stdout:

```text
Check finished
```

```cpp
#include <iostream>

int main() {
    const int measurement_target = 3;
    int measurement_count = 2;
    bool target_matched = measurement_count == measurement_target;

    if (target_matched) {
        std::cout << "Target matched\n";
    }
    std::cout << "Check finished\n";
    return 0;
}
```

### identifier

Expected stdout:

```text
Identifier matched
Check finished
```

```cpp
#include <iostream>

int main() {
    const int expected_identifier = 7;
    int observed_identifier = 7;
    bool identifier_matched = observed_identifier == expected_identifier;

    if (identifier_matched) {
        std::cout << "Identifier matched\n";
    }
    std::cout << "Check finished\n";
    return 0;
}
```

### misplaced

Actual output: none; expected Check finished followed by a newline. Deliberately misplaced continuation.

```cpp
#include <iostream>

int main() {
    const int measurement_target = 3;
    int measurement_count = 2;
    bool target_matched = measurement_count == measurement_target;

    if (target_matched) {
        std::cout << "Target matched\n";
        std::cout << "Check finished\n";
    }
    return 0;
}
```

## Contribution, traces and UML

| Case | Model | Contribution |
| --- | --- | --- |
| matched | 01-activity-matched | True path executes the message, then reaches common continuation |
| unmatched | 02-activity-unmatched | Changing only input to 2 skips the block but still prints Check finished |
| identifier | 03-activity-identifier | Exact identifier recognition uses the same control flow in another context |
| misplaced | 02-activity-unmatched, intended model | Moving Check finished inside the block silently removes required output when false |

Use four complete code examples rather than impose the previous five-example count. A table at measurement counts 2/3/4 verifies both directions of mismatch. A transfer table at identifiers 5/7/9 keeps the exact-label meaning. The fourth example is a behavior error, not invalid syntax: at count 3 it prints the expected two lines, masking the error; at 2 or 4 it incorrectly prints nothing. Cards must state intended versus actual output; silent output is not a blank text block that could be mistaken for missing content.

Trace condition value, chosen path, executed/skipped write, common write, and normal return. Variable values remain unchanged. Explain the skipped instruction explicitly; do not list it as executed. Actual stdout and exit status are separate: return 0 is also possible for the wrong program, so successful execution does not prove the requirement is met. Both non-selected and selected paths remain visible in each UML model: a scenario input does not remove the program's alternative path.

UML introduces a decision node and merge node, not a fork/join. A false path performs no controlled write and rejoins the true path before the common write. A merge does not wait for both paths; there is only one selected path in this single-token activity. Guard predicates are [target_matched] / [not target_matched], or identifier equivalents. Explain not as a UML guard predicate (the value is false); do not suggest adding it to these programs. C++ also has not as an alternative token for !, which is deferred with logical operators, not denied. Reference: https://eel.is/c++draft/lex.digraph. This editorial correction changes no diagram or program behavior. Guards are mutually exclusive and exhaustive for bool. The input to the decision is already stored; the == expression is not reevaluated by if(flag). Rendering uses native PlantUML activity decisions, with an explicit merge after the empty false branch. Diagram scope begins in main; include is a declaration dependency, not a runtime action.

The error card reuses intended unmatched UML, with an explicit discrepancy mapping. Reuse the current discreet card UI, output blocks and full-size SVG links. No new UI controls or practice publication. Companion explorer sheets remain an authoring gap.

## Four-pass review

1. Requirements/traceability: the two initial examples differ only in input. A shared output after the block distinguishes skipping from terminating, while the final misplaced statement tests this exact distinction. Transfer is contextual, not a new API. Exact matching removes the previous ambiguous target reached wording.
2. Dependencies/SOLID: only already-taught library syntax and data operations. No physical pins, Arduino startup, new function design or external interaction. No domain architecture required for four simple sequential programs.
3. KISS/YAGNI/DRY: three models cover four complete programs. Returning to complete programs makes stdout testable; do not introduce a helper abstraction to shorten teaching code. Reuse existing site components and local harness patterns.
4. Pattern fit: no design pattern or state machine is justified. Avoid treating many examples as a fixed quota. Defer state changes inside branches and hardware examples until the reader can explain skipped instructions and common continuation.

## Alternatives and scored decision

Editorial judgments, not experimental evidence. Weights: progressivity 35%, observable behavior 25%, misconception coverage 25%, simplicity 15%.

| Option | Progressivity | Observable | Coverage | Simplicity | Weighted /5 |
| --- | --- | --- | --- | --- | --- |
| A: if alone now, else in the next small module | 5 | 5 | 5 | 4 | 4.85 |
| B: one lesson, if first then if/else | 4 | 5 | 5 | 4 | 4.50 |
| Original: start immediately with if/else and two outputs | 4 | 5 | 4 | 4 | 4.25 |
| C: modify a variable conditionally before returning to output | 4 | 3 | 4 | 4 | 3.75 |
| Begin directly with a real LED and digitalWrite | 2 | 5 | 3 | 2 | 3.00 |

A is preferred because the owner explicitly chose small independently revisitable modules. B is a close alternative if the reader wants faster progression, and avoids an extra page. The 0.35 gap is not proof of a measurable learning benefit. Variable mutation is a legitimate next application, but a trace-only result is less direct than already-known console output. Real hardware adds pin setup, board/runtime assumptions and safety/IO prerequisites to a control-flow lesson. Do not describe postponement as a universal teaching rule: language semantics do not mandate learning all comparison operators before if.

## What changed after investigation

The initial recommendation was usable but under-specified: it combined selection and an explicit alternative, did not demonstrate common continuation, and used reached for an exact-target context. Re-reading the actual output lessons confirms that console messages add no new output API prerequisite, whereas hardware does. The revised plan isolates skipping a block, keeps the named bool bridge, adds an observable common continuation and tests a misplaced statement rather than a familiar but prerequisite-heavy syntax trap.

Confidence: high for C++ behavior once the exact outputs compile/run, moderate for the preferred lesson split. No diagnostic answers demonstrate the reader's mastery. Reconsider B if the split proves repetitive; reconsider C if console syntax itself blocks comprehension.

## Implementation scope after approval

- Add src/content/docs/notions/premiere-condition.md with four complete programs, stdout blocks, path traces and UML cards.
- Copy three authoritative SVG snapshots to public/diagrams/examples/first-if-*.svg.
- Update sidebar, prior equality lesson, roadmap (if then else as separate steps), introduction availability and README test command.
- Add tests/first-if.py to compile actual programs in C++17 with -Wall -Wextra -Werror and assert exact stdout, empty stderr and exit 0. Test alternate input values 2/3/4 and identifier 5/7/9 by replacing only the explicit supplied initializer, including masking/exposure of misplaced continuation. Check unchanged inputs with an instrumented copy and SVG provenance.
- Extend browser route/card counts and no-JS checks; inspect decision/merge legibility on mobile, common continuation, error card and lack of page overflow. Run Astro check, build, Node tests and focused C++/browser checks. Record evidence and local commit.
- No shared UI, CI/deployment, practice repository, quizzes or downloads.

## References and attribution limits

- https://eel.is/c++draft/stmt.if: true executes first substatement; false executes else only when present. Working draft, not published C++17; proposed snippets compile in C++17.
- https://eel.is/c++draft/stmt.block: braces group statements into a block. Block scope exists, but this lesson adds no block-local declaration.
- https://www.learncpp.com/cpp-tutorial/introduction-to-if-statements/: the author's introductory sequence moves from if to if/else and uses observable console output. Its input, brace omission and further chaining are not copied into this prerequisite set. This is a curriculum comparison, not causal evidence.
- https://www.omg.org/spec/UML/2.5.1/PDF: sections 15.3.3.5, 15.3.3.6 and 15.3.4.3 were checked in the official PDF: merge without synchronization, guarded selection without token duplication, and diamond notation.

The educational split is derived from the owner's modularity preference and inspected prerequisite pages, not prescribed by the C++ standard or another author's course.

## Proposal verification

All four proposed programs compile in C++17 with -Wall -Wextra -Werror. Exact stdout, empty stderr and exit status 0 match their stated actual behavior, including the silent wrong program. This is conception verification, not evidence of an implemented lesson.

All three native PlantUML activities render successfully. The unmatched model was visually inspected: false bypasses the conditional write and merges before Check finished. Twelve additional program variants (measurement counts 2/3/4 and identifiers 5/7/9) verify both paths, common continuation and masking/exposure of the misplaced statement. No lesson, sidebar, live site or UI file has been changed.
