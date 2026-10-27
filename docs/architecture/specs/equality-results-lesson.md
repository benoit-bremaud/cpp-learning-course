# Equality results - focused lesson conception

Status: option A (455/500), weights35/30/20/15 and concrete file plan explicitly approved by the owner on2026-10-27. Issue: [26](https://github.com/benoit-bremaud/cpp-learning-course/issues/26). Baseline clean main5da969e7cfd56922aa4064ef7465ef373f85428c. Conception branch codex/26-equality-results-conception. The owner selected the task (B460/500), weights actual prerequisites30/continuity30/focus25/estimated maintenance15 on2026-10-27; the owner subsequently approved this concrete two-program design and local implementation plan. The separate conception delivery and its authorized merge must occur first. No push, PR, merge or deletion is authorized.

## Need, evidence and progression boundary

Teach a question with an observable answer: does a supplied count equal a target? Comparison produces a bool value. Storing that answer does not retain a live formula, subscribe to a sensor or select a branch. A later explicit assignment evaluates the comparison again.

The proposed practice catalog lists CPP-02 before full CPP-04, which also includes short-circuit evaluation. That broad dependency is not a C++ language requirement for comparing known small operands of the same int type. This narrow introductory lesson does not claim completion of CPP-04, cover mixed types/conversions or alter the practice catalog. CPP-02 remains a separate integer-width/signedness/range study. Current practice target-check also requires if; it is not newly declared ready by this lesson. Its README links unpublished comparison/if lessons; do not import that historical availability claim.

Direct prerequisite CPP-09 (its recursive CPP-01/first-program/setup prerequisites provide initialization, assignment, complete sources and output). The new page is proposed after premiers-calculs for reading order, but arithmetic is not a technical prerequisite. French title: Égal ou différent. Route /notions/egal-ou-different/. No numbered CPP-04 identity or full-module completion claim. No companion/explorer is manufactured. Practice status: complete sources can be tried in the known IDE; no dedicated equality-only laboratory is claimed published.

Verified primary C++17 source: [N4659 expr.eq](https://timsong-cpp.github.io/cppwp/n4659/expr.eq) specifies bool results for == and !=. Both operands here have type int after reading their values; no mixed signed/unsigned or numeric conversion curriculum is needed. Default bool stream formatting is a presentation rule, not proof that bool and int are the same type; [ostream arithmetic inserters](https://timsong-cpp.github.io/cppwp/n4659/ostream.inserters.arithmetic) dispatch bool formatting. Stored true/false, printed1/0 and successful process status0 are distinct concepts. No boolalpha manipulator is introduced. No claim that a false comparison means less-than: both count2 and count4 differ from target3.

No if/else, loop, logical operator/short circuit, ordering operator, input, sensor, arithmetic, helper, floating point, unsigned type or overflow example. No side-effecting assignment inside a comparison is taught. All executable integer values are safe small initialized int values.

## Concrete design alternatives

The task selection above is separate from this source-inventory choice. Owner-approved weights: evidence35, reading focus30, continuity20, estimated maintenance15; sum100. Scores0..5 are editorial judgments, not measured learning gains.

- A: two complete programs: paired equality/inequality observations, then a stored snapshot and explicit reevaluation.
- B: one paired-comparison complete program; snapshot semantics explained only in prose, deferred executable contrast.
- C: three complete programs: paired comparison, stale stored-result contrast, repaired explicit reevaluation.

| Criterion | Weight | A | B | C |
| --- | ---: | --- | --- | --- |
| Direct reproducible evidence |35|5: both operators and storage/recalculation observed|4: storage boundary only prose|5: separate actual/repaired storage files|
| Reading focus |30|4: second program introduces only known assignment on a bool|5: shortest one-source introduction|3: third wrapper and repeated source split the explanation|
| Continuity toward future conditions |20|5: condition value and reevaluation already distinguished|4: future if/while must introduce reevaluation distinction|5: same distinction with explicit contrast|
| Estimated maintenance |15|4: two fixed success contracts/models|5: one contract/model|3: three contracts/models and repeated mapping|
| Total |100|455/500|445/500|410/500|

A vs B: A makes the non-live stored result observable now; B reduces source length. Ten points is a narrow judgment, not empirical superiority. Transfer5 weight points evidence->focus: A450/B450 tie. Transfer10: A445/B455. A vs C: A observes unchanged and recomputed answers in the same run, without a third source; C permits separate copying of faulty and repaired examples. Owner-approved winner A455, fallback B445; activating B removes the second source/model and requires a revised file plan and owner approval. The owner approved A and these weights on2026-10-27; B/C are not selected.

## Approved A source contracts

These are conception studies, not published teaching excerpts. Implementation must extract the actual lesson page rather than copy fixtures. Marker and card keys below are unique. Every source independently compiles strict C++17, has closed stdin and bounded execution, exact stdout, empty stderr and exit0.

### Paired comparison

Key program-equality-pair; exact stdout b'1\n0\n'. Five actions map nine statements: initial target/count2; equality1; inequality1; observe both4; return1. Both comparisons are evaluated when their initializers execute; no branch is selected. Count3 equals target3; equal true/different false. Count2 and count4 variations both yield b'0\n1\n'.

```cpp
#include <iostream>

int main() {
    const int measurement_target = 3;
    int measurement_count = 3;
    bool target_matched = measurement_count == measurement_target;
    bool target_different = measurement_count != measurement_target;
    std::cout << target_matched;
    std::cout << "\n";
    std::cout << target_different;
    std::cout << "\n";
    return 0;
}
```

[ACT-equality-pair](../diagrams/equality-results/07-activity-equality-pair.md).

### Stored result and explicit reevaluation

Key program-equality-snapshot; exact stdout b'1\n1\n0\n'. Eight actions map twelve statements: initial target/count2; compute bool1; observe2; replace count1; observe2; recompute/assign bool1; observe2; return1. After count becomes2, target_matched remains true until the explicit assignment evaluates equality again. Every result belongs to a specific evaluation moment; displaying it does not update it.

```cpp
#include <iostream>

int main() {
    const int measurement_target = 3;
    int measurement_count = 3;
    bool target_matched = measurement_count == measurement_target;
    std::cout << target_matched;
    std::cout << "\n";
    measurement_count = 2;
    std::cout << target_matched;
    std::cout << "\n";
    target_matched = measurement_count == measurement_target;
    std::cout << target_matched;
    std::cout << "\n";
    return 0;
}
```

[ACT-equality-snapshot](../diagrams/equality-results/07-activity-equality-snapshot.md). The middle1 is legal expected behavior of a stored result, not a faulty comparison or a compiler rejection. Do not label the model a branching decision or call the first stored answer continuously current.

## Approved French reading sequence

1. State the target3/count3 question; predict equal true and different false. Recall assignment versus initialization.
2. Explain bool with true/false and default output1/0, separately from return0. Read the first sequential model, complete source, immediate card and actual two-line result.
3. Distinguish = (initialize/assign in these declarations/statements), == (compare equality) and != (compare inequality). No truth-by-assignment example is executed in the lesson.
4. Value table for count2/3/4 against target3: equal false/true/false, different true/false/true. Less-than is not inferred from inequality. Values describe separate supplied cases, not events or a loop.
5. Predict three observations of a stored answer around the known literal count replacement. Read the second model/source/card and exact1/1/0 result with an ordered twelve-statement/value trace. The final assignment recomputes explicitly; no automatic formula is stored.
6. Retrieval questions: why middle1, what caused final0, does false stop the program, why both2 and4 differ, how does printed0 differ from exit0? State that branch selection comes later; no if implementation is implied.
7. Honest practice/catalog status, direct prerequisite link and known IDE use. No empty explorer or claim that target-check practice is fully supported.

Reuse observable-values HTML tables, existing native details/cards,80ms delay/160ms fade and zero duration under reduced motion. Full-width white diagram paper, natural centered sizes shrinking to fit, French16px labels. Each immediate card maps every body statement in exact order. A tall snapshot model can scroll in the existing card; measure320px,200% text, keyboard/close/focus before publication. No shared CSS/component/script/schema change is proposed.

## Approved file plan and separate delivery

Conception delivery only: this specification; two07-activity-equality-* triplets; scoped glossary additions and REQ17..24/NFR9..12 matrix extension. Review/smoke evidence after conception approval. Do not publish source/card/navigation/test/public assets in this first documentation PR; Refs26. All publication and merge approvals remain separate.

After explicit owner approval and separately authorized conception merge, branch codex/26-equality-results-lesson from updated main:

| File | Responsibility |
| --- | --- |
| src/content/docs/notions/egal-ou-different.md | New focused French page; two marked complete sources, immediate cards, actual observations, tables/traces, stored-result boundary, no CPP-04 completion claim |
| src/content/docs/notions/premiers-calculs.md | Append next link only; preserve both prior source contracts |
| src/content/docs/index.md and parcours.md | Seven available introductions and equality link, preserve all earlier availability/prerequisites |
| astro.config.mjs | Append existing-pattern sidebar entry after premiers-calculs, no deployment/runtime mechanism change |
| public/diagrams/examples/program-equality-pair.svg and program-equality-snapshot.svg | Exact authoritative generated snapshots |
| tests/program-output.py | Add fixed equality-results two-success mode, exact9/12-statement intent and wrappers; retain all four earlier modes, diagnostics, public API, flags/timeouts/provenance; no generic runner/registry |
| tests/equality-results.test.mjs | Actual-source contracts, both operator truth values via safe2/3/4 variations, snapshot moment/reevaluation tests, fixed inventory and source-intent mutants, exact ordered mappings and honest navigation/catalog scope |
| tests/explorer-content.test.mjs | Preserve10 provenance pairs, add2 for12 |
| tests/explorer-browser.py and browser-coverage.mjs | New page identities, mapping row counts6/9 including headers, geometry, keyboard/focus, reload, native/no-JS fallback,320/390/768/1440, theme/motion,200% text, next/prev/search/original SVG links; retain all existing guards and floors |
| tests/arithmetic-update.test.mjs and ordered-output.test.mjs | Only existing global teaching-fence/availability assertions17->19 and six->seven; preserve earlier source/mutation/behavior assertions |
| docs/architecture/specs/inline-uml-panels.md and docs/architecture/README.md | Two associations and accepted conception/model links,17->19 teaching fences |
| README.md | Seven introductions,12 complete successes +1 complete rejection +6 fragments; fixed CLI mode and accurate runner inventory |
| docs/reviews/equality-results/implementation.md | Full structured review, metrics and owner dispositions |
| docs/architecture/qa/<date>-equality-results.md and inspected screenshots | Routine delivery QA, inspector/security applicability; comprehensive campaign remains deferred |

No change to constant-limit.py, example-code.py, generic UML panel test, shared runtime scripts/components/CSS, schema, companions, dependencies, lockfile, workflow, practice repository or its proposed catalog. Prior source inventories/contracts and historical branch remain preserved. No new pattern, abstraction, API, browser compiler or helper function is warranted.

## Acceptance and stable IDs

REQ-17: focused same-int ==/!=, bool value, direct CPP-09 prerequisite, no excluded syntax/concepts above; no CPP-04 completion claim.
REQ-18: exactly two complete marked sources in order, corresponding immediate keys, correct default output1/0 and1/1/0, independent successful execution.
REQ-19: actual authored sources compile GCC C++17 Wall/Wextra/Werror/pedantic-errors; closed stdin/timeouts, exact stdout/empty stderr/exit0. Safe primary count2/3/4 variations prove both operators; no undefined/uninitialized execution. Test-only truth probes extract the authored primary and replace only its count initializer with2 or4, compiling against independent fixed expected0/1 bytes. They do not relax the baseline harness or accept expectations from a fixture.
REQ-20: literal true/false, fixed output, replacing == with =, != with == or deleting/reordering evaluation cannot fake source intent even if one output happens to match. Preserve default bool stream formatting; no boolalpha state introduced.
REQ-21: ACT-equality-pair five actions/nine statements and ACT-equality-snapshot eight/twelve, ordered exhaustive maps; initial target/count grouped, observations grouped, comparison is an action without decision diamonds.
REQ-22: stored snapshot remains unchanged after count assignment; explicit reevaluation changes it. false, printed0 and exit0 distinct; not-equal does not mean below; no autonomous/hardware behavior.
REQ-23: seven available intros and honest practice/catalog/prerequisite links; no completed CPP-04 or ready target-check claim; old identities preserved.
REQ-24: safe mutants cover wrong operator/operand/initial value/fixed result/fake output, stale/moved/missing reevaluation, changed output/newline/stderr/status, missing/wrong/duplicate marker, extra fence/incomplete source; prior68 probes retained.
NFR-9: deterministic formal renders, exact public snapshots, natural centered full-width white paper,16px labels, exhaustive mappings.
NFR-10: full check/build/tests, runtime coverage>=80% target100, public docs>=90%, exact-head Sonar and Gitleaks full reachable history/exact snapshot.
NFR-11: routine production QA/inspector/security applicability, three engines, accessibility and screenshots; no inherited SEC-01 waiver; comprehensive campaign deferred.
NFR-12: owner approval before implementation, separate conception delivery/merge, explicit push/PR/merge/deletion/external messages; no Copilot.

IDs17..24 and9..12 are next free in the normalized registry, approved in this conception; earlier scoped IDs remain unchanged. Implementation verification remains future work.

## Four-pass proportional review

Requirements: two distinct questions (operator answer, then result evaluation time) serve the one stored-comparison-result objective. Real observations expose the snapshot trap without introducing a branch.3equal and2/4unequal separate exact match from ordering; output intent is checked independently from bytes.

Dependencies/SOLID: authored static page/model feeds the existing builder; tests consume actual sources. Same-int bounded domain avoids conversions and representation internals. No new layers, service, persistence or network dependency.

KISS/YAGNI/DRY: repeat known wrapper for independent copying, reuse existing fixed-success runner and HTML table styling, no helper/registry/pattern. The existing reader architecture already supports both ordinary comparison and taller snapshot cards.

Anti-patterns: comparison diamond without if, conflating =/==, bool/int equivalence inferred from printed1/0, assuming false means below, implicit live formula, matching bytes via fixed booleans, full catalog module claimed from a narrow intro, stale practice links and tall clipped maps. Explicit semantics, fixed intent/truth cases, honest scope and measured layout are proposed controls. No empirical learning claim.

## Conception study evidence - not lesson delivery validation

On2026-10-27 both proposed actual source studies compiled/executed under GCC15.2.0 strict C++17 flags with exact1/0 and1/1/0 outputs, empty stderr and exit0. Primary count2 and4 variants each produced0/1. No overflowing or uninitialized case ran. Temporary source studies are in /tmp/cpp26-conception-study; they are not a published lesson or final automated tests.

Headless authoritative PlantUML renders are285x500 (pair) and285x729 (snapshot), French16px labels. Both PNGs were visually inspected: all actions and initial/final nodes legible without clipping. No decision diamond is present. Responsive card/200% text and final public-snapshot proofs remain implementation gates; a natural285px model shrinks on a narrow panel, never enlarges. The documentation delivery records its fresh routine gates separately; these studies do not claim future published-lesson extraction or responsive validation.
