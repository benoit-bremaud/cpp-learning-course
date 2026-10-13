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

### capacity

Result pair: false / true.

```cpp
const int box_capacity = 8;
int item_count = 8;
bool has_space = item_count < box_capacity;
bool within_capacity = item_count <= box_capacity;
```

### reversed

Result pair: false / true (expected true / true).

```cpp
const int measurement_limit = 3;
int measurement_count = 2;
bool below_limit = measurement_limit < measurement_count;
bool within_limit = measurement_count <= measurement_limit;
```

## Learning contributions and traceability

| Example | Model | Contribution |
| --- | --- | --- |
| below | 01-activity-below | Read both questions with count 2 and maximum 3 |
| equal | 02-activity-equal | A reached maximum is still respected; only <= is true |
| above | 03-activity-above | Both false; computing false does not reduce or stop the count |
| capacity | 04-activity-capacity | A full box has no room for another item but still respects capacity |
| reversed | 01-activity-below, expected only | Same operator with reversed operands answers a different question |

The reversed example deliberately contradicts its requirement. Its card must say expected true/true versus actual false/true, and state that the diagram models intended behavior. Correct the first expression to measurement_count < measurement_limit. Also explain the valid equivalent measurement_limit > measurement_count in prose: swapping operands AND reversing the operator preserves the question. Do not teach that the constant must always be on the right. At equality both operand orders with < are false, so equality alone masks this error.

The capacity transfer is more than renamed variables: has_space is false while within_capacity is true, so respecting capacity is insufficient to conclude that another item fits. Supplied count 9 describes an excessive recorded count in an independent hypothetical case, not an insertion performed by these four lines. A small table at 7/8/9 will support transfer without inflating code blocks. No historical latch or physical sensing is implied.

Each example states the question and expected result, shows conception before code, has a discreet existing UML card, maps each action to its declaration, and traces all four instructions. Mark variables not yet created before their declarations. First result remains unchanged when computing the second. Sequential evaluation/storage actions describe one declaration, not invented temporary variables. No decision diamonds: the program computes answers and does not choose paths.

A compact final table will align >, >=, <, <= at 2/3/4 with a fixed maximum 3. Label it as a recap, not another example. Scope claims to these same-type integer inputs; do not generalize complements to floating-point NaN. Questions ask readers to explain equality, operand order, full-box capacity and lack of enforcement. The next separate module will address equality/inequality before conditions.

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

## Revised teaching sequence after deeper review

Proposal only: the owner requested deeper analysis, not implementation. Preserve all five verified snippets and four models, but use the order below / equal / above / capacity / reversed. Put the positive transfer before the deliberate error, then explicitly return to the original measurement context for the diagnostic example.

The first example fully explains syntax, conceptual evaluation/storage and the UML nodes. Subsequent examples still retain their own conception, card and trace for independent reading, but prose emphasizes what changed rather than repeating definitions. For equality and the box, invite a brief prediction in ordinary text before revealing the expected result; no quiz widget, score, hidden state or new interaction. Keep expected values before the diagram and code. This is a reading prompt, not the deferred assessment feature.

Three observed weaknesses in the initial proposal:

- Another complete 2/3/4 lesson risks superficial symbol memorization after > and >=. Add an explicit bridge: measurement_count < measurement_limit asks the same integer question as measurement_limit > measurement_count. Swapping only the operands changes the question; swapping both operands and direction preserves it. This is already technically present in the proposal but must be a visible teaching point, not a side remark.
- The inverted-operand bug is already taught in the strict-comparison module. Keep it as a clearly identified diagnostic reuse, not a newly discovered pitfall. Ask the learner to explain the incorrect question in words and identify both a direct correction and the equivalent reversed formulation.
- The transfer was last, after the error. Move it before the error so the learner first applies a correct model to a new requirement. This is an editorial hypothesis about clarity, not evidence from learner testing.

The box example's two answers should be linked to two explicit questions: room for one additional same-size item under the count model, and current count at most capacity. Neither bool inserts an item or prohibits insertion. The design prepares later condition lessons, but no single Boolean is a general hardware-safety or multi-item admission check. Do not introduce buffers, voltages, sensor tolerances or arrays merely to make this module appear embedded-specific.

## Alternatives and weighted judgment

Scores /5 are editorial judgments, not measured comprehension. Unchanged weights: progressivity 35%, conceptual transfer 30%, readability 20%, simplicity 15%. Wider alternatives include keeping the original design and a compact addition to the existing page.

| Option | Progressivity | Transfer | Readability | Simplicity | Weighted /5 |
| --- | --- | --- | --- | --- | --- |
| A: revised pair, positive transfer before diagnosis, explicit equivalence bridge | 5 | 5 | 4 | 4 | 4.65 |
| Original proposal unchanged | 5 | 4 | 4 | 4 | 4.35 |
| One box context throughout | 4 | 4 | 5 | 4 | 4.20 |
| B: separate < and <= modules | 5 | 3 | 5 | 3 | 4.10 |
| Compact addition to the previous page | 4 | 3 | 3 | 5 | 3.65 |
| C: conditions now, comparisons later | 3 | 4 | 3 | 4 | 3.45 |
| All four remaining comparisons together | 2 | 4 | 2 | 4 | 2.90 |

A remains the recommendation. The original proposal's transfer score is revised downward because its repeated operand error and late transfer did not justify the original maximum score. The small A/original difference does not prove superior outcomes. The practical choice rests on the explicit learning purposes and low cost of reordering, not on the numerical gap. If two-context switching proves difficult, the single-box option becomes preferable. If actual comprehension of paired bools is weak, separate modules become preferable; approval of the preceding page is not evidence of mastery.

## External comparison and limits

LearnCpp's authored relational-operator lesson presents all six operators and illustrates them with input and if statements. That establishes a viable reference-style approach, not the best prerequisites for this course: here input and conditions are deliberately not assumed. Its broader floating-point discussion must not be imported into this integer-only step. Source: https://www.learncpp.com/cpp-tutorial/relational-operators-and-floating-point-comparisons/ (consulted 2026-10-13).

Stroustrup's own PPP3 presentation emphasizes foundational concepts and practical programming, with specialized chapters available separately. That supports considering conceptual purpose beyond a symbol catalog, but does not prescribe this five-example sequence or prove this recommendation. Source: https://www.stroustrup.com/programming.html (consulted 2026-10-13). The book uses C++20/23; this course's examples remain verified in C++17.

Semantics are high-confidence for the stated integer domain, backed by the draft and compiled snippets. Teaching-order confidence is moderate: no diagnostic response or learner trial has measured mastery. No new prerequisite, code behavior, diagram, UI or implementation scope results from this refinement.

## Primary reference

https://eel.is/c++draft/expr.rel, consulted 2026-10-13: built-in relational operators return bool and compare arithmetic values. This is a working draft, not the published C++17 edition. Proposed excerpts will be compiled explicitly in C++17 mode before owner review. Normative semantics support the results; the teaching sequence is a project-specific editorial decision.

## Proposal verification

The five specification excerpts compile in C++17 with -Wall -Wextra -Werror. Assertions verify every initialized-value checkpoint, bool storage types, alternative measurement counts 0/2/3/4/20, reversed-operand behavior, equivalent swapped > expressions and transfer counts 7/8/9. Execution is silent. All four authoritative PlantUML sources render successfully; the full-box activity was visually inspected. This verifies the proposal, not an implemented lesson or browser acceptance.
