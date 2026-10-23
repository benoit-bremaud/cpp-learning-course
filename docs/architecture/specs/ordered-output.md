# Ordered output and newline placement

Status: the owner explicitly approved option A, its weights, three-program inventory and concrete local implementation plan on 2026-10-23. Work item: [#13](https://github.com/benoit-bremaud/cpp-learning-course/issues/13). Push, PR creation and merge remain separately authorized. The separate conception documentation delivery precedes lesson implementation.

## Context and need

Main is `4cdf2df`, after first-program conception PR #11 and implementation PR #12. The owner explicitly authorized continuing issue #13 in the same chat as an exception to the one-task-per-chat rule on 2026-10-23. The previous task is finished and its checkout is clean. This exception does not waive conception, publication, review or merge gates. Commands target the actual course repository, not the app's separate practice-repository binding.

The reader has completed `notions/programme-minimal`: main, its body, cout, literals, newline and return status are already explained. The new objective is to predict exact text from successive output statements. Hosted desktop C++17, ordinary functioning standard output, no variables, input, hardware APIs, helper functions or browser execution. Standalone practice remains unpublished. No buffering tutorial, flushing guarantee, stream chaining, formatting API, namespace tutorial or new syntax family is added.

Historical source `7cdb30357c743ce2a6adf38a65dae1f655e93851` contains a draft premiers-affichages lesson and three activities. Its approval is not inherited. A conception study compiled those three historical complete programs with strict C++17 flags on 2026-10-23 and observed the exact outputs below, empty stderr and exit 0. This is study evidence, not a claim that the future authored lesson has been implemented or tested.

## Approved option A: three contrasts on one page

| Contract | Distinct question | Exact expected stdout | Model |
| --- | --- | --- | --- |
| OO-01 ordered | Which message comes first? | `Program started\nProgram finished\n` | [Ordered](../diagrams/ordered-output/01-activity-ordered.md) |
| OO-02 reversed | Do English message meanings control execution? | `Program finished\nProgram started\n` | [Reversed](../diagrams/ordered-output/02-activity-reversed.md) |
| OO-03 joined | Do two source statements necessarily make two output lines? | `System ready\n` | [Joined](../diagrams/ordered-output/03-activity-joined.md) |

Each program includes iostream and defines int main() with two cout statements followed by return 0. OO-01 writes the two literals with their own newline; OO-02 swaps only those statements. OO-03 writes `"System "` then `"ready\n"`. Preserve the significant trailing space in the first literal. All three require empty stderr and successful exit. Linux checks assert raw bytes; do not claim identical external text-mode bytes on every desktop platform.

OO-02 is an intentional alternative requirement, not a solution to OO-01. Explicitly compare unchanged strings/newlines with changed statement order. OO-03 establishes a separate output requirement and contrasts source layout with output layout; do not pretend it changes only one character of OO-01. A short trace records System plus a space after the first write, then System ready plus newline after the second. Trace wording describes requested stream output, not the instant a terminal physically paints it.

Sequence: objective/prerequisite and expected observation; primary UML; complete ordered program and adjacent UML card; result and explanation; reversed requirement/model/program/result; joined requirement/model/program/result and trace; compact retrieval summary. Do not repeat the first lesson's full syntax table. Explain that started/finished are ordinary text, source newlines do not request output newlines, and return 0 adds no printed line. All three comparisons stay visible on the main page. No empty explorer or unreviewed companion sheets; complementary contexts remain an explicit authoring gap.

## Proportional UML and presentation

Three activity models each show the two exact write actions and return in execution order. Their scope begins at entry to main's body. Initial/final nodes are not extra C++ statements. Include/signature/braces are structure. No branches, loops or state machine are introduced. Existing reader component/state views already cover the unchanged UI; no additional system diagram or GoF pattern is justified.

New authoritative sources live in `docs/architecture/diagrams/ordered-output/`, separately from the accepted first-program models. Use numbered puml/svg/md triplets. French labels, 16px type, compact line breaks and no wide observation notes. SVGs are generated, never geometry-edited. Reuse the existing full-width white paper, centered natural-size images shrinking only to fit, original-SVG links, native card/dismissal behavior, 80ms opening delay, 160ms fades and reduced-motion behavior. New prose and link labels use ASCII hyphens.

## Alternatives and weighted decision

Scores are editorial judgments supported by the source inventory, not measured learning outcomes. Cost scores are estimates. Weights sum to 100; points are score times weight.

| Criterion | Weight | A: three contrasts, one page | B: ordered + joined only | C: split order and newline across two pages |
| --- | --- | --- | --- | --- |
| Observable misconception coverage | 35 | 5: all three explicit contrasts | 3: reversal is described without a worked contrast | 5: all three retained |
| Reading focus | 30 | 4: coherent output-prediction objective, three cases | 5: shorter page | 5: narrower page objectives |
| Progression continuity | 20 | 5: one bridge from first program to variables | 4: bridge omits concrete reversal evidence | 3: introduces another navigation/prerequisite stop |
| Estimated maintenance proportionality | 15 | 4: one host page and three models | 5: two models/programs | 2: two host pages, additional links/status/tests |
| Weighted points | 100 | 455/500 | 410/500 | 415/500 |

A versus C: both retain coverage; A keeps the three related output comparisons together and needs one fewer host page. C reduces per-page reading load. A versus B: A's reversal demonstrates that source order wins over message meaning; B saves length but relies on explanation for that distinction. Owner-approved winner: A (weights validated on 2026-10-23). Runner-up/fallback: C, 415/500; activation retains the models but splits content/navigation and requires revised page/test plans. It is a design change, not a drop-in switch.

Sensitivity: moving 10 weight points from maintenance to reading focus leaves A at 455 and raises C to 445. Moving 15 gives C 460 and A 455. Thus the recommendation depends on accepting the proposed balance between a coherent short unit and smaller pages. The owner validated these weights and inventory on 2026-10-23; no claim of an objectively optimal lesson length is made.

## Concrete delivery plan

Conception-only branch `codex/13-ordered-output-conception`, from clean main: this specification and the three model triplets. Render and visually inspect them, verify links/action order, and obtain owner approval. The UML skill requires a separate conception documentation PR; push, PR and merge need explicit authorization. Keep #13 open until the implementation is accepted and merged.

After that delivery, use a fresh codex/ branch from updated main for option A:

- Add `src/content/docs/notions/premiers-affichages.md` with exactly three complete marked programs (`program-ordered`, `program-reversed`, `program-joined`), primary diagrams and immediate uniquely keyed cards.
- Add `public/diagrams/examples/program-{ordered,reversed,joined}.svg`, byte-identical to approved generated sources.
- Update `astro.config.mjs` to insert the page after programme-minimal and before CPP-01; update `src/content/docs/parcours.md` for actual availability (five introductory lessons); update only programme-minimal's next link and obsolete future-availability sentence. Keep CPP-01's direct prerequisites unchanged: its initialization fragment does not require the output-order lesson. Reading order is not permission to inflate prerequisite lists.
- Add links to the new specification from `docs/architecture/README.md` and append three exact mappings to `docs/architecture/specs/inline-uml-panels.md` (fifteen fences total). Preserve earlier mappings and diagrams.
- Extend `tests/program-output.py` with explicit fixed per-lesson contract tables and a small shared private compiler/extraction loop. Preserve existing validate_lesson behavior and default CLI for exactly Ready/Silent. An explicit `--lesson ordered-output` selects exactly the new three IDs and authoritative paths; no arbitrary code execution service, registry, plugin abstraction or external fixture source.
- Keep `tests/program-output.test.mjs` first-lesson count/output tests. Replace its obsolete blanket ban on premiers-affichages links with checks that the first lesson still has only its two programs and now links to the published next page. Add `tests/ordered-output.test.mjs` for the new inventory, outputs, three mappings and navigation. Both lesson sets run through the existing npm test glob without CI edits.
- Extend `tests/explorer-browser.py` and `tests/browser-coverage.mjs` for three cards, exact mappings, production search, keyboard/focus, original SVG links, responsive/dark/reduced-motion/text-enlargement/reload/fallback behavior. Reuse the existing accessibility diagnostic handling without broadening its exception.
- Add `docs/reviews/ordered-output/` evidence and selected screenshots; update README commands/available-page count as necessary. Do not edit runtime components/scripts/CSS/schema, package versions, lockfile or CI workflows.

## Acceptance criteria

1. Actual three authored C++ excerpts compile independently with C++17, Wall/Wextra/Werror/pedantic-errors and execute with a timeout; exact raw stdout, empty stderr, exit 0. No duplicate source fixtures stand in for lesson text. Both lessons enforce their own exact ID/fence inventories.
2. Isolated mutations detect reordered messages, a missing joining space/newline, unexpected stderr/status, duplicate/missing markers and extra fences. Existing first-lesson and earlier excerpt tests remain green.
3. Primary model precedes each code block; each block has the correct adjacent card and scoped three-row action mapping. Generated authoritative SVGs equal public snapshots; earlier assets stay unchanged. All internal links/anchors/assets and published availability agree.
4. No implementation-time first-lesson test continues to assert that the new route is absent. Conception documents retain their historical #10 scope; new acceptance supersedes only its former route-unavailability condition.
5. Full check/build/test, prior C++ and invalid-content suites, production Chrome/Firefox/WebKit QA where installed, and accessibility checks pass. Record unavailable tools instead of claiming they ran. Browser runtime coverage floor 80%, target approximately 100%; public-export documentation at least 90%, with denominators and limits stated.
6. Verify natural-size diagrams, white panel width, body-comparable labels, no overflow, exact card timing/reduced motion, keyboard/focus, dark mode and no-script fallbacks at desktop/390px/320px and enlarged text. Retain screenshots and console/network results. Scope search locators to the search dialog, not the matching sidebar title.
7. SonarQube passes on the final reviewed SHA; full-history and exact delivery-snapshot Gitleaks scans pass; no tracked env files; structured diff review addresses every finding. No Copilot review. Remote review and CI must pass before separately authorized merge.
8. Joint owner review covers keep/improve/reject/defer/investigate for material points. No publication without explicit authorization. Keep #7, #8, #3 and standalone practice outside this increment.

## Four-pass conception review

Requirements/traceability: OO-01/02/03 each has a distinct question, exact observation, model, planned marker and mutation. Main's return remains separate from output. Concrete reversal retains the same strings and changes their order; joining has its own explicit need.

Dependency/SOLID: authored content feeds the existing static build and native progressive enhancement. Shared test extraction belongs in the test harness; fixed lesson contracts stay separate, and first-lesson validation does not silently broaden to five programs.

KISS/YAGNI/DRY: one proposed page, three small activities, no custom runtime UI. Sharing the existing compiler loop has a present second consumer; no generalized course-testing framework is justified. Keep content duplication that supports direct comparison instead of hiding the programs behind new machinery.

Patterns/anti-patterns: no application pattern is warranted. Risks are cognitive repetition, treating reversed output as fulfilling the original need, losing the significant space, claiming screen-paint timing, weakening old tests or leaving stale navigation. The explicit contracts, weighted alternatives and acceptance checks address those risks. No outstanding implementation is implied by this review.
