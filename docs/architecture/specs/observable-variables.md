# CPP-01 - observable initialization and assignment

Status: option A, weights and concrete implementation plan explicitly approved by the owner on 2026-10-24. Work item: [#16](https://github.com/benoit-bremaud/cpp-learning-course/issues/16). The approval covers the one-program design and listed local implementation after the separate conception delivery. Baseline: clean main `8712767`, after PR #15. The owner asked to continue in this chat; no new chat was created. This document does not authorize push, PR creation or merge.

## Need and current evidence

CPP-01 currently teaches two instructions in a fragment: initialize `measurement_count` to 0, then assign the supplied known total 1. Its harness wraps that fragment in a generated main and asserts both values. The reader now has published complete-program and ordered-output lessons, so the next bridge is to observe those same values in a complete hosted desktop C++17 program.

The [original measurement-count conception](measurement-count.md) remains the historical fragment contract. This accepted extension retains its meaning, scalar, chosen values and unconditional literal assignment, but replaces the primary fragment with a complete program and includes output actions in the primary activity. This accepted extension governs the future complete-program implementation. The original MC-03/04 and no-output boundary still describe the currently published fragment and must be explicitly marked superseded when that implementation is delivered; do not leave both versions claiming to govern the same primary example. The original two-action model remains a documented historical view, not the exact model of the future complete program.

The stock and independent-copy sheets stay scoped fragments with their current contracts. CPP-09 stays unchanged. Reading order is not a reason to inflate direct prerequisites: retain TOOL-01 and the first-program lesson, and cross-reference the available ordered-output page for the two successive writes used to end an observation line. Explain the necessary output behavior locally as well.

## Objective and scope

One objective: distinguish a variable's initial value from a later replacement by observing both in order. Introduce the ordinary local integer, its chosen name, initialization, assignment and reading its current value for output. Essential understanding stays on the main page; companion sheets provide transfer and depth.

The program has one ordinary local `int`, one main, no input, no arithmetic, no comparison, no branch, no loop, no helper function and no hardware API. The assignment stores the supplied literal 1, not previous value plus one. No wait, event or sensor acquisition is represented. Explain the story as two known totals, avoiding the current implication that the sample automatically reacts to a measurement arrival.

Show one complete program, not a fragment followed by an almost identical wrapper. Structural syntax comes from the first-program prerequisite; do not repeat its full syntax table. Explain `std::cout << measurement_count;` as reading the current integer and writing its digits for the small values in this example. Contrast the identifier with quoted text using inline expressions and a short observation table, not another fenced teaching program. A name is not printed merely because that name appears in source.

Keep each write separate: output the value, then output the already-known newline string. Do not introduce stream chaining, a character-literal syntax family, formatting APIs or namespace explanations. Keep declaration/initialization/assignment vocabulary attached to the concrete program. Preserve the safe-initialization warning without executing an uninitialized read or presenting any particular accidental value as a result. Redeclaration, nested scopes, shadowing, arithmetic and full type-range study remain later bricks.

## Alternatives and weighted choice

The owner validated these weights and selected A on 2026-10-24. Scores are editorial judgments, not learning-effectiveness measurements. Maintenance costs are estimates. Weights sum to 100; scores range from 0 to 5, with weighted totals out of 500.

- A: replace the primary fragment with one complete observed program; retain the two companion sheets.
- B: retain the primary fragment and append the complete observed program on the same page.
- C: replace the fragment with two complete programs, the correct update and an explained missing-assignment case producing 0 then 0.

| Criterion | Weight | A | B | C |
| --- | ---: | --- | --- | --- |
| Evidence for the distinction | 25 | 4: two observed values and inline identifier/literal contrast | 4: same observations plus a structural comparison | 5: adds an executable missing-update contrast |
| One-difficulty reading focus | 30 | 5: one program and one chronological trace | 3: duplicate representations and two primary blocks | 4: second result adds a comparison to track |
| Continuity with the accepted lesson | 30 | 5: same name, values, semantics and companions | 4: keeps old framing beside the new objective | 5: same concept and supplied values |
| Estimated proportional maintenance | 15 | 4: one model/program and targeted harness adaptation | 3: two mappings for nearly identical teaching actions | 3: two complete contracts and activities |
| Weighted points | 100 | 460/500 | 355/500 | 440/500 |

A versus C: A makes the current lesson directly observable with less repeated reading. C adds stronger executable evidence of what an omitted assignment does, at the cost of a second complete case. A versus B: retaining both forms preserves the earlier fragment but repeats the same state changes, without adding the independent behavioral contrast C offers. Owner-selected winner A: 460/500. Runner-up/fallback C: 440/500; activation requires a second reviewed model, program, mutation inventory and reading sequence. It is a conception change, not a drop-in implementation variant.

Sensitivity: transfer 10 weight points from reading focus to evidence and A becomes 450, C becomes 450. Transfer 15 and A becomes 445, C becomes 455. Thus the 20-point lead depends on preferring a focused single-program bridge over a second worked error; it is not an objectively measured advantage. The earlier 485/500 score selected this task against other backlog bricks, not option A against these designs.

## Concrete option A program and observations

Proposed future source marker: `program-measurement-observed`. Keep the existing card key `measurement-primary`.

<!-- example:program-measurement-observed -->
```cpp
#include <iostream>

int main() {
    int measurement_count = 0;
    std::cout << measurement_count;
    std::cout << "\n";
    measurement_count = 1;
    std::cout << measurement_count;
    std::cout << "\n";
    return 0;
}
```

Expected raw stdout on the Linux validation host: `0\n1\n`. Empty stderr and exit status 0. This is a proposed source contract, not a claim that the reader lesson has been changed or executed. C++17 compilation uses `-Wall -Wextra -Werror -pedantic-errors`; execution uses closed stdin, captured bytes and a timeout.

Conception study on 2026-10-24: the exact program above was extracted from this specification, compiled under those flags and executed with stdout `b'0\n1\n'`, empty stderr and exit 0. Two fresh PlantUML renders were byte-identical to the proposed SVG, which was visually inspected at its natural 225px by 544px size. Authored links, ASCII hyphens and whitespace passed checks. These are study results only; the future lesson and its planned tests have not been implemented. These study checks do not substitute for the separate full publication gates.

| Point | Current integer value | Accumulated stdout |
| --- | --- | --- |
| Initialization | 0 | Empty |
| First value write | 0 | `0` |
| First newline write | 0 | `0\n` |
| Assignment | 1 | `0\n` |
| Second value write | 1 | `0\n1` |
| Second newline write | 1 | `0\n1\n` |
| Successful return | 1 | Unchanged |

At the initial value, the inline comparison `std::cout << measurement_count;` writes `0`, whereas `std::cout << "measurement_count";` writes the name as literal text. Neither expression alone requests a newline. This distinction must be explained without confusing an output operation with a modification of the integer. Return status 0 is independent from the displayed first value 0.

## Minimal UML and code mapping

The [observed-values activity](../diagrams/measurement-count/02-activity-observed-values.md) models five conceptual actions. Each observation action is deliberately realized by two consecutive C++ statements: read/write the integer, then write a newline. Grouping is explicit; no statement is hidden or invented. The per-statement trace above resolves the finer question.

| Activity action | Exact C++ realization |
| --- | --- |
| Initialize measurement_count to 0 | `int measurement_count = 0;` |
| Write its current value then a newline | `std::cout << measurement_count;` followed by `std::cout << "\n";` |
| Assign supplied total 1 | `measurement_count = 1;` |
| Write its current value then a newline | `std::cout << measurement_count;` followed by `std::cout << "\n";` |
| Return success | `return 0;` |

The activity begins at entry to main's body. Include/signature/braces and initial/final nodes are structural, not extra C++ statements. No class, state, sequence, component or use-case diagram answers a new question here. Reuse the existing reader architecture. The old two-action model stays untouched in the conception delivery; update the public snapshot and its provenance test only with the approved lesson implementation.

French teaching labels use 16px text and short line breaks. Generate SVG bytes from PlantUML without geometry edits. Retain full-content-width white paper, centered intrinsic image size shrinking only to fit, original-SVG links, 80ms opening delay, 160ms fades, reduced motion and native fallback. Code fences may use the renderer's existing wrap metadata for reflow; it changes no copied C++ statements.

## Concrete files and delivery sequence

Conception-only branch from clean main: `codex/16-observable-variables-conception`.

1. Add this specification and `docs/architecture/diagrams/measurement-count/02-activity-observed-values.{puml,svg,md}`.
2. Render and inspect the model; compile the exact proposed program as study evidence, keeping it distinct from testing the future authored lesson. Perform the four-pass review below and obtain explicit owner approval of option, weights and file plan.
3. Deliver these documents in a separate conception PR with Refs #16 after the applicable local gates and separate push/PR authorization. Preserve current published content and tests in that delivery. Merge requires separate authorization.
4. Implement the accepted plan on a fresh codex/ branch from updated main after the conception delivery. The implementation file inventory follows; no production/test file has been edited by this proposal.

| Implementation file | Planned responsibility |
| --- | --- |
| `src/content/docs/notions/cpp-01.mdx` | Replace its one primary fragment with one marked complete program; correct the known-total framing; explain integer output, add exact result/trace and five-action card mapping; preserve slug, card key, direct prerequisites and companion IDs |
| `public/diagrams/examples/measurement-count.svg` | Replace snapshot with byte-identical output of the newly approved observed-values model, retaining the public URL |
| `tests/program-output.py` | Add a third explicit fixed lesson mode for the single observed-variable contract, without broadening either existing lesson's inventory or default API/CLI; support the one-marker diagnostic |
| `tests/observable-variables.test.mjs` | Execute the actual authored excerpt; test mutations, exact inventory, mapped statements, output, card and provenance; assert retained companion and navigation relationships |
| `tests/example-code.py` | Remove only the replaced measurement fragment from the generated fragment wrapper; retain all nine remaining authored excerpts and their assertions; accept existing fence metadata during extraction; update the count honestly |
| `tests/explorer-content.test.mjs` | Change only measurement-count snapshot's authoritative source to the observed-values model; retain other six provenance pairs and explorer assertions |
| `tests/explorer-browser.py` | Exercise CPP-01's complete-program card outside the companion dialog, exact mapping rows, reflow and enlarged text, while retaining all explorer/other-lesson regressions |
| `tests/browser-coverage.mjs` | Add settled main-card accessibility and keyboard checks, preserving diagnostic guards, error handling and the coverage floor |
| `docs/architecture/specs/measurement-count.md` | Explicitly mark the former primary-fragment framing as superseded by this accepted extension while preserving the historical two-action study |
| `docs/architecture/specs/inline-uml-panels.md` | Update the measurement-primary mapping to the five-action complete program; total teaching-fence count remains fifteen |
| `docs/architecture/README.md` | Link the accepted extension and current model |
| `README.md` | Record six complete programs across three lesson modes, nine remaining fragments and the explicit observed-variable validation command |
| `docs/reviews/observable-variables/implementation.md` and selected screenshots | Record actual implementation review, tests, limitations, owner questionnaire and verification evidence |
| `docs/architecture/qa/<date>-observable-variables.md` and selected screenshots | Record the current QA checklist verdicts and inspector/security evidence for the implemented page |

No new page, sidebar item, availability count, dependency, workflow, runtime component/script, shared CSS or content-schema change. No companion source changes. The five introductory lessons remain five. Existing first-program and ordered-output tests remain intact, except a demonstrated regression must be separately assessed. A material scope/design defect requires revised conception and owner validation.

## Acceptance and verification

- OV-01: exactly one CPP-01 complete-program marker and fence; copied source is independently valid C++17, with the exact output/status contract above. Extract from the lesson, not a duplicate source fixture.
- OV-02: initialization and assignment target the same ordinary integer. Output statements read that identifier at both checkpoints. Check exact code-to-model realization, not stdout alone, which could be faked by hard-coded output literals.
- OV-03: mutations detect changed initial/assigned values, moving assignment before the first observation, quoting the identifier, newline loss, extra stderr, nonzero exit, missing/duplicate markers and extra fences. Never execute an uninitialized read. Syntax/compiler diagnostics are not locale-specific expected strings.
- OV-04: keep all nine remaining excerpt checks, the first lesson's exactly-two-program contract and ordered-output's exactly-three contract. Total complete programs become six. No raw-source compiler fixture substitutes for actual lesson extraction.
- OV-05: verify exact source/SVG provenance, stable URL/card key, five conceptual mapping rows covering all seven statements, primary model before code, immediate panel, unique IDs and original-SVG links. Stock/copy fragments and their current diagrams remain unchanged. Fifteen fenced teaching excerpts remain fifteen.
- OV-06: verify the page remains self-contained without opening the explorer, states supplied-total semantics and honest practice availability, and explains integer value versus quoted name without a new syntax family. No unapproved redeclaration example or arithmetic update is folded in.
- OV-07: run full check/build/test, C++ fragment and complete-program suites, invalid-content tests and current production Chrome/Firefox/WebKit checks where installed. Target runtime coverage approximately 100%, enforce at least 80%; exported/public documentation at least 90%, with denominators and limits.
- OV-08: current global QA rules apply at implementation: a local production-build pass with desktop, tablet, 390px and 320px, theme, keyboard/focus, 200% text enlargement, native fallbacks, inspector review and SEC-01 through SEC-10 verdicts under their rules of engagement. Explain N/A cases for a static reader rather than inventing authentication/API behavior. Observe third parties without probing them. File applicable findings per the global rules; no unreviewed infrastructure changes or bypasses. Conception-only documents need smoke-level product QA.
- OV-09: SonarQube passes on the exact reviewed head, Gitleaks covers full history and exact delivery snapshot, no tracked env files, and structured diff review has no outstanding Must/Should findings. Preserve generated SVG bytes. Record unavailable tooling rather than substituting a claim of completion. No Copilot request.
- OV-10: owner acceptance covers keep/improve/reject/defer/investigate for material points. Separate approvals govern conception publication, implementation publication, merge and branch deletion. Deferred issues #7/#8/#3, assessments, downloads and standalone practice stay separate.

## Four-pass conception review

Requirements and traceability: one variable, two observations and one literal replacement answer the selected need. The model's observation actions deliberately group value/newline statements, with an explicit per-statement trace. Both state and output are checked, so a fake literal-output program cannot satisfy the source contract.

Dependency direction and SOLID: authored content feeds the static build; browser enhancement consumes generated HTML. The lesson depends only on the known standard console interface. Fixed test contracts use the existing private extraction/compiler loop; there is no new runtime dependency or abstraction. Companion fragments remain separate from whole programs in the harness.

KISS/YAGNI/DRY: replace the old fragment rather than duplicate the same actions. Retain two useful companion contexts. Do not generalize the test system into a plugin registry or add a browser execution service. The third fixed lesson mode is a present consumer, not hypothetical extensibility.

Patterns and anti-patterns: no GoF pattern is warranted. Main risks are false acquisition semantics, printing a quoted name, hidden hard-coded observations, stale two-action provenance, accidental nesting of main in the old harness, and weakening earlier exact inventories. The stated narrative corrections, mapping and mutation checks address these. The owner accepted the stated trade-off, weights and concrete plan on 2026-10-24. Publication and merge approvals remain separate; no lesson implementation is included in the conception delivery.
