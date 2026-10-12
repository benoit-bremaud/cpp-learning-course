# Subtraction review and next learning step

## Scope and evidence

Read the complete first-subtractions lesson, its three authoritative PlantUML sources, its extraction harness and roadmap stage 3. Re-ran tests/first-subtractions.py and the five Node tests in uml-panels.test.mjs and reader.test.mjs: all pass. The latter inspect the existing local build; no source/site change was made in this review. Browser acceptance from implementation remains recorded in docs/validation.md; it was not rerun for this read-only review.

## Findings and disposition

- Must Have: none identified. The four results 7, 7, 0 and -7, retained inputs and expected-model mapping are consistent. No undefined behavior is used as a teaching device.
- Should Have: none identified within this focused scope. Preconditions are explicitly not guards; fragments are independent and do not print. S4 is language-valid but fails the stock requirement; the discrepancy card states this before its diagram.
- Nice to Have: alternative subtraction contexts could support transfer later. Deferred: the four current cases have distinct purposes, and duplicating the stock with new names would not establish transfer. No empty explorer is needed.
- Repetition review: repeated calculation/storage clarification is inside independently opened UML cards, where it supports self-contained reading. Keep it. The literal-to-named pair isolates the new operator from data naming, and the zero/reversed cases add distinct checks.

## Limits and next step

Passing compilation and browser checks does not demonstrate learner comprehension. A future learner review can examine the short explanation prompts. Downloadable summaries and interactive assessments remain deferred.

Next conception: multiplication for equal-size groups, before mixed arithmetic/grouping. A count of kits and components per kit carry different roles; multiplying them yields components. This must not be presented as indiscriminate multiplication of two stock totals. The same number per kit is a required assumption, not checked by code. See ../architecture/specs/first-multiplications.md.
