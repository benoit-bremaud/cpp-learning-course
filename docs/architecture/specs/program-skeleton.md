# First complete C++ program

Status: conception and concrete local implementation plan explicitly approved by the owner on 2026-10-22. Work item: [#10](https://github.com/benoit-bremaud/cpp-learning-course/issues/10). The earlier task selection (465/500) was separate from this approval. Push, PR creation and merge require their own explicit authorization.

Historical reference: `7cdb30357c743ce2a6adf38a65dae1f655e93851`. That study covers two lessons and five programs. This proposal covers one lesson and exactly two programs. Historical approval is not inherited.

## Need and boundaries

After the published TOOL-01 compilation introduction, the reader can recognize a complete hosted desktop C++17 program, relate its actions to observations, and distinguish standard output from termination status. TOOL-01 explains compilation; it does not supply an IDE installation or executable practice project. Do not claim otherwise or add setup instructions to this brick.

The ordinary successful output environment connects standard output to the console. No variables, input, hardware APIs, helper functions, browser compiler or standalone practice repository are introduced. Ordered output, reversed writes and joining two writes onto one line remain a separate future brick.

## Two contracts and proportional models

| ID | Need | Activity | Planned excerpt marker | Observation |
| --- | --- | --- | --- | --- |
| PS-01 | Write Ready followed by a newline, then terminate successfully | [Ready](../diagrams/program-skeleton/ready.md) | `example:program-ready` | stdout `Ready\n`, stderr empty, exit 0 |
| PS-02 | Terminate successfully without writing text | [Silent](../diagrams/program-skeleton/silent.md) | `example:program-silent` | stdout empty, stderr empty, exit 0 |

PS-01 defines `int main()` with a body containing `std::cout << "Ready\n";` then `return 0;`, preceded by `#include <iostream>`. PS-02 defines `int main()` with only `return 0;` and no unused include. Both are complete translation units. These exact two programs are the implementation contract; do not add a third implicit-return variant.

Activities begin at entry to the body of main. The initial and final nodes are modeling notation, not C++ statements. Include directives, signatures and braces are structure, not output actions. PS-01 has two actions in order; PS-02 has one. The activity final marks this scoped activity ending, not a model of runtime initialization, stream teardown or OS internals.

Only two activity diagrams are needed. Existing reader component/state views already describe the unchanged presentation. No new class, component, sequence, state, deployment or use-case diagram adds information to this content increment. PlantUML retains the repository's authoritative activity-source and generated-SVG convention. French diagram labels are teaching content; engineering explanations are English.

## Teaching sequence

1. State objective, TOOL-01 prerequisite, desktop scope and honest practice availability.
2. Establish the visible need and exact expected observation before UML and code.
3. Show the primary Ready activity, complete program, immediate authored UML disclosure and observed output.
4. Explain the two statements first, then recognize structure: main, int result, empty parameter list, function body, braces, semicolons, iostream, std::cout, insertion, quotes and newline. Namespace and stream internals remain deferred.
5. Contrast with the silent contract, its primary activity, complete program, immediate UML disclosure and explicit absence of output. Return status is not printed text and is not proof of arbitrary requirement satisfaction.
6. Briefly explain main's special implicit-zero rule without another code fence. Retrieve the output/status distinction and link to the existing CPP-01 introduction.

Do not call main the first machine instruction or suggest cout is Arduino Serial. Explain that `\n` represents a newline, not a literal backslash and n, and makes no claim to immediate flushing. The observable stdout bytes are verified on the local Linux test host; desktop text-mode representation can differ by platform.

## Reuse and navigation

Keep `ExampleExplorer.astro`, `CourseFooter.astro`, `src/content.config.ts`, both browser enhancement modules and shared CSS unchanged. The collection requires two nonempty categories when an explorer is used; this lesson has no reviewed companion sheets. Keep both essential programs on the lesson page, omit an empty explorer, and record complementary-context coverage as deferred authoring work under EX-01/EX-03 rather than inventing sheets.

Insert the available lesson between TOOL-01 and CPP-01 in the explicit sidebar and published progression. Update TOOL-01's next link and CPP-01's direct prerequisites to include the new structure lesson. Preserve CPP-01's existing example, companion sheets, stable ID and next link to CPP-09. Keep optional guided discovery available. No link to unpublished `premiers-affichages` is introduced. Correct the progression's available-introduction count only to reflect actual published content.

## Presentation contract

Reuse the current full-width white paper and `width: auto; max-width: 100%` centered images. Generate activities at 16px label size, comparable to normal body text. Measure rendered label and body size; at narrow widths diagrams may shrink to fit. Original SVG links remain available after every occurrence. New authored labels use ASCII hyphens; existing em-dash text remains under issue #8.

Retain the card's 80ms opening delay, 160ms opacity fade in, 160ms fade out without closing delay, immediate native dismissal/focus handling, and reduced-motion transitions disabled. Preserve native details fallback and one native auto-popover. No presentation redesign is proposed.

## Implementation files

Conception-only branch `codex/10-first-program-conception`: this specification and `docs/architecture/diagrams/program-skeleton/{ready,silent}.{puml,svg,md}`. Conception publication is a separate docs PR as required by the UML skill, subject to explicit push/PR authorization.

After conception validation and the separate documentation delivery, create a dedicated implementation branch from updated main. Planned changes:

- Add `src/content/docs/notions/programme-minimal.md`.
- Add generated snapshots `public/diagrams/examples/program-{ready,silent}.svg` from the accepted conception, never hand-edit SVG geometry.
- Update `astro.config.mjs`, `src/content/docs/parcours.md`, TOOL-01 and CPP-01 only for the published progression changes above.
- Extend `docs/architecture/specs/inline-uml-panels.md` with two new exact mappings, without changing the ten historical pilot mappings; link this study from `docs/architecture/README.md`.
- Add `tests/program-output.py`; integrate its execution through a Node test so `npm test` and the existing validation workflow run the actual C++ checks without workflow edits. Requires g++ on test hosts; fail clearly when absent.
- Update `tests/uml-panels.test.mjs` to accept either the existing em dash or the new ASCII hyphen in the same explicit new-tab label. Add lesson-specific built-output/mapping assertions and provenance checks.
- Extend `tests/explorer-browser.py` and `tests/browser-coverage.mjs` for the new page's cards, fallback, sizing and accessibility while preserving the existing reader coverage and pilot cases.
- Add `docs/reviews/first-program/README.md` and selected screenshots; update README validation commands if needed. No dependency, lockfile, CI or site-wide punctuation changes.

## Acceptance and verification

- Extract the actual two marked lesson fences, require exactly the two expected IDs and exactly two C++ fences, and compile each independently with `g++ -std=c++17 -Wall -Wextra -Werror -pedantic-errors`.
- Execute with a timeout, capture raw bytes, and assert exact stdout, empty stderr and status zero. No duplicate source fixture can stand in for the lesson. Missing/duplicate markers or extra fences fail.
- Regenerate diagrams from puml and compare authoritative SVGs with published snapshots; inspect label/action order and each card's scoped mapping. Keep the two model sources independent.
- Run `npm run check`, `npm test`, existing C++ excerpt and invalid-content probes, browser suites and a structured diff review. Navigation/anchor/asset tests must include the new page. Confirm the ordered-output page is absent.
- Run real production browser QA at 1440px, 390px and 320px, light/dark, enlarged text and reduced motion: full-width white paper, centered natural-size images, readable labels, no horizontal overflow, keyboard opening, Escape/Close/outside dismissal, focus return, mutual exclusion and no-JavaScript fallback. Retain screenshots and console/network results; run supported installed engines and explicitly report unavailable engines.
- Print authored-browser line coverage (floor 80%, target approximately 100%) and public-export documentation coverage (floor 90%), preserving meaningful assertions. These metrics do not measure teaching outcomes or screen-reader conformance.
- Obtain a passing local SonarQube gate on the reviewed SHA, full public-repository history and working-tree Gitleaks scans, no tracked env files, and manual sensitive-data review. Record advisory #7 without silently changing dependency policy.
- Complete the owner's joint critical review and questionnaire (keep/improve/reject/defer/investigate) before requesting separate push/PR authorization. Do not request Copilot review. No gate results are claimed by this proposal.

## Four-pass conception review

1. Requirements and traceability: PS-01/02 map to two activities, two excerpts and exact output/status assertions. All syntax explanations use these concrete programs. The second historical lesson and its three programs are excluded. TOOL-01 is conceptual compilation background, not an installation tutorial.
2. Dependency direction and SOLID: authored content flows into the static build; the existing footer enhances authored disclosures. No runtime data access, new schema, presentation responsibility in content scripts, or dependency on a practice implementation is introduced.
3. KISS/YAGNI/DRY: two small independent activities expose the output/status distinction. Reuse cards and sizing rules. No generalized example framework, extra practice repository, companion-category workaround or redundant implicit-return program.
4. Pattern fit and anti-patterns: no new pattern has a present force. Avoid premature abstraction and silently broadening scope. Principal risks are misleading main/startup wording, treating status as proof, stale navigation, a newline hidden by text rendering, and the em-dash-only link assertion. Explicit wording, byte assertions and focused regression checks address them.

## Sources and limits

C++17-era working draft N4659: [main](https://timsong-cpp.github.io/cppwp/n4659/basic.start.main), [iostream objects](https://timsong-cpp.github.io/cppwp/n4659/iostream.objects.overview), [escape sequences](https://timsong-cpp.github.io/cppwp/n4659/lex.ccon). Original French adaptation; no copied tutorial prose. Compiler execution remains required after implementation.

No repository-linked GitHub Project exists and the visible owner project inventory has no course-specific board. Issue #10 remains unassigned to a board, matching the documented pilot limitation; do not use the unrelated V-SEA board.

Handover limitation: desktop chat metadata still points to `/home/vev/ChatGPT/C++`, a distinct `cpp-learning` repository. All task commands explicitly target `/home/vev/ChatGPT/cpp-learning-course`. The previous chat must remain open until this chat's actual repository binding is corrected and verified, per the global handover rule.
