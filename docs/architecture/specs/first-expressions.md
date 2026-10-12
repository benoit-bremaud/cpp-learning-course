# First expressions: adding known integer quantities

Status: option A approved by the owner; implemented locally, validation recorded in docs/validation.md.

## Need and acceptance criteria

Continue roadmap stage 3 after initialization and assignment. The learner should distinguish a written expression, its computed value, initialization and later assignment. Use counts of components in two trays, explicitly chosen in 0..10 (sum 0..20). This is an example domain, not an input check or an int type limit. No hardware readings, looping, increments, multiplication, precedence puzzle, custom function or design pattern.

## Proposed independent snippets

E1 — literal expression:
```cpp
int component_count = 2 + 3;
```
Explain that 2 + 3 is evaluated to 5 and initializes component_count. A literal is also an expression; an expression need not contain an operator. The whole declaration is not synonymous with its initializer expression.

E2 — named operands:
```cpp
int left_tray_count = 2;
int right_tray_count = 3;
int component_count = left_tray_count + right_tray_count;
```
Trace 2, then 3, then total 5. Addition reads the operands; their stored values remain 2 and 3. Names express quantities in the same unit. No const prerequisite is necessary; retain int consistently rather than introducing a separate design question.

E3 — an empty tray:
```cpp
int left_tray_count = 0;
int right_tray_count = 3;
int component_count = left_tray_count + right_tray_count;
```
Trace 0, 3, 3. Here zero is a valid count, not missing data or an error. This is a contrasting supplementary example, not another main explanation of identical syntax.

E4 — assigning a computed result:
```cpp
int component_count = 0;
component_count = 2 + 3;
```
Trace 0 then 5. Relate to known assignment of a literal. The previous zero is replaced and does not participate in the sum. Defer component_count = component_count + 1 to the next progression step.

## UML and presentation

Four PlantUML activities, one per independent fragment. Separate calculation and storage as conceptual actions; explicitly state that these do not imply a named temporary variable, machine instruction count, or compiler operand evaluation order. The final node is the end of the fragment, not an implied return statement. The named operands are both read by one calculation action.

Use existing discreet UML buttons, cards and fade unchanged. E1, E2 and E4 in the main reading; E3 in the existing complementary-example explorer. Reuse independent-copy in its required deeper tab as an explicitly labelled optional reminder about stored values; this adds no new snippet or interaction design. Identify all snippets as fragments inside main, with no output instruction. Observed values are explanatory traces, never stdout. Explain expression, operand and operator in this order using the concrete sum. Parentheses and other operations follow in another small lesson.

## Planned implementation files and validation

- src/content/docs/notions/premieres-expressions.mdx: focused lesson and three main examples.
- src/content/examples/expressions/empty-tray.md: fourth contextual example, using the existing collection contract.
- public/diagrams/examples/: four generated snapshots from this conception.
- astro.config.mjs, parcours.md and CPP-09: navigation and availability, including removal of stale planned status for completed assignment comparisons.
- Tests: extract actual lesson examples, compile as C++17, assert each checkpoint and unchanged operands; validate all four source/SVG pairs, structural UML coverage and browser controls. Keep the site checks and existing regression suite.
- README.md and docs/validation.md: command and evidence updates after implementation.

## Four-pass review

1. Requirements/traceability: each snippet resolves a distinct question (calculation, named inputs, valid zero, replacement). Exact identifiers and values are mirrored by its own diagram.
2. Dependencies/responsibilities: requires only initialized int and assignment. No hardware framework, new application layer or IO dependency. Existing UI infrastructure suffices.
3. Simplicity: four small examples with one operator. Empty-tray variant belongs in supplementary content to avoid repetitive main prose. No general arithmetic framework or new storage schema.
4. Pattern fit and risks: no recurring design force justifies a pattern. Avoid implying automatic recalculation, operand sequencing, an actual sensor, mathematical unlimited integers, or console output. Self-update and integer limits have later dedicated steps.

## Alternatives (internal pedagogical judgment, not measured learning outcomes)

Scores /5, weighted: progressive prerequisites 40%, meaningful code coverage 30%, cognitive load 20%, implementation simplicity 10%.

- Focused addition lesson: 5, 4, 5, 5 = 4.7/5.
- All arithmetic operators and precedence together: 2, 5, 2, 4 = 3.1/5.
- Start immediately with a self-updating counter: 3, 3, 3, 5 = 3.2/5.

## References and limits

- https://www.learncpp.com/cpp-tutorial/introduction-to-expressions/ — progression from concrete values to expressions; original lesson wording, not copied.
- https://eel.is/c++draft/expr.add — built-in additive expressions.
- https://eel.is/c++draft/expr.assign — assignment semantics.

The latter two are a public HTML rendering of the current working draft, not the published ISO C++17 standard. The proposed small integer examples target C++17 and will be compiled in that mode. Compilation establishes technical behavior, not learner comprehension.
