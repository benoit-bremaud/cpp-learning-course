# Arithmetic update - introductory lesson conception

Status: option A (455/500), weights 30/30/25/15 and concrete file plan explicitly approved by the owner on 2026-10-26. Issue: [#23](https://github.com/benoit-bremaud/cpp-learning-course/issues/23). Baseline: clean main 060c54562d2b7e0948de9cf2abb15f55e554595a. The owner selected arithmetic after completed #20 and asked to continue; the concrete local implementation plan is approved, with separate conception delivery/merge first. No push, PR, merge or deletion is authorized. A separate comprehensive QA campaign is deferred by the owner. Routine delivery gates remain required.

## Need and evidence

CPP-01 distinguishes initialization from storing a supplied total. CPP-09 observes constant and mutable objects but explicitly performs no arithmetic. The next narrow step is computing a new ordinary integer value from the current one and then assigning that result to the same object. Reuse complete main/iostream syntax and separate value/newline writes.

The nonzero baseline matters: at initial 0, both x = x + 1 and x = 1 produce 0 then 1. That experiment cannot distinguish the concepts. Initial 2 makes the observations differ: 2 then 3 versus 2 then 1. A literal assignment of 3 can still fake the arithmetic baseline, so exact stdout alone cannot prove the intended expression; source intent and a fake-result mutation are required.

Direct prerequisite CPP-01; its recursive prerequisites already supply structure and output. Published reading order may place this after CPP-09 without claiming const is a direct prerequisite. Do not label it CPP-02: the existing planning catalog reserves that ID for integer representation. Approved future route: /notions/premiers-calculs/; French title: Calculer une nouvelle valeur.

The current practice workshop-total source initializes a separate total from two tray variables. Its README refers to an addition lesson title not currently published in the course. It is context, not the dedicated self-update practice for this brick. No practice repository edit, exercise-availability claim or pinned code import is selected here. A separate sum/derived-value lesson or practice alignment can follow its own review. The new page may invite trying its complete sources in the known IDE, while stating no dedicated self-update exercise is published.

## Language contract and limits

C++17 N4659 [expr.add/3](https://timsong-cpp.github.io/cppwp/n4659/expr.add#3) defines the arithmetic sum. [expr.ass/1-2](https://timsong-cpp.github.io/cppwp/n4659/expr.ass) orders assignment after operand value computation and specifies replacement of the left-hand object by the right-hand result. Explain concretely: read 2 on the right, compute 2 + 1, then store 3 on the left. It is one instruction, not an algebraic equation and not a formula retained for automatic recomputation.

Only small initialized int values are executed. int is not an unbounded mathematical integer; range/representation and overflow require a later study; [N4659 expr/4](https://timsong-cpp.github.io/cppwp/n4659/expr#4) defines out-of-range expression behavior as undefined; no such case is executed here. No overflowing or uninitialized-read mutation is permitted. No promise of a fixed 32-bit int. No input, physical event/acquisition, automatic recount, branch, loop, helper function, compound assignment, increment operator, other arithmetic operator, numeric conversion, floating point or generic expression-precedence curriculum.

## Owner-approved weighted decision

Task order was already selected; this matrix chooses the lesson's evidence shape. Weights sum to 100, scores 0..5; maintenance/reading estimates and scores are editorial judgments, not measured effectiveness. The owner validated these weights and option A on 2026-10-26.

- A: two independently copyable complete programs: compute the next value versus replace with a supplied literal, same nonzero start 2.
- B: one complete arithmetic-update program, referring in prose/inline syntax to CPP-01's known literal assignment, without a second complete contrast file.
- C: one complete program performing two explicit additions, output 2/3/4; literal replacement remains an inline comparison.

| Criterion | Weight | A | B | C |
| --- | ---: | --- | --- | --- |
| Observable distinction and reproducible evidence | 30 | 5: each competing operation has its own whole file and different output | 4: new operation direct; replacement comparison reconstructed from prior lesson | 5: two explicit updates distinguish the running value from a fixed result |
| Reading focus | 30 | 4: repeats known wrapper, keeps one direct contrast | 5: one concise program | 3: repeated updates add a third observation before the base contrast is settled |
| Continuity with the prior supplied-total story | 25 | 5: same start/output structure, only the update changes | 4: relation explained through prose and earlier source | 4: same count, but two updates shift attention toward repetition |
| Estimated proportional maintenance | 15 | 4: two small fixed success contracts and two models | 5: one contract/model | 4: one longer contract/model and update-position checks |
| Total | 100 | 455/500 | 445/500 | 400/500 |

A vs B: A exposes both outcomes without requiring the learner to reconstruct a file; B saves a repeated wrapper. The ten-point margin is narrow and weight-dependent, not decisive evidence of a learning advantage. A vs C: the two contrast sources isolate calculation versus replacement; C proves sequential updates but leaves replacement as prose. Owner-approved winner A 455, fallback B 445. Transfer 5 weight points from reproducible evidence to reading focus: A 450/B 450 tie. Transfer 10: A 445/B 455. The owner chose the explicit contrast despite that duplication and narrow margin. Activating B removes one source/card/model and changes the inventory/file plan; it requires revised review rather than silent simplification.

## Exact approved A source contracts

These are conception studies, not published lesson excerpts. Implementation must extract the actual authored page. Both sources use cpp wrap metadata and immediate unique cards. Closed stdin, bounded execution, exact stdout, empty stderr and successful status are independent contracts.

### Compute from the current value

Marker and panel: program-arithmetic-update. Required stdout: `b'2\n3\n'`; stderr empty; exit 0. Five actions and seven body statements. The single assignment action groups reading, adding and storing; each observation groups two writes.

```cpp
#include <iostream>

int main() {
    int measurement_count = 2;
    std::cout << measurement_count;
    std::cout << "\n";
    measurement_count = measurement_count + 1;
    std::cout << measurement_count;
    std::cout << "\n";
    return 0;
}
```

[ACT-arithmetic-update](../diagrams/arithmetic-update/07-activity-arithmetic-update.md) models the required behavior. Explain the right-hand read before replacement and that displaying the count is only an observation. One execution updates once; elapsed time alone triggers nothing.

### Replace with the supplied literal

Marker and panel: program-literal-replacement. Actual stdout: `b'2\n1\n'`; stderr empty; exit 0. The only source difference is the assignment. This legal contrast fails the stated add-one requirement; do not call it a compilation error or redefine required 3 as 1.

```cpp
#include <iostream>

int main() {
    int measurement_count = 2;
    std::cout << measurement_count;
    std::cout << "\n";
    measurement_count = 1;
    std::cout << measurement_count;
    std::cout << "\n";
    return 0;
}
```

[ACT-literal-replacement](../diagrams/arithmetic-update/07-activity-literal-replacement.md) models this actual contrast. Preserve the primary required model separately. No successful/failed type-checking narrative is introduced.

## Approved French reading sequence

1. Recall the prior supplied-total assignment and state the new need: start 2 and calculate one more.
2. Predict 2 then 3; read the primary activity and complete source, immediate card, exact result and chronological trace.
3. Read current value 2, compute 3, store 3: one assignment statement. Distinguish the computed value from a permanently attached formula or an algebraic equality.
4. Observe the full literal-replacement contrast 2 then 1, with its own actual model and all seven statements mapped. It is legal C++ with different behavior.
5. Explain why starting 0 masks the contrast, using a short value table rather than two more C++ fences. A fixed literal 3 matching the first baseline does not express the relation; mention this as a reasoning question without another full program.
6. Restate the boundaries: exactly one explicit update, no sensor event, no loop, known safe small int values. Defer +=, ++, other operators and full type/range study.
7. Honest IDE/practice status, retrieval questions and links to the direct prerequisite. No empty explorer or invented companion sheet.

Reuse observable-values HTML tables. Preserve 80ms card delay, 160ms fades, reduced-motion zero duration, native/no-JavaScript disclosures and dialog independence. White paper spans content width; diagrams remain centered at natural size and shrink only to fit. Use 16px French labels, source/render/public provenance, original SVG links and inspected screenshots.

## Approved files and separate delivery

Conception branch codex/23-arithmetic-update-conception may add this specification and the two activity triplets; update only needed glossary/traceability entries. Review/smoke evidence may follow owner validation. No lesson/test/navigation/public source changes in this separate conception PR; use Refs #23. Publication/merge require separate explicit authorization. Drafting or committing conception documents does not constitute owner validation.

After owner approval and separately authorized conception merge, branch codex/23-arithmetic-update-lesson from updated main:

| File | Responsibility |
| --- | --- |
| src/content/docs/notions/premiers-calculs.md | New focused French page, two marked complete sources, immediate keys, two actual models, exact outputs, source/value trace, retrieval and honest practice status |
| src/content/docs/notions/cpp-09.md | Append next-lesson link only; retain all three existing sources/cards/contracts |
| src/content/docs/parcours.md | Six available introductory steps, new arithmetic row/link, keep other topics planned |
| src/content/docs/index.md | Correct the old availability sentence while adding this sixth introduction; no broader home redesign |
| astro.config.mjs | Append new existing-pattern sidebar entry after CPP-09; no runtime/deployment configuration changes |
| public/diagrams/examples/program-arithmetic-update.svg and program-literal-replacement.svg | Exact generated snapshots from the two reviewed activities |
| tests/program-output.py | Add fixed arithmetic-update success mode and two contracts; derive marker diagnostic from expected keys rather than assuming a count of 2 means Ready/Silent; preserve all current diagnostic strings, public first-program function/API, existing modes/inventories/flags/timeouts/provenance; add exact seven-statement source intent for both new keys |
| tests/arithmetic-update.test.mjs | Actual-source execution, meaningful mutants, exact mapping/inventory/progression assertions; no copied primary-source fixture |
| tests/explorer-content.test.mjs | Existing eight provenance pairs preserved, two added for ten |
| tests/explorer-browser.py and tests/browser-coverage.mjs | New two-card page, identities and six rows incl header, keyboard/dismissal/focus, natural diagrams, narrow/tablet/theme/motion/reflow/200%, native fallbacks and navigation; keep existing guards/floors |
| docs/architecture/specs/inline-uml-panels.md | Two added mappings, fifteen teaching fences become seventeen |
| docs/architecture/README.md | Link accepted specification and both current activities |
| README.md | Six intros, ten executable successes plus one complete rejected source and six fragments; CLI validation entry |
| docs/reviews/arithmetic-update/implementation.md | Structured review, measured gates, owner dispositions and limits |
| docs/architecture/qa/<date>-arithmetic-update.md and inspected screenshots | Proportionate delivery QA evidence; separate comprehensive campaign stays deferred |

No edits to tests/constant-limit.py, tests/example-code.py, companion sheets, content schema, shared CSS, components/scripts, dependencies, lockfile, workflow or the practice repository. Existing tests/uml-panels.test.mjs already walks all fences generically; retain it unchanged. No new generic runner/registry or design pattern is justified: this is another fixed all-success lesson, unlike CPP-09's mixed rejection contract. A adds two executable sources to eight, retains the one complete rejected source and all six fragments. Total 17 teaching fences and 6 introductory pages; existing routes retain their identities. This does not complete the catalog's CPP-02 or introduce a new numbered catalog entry.

## Acceptance and stable traceability

REQ-9: one central new operation, small int plus 1 from current value, direct prerequisite CPP-01, no prohibited syntax/concept family above.
REQ-10: exactly two complete marked A sources in order; before/after observations 2/3 and 2/1; copied wrappers compile independently.
REQ-11: C++17 Wall/Wextra/Werror/pedantic-errors, closed stdin, timeout, exact stdout, empty stderr, exit 0 for both actual authored sources.
REQ-12: exact source intent preserves the old-value read and addition. Reject literal 3/fake outputs even when baseline stdout matches; no undefined/uninitialized mutation.
REQ-13: five conceptual actions map all seven statements in order per source; computation/storage belong to one update action, not separate invented instructions.
REQ-14: the literal contrast is legal actual behavior against required 3, never a compiler rejection. No event, formula retention or arithmetic during output is implied.
REQ-15: navigation/availability reflects six intros and new route, catalog CPP-02 reserved, existing prerequisites/routes preserved; dedicated practice not claimed.
REQ-16: fixed-inventory/source/output mutants cover missing/wrong/duplicate marker, extra fence, wrong initial value, missing/moved/wrong assignment, replacement/calculation swap, fake literal 3, fake observations, quoted name, newline, stderr and status; preserve current contracts.
NFR-5: deterministic authoritative diagrams, exact public snapshots, full-width white paper, intrinsic centered 16px labels, statement/card mappings.
NFR-6: full existing tests/build/check, runtime line floor 80% and public documentation >=90%, fresh exact-head Sonar and reachable-history/snapshot Gitleaks.
NFR-7: proportionate production delivery QA/inspector/security applicability, keyboard, Chrome/Firefox/WebKit, responsive/theme/motion and fallbacks; no silently inherited SEC-01 waiver; the separate comprehensive campaign remains deferred.
NFR-8: owner validation before implementation; separate conception PR/merge; explicit publication, merge, deletion and external-message approvals; no Copilot.

The next free normalized requirement IDs are 9..16 and NFR 5..8; earlier scoped IDs and REQ-1..8/NFR-1..4 remain unchanged. Central matrix rows cite these new IDs and both ACT realizations; they are proposed verification, not implemented coverage.

## Four-pass proportional review

Requirements: nonzero baseline distinguishes the intended relation; literal 3 still exposes black-box limits. Both concepts use known assignment/output syntax and just one new operator. The alternative may be longer without being a new central concept; the owner accepted that reading cost through the close MCDA.

Dependencies/SOLID: authored static page/model feeds the existing build. Existing fixed all-success harness consumes the actual page; no new domain/framework or network dependency. The practice sum is kept as contextual evidence without conflating initial derived totals and updates.

KISS/YAGNI/DRY: a little whole-file repetition makes contrast independently reproducible. Reuse the existing success harness and table layout. No helper, browser compiler, new explorer, framework registry or pattern has a present force.

Anti-pattern risks: zero baseline hiding distinct operations, fixed-result fake success, algebraic-equality framing, autonomous recount/event language, signed overflow, false practice publication, stale counts/navigation and marker identity inferred solely from cardinality. Exact fixed intent, safe mutants, actual outputs, qualified story and updated inventory address these. Full user-research or comprehensive site-audit claims are deferred.

## Conception study evidence

Temporary sources compiled/executed on 2026-10-26 with GCC 15.2.0 under the strict flags above. A's two sources produce 2\n3\n and 2\n1\n. C's two-update alternative produces 2\n3\n4\n. Starting 0 makes both operations produce 0\n1\n. Replacing the arithmetic expression with literal 3 still produces 2\n3\n. All successful studies have empty stderr/status 0. These demonstrate consequences, not learner effectiveness or implemented future lesson tests. Both models were rendered in Java headless mode, with French 16px labels; natural sizes are 235x544 (update) and 225x522 (replacement). Fresh SVG output matches the authoritative renders. Both PNG previews were visually inspected; all five actions and initial/final nodes are readable without clipping. No public snapshot or lesson is changed by these studies.
