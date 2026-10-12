# First integer division: count complete kits

Status: option A approved by the owner and implemented locally; verification recorded in docs/validation.md.

## Need and scope

Given a known nonnegative stock of components and a strictly positive number of components per kit, compute how many complete kits could be made. No physical assembly, stock mutation, IO or leftover computation takes place. The quotient is an integer because both operands are int; truncation happens in the division, not merely when assigning to kit_count.

Inputs: component_count in 0..20, components_per_kit in 1..10, with four used in the worked cases. The bounds are preconditions, not enforced checks. All results are representable by int. Introduce only binary /. No %, floating-point types/conversions, negative examples, division assignment, conditionals or functions. In prose, the general integer rule is truncation toward zero; for our nonnegative inputs, the fractional part is discarded, not rounded to nearest. Do not state a general rule of rounding down for negative integers.

## Four independent proposed fragments

D1 — exact division, three complete kits:
```cpp
int component_count = 12;
int components_per_kit = 4;
int kit_count = component_count / components_per_kit;
```
Explain / as division, dividend 12 and divisor 4 using concrete roles rather than a vocabulary list. Component inputs remain unchanged. Start directly with named inputs: initialization and named operands have already been taught; a duplicate literal-only fragment is not necessary.

D2 — incomplete extra kit, still three complete kits:
```cpp
int component_count = 14;
int components_per_kit = 4;
int kit_count = component_count / components_per_kit;
```
Expected quotient three, not 3.5 and not four. Three kits would use twelve components, leaving two in the physical reasoning; no variable stores that leftover and no code computes it here. Important causal statement: integer division itself gives three. Do not imply assigning to a different destination type alone would recover the discarded fraction. A floating-point comparison will be designed later with its prerequisites.

D3 — insufficient stock for one kit:
```cpp
int component_count = 3;
int components_per_kit = 4;
int kit_count = component_count / components_per_kit;
```
Expected zero kits despite nonzero stock. Zero quotient does not imply zero components. Input stock remains three.

D4 — no stock:
```cpp
int component_count = 0;
int components_per_kit = 4;
int kit_count = component_count / components_per_kit;
```
Expected zero, with valid nonzero divisor. Explicitly distinguish a zero dividend from a zero divisor. Zero kits has different input situations in D3/D4; the quotient alone does not recover the original stock.

## Divisor validity

State before code that components_per_kit must be positive for this requirement. Include a short prose/table contrast: zero components divided into four-component kits is allowed; a zero kit size is outside the requirement and integer division by zero has undefined behavior. Explain that this means C++ guarantees no usable outcome: do not promise a compiler diagnostic, crash, exception or zero result. No runnable zero-divisor snippet, runtime experiment or successful activity branch is authored. Conditions and safe validation will follow in their module. A missing guard is an explicit teaching precondition, not silently claimed robustness for external inputs.

## UML and delivery

Four native activity diagrams, one per actual valid snippet: initialize both inputs, conceptually calculate the integer quotient and initialize kit_count. No leftover variable, stock decrement, physical assembly, or undefined-behavior trace. Final node ends the fragment, not an implicit return. Four code examples/cards cover four distinct questions.

Use existing UML card UI and no-JS fallback. All snippets independent inside main, with explicit absence of stdout. Show input/quotient observations; retain one new difficulty per step. No explorer without meaningful companion categories. Deferred downloads and assessments remain deferred.

## Planned implementation after approval

- src/content/docs/notions/premieres-divisions.md, four snippets and concept/model/result mappings.
- public/diagrams/examples/division-{exact,partial,insufficient,empty}.svg from authoritative PlantUML.
- astro.config.mjs, parentheses continuation, parcours.md and homepage availability count.
- tests/first-divisions.py: extract actual snippets, C++17 compile, every initialized-value checkpoint and unchanged inputs, quotient results 3/3/0/0, no output, SVG provenance. No execution with zero divisor.
- Browser route/count coverage for four normal UML cards; structural/link checks, README command and validation evidence.

## Four-pass conception review

Requirements: complete-kit contract makes truncation appropriate, not a universal desirable arithmetic outcome. Each case has a distinct purpose: exact, discarded fraction, nonzero stock yielding zero, valid zero dividend.
Dependencies: only known local ints plus /. Arithmetic inputs stay bounded and divisor positive. No new application architecture, type system, input path or interactive feature.
Simplicity: four purposeful cases, no duplicate literal baseline or remainder algorithm. Dedicated models retain exact values and names.
Pattern fit/risks: no design pattern. Explicitly prevent conflation of truncation with assignment conversion, zero stock with zero kits, undefined behavior with guaranteed rejection, and available stock with consumed stock. No physical allocation is performed.

## Alternatives and recommendation

Judgment /5, not measured learner outcomes. Weights: progressive prerequisites30%, misconception coverage30%, reading load25%, simplicity15%.
A — Complete-kit integer division only: 5,5,4,4 = 4.60.
B — Quotient and remainder operator together: 3,5,3,3 = 3.60; useful paired topic, but introduces another operator before quotient is consolidated.
C — Integer versus floating-point division immediately: 2,5,2,2 = 2.90; addresses fractional answers but adds types/conversions.
Defer division: not preferred without evidence of a previous learning gap; it postpones the next promised skill.

## Primary reference and confidence

https://eel.is/c++draft/expr.mul — integer quotient discards fractional part (toward zero), zero divisor yields undefined behavior. Public HTML working draft, not published ISO C++17. Proposed examples verified in C++17. High confidence on concrete behavior; moderate confidence on pedagogical effectiveness pending reader feedback.
