# Observable constants - CPP-09 lesson conception

Status: option A (445/500), weights 35/25/25/15 and concrete file plan explicitly approved by the owner on 2026-10-26. Issue: [#20](https://github.com/benoit-bremaud/cpp-learning-course/issues/20). Baseline: clean main 40ea5e5e267a93f4df0075eeea6cb0a650823b66. The owner selected this brick after #16 and asked to continue in the existing conversation. Selection is not implementation or publication approval. This document does not authorize push, PR creation, merge or deletion.

## Need and preserved contracts

The published CPP-01 now provides a complete program observing an integer before/after assignment. The next published page, CPP-09, retains three scoped fragments governed by [constant-limit](constant-limit.md): a constant limit 3 with count 0 then 1, forbidden direct assignment to the constant, and legal initialization to 30 contrary to the requirement. The course/practice split and optional guided reference remain authoritative.

Make these three outcomes independently verifiable without introducing arithmetic, input, conditions, loops, helper functions, hardware APIs, containers, new types, constexpr or a browser compiler. Reuse known main/iostream/output/newline syntax. Explain that reading a variable does not change it, literal assignment stores a supplied total rather than calculating an increment, and a constant does not enforce a capacity or reserve storage. No broad punctuation cleanup, dependency migration or deployment work.

The direct prerequisite remains CPP-01; its own prerequisites already establish complete-program structure. Do not add new navigation or inflate the five available introductory lessons. The main page must be understandable without a dialog. No new explorer or companion sheet is justified for this brick.

## Alternatives and owner-approved weighted decision

The earlier 460/500 selected the next task against arithmetic/comparison; the following matrix chooses its delivery shape. Scores are editorial judgments, not learning-effectiveness measurements. Maintenance estimates are marked as such. Weights total 100, scores 0..5.

- A: replace all three fragments with complete source files: two executable programs and one intentionally ill-formed compile-only case.
- B: replace only the primary fragment with a complete observed program; retain the two existing short error fragments, wrapped only by their tests.
- C: retain the primary fragment and append the observed complete program, followed by the two existing error fragments: four fenced teaching blocks.

| Criterion | Weight | A | B | C |
| --- | ---: | --- | --- | --- |
| Independently reproducible evidence | 35 | 5: each case can be copied as one translation unit | 4: primary direct, error fragments still require a wrapper | 4: complete primary, error fragments still need wrappers |
| Continuity with the new executable reading path | 25 | 5: same complete-file format for every case | 4: mixed whole-program and fragment contracts | 4: transition explained through duplicate representations |
| Focus and reading load | 25 | 4: repeated structure, one central const objective | 5: shorter counterexamples | 3: primary fragment and near-duplicate full program |
| Estimated proportional maintenance | 15 | 3: two runtime contracts plus compiler-rejection controls/models | 4: existing fragment controls retained | 2: four mappings and repeated primary content |
| Total | 100 | 445/500 | 425/500 | 345/500 |

A vs B: A permits independent compile/run-or-reject observations for every case, while B is shorter but still requires the reader to reconstruct a wrapper for the error cases. A vs C: C preserves the historical primary representation but duplicates it without adding a new outcome. Owner-approved winner A: 445/500. Fallback B: 425/500, requiring revised extraction/fragment counts, mapping scopes and owner approval before activation. It is not a drop-in variant.

Sensitivity: move 10 points from independent evidence to reading focus: A 435, B 435. Move 15: A 430, B 440. The recommendation depends on preferring independently reproducible cases over minimum page length. No observed learner result proves those weights; the owner explicitly validated these weights and option A on 2026-10-26.

## Exact proposed source contracts

These are conception studies, not published lesson excerpts. In implementation, extract and test the actual authored page, not these copies. Use the existing renderer's cpp wrap metadata for each C++ fence.

### Stable limit, mutable count

Marker: constant-stable. Existing panel key: constant-valid. Stdout bytes: 3\n0\n3\n1\n; empty stderr; exit 0; closed stdin. Each observation writes the limit first, then the count, one integer per line. The four-line trace distinguishes (3,0) before assignment from (3,1) afterward. Do not introduce stream chaining or character-literal syntax.

```cpp
#include <iostream>

int main() {
    const int measurement_limit = 3;
    int measurement_count = 0;
    std::cout << measurement_limit;
    std::cout << "\n";
    std::cout << measurement_count;
    std::cout << "\n";
    measurement_count = 1;
    std::cout << measurement_limit;
    std::cout << "\n";
    std::cout << measurement_count;
    std::cout << "\n";
    return 0;
}
```

The [stable-limit activity](../diagrams/observable-constants/07-activity-stable-limit.md) has six conceptual actions. Initialization actions each map one statement. Each pair observation maps four statements. Assignment and successful return each map one statement: twelve in total. Include/signature/braces and initial/final nodes are structural. Displayed zero and process success remain independent.

### Assignment rejected by the compiler

Marker: constant-rejected. Existing panel key: constant-rejected. This whole source file is intentionally ill-formed. Compile only, expect rejection, do not run or describe a successful stdout/status. The final write/return statements are present to make the otherwise valid controls observable, not to imply they execute in the rejected program.

```cpp
#include <iostream>

int main() {
    const int measurement_limit = 3;
    measurement_limit = 4;
    std::cout << measurement_limit;
    std::cout << "\n";
    return 0;
}
```

Isolate the cause with two derived verification controls: remove const and obtain successful 4\n output; remove only the forbidden assignment and obtain successful 3\n output. These controls are test-only, not extra teaching programs. They prevent an unrelated syntax/header defect from masquerading as evidence of const enforcement. Test exact source intent and fixed inventory as well; never rely on a localized diagnostic string alone.

Reference the stable-limit activity as expected conception only, with explicit scoped comparison: constant initialization corresponds to its first action; the attempted assignment has no valid action in that design; neither subsequent writes nor return can execute from this ill-formed translation unit. The rejected source omits the mutable count, so the complete reference activity is not its actual runtime model. Map all five authored statements with that qualification. No separate activity of a successful forbidden assignment or of compiler internals is warranted.

A real diagnostic may be quoted in French teaching prose with compiler/version and an explicit nonportable-wording qualification. The study host is GCC 15.2.0. Capture paths must be sanitized to a neutral example filename; no expectation depends on exact English wording.

### Legal constant, wrong requirement value

Marker: constant-wrong. Existing panel key: constant-wrong. The entire source is the stable-limit program above with only the initializer measurement_limit = 3 changed to measurement_limit = 30. The complete source is listed below to make the accepted contract independently reviewable. Expected actual stdout: 30\n0\n30\n1\n; empty stderr; exit 0. Required output remains 3\n0\n3\n1\n. The program is legal and the integer remains constant, but the requirement is violated from initialization.

```cpp
#include <iostream>

int main() {
    const int measurement_limit = 30;
    int measurement_count = 0;
    std::cout << measurement_limit;
    std::cout << "\n";
    std::cout << measurement_count;
    std::cout << "\n";
    measurement_count = 1;
    std::cout << measurement_limit;
    std::cout << "\n";
    std::cout << measurement_count;
    std::cout << "\n";
    return 0;
}
```

The [wrong-limit activity](../diagrams/observable-constants/07-activity-wrong-limit.md) models the actual value 30 and the same six actions/twelve statements. Label it explicitly as actual faulty behavior against the required value 3. Preserve the primary required activity as the reference; do not silently replace the requirement with 30. No runtime mutation of the constant is represented.

## Proposed French teaching sequence

1. State the fixed requirement 3 and the supplied count totals 0 then 1; predict (3,0) and (3,1).
2. Read the primary six-action activity, with 16px labels and no omitted output actions.
3. Copy/read the complete primary program, immediate UML card, exact four-line expected output and chronological value/output trace.
4. Explain which object carries const, when initialization happens, and why the independent count can change.
5. Predict the compiler's refusal of the complete rejected case, inspect the qualified diagnostic and compare its five statements with the expected design without inventing an execution.
6. Predict/observe the complete wrong-initializer program; compare actual 30 with required 3 before discussing the invariant that still holds at the wrong value.
7. Preserve the runtime-known const nuance as conceptual prose; no unexplained API call or constexpr lesson. Optional narrated transfer to the already published strict indicator may be linked, without adding a prerequisite or executable example.
8. Conclude with what const checks, what it cannot choose, and truthful standalone-practice availability.

Use existing observable-values table markup where tables require reflow; no new CSS rule or runtime change is proposed. Keep natural diagram dimensions, centered image on content-wide white paper, original-SVG links, 80ms opening delay, 160ms fades, reduced-motion and native fallbacks. The new model sources use current naming conventions; the old constant-limit/01-activity-values triplet stays historical, not renamed or rewritten.

## Proposed files and delivery sequence

Conception-only branch from main: codex/20-observable-constants-conception. This branch may add only this specification, the two PlantUML triplets under diagrams/observable-constants/, and small central glossary/traceability entries required by the current conception naming convention. They cover the new normalized IDs only and do not claim a retrospective audit of older scoped contracts. Add conception review/smoke evidence after owner review. No lesson, public snapshot or test changes in the separate conception PR; use Refs #20.

After explicit owner approval and separately authorized conception publication/merge, implement on codex/20-observable-constants-lesson from updated main:

| File | Responsibility |
| --- | --- |
| src/content/docs/notions/cpp-09.md | Replace three fragments with three marked full sources; retain card keys/prerequisite/route, add outputs/trace and qualified compile rejection; preserve conceptual boundaries |
| public/diagrams/examples/constant-limit.svg | Replace with byte-identical stable-limit render while retaining the URL used by valid/rejected cards |
| public/diagrams/examples/constant-wrong-limit.svg | New exact snapshot for actual wrong-initializer behavior |
| tests/constant-limit.py | Dedicated fixed-contract extraction CLI: exactly three sources, two run contracts and one compile-only rejection with independent controls; source intent and provenance, no compiler-message locale dependency |
| tests/constant-limit.test.mjs | Invoke actual-source validation; mutation fixtures and rendered mappings/inventory/links; no duplicated primary-source fixture |
| tests/example-code.py | Remove only CPP-09's three replaced fragment extractions/assertions; preserve all six other excerpts and boundary checks; update honest count |
| tests/explorer-content.test.mjs | Update only constant-limit provenance and add wrong-limit pair; seven current pairs become eight |
| tests/explorer-browser.py | Exercise all three CPP-09 card identities/mapping rows, diagrams, native fallbacks, normal/reduced motion, keyboard, table reflow and enlarged text while retaining existing regression paths |
| tests/browser-coverage.mjs | Add settled CPP-09 course/card accessibility and narrow/dark checks; preserve existing guard and coverage floor |
| docs/architecture/specs/constant-limit.md | Explicitly mark old fragment/output-model framing superseded by this extension; preserve original const semantics/history |
| docs/architecture/specs/inline-uml-panels.md | Update three constant mappings and all-five-/twelve-statement scopes; fifteen teaching fences remain fifteen |
| docs/architecture/README.md | Link current extension and both model realizations |
| README.md | Explain eight executable complete programs, one complete rejected source, six remaining fragments and the dedicated CLI |
| docs/reviews/observable-constants/implementation.md | Structured review, measured local gates, owner disposition and limitations |
| docs/architecture/qa/<date>-observable-constants.md and screenshots | Current production QA checklist, inspector/security verdicts, screenshots showing full code/result evidence |

No change to tests/program-output.py or its three existing modes/public API, compiler flags or exact program inventories. Mixed compile/run contracts justify a small dedicated runner; do not generalize the existing private harness into a registry. Six existing executable programs stay protected; with the two new runtime cases there are eight. The complete rejected source is not counted as an executable success. Three old CPP-09 fragments leave the generated wrapper, so nine remaining fragments become six. No source schema, shared CSS, component/script, navigation, lesson count, dependency, lockfile or CI change.

## Acceptance, traceability and verification

REQ-1: retain the specified limit 3, ordinary mutable count 0 then 1 and supplied-total semantics; no arithmetic/acquisition/capacity claim.
REQ-2: exactly three marked complete-source fences/card keys in CPP-09, two valid translation units and one intentionally invalid case, retaining fifteen teaching fences overall.
REQ-3: actual stable/wrong sources compile under C++17, Wall/Wextra/Werror/pedantic-errors; execute with closed stdin, bounded timeout, exact independent stdout bytes, empty stderr and status 0.
REQ-4: invalid source is rejected and never executed; both derived controls compile/run successfully. Reject malformed baselines and accidental unrelated compile failures.
REQ-5: both valid-runtime sources read each named object at both observation points. Source/model assertions and fake-literal-output mutants must protect this, not stdout alone.
REQ-6: runtime model/card mapping covers twelve statements through six conceptual actions; rejected card maps all five authored statements without assigning a successful execution to them.
REQ-7: retain route, direct CPP-01 prerequisite, availability/progression, reader behavior and honest practice status; main explanation needs no dialog.
REQ-8: mutation inventory catches missing/wrong/duplicate markers, extra fences, changed initial count, missing/moved count update, changed required/wrong limit, missing const on valid limit, quoted name or fake numeric observations, missing newline, stderr, nonzero exit, and invalid source made valid or invalid for unrelated reasons. No uninitialized-read mutant.
NFR-1: source/render/public provenance and intrinsic diagram layout verified; all previous program/fragment/card/navigation contracts retained.
NFR-2: full checks/build/tests, unchanged >=80% runtime coverage floor and >=90% public documentation presence; exact-SCM-revision Sonar and history/snapshot Gitleaks before authorized publication.
NFR-3: current production browser QA, accessibility, keyboard/focus, 320/390/tablet/desktop, theme, enlarged text, fallbacks, inspector and SEC-01..10 applicability. No silent extension of #16's local-preview waiver: identify any needed owner disposition explicitly for #20. Screenshots must show the result they claim.
NFR-4: reviewed conception and explicit owner approval before implementation; separate conception PR; separate push/PR, merge/deletion authorizations; no Copilot review. Existing #3/#7/#8 remain separate.

The central traceability matrix links REQ-1..8 and NFR-1..4 to ACT-stable-limit, ACT-wrong-limit and proposed test paths. Older requirements retain their original IDs in their original specifications.

Conception study on 2026-10-26: exact primary/wrong sources and both valid rejection controls were compiled/executed in /tmp using GCC 15.2.0. Observations matched the contracts above. The rejected source failed compilation and was not executed. This is study evidence only; the published lesson and future extraction tests are unchanged. PlantUML rendering requires Java headless mode under the current sandbox; use JAVA_TOOL_OPTIONS=-Djava.awt.headless=true, no GUI server. The two activities render at 239x649 with 16px labels; repeated renders must match. Visual review is part of conception delivery.

## Four-pass proportional review

Requirements: every existing const distinction is preserved and tied to a distinct observation/diagnostic. The longer complete cases repeat known structure but share one central learning objective. The target-value invariant and requirement correctness remain separate.

Dependencies/SOLID: authored text/model feeds the existing static renderer; tests consume actual source and fixed external observations. No domain layer depends on Astro. The compile-rejection runner has a different contract from all-success programs, without forcing a new runtime abstraction.

KISS/YAGNI/DRY: retain one page and three existing card identities. Small source repetition makes independent copying possible. Do not introduce helpers, a browser compiler, input APIs or an empty explorer to manufacture novelty. Reuse existing reflow styling; no new design pattern has a present force.

Anti-pattern risks: fake hard-coded observations, a rejected program portrayed as executing, a wrong actual model confused with the requirement, stale fragment wrapping or counts, missing const accepted by output-only checks, compiler rejection caused by unrelated broken source, and clipped screenshots. The explicit source contracts, paired compiler controls, scoped mappings, fixed inventories and measured QA address these. No implementation or publication approval is inferred from passing the study.
