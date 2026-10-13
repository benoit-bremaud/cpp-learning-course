# Exact equality and difference

Status: option A approved by the owner on 2026-10-13; implemented and verified locally; evidence is recorded in docs/validation.md.

## Need and acceptance criteria

After relational comparisons, teach two distinct built-in integer questions: exactly equal, and different. Start with equality where the pair is true/false, then lower and higher values where both cases give false/true. Inequality says nothing about direction or numerical distance. The last two examples transfer exact matching to an identifier and diagnose using >= where == was required.

Use independent four-line snippets inside main. All supplied values are int in 0..20, no mixed types, acquisition, output, branch or hardware action. measurement_target replaces measurement_limit deliberately: the requirement is now an exact target, not an acceptable upper bound. Explain that name change before the first example. Computing either bool leaves both inputs unchanged. On these integers the correct pair always contains one true and one false, but neither stored variable is automatically linked to the other.

Explain == and != as single two-character operators. != is not subtraction and does not introduce standalone !. In bool target_matched = measurement_count == measurement_target, the first = initializes the result and == compares the two inputs. Contrast with previously learned standalone assignment in prose, linking the variable lesson. Do not demonstrate assignment inside a bool initializer/condition: that would add assignment-expression values and integer-to-bool conversion before their prerequisites. Do not claim such code always fails compilation.

## Proposed examples

### equal

Result pair: true / false.

```cpp
const int measurement_target = 3;
int measurement_count = 3;
bool target_matched = measurement_count == measurement_target;
bool target_different = measurement_count != measurement_target;
```

### below

Result pair: false / true.

```cpp
const int measurement_target = 3;
int measurement_count = 2;
bool target_matched = measurement_count == measurement_target;
bool target_different = measurement_count != measurement_target;
```

### above

Result pair: false / true.

```cpp
const int measurement_target = 3;
int measurement_count = 4;
bool target_matched = measurement_count == measurement_target;
bool target_different = measurement_count != measurement_target;
```

### identifier

Result pair: false / true.

```cpp
const int expected_identifier = 7;
int observed_identifier = 9;
bool identifier_matched = observed_identifier == expected_identifier;
bool identifier_different = observed_identifier != expected_identifier;
```

### threshold

Result pair: true / true; expected false / true.

```cpp
const int measurement_target = 3;
int measurement_count = 4;
bool target_matched = measurement_count >= measurement_target;
bool target_different = measurement_count != measurement_target;
```

## Teaching order and traceability

| Example | Model | Distinct purpose |
| --- | --- | --- |
| equal | 01-activity-equal | Exact target; distinguish initialization = from comparison == |
| below | 02-activity-below | Different includes lower values |
| above | 03-activity-above | Different also includes higher values; != is not > |
| identifier | 04-activity-identifier | An integer identifier is a label, not a quantity where higher is better |
| threshold | 03-activity-above, intended behavior only | >= accepts an excess where exact matching must reject it |

The identifier is a supplied fictional number, not proof that a device was detected or authenticated. Compare 5/7/9 in a small table: only 7 matches. Do not introduce protocols, characters, strings or enum syntax. Real device identifiers may use other representations; this example is explicitly about integer labels.

The wrong threshold example preserves the exact-target requirement, with obtained true/true versus expected false/true. Its card labels the intended model versus actual execution. Correct only >= to ==. Values 2 and 3 mask the replacement, while 4 exposes it; test all three and explain why this differs from the preceding strict/inclusive error at equality. Do not claim every pair of separately stored bools is always complementary: this statement concerns the two correctly evaluated integer expressions with the same unchanged inputs.

Every excerpt states requirements and expected result before conception and code, includes a compact existing UML card, exact name/action mapping and four-instruction value trace. Model evaluation and storage sequentially without fictional decision diamonds or temporary variables. Explain symbols fully only on the first example. Prediction prompts are plain reading text, not interactive assessment. Show the primary intended diagram before code or explicitly refer back to its earlier visible study for the deliberate discrepancy.

