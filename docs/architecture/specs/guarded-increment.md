# Guard one increment with an upper limit

Status: refined after owner-requested deeper analysis; owner review still required before lesson implementation.

## Need and contract

Connect const, explicit count updates, < versus <=, and if/else. Author one short module on admitting ONE increment, not a general input-validation system. Preconditions: supplied int count in 0..20, fixed positive limit 3 (or capacity 8), normal console output. No input, sensors, storage allocation, concurrency, loops, ++, direct conditions, logical operators or functions. A count models known items; incrementing it does not acquire a measurement or insert a physical object.

Compute can_add once before the operation. If count < limit, update count = count + 1; otherwise preserve count. Print one branch message and the final count on its own line. For initially valid 0 <= count <= limit, final count stays within that interval. For an already excessive count, refuse further addition but do not repair the input. The lower-bound assumption is not checked. Limited teaching values avoid arithmetic overflow; this is not a general proof over arbitrary ints.

Critical second-order consequence: after 2 becomes 3, can_add remains true because it records the pre-operation comparison. Do not interpret it as remaining capacity afterward or reuse it for another operation. Show before/after state for both count and bool. Repeated operations require a fresh decision and are deferred. Explain that const only fixes the limit object; the guarded assignment enforces this operation's admission rule.

## Alternatives

Scores /5 are editorial judgments, not learner measurements. Weights: prerequisite continuity 35%, control-rule understanding 35%, reading load 20%, transfer 10%.

| Option | Continuity | Rule | Reading | Transfer | Weighted |
| --- | --- | --- | --- | --- | --- |
| A: one guarded increment, five focused examples | 5 | 5 | 4 | 5 | 4.80 |
| B: another message-only threshold lesson | 5 | 3 | 5 | 3 | 4.10 |
| C: direct conditions plus repeated attempts | 3 | 5 | 2 | 5 | 3.70 |

A connects known syntax to a new responsibility without introducing a new syntax feature. B is suitable if if/else remains unclear, but repeats observation without enforcing the requested operation. C risks mixing repeated decisions and stored-state freshness with a syntax change. Full interval validation is deferred until logical combinations; silent clamping would introduce a different requirement.

## Approved-prerequisite sources

- [Constant limit](constant-limit.md): const does not enforce another variable's bound.
- [Counter update](counter-update.md): explicit increment syntax.
- [Lower comparisons](lower-comparisons.md): room for one item versus already within capacity.
- [First else](first-else.md): exclusive branches and common continuation.
- https://eel.is/c++draft/stmt.if and https://eel.is/c++draft/expr.rel (verified selection and strict/inclusive comparison semantics).
- UML 2.5.1, https://www.omg.org/spec/UML/2.5.1/PDF, 15.3.3.5–15.3.3.6: decision and merge.

## Proposed programs and outcomes

### room

```cpp
#include <iostream>

int main() {
    const int measurement_limit = 3;
    int measurement_count = 2;
    bool can_add = measurement_count < measurement_limit;

    if (can_add) {
        measurement_count = measurement_count + 1;
        std::cout << "Count increased\n";
    } else {
        std::cout << "Addition refused\n";
    }
    std::cout << measurement_count;
    std::cout << "\n";
    return 0;
}
```

Expected stdout:

```text
Count increased
3
```

Before/after count: 2 → 3; stored can_add remains true.

### full

```cpp
#include <iostream>

int main() {
    const int measurement_limit = 3;
    int measurement_count = 3;
    bool can_add = measurement_count < measurement_limit;

    if (can_add) {
        measurement_count = measurement_count + 1;
        std::cout << "Count increased\n";
    } else {
        std::cout << "Addition refused\n";
    }
    std::cout << measurement_count;
    std::cout << "\n";
    return 0;
}
```

Expected stdout:

```text
Addition refused
3
```

Before/after count: 3 → 3; stored can_add remains false.

### already-above

```cpp
#include <iostream>

int main() {
    const int measurement_limit = 3;
    int measurement_count = 4;
    bool can_add = measurement_count < measurement_limit;

    if (can_add) {
        measurement_count = measurement_count + 1;
        std::cout << "Count increased\n";
    } else {
        std::cout << "Addition refused\n";
    }
    std::cout << measurement_count;
    std::cout << "\n";
    return 0;
}
```

Expected stdout:

```text
Addition refused
4
```

Before/after count: 4 → 4; stored can_add remains false.

### box

```cpp
#include <iostream>

int main() {
    const int box_capacity = 8;
    int item_count = 7;
    bool can_add = item_count < box_capacity;

    if (can_add) {
        item_count = item_count + 1;
        std::cout << "Count increased\n";
    } else {
        std::cout << "Addition refused\n";
    }
    std::cout << item_count;
    std::cout << "\n";
    return 0;
}
```

Expected stdout:

```text
Count increased
8
```

Before/after count: 7 → 8; stored can_add remains true.

### inclusive-error

```cpp
#include <iostream>

int main() {
    const int measurement_limit = 3;
    int measurement_count = 3;
    bool can_add = measurement_count <= measurement_limit;

    if (can_add) {
        measurement_count = measurement_count + 1;
        std::cout << "Count increased\n";
    } else {
        std::cout << "Addition refused\n";
    }
    std::cout << measurement_count;
    std::cout << "\n";
    return 0;
}
```

Actual stdout:

```text
Count increased
4
```

Before/after count: 3 → 4; stored can_add remains true.

Required instead: `Addition refused` then `3`, each followed by a newline. The full model is the intended design. The <= comparison admits equality and permits 3 → 4. At 2 this defect is masked. Do not diagnose const or assignment as the fault.

