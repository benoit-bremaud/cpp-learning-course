# Below a limit versus at most the limit

Status: conception proposal; owner implementation approval pending.

## Need and acceptance criteria

Continue after strict/inclusive greater-than comparisons. Teach reading < and <= from left to right, including equality, without control flow. The learner should distinguish a count strictly below a maximum from one that does not exceed it, and transfer that distinction to a full box.

Five independent four-line excerpts inside main. All data are supplied int values, counts in 0..20, positive limits in 1..20. These are stated preconditions, not checks performed by the code. Both comparisons produce bool; inputs remain unchanged. within_limit refers only to the upper bound under the nonnegative-count assumption, never a complete validation of an arbitrary input. has_space refers to room for ONE same-size item in the simplified count-capacity model, not physical geometry, weight or permission to insert.

No if, equality operators, logic operators, numeric conversions, arrays, hardware IO or new UI. No performance claim or forced design pattern. <= is one comparison operator, not a comparison followed by assignment. In declarations, = initializes the bool with the computed answer.

## Proposed excerpts

### below

Result pair: true / true.

```cpp
const int measurement_limit = 3;
int measurement_count = 2;
bool below_limit = measurement_count < measurement_limit;
bool within_limit = measurement_count <= measurement_limit;
```

### equal

Result pair: false / true.

```cpp
const int measurement_limit = 3;
int measurement_count = 3;
bool below_limit = measurement_count < measurement_limit;
bool within_limit = measurement_count <= measurement_limit;
```

### above

Result pair: false / false.

```cpp
const int measurement_limit = 3;
int measurement_count = 4;
bool below_limit = measurement_count < measurement_limit;
bool within_limit = measurement_count <= measurement_limit;
```

### reversed

Result pair: false / true (expected true / true).

```cpp
const int measurement_limit = 3;
int measurement_count = 2;
bool below_limit = measurement_limit < measurement_count;
bool within_limit = measurement_count <= measurement_limit;
```

### capacity

Result pair: false / true.

```cpp
const int box_capacity = 8;
int item_count = 8;
bool has_space = item_count < box_capacity;
bool within_capacity = item_count <= box_capacity;
```

## Learning contributions and traceability

| Example | Model | Contribution |
| --- | --- | --- |
| below | 01-activity-below | Read both questions with count 2 and maximum 3 |
| equal | 02-activity-equal | A reached maximum is still respected; only <= is true |
| above | 03-activity-above | Both false; computing false does not reduce or stop the count |
| reversed | 01-activity-below, expected only | Same operator with reversed operands answers a different question |
| capacity | 04-activity-capacity | A full box has no room for another item but still respects capacity |

The reversed example deliberately contradicts its requirement. Its card must say expected true/true versus actual false/true, and state that the diagram models intended behavior. Correct the first expression to measurement_count < measurement_limit. Also explain the valid equivalent measurement_limit > measurement_count in prose: swapping operands AND reversing the operator preserves the question. Do not teach that the constant must always be on the right. At equality both operand orders with < are false, so equality alone masks this error.

The capacity transfer is more than renamed variables: has_space is false while within_capacity is true, so respecting capacity is insufficient to conclude that another item fits. Supplied count 9 describes an excessive recorded count in an independent hypothetical case, not an insertion performed by these four lines. A small table at 7/8/9 will support transfer without inflating code blocks. No historical latch or physical sensing is implied.

Each example states the question and expected result, shows conception before code, has a discreet existing UML card, maps each action to its declaration, and traces all four instructions. Mark variables not yet created before their declarations. First result remains unchanged when computing the second. Sequential evaluation/storage actions describe one declaration, not invented temporary variables. No decision diamonds: the program computes answers and does not choose paths.

A compact final table may align >, >=, <, <= at 2/3/4 with a fixed maximum 3. Label it as a recap, not another example. Scope claims to these same-type integer inputs; do not generalize complements to floating-point NaN. Questions ask readers to explain equality, operand order, full-box capacity and lack of enforcement. The next separate module will address equality/inequality before conditions.