A final compact recap contrasts ==, != and >= for 2/3/4 against target 3; do not repeat a large six-operator catalog. Equality on these exact ints must not be generalized to approximate physical measurements, floating-point tolerance, pointer identity or overloaded operators. These topics remain deferred. Next teaching step: if/else, subject to its own design approval.

## Implementation files after approval

- src/content/docs/notions/egal-ou-different.md: five examples, four authoritative models, five cards and traces.
- public/diagrams/examples/equality-{equal,below,above,identifier}.svg: copies of authoritative generated snapshots.
- Update previous lesson next link, sidebar, parcours.md, index.md and README.md counts/test command.
- tests/equality-comparisons.py: actual snippet extraction, all checkpoints, bool result/expression types, unchanged inputs, silent C++17 execution with -Wall -Wextra -Werror; alternate counts 0/2/3/4/20, identifier values 5/7/9, and >= substitution masking/exposure. Check SVG provenance.
- Browser coverage: five cards at 1440/390/320px, no-JS reading, explicit discrepancy text, transfer mobile screenshot and overflow. Astro check/build/Node checks; validation evidence in docs/validation.md.
- No shared UI, deployment, practice repository, quiz or download changes. Companion explorer sheets remain an authoring gap, with no empty control.

## Four-pass conception review

1. Requirements: equality-first makes the new predicate's true case visible immediately. Both directions of difference defeat confusing != with >. The identifier requires exact selection rather than mere renamed threshold vocabulary. The >= discrepancy uses already-known syntax.
2. Dependencies/SOLID: only existing declarations, ints, const and bool are prerequisites. UI uses current reader components. No new infrastructure dependencies or type conversions.
3. KISS/YAGNI/DRY: four activities cover five snippets; the deliberate error reuses its expected model. Independent four-line examples support rereading; no new abstraction or unnecessary six-operator repetition.
4. Pattern fit: none is warranted. Avoid silently introducing authentication, approximate sensor equality or live binding of stored results. Keeping == and != together exposes their contrasting answers with limited extra syntax.

## Alternatives and judgment

Editorial scores /5, not measured learning outcomes. Weights: progressivity 35%, misconception coverage/transfer 30%, readability 20%, simplicity 15%.

| Option | Progressivity | Coverage | Readability | Simplicity | Total /5 |
| --- | --- | --- | --- | --- | --- |
| A: paired exact equality/difference, five examples above | 5 | 5 | 4 | 4 | 4.65 |
| B: == alone now, != in another module | 5 | 3 | 5 | 3 | 4.10 |
| C: introduce if with == immediately | 3 | 4 | 3 | 4 | 3.45 |
| Add assignment-in-condition error now | 2 | 4 | 2 | 3 | 2.75 |

A best fits the accepted small-module, contrasted-example format. B becomes preferable if paired results are hard to read; current approval does not prove mastery. C makes behavior concrete sooner but combines expression semantics with control flow. The assignment-in-condition variant is a useful future pitfall once expression values and conditions are taught; its familiar reputation does not justify importing hidden prerequisites here. Rankings are contextual, not a demonstrated improvement in retention.

## Primary references

Consulted 2026-10-13:
- https://eel.is/c++draft/expr.eq: equality operators produce bool; equal versus unequal arithmetic values.
- https://eel.is/c++draft/dcl.init: = may appear in an initializer; it must not be described as the equality operator.

These are working-draft references, not the published C++17 edition. Proposed examples are separately compiled in C++17. Normative semantics do not prescribe the teaching order.

## Proposal verification

All five proposed snippets compile in C++17 with warnings as errors. Assertions check every initialized-value checkpoint and bool storage types; execution is silent. This verifies the proposed excerpts, not an implemented lesson or browser acceptance.

All four PlantUML sources rendered successfully. The identifier activity was visually inspected; no implementation or site content has changed.
