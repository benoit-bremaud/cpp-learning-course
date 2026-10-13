# Explicit alternative: if and else

Status: option A approved by the owner; implemented and verified locally; evidence is recorded in docs/validation.md.

## Need and acceptance criteria

Follow premiere-condition with one new mechanism: else. Keep the named bool, complete C++17 console programs, known integer inputs in 0..20 and normal stdout. A single normal passage selects exactly one branch, then executes the shared continuation. No input, hardware, nested conditions, loops, logical operators, direct comparison inside if, branch-local declarations or patterns. None has a present pedagogical need here.

The false branch means the stored answer is false; its domain meaning depends on the comparison. For exact equality to 3, both 2 and 4 select else. Do not translate this into below target or target not reached. No mutation occurs between bool initialization and selection. As already taught, a stored bool does not automatically recompute when operands change.

Five complete examples have distinct roles: match (3), below (2), above (4), identifier transfer (9 versus 7), and a deliberately wrong directional message at 4. Introduce both correct numeric false cases before the error. The error compiles but violates the intended message; label actual versus expected output and retain the intended above activity as its reference. Show a 2/3/4 boundary table and 5/7/9 identifier table. Explain each English output in French without changing its literal spelling.

Every example needs purpose, full code, expected/actual stdout, a short execution trace, and an adjacent UML control. In the trace name the selected branch, skipped branch, shared continuation and return. Teach decision and merge diamonds; the merge does not execute both branches or synchronize parallel work. UML guards [target_matched] and [not target_matched] are mutually exclusive here. The predicate not is also a C++ alternative token, but no negation operator is introduced in this lesson.

## Alternatives and decision

Scores are editorial judgments, not measured learning outcomes. Weights: continuity 35%, semantic coverage 30%, reading load 25%, transfer 10%.

| Option | Continuity | Coverage | Reading load | Transfer | Weighted /5 |
| --- | --- | --- | --- | --- | --- |
| A: five focused examples, named bool | 5 | 5 | 4 | 5 | 4.75 |
| B: three examples, below case only in table | 5 | 4 | 5 | 3 | 4.50 |
| C: else plus direct conditions and else if | 3 | 5 | 2 | 4 | 3.45 |

A is preferred for the owner's explicit emphasis on many meaningful examples. B becomes preferable if repetition burdens reading; this has not been measured. C adds too many independent mechanisms. Deferring else for another full comparison module would repeat already published prerequisites; use refresher links instead.

## Proposed complete programs

### matched

```cpp
#include <iostream>

int main() {
    const int measurement_target = 3;
    int measurement_count = 3;
    bool target_matched = measurement_count == measurement_target;

    if (target_matched) {
        std::cout << "Target matched\n";
    } else {
        std::cout << "Target not matched\n";
    }
    std::cout << "Check finished\n";
    return 0;
}
```

Expected stdout:

```text
Target matched
Check finished
```

### below

```cpp
#include <iostream>

int main() {
    const int measurement_target = 3;
    int measurement_count = 2;
    bool target_matched = measurement_count == measurement_target;

    if (target_matched) {
        std::cout << "Target matched\n";
    } else {
        std::cout << "Target not matched\n";
    }
    std::cout << "Check finished\n";
    return 0;
}
```

Expected stdout:

```text
Target not matched
Check finished
```

### above

```cpp
#include <iostream>

int main() {
    const int measurement_target = 3;
    int measurement_count = 4;
    bool target_matched = measurement_count == measurement_target;

    if (target_matched) {
        std::cout << "Target matched\n";
    } else {
        std::cout << "Target not matched\n";
    }
    std::cout << "Check finished\n";
    return 0;
}
```

Expected stdout:

```text
Target not matched
Check finished
```

### identifier

```cpp
#include <iostream>

int main() {
    const int expected_identifier = 7;
    int observed_identifier = 9;
    bool identifier_matched = observed_identifier == expected_identifier;

    if (identifier_matched) {
        std::cout << "Identifier matched\n";
    } else {
        std::cout << "Identifier not matched\n";
    }
    std::cout << "Check finished\n";
    return 0;
}
```

Expected stdout:

```text
Identifier not matched
Check finished
```

### wrong-message

```cpp
#include <iostream>

int main() {
    const int measurement_target = 3;
    int measurement_count = 4;
    bool target_matched = measurement_count == measurement_target;

    if (target_matched) {
        std::cout << "Target matched\n";
    } else {
        std::cout << "Below target\n";
    }
    std::cout << "Check finished\n";
    return 0;
}
```

Actual stdout:

```text
Below target
Check finished
```

Required stdout instead: `Target not matched` then `Check finished`, each followed by a newline. Reference: above model. At 2 the incorrect wording happens to describe the value correctly; at 4 it fails. Compilation cannot detect this semantic error.

## Implementation scope after approval

Add src/content/docs/notions/premiere-alternative.md; copy the four authoritative SVGs into public/diagrams/examples/first-else-*.svg. Use the existing UML popup component and animations unchanged. Integrate navigation and availability in astro.config.mjs, the homepage, README and progression documents after reading their current state. Link the preceding lesson and retain explicit unavailable status for future practice repositories. Do not add empty companion explorer controls.

Add tests/first-else.py extracting actual published programs: exact stdout/stderr/status for 2/3/4 and 5/7/9, with wrong-message expectations separated from intended behavior. Verify stored values and bool types independently. Extend tests/explorer-browser.py for all five cards, keyboard/outside/Escape closing, focus and 320/390/1440px layout. Verify source/public SVG byte identity, npm run check and npm test. Record evidence in docs/validation.md. No CI change, deployment, push or PR.

## Four-pass conception review

1. Requirements and traceability: five examples map to the five stated learning roles. False includes both directions for equality. The faulty case references intended behavior, not a misleading actual-flow diagram.
2. Dependencies and SOLID: static course content uses existing rendering. No runtime domain service or interface is justified.
3. KISS/YAGNI/DRY: complete snippets intentionally repeat stable context to isolate one changed input; shared site controls are reused. Four input-specific diagrams keep correspondence explicit.
4. Pattern fit: no design pattern is warranted by one conditional. No speculative abstraction, synthetic embedded IO, or premature multi-branch syntax.

## References and verification

- C++ working draft: https://eel.is/c++draft/stmt.if (normal true/false branch selection).
- UML 2.5.1: https://www.omg.org/spec/UML/2.5.1/PDF, sections 15.3.3.5–15.3.3.6 and 15.3.4.3 (merge and decision semantics/notation).
- Existing prerequisite: first-if.md and premiere-condition.md.

Design validation: five proposed programs compiled under C++17 with -Wall -Wextra -Werror, each exercised with three values (15 compilations/runs). Exact stdout, empty stderr and zero status verified. This verifies sample behavior, not learner assimilation. Visual rendering and browser integration remain separate checks.