## Integration after approval

Create src/content/docs/notions/ajout-sous-limite.md, with five complete examples and adjacent UML cards, primary diagrams before correct code, exact outputs and before/after tables. Translate output meanings; Count increased reports the modeled count change, not hardware activity. Reuse the full expected diagram for the incorrect comparison, explicitly labeled as intended behavior. Include a 0/2/3/4 table and 7/8/9 transfer checks. Keep naming consistent with previous measurement and box examples.

Publish four byte-identical SVG snapshots; update sidebar, previous/next links, counts, roadmap and docs/design.md. Add actual-snippet C++ checks for branch messages, exact final values, unchanged limit, stored bool, admitted/refused paths, boundaries and the inclusive error. Extend existing browser coverage for five cards and no-JS, narrow layouts and discrepancy text. Run check/build/tests and record evidence in docs/validation.md. No shared UI, CI, practice-repository, deployment or deferred-feature change.

## Four-pass review

1. Requirements: new objective is a conditional state change. Below/full/above distinguish admission, rejection and non-repair; box transfers; <= error exposes the equality boundary. Output and UML refer to the same modeled operation.
2. Responsibilities/dependencies: authored content and existing rendering suffice. No class, service or hardware adapter is justified.
3. KISS/YAGNI/DRY: reuse familiar syntax and small integers; complete programs intentionally retain context. Reuse intended model for the faulty variant. No abstraction or loop solely to shorten examples.
4. Pattern fit: no pattern required. Avoid stale-permission reuse, implicit clamping and treating a constant as automatic validation.

## Design verification

Five proposed programs tested over five supplied values each: 25 C++17 compilations/executions with -Wall -Wextra -Werror. Instrumented assertions verify final count, preserved limit and stored pre-operation bool; exact stdout, empty stderr and normal exit pass. This validates candidate behavior, not learner mastery or final page integration. Browser verification is deferred until approved implementation.


## Deeper review: refined recommendation

This review supersedes the initial comparison table, not the candidate program behavior. No lesson implementation is approved by this review.

### Findings that change the teaching proposal

1. Numeric stream output is an implicit prerequisite in the candidates: programme-minimal and premiers-affichages teach text literals, not integer-variable output. Add a short explicit reading bridge before the first program: cout receives the current integer value without quotes; the following newline is a separate write. Explain using the existing candidate lines and their UML actions, not a new unreviewed program. Retain the exact final-value output because messages alone do not demonstrate the update.
2. Stored bool freshness is already taught by premiere-comparaison's recalculation case and premiers-booleens. Add a direct refresher link and an explicit pre-operation label in state tables. Do not pretend can_add describes available space after the operation. A direct condition is a legitimate simpler alternative, not unsafe or intrinsically premature.
3. The original alternative C bundled direct conditions with repeated attempts, unfairly conflating two teaching choices. Compare a single direct condition independently. It yields the same result as the named bool here because no state changes between calculation and use. Its advantage is one fewer stored value; its cost is changing the established presentation while introducing conditional mutation.
4. Revise the teaching order to room, full, box transfer, inclusive error, then already-above as an explicit scope-limit section. This consolidates normal operation before the anomalous initial state. All five existing programs and four models are retained; no new example behavior is introduced.
5. Use a precise title such as “Control one increment with a limit”, rather than implying a globally valid final state for any starting input. The contract preserves an existing valid upper bound; it does not sanitize arbitrary inputs. Do not make limit-wide safety or hardware-capacity claims.

### Refined alternatives and sensitivity

Weights now explicitly isolate missing prerequisites and misconception risk: continuity 30%, contract clarity 30%, reading load 25%, transfer 15%. Scores /5 remain subjective.

| Option | Continuity | Clarity | Reading | Transfer | Weighted |
| --- | --- | --- | --- | --- | --- |
| A: named bool, output bridge, reordered five cases | 5 | 5 | 4 | 5 | 4.75 |
| B: same scope, single direct condition, output bridge | 4 | 5 | 5 | 5 | 4.70 |
| C: separate output micro-lesson before conditional mutation | 5 | 5 | 3 | 4 | 4.40 |
| D: message-only threshold consolidation | 5 | 3 | 5 | 3 | 4.10 |
| E: direct conditions plus repeated attempts | 3 | 4 | 2 | 5 | 3.35 |

A and B are effectively tied given subjective scoring. A is recommended specifically for continuity with the owner's approved named-bool sequence, not numerical certainty. Moving 10 percentage points from continuity to reading load reverses their order. Choose B if eliminating the stored snapshot is more useful than preserving the previous presentation. C is appropriate if numeric output itself is difficult; D if if/else remains difficult. No evidence currently establishes either learner difficulty. E remains deferred because repeated attempts require a new decision each time.

### Additional evidence

The C++ working draft condition grammar permits an expression directly: https://eel.is/c++draft/stmt.pre. Assignment modifies the designated object: https://eel.is/c++draft/expr.assign. LearnCpp's introduction to if statements shows direct conditions early (https://www.learncpp.com/cpp-tutorial/introduction-to-if-statements/); this establishes a viable curriculum alternative, not measured superiority for this learner.

An independent temporary C++17 verification compared named and direct forms for all 0..20 supplied counts at limits 3 and 8: 42 cases passed. It checked equal final counts, preservation of initially valid upper bounds, preservation of already excessive counts and the stored pre-operation bool. This harness is engineering verification, not an additional learner-facing loop example. Language semantics confidence is high; relative learning effectiveness is unmeasured.
