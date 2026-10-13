# Guard one increment with an upper limit

Status: proposed; owner review required before lesson implementation.

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