## Files and verification after approval

- Add src/content/docs/notions/en-dessous-ou-au-maximum.md and four public/diagrams/examples/lower-*.svg snapshots.
- Reuse existing card scripts/styles with no UI change.
- Update astro.config.mjs sidebar, previous lesson's next link, parcours.md, index.md and README.md availability/test command.
- Add tests/lower-comparisons.py: extract actual snippets, check every initialized-value checkpoint, bool types, unchanged inputs, silent execution, and public/source SVG identity. Compile C++17 with -Wall -Wextra -Werror.
- Reuse actual expressions at counts 0/2/3/4/20 and item counts 7/8/9 to check boundary behavior and reversed-operand masking; verify the equivalent swapped > expression separately.
- Extend tests/explorer-browser.py for five cards at 1440/390/320px, the discrepancy text, no-JS disclosures, page overflow and visual inspection of the transfer card.
- Run Astro check, build, Node tests and focused C++/browser checks; record evidence in docs/validation.md. Local commit, no deployment or practice repository change.

## Four-pass conception review

1. Requirements and traceability: all three boundary positions, one directional error and one transfer misconception have distinct purposes. Retain many examples without repeating both substitution errors from the prior module. Teach two closely related operators using the already-established strict/inclusive distinction.
2. Dependencies/SOLID: content uses existing rendering and card mechanisms. Pure integer examples depend only on established declarations and bool. No infrastructure or framework teaching enters the lesson.
3. KISS/YAGNI/DRY: four authoritative activities serve five examples; the deliberate discrepancy reuses the intended model. Four-line repetition supports independent reading. No abstraction, new modal or additional persistence.
4. Pattern fit and anti-patterns: no recognized pattern is justified. Avoid claim that every new operator warrants an otherwise identical standalone page; the pair forms one coherent contrast. Explicit domain assumptions prevent within_capacity from masquerading as general validation or physical safety.

## Alternatives and weighted judgment

Scores /5 are editorial judgments, not measured learner comprehension. Weights: progressivity 35%, conceptual transfer 30%, readability 20%, simplicity 15%.

| Option | Progressivity | Transfer | Readability | Simplicity | Weighted /5 |
| --- | --- | --- | --- | --- | --- |
| A: paired < and <=, five examples above | 5 | 5 | 4 | 4 | 4.65 |
| B: < alone, <= in another module | 5 | 3 | 5 | 3 | 4.10 |
| C: all four remaining comparisons together | 2 | 4 | 2 | 4 | 2.90 |
| D: conditions now, remaining comparisons later | 3 | 4 | 3 | 4 | 3.45 |

A best matches the owner's small but example-rich modules. B is viable if reading paired booleans proves difficult, but that format is already approved and postponing <= would fragment an established contrast. C adds the equality/assignment distinction prematurely. D gives visible branching sooner but leaves the requested comparison progression incomplete. A's advantage depends on current paired examples remaining readable; no learning outcome has been measured.

## Primary reference

https://eel.is/c++draft/expr.rel, consulted 2026-10-13: built-in relational operators return bool and compare arithmetic values. This is a working draft, not the published C++17 edition. Proposed excerpts will be compiled explicitly in C++17 mode before owner review. Normative semantics support the results; the teaching sequence is a project-specific editorial decision.

## Proposal verification

The five specification excerpts compile in C++17 with -Wall -Wextra -Werror. Assertions verify every initialized-value checkpoint, bool storage types, alternative measurement counts 0/2/3/4/20, reversed-operand behavior, equivalent swapped > expressions and transfer counts 7/8/9. Execution is silent. All four authoritative PlantUML sources render successfully; the full-box activity was visually inspected. This verifies the proposal, not an implemented lesson or browser acceptance.
