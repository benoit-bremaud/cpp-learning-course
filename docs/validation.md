# Local validation

- `npm run check`: no errors, warnings or hints.
- `npm run build`: ten static pages generated and Pagefind indexed. Starlight emits non-blocking notices for the absent optional custom i18n collection and custom 404 entry; its built-in French UI and fallback page are used.
- `npm test`: two production-output tests pass, covering internal links, anchors, assets, project-base paths, French language metadata and search artifacts.
- Headless Chrome: desktop 1440px and mobile 390px inspected; no horizontal overflow or page errors on the home page. Search for `const` returns CPP-09 and opens its page. Mobile menu opens the progression successfully.
- npm install audit: no known dependency vulnerabilities reported.

Chrome DevTools MCP could not launch its graphical browser (no X server). Browser verification used the installed Python Playwright with headless Chrome instead. The initial browser test selected an input type not used by this search implementation; correcting that selector confirmed the search flow.

## Structured local review

Must Have: missing favicon found by output tests; added and verified. Default-export exception explicitly approved and limited to Astro configuration. Reader availability accurately distinguishes theory introductions from planned exercises and the published threshold reference.

Should Have: ordered the three introductions by prerequisites rather than alphabetically. Done.

Nice to Have: custom 404/i18n overrides are unnecessary for this initial reader; retained framework defaults.

The owner explicitly authorized publication of this site branch and creation of its independent PR. No CI changes or deployment are included.

## Pedagogical review corrections

Separated the build-chain overview from stable module TOOL-01. Simplified CPP-01 and CPP-09 to match their entry prerequisites, retaining explicit future-study boundaries. Updated introductory navigation and local implementation status. Type checks, production build, and both output tests pass after these edits. Browser interaction checks above describe the initial reader verification, not a new browser run.

## Publication review

Must Have: updated the README to reflect the published practice catalog and corrected the built page count. Done. Guided-example links were verified against published practice commit 6f6da4c; its code excerpt matches the source. The generated UML SVG is an unchanged snapshot with provenance documented in design.md. Existing production-output tests cover its local asset and navigation. No remaining blocking finding from the local self-review.

## Approved PR review correction

Copilot comment 4134840929 was verified and the owner approved building before output tests. `npm test` now runs the production build and only runs tests if it succeeds. The README avoids a duplicate build. An isolated source copy with copied installed dependencies and no dist directory passed both tests; after changing its source while retaining the old dist, npm test rebuilt the changed content and passed again. An initial dependency-symlink setup failed in Astro path resolution; using independent copied dependencies resolved that test-fixture issue. No production sources were modified for the freshness probe.

## Local example explorer validation — 2026-10-12

The owner approved the four subjects and detailed conception before implementation. CPP-01 and the guided indicator now use a shared explorer with four Markdown sheets. Other course pages are not migrated. No push or deployment occurred.

- Astro check: zero errors, warnings or hints; four production-output tests pass, including unique IDs and ARIA reference targets on pilot pages.
- Browser acceptance: both pages at 1440, 390 and 320 CSS pixels; one visible sheet, manual tab activation, modal keyboard focus, Escape/close, original scroll and focus restoration, scroll reset, reopening, multiple-sheet/instance fixture and no-JavaScript fallback pass. Screenshots were inspected; inherited Markdown margins causing uneven header/tab alignment were corrected. Browser coverage is Chrome only; screen-reader and browser-zoom acceptance remain manual checks.
- Actual C++ excerpts compile with C++17, Wall/Wextra/Werror and pass stock/copy, reservoir boundary and strict/inclusive threshold assertions in temporary files.
- Isolated negative builds reject duplicate example IDs, invalid categories, unknown prerequisites and missing example references. The test copies dependencies with internal symlinks preserved: sharing the original node_modules caused an unrelated Astro cache-path failure, while dereferencing executable symlinks broke the copied CLI. Both fixture defects were corrected before the negative scenarios passed.
- Build succeeds with existing optional i18n/404 notices and MDX head-injection bundler warnings. The real browser checks confirm the component script and styling load; these warnings were not suppressed.

Local self-review: corrected keyboard focus escaping at modal boundaries and header/tab margins. No database, runtime content fetch, innerHTML insertion or new dependency was introduced. Diagram renders are local snapshots of the reviewed sources under docs/architecture/diagrams/example-explorer. Standalone practice publication and moving authoritative teaching sources into the practice repository remain outside this local pilot; the sheets state that practice projects are not yet published.

Human visual/pedagogical acceptance of the pilot remains pending. This record does not claim a complete accessibility audit or site-wide migration.

## CPP-01 primary example refinement

After explicit conception approval, the lesson was reordered as situation, expected values, UML, code reading, correspondence, pitfalls and summary. The new SVG is an unchanged generated snapshot of `docs/architecture/diagrams/measurement-count/01-activity-update.puml`. The C++ harness extracts the actual two-line lesson excerpt and checks zero after initialization and one after assignment.

Astro check passes with no diagnostics; all four output tests pass. The unique-ID test caught a heading collision with the stock sheet, corrected by giving the primary activity a distinct heading. All five excerpt contracts and the existing Chrome desktop/mobile/keyboard/fallback checks pass. No other audit finding is claimed resolved and no new standalone practice project is published.

## CPP-09 graduated examples

After explicit owner approval, CPP-09 now includes the stable-limit/mutable-count activity, a permitted update, a separately labelled forbidden assignment and a wrong-but-valid initial value. The generated SVG snapshot matches its reviewed source. `tests/constant-limit.py` extracts the actual labelled lesson snippets, checks every valid checkpoint, confirms the GCC read-only-assignment diagnostic and verifies the faulty value differs from the required 3. The diagnostic shown in the lesson was captured with g++ 13.3.0 in C++17 mode.

Astro check passes without diagnostics, production build succeeds and all four output tests pass. Existing build notices are not suppressed. No new runtime UI or dependency was introduced. Human pedagogical acceptance and further companion-sheet coverage remain pending.

## Project-wide inline UML panels

The approved disclosure design is implemented for all ten current fenced C++ teaching excerpts across three lessons and four companion sheets. Existing diagrams are reused; primary conception remains visible before code. Faulty excerpts explicitly distinguish the expected model from rejected compilation or a wrong initial value.

Verification: Astro check reports zero diagnostics; production build and five Node tests pass. The new coverage guard scans teaching sources for an immediate, uniquely identified UML panel after every C++ fence. Both C++ excerpt harnesses pass. Chrome checks pass at desktop and mobile sizes, including expanded panel tables/images, Enter/Space activation inside both explorer categories, retained code, no horizontal panel overflow at 320px, and JavaScript-disabled disclosure. Existing modal focus/close/scroll tests remain green. This verifies rendering and interaction, not learning effectiveness or full accessibility conformance. Human pedagogical review remains necessary.

## Approved editorial consolidation

Clarified guided-reading expectations across the three lessons and four sheets, added the caller/precondition explanation to the main reservoir reading, and sharpened independent-copy and boundary-test reasoning. A before/after extraction comparison confirms every C++ fenced block is byte-for-byte unchanged. No UML asset or runtime component was edited in this pass.

Astro check passes with zero errors, warnings or hints. Production build and all five Node tests pass. Existing Chrome checks pass, including desktop/mobile reading, inline UML disclosures, explorer keyboard focus and no-JavaScript fallback. The pedagogical audit now distinguishes historical findings, locally addressed points and remaining work. No learner-effectiveness claim follows from these checks.

## Mobile diagram presentation

Seven local teaching PlantUML sources were regenerated with compact French labels and unchanged actions/guards. CPP-09 width decreased from 595 to 238 SVG units; measurement-count is now 225 units wide. Side-note observations remain in lesson prose/tables. All twenty teaching diagram occurrences link to their own SVG with an explicit new-tab label. The pinned practice indicator asset is unchanged.

Astro check, production build and six Node tests pass. Browser tests pass at desktop and narrow/mobile widths, including opening SVG tabs from both explorer categories, returning to the dialog, disclosure keyboard behavior and focus containment. Fixed focus enumeration to exclude links inside closed disclosures. The 320px CPP-09 screenshot was visually inspected: its compact diagram and new-tab link fit the panel. Branching diagrams still scale on narrow screens; this is not a claim of universal diagram readability or physical-phone zoom verification.

## Compact UML cards

Owner-approved option A replaces the expanded complementary panel with compact UML/UML · écart invokers on all ten excerpts. The original details remain as progressive fallback; existing primary diagrams and teaching mappings are unchanged. Native auto popovers provide outside dismissal and mutual exclusion. The enhancement bounds card coordinates to the viewport and preserves the surrounding explorer on Escape.

Astro check reports zero diagnostics; build and six Node checks pass. Chrome acceptance covers Enter activation, Escape and Close focus restoration, outside dismissal without closing the explorer, structured content and viewport bounds at 1440/390/320px, plus the unchanged no-JavaScript reading fallback. A 320px screenshot of a card within the explorer was visually inspected. This is browser verification, not full assistive-technology or physical-device certification.

Platform reference: https://developer.mozilla.org/en-US/docs/Web/API/Popover_API/Using (native auto popover dismissal and invoker relationships). No additional runtime package was added.

## UML opening motion refinement

Prevent the unpositioned first paint, then apply an 80ms delay and 160ms opacity fade; reduced-motion disables the animation. Astro check, build and six Node tests pass. Browser acceptance passes, including frame-by-frame sampling on repeated openings at 1440px and 320px: visible samples remain within one pixel of the same x/y position and finish fully opaque. Reduced-motion reports no animation. Nested explorer closure/focus tests remain green. Human acceptance of the timing remains pending.

## Bidirectional card fade

Owner-requested opacity exit implemented with native discrete display/overlay transitions. Astro check, build, six Node checks and Chrome acceptance pass. Frame sampling at 1440px and 320px confirms intermediate visible opacity during the exit followed by display:none, with focus restored to the trigger. Repeated openings stay positioned; reduced-motion has zero transition duration. Outside click and Escape remain covered by the dialog interaction suite.


## First visible programs

Implemented the approved two-lesson sequence, five complete hosted C++17 programs and five generated activity diagrams. Updated sidebar, progression, TOOL-01 continuation and CPP-01 prerequisite. tests/program-output.py extracts actual labelled snippets and verifies exact stdout, zero exit status, empty stderr and matching source/public SVG snapshots. All five pass. No new practice repository publication is implied. The previously proposed no-output-first design is superseded; its old diagram remains an unpublished historical artifact.

## Repeated assignment in CPP-01

Added the approved 0→1→1 comparison after the baseline, with independent-snippet scope, compact UML and explicit distinction between explanatory trace and console output. A guide connects four existing/new readings by learning purpose. The extractor now uses MDX-compatible stable labels and checks all five checkpoints across the baseline and repeated variant; generated/public repeat SVGs match. Astro check passes, production build and six Node checks pass, C++17 excerpt checks and expanded browser route/card checks pass. Interactive assessments remain deferred.

## Assignment versus redeclaration

Approved VC-03 integrated as two complete programs in CPP-01. The expected activity includes initialization, assignment and return; the rejected variant references that model without a fabricated runtime trace. Captured GCC 13.3.0 diagnostic is shown verbatim. Explained the deliberate unused-variable warning separately from the redeclaration error and distinguished return status from the variable's value. Re-read the section for same-block scope, independent programs and absence of implied console output.

Astro check: zero diagnostics. Build and six Node tests pass. The new extraction harness verifies the actual valid program's exit/output, both instrumented values, the rejected program's specific diagnostic and SVG provenance. Existing excerpt tests and Chrome desktop/mobile/card checks pass with six CPP-01 controls. No publication or interactive assessment was performed.


## First expressions and addition

Implemented owner-approved option A: three primary fragments, an empty-tray companion, four authoritative activities and generated/public SVG snapshots. Reused the existing independent-copy sheet in the deeper tab as an explicitly optional reminder; no new interaction or content schema. Updated the sidebar, CPP-09 continuation, roadmap availability and introductory-page count.

Editorial review checked one new operator, explicit prerequisites, same-unit quantities, bounded example inputs, declaration versus initializer expression, unchanged operands, replacement versus self-update, independent fragments and traces versus stdout. UML separates conceptual calculation/storage without inventing C++ temporaries, processor steps or operand evaluation order. Practice availability and future operations remain explicit.

Astro check reports zero errors/warnings/hints. Build succeeds (13 pages) and six Node tests pass; existing MDX head-directive and optional i18n/404 build warnings remain. The new C++17 extraction test checks every example checkpoint, unchanged inputs, replacement even from eight, empty output and SVG provenance. All four existing C++ harnesses also pass. Chrome acceptance passes at desktop, mobile and 320px widths, including the new route's five UML controls (four new examples plus the reused copy), explorer tabs, keyboard/focus, outside closing and existing fade regression. A separate new-route check confirms no-JS sheets and UML disclosure, and HTTP 200 on the local preview. Desktop rendering was visually inspected. This establishes technical checks, not measured learner comprehension. Work remains local.


## First subtraction and remaining stock

Implemented the approved four-fragment lesson with three authoritative activities. The reversed formula is valid C++ with actual result -7, explicitly contrasted with the expected 7; its card announces the distinction before the reference diagram. Reviewed unchanged operands, exactly-empty stock, input assumptions without guards, independent fragments and absence of stdout. Updated navigation and course availability. No complementary explorer was fabricated.

C++17 extraction checks pass for all checkpoints, unchanged inputs, the wrong-but-valid result and SVG provenance. All five existing C++ harnesses pass. Astro check has zero diagnostics; build and six Node tests pass, with the previously recorded nonblocking build warnings. Chrome regression passes including four new cards at desktop/mobile/narrow widths, keyboard, outside closing and fade. Additional local-route checks confirm HTTP 200, the discrepancy label and no-JS disclosure. The first ad hoc text check raced the opening fade; using a waiting assertion passed without UI changes. The rendered discrepancy card was visually inspected; its expected/actual explanation was then moved above the diagram for immediate clarity. Downloadable summaries remain deferred.


## Equal-size groups and first multiplication

Implemented owner-approved enriched option A: five fragments in reading order literal, named, one kit, zero kits, wrong addition. Four authoritative diagrams back the cards; the faulty case explicitly identifies expected 12 versus actual 7 before showing the named reference model. Added the result table contrasting discriminating inputs (3,4) with masking inputs (2,2), without extra syntax or scored assessment. Navigation, previous lesson, availability and introductory count are updated.

Editorial rereading checked equal-size assumptions, group/per-group/total roles, unchanged input values, one and zero contrasts, independent fragments, conceptual UML rather than processor execution, and the limits of a passing example. No new interaction, practice repository publication or downloadable summary was introduced.

Astro check: zero diagnostics. Build: 15 pages; six Node tests pass. Previously recorded MDX directive and optional i18n/404 warnings remain. The new C++17 harness checks all five actual snippets and checkpoints, retained input values, exact empty output, matching SVG snapshots and both actual expressions with the alternate inputs 2 and 2. All six existing C++ harnesses pass. Chrome regression passes at desktop, mobile and narrow widths with five cards on the new route. Additional checks confirm HTTP 200 on the local preview, discrepancy text/label and no-JS disclosure. The rendered discrepancy card was visually inspected. git diff --check passes. These checks establish technical consistency, not measured learner mastery.


## Grouped calculations and parentheses

Implemented the approved enriched five-case progression: named intermediate, grouped sum, omitted grouping, ineffective outer-only parentheses, then a distinct loose-components requirement where eleven is correct. Three authoritative models back five cards. Both discrepancy cards state expected twenty versus actual eleven before their image; the transfer card is a valid model. Updated sidebar, prior lesson, roadmap and introductory count.

Editorial review verified input units, independent excerpts, actual versus conceptual intermediates, unchanged inputs, dependence versus evaluation order, and explicitly changed requirements. Clarified the introductory numeric bounds as bounds on kit totals, not on every possible addition in the transfer case. No claim that shorter code is faster or intrinsically better.

Astro check has zero diagnostics. Build succeeds with 16 pages and the existing nonblocking MDX/i18n/404 warnings; six Node tests pass. The new C++17 extractor verifies all five cases, initialized inputs and named intermediate checkpoints, results 20/20/11/11/11, masking alternate values and matching public/source SVG snapshots. All seven prior C++ harnesses pass. Chrome regression passes across desktop, mobile and 320px widths with five new cards. Additional checks confirm local HTTP 200, both discrepancy labels and expected results, the valid transfer card, and all five no-JS disclosures. Mobile transfer-card rendering was visually inspected. A final rebuild validates the prose clarification; UI/code were unchanged. Work remains local; practice publication, downloads and interactive assessments remain deferred.


## Integer division and complete kits

Implemented approved option A: four independent examples with stock 12/14/3/0, divisor four and quotient 3/3/0/0; four authoritative activities and matching public SVG snapshots. Updated sidebar, preceding lesson, roadmap availability, introductory count and README command. Reviewed division truncation versus destination conversion, retained stock, no calculated remainder, and zero dividend versus forbidden zero divisor. Refined the rounding sentence to avoid implying a universal tie-breaking rule at 3.5. No zero-divisor execution or guaranteed crash/diagnostic is claimed.

Astro check: zero diagnostics. Build: 17 pages and six passing Node tests, with the existing nonblocking MDX/i18n/404 warnings. New C++17 extraction harness verifies all initialized-value checkpoints, unchanged inputs, quotient outcomes, empty output and SVG provenance. All eight preceding C++ harnesses pass. Chrome regression passes including the four new cards at desktop/mobile/narrow widths. Additional checks confirm local HTTP 200, four normal UML labels and all no-JS disclosures. The mobile partial-division card was visually inspected. Final rebuild covers the prose-only rounding clarification. No public deployment or practice repository change; downloads and assessments remain deferred.


## Explicit counter updates

Implemented option A approved on 2026-10-13: six independent snippets covering one update, successive updates, a nonzero initial value, deliberately faulty reset-to-one, batch addition and withdrawal. Five authoritative activity models supply six cards; the reset card explicitly labels the intended model versus the actual wrong-but-valid result. No new syntax, hardware IO, event detection, persistence or loop is implied.

Editorial rereading checked initialization versus reassignment, current value versus initial value, mathematical equality versus assignment, unchanged batch/withdrawal operands, bounded values and unimplemented preconditions. The reset contrast explains why the first update from zero masks the error. Each code block has its expected result, conception mapping and value trace. Existing card behavior is reused; no new practice publication, assessment, download or deployment.

Verification: Astro check has zero errors/warnings/hints. Build succeeds with 18 pages and six passing Node tests; existing MDX directive and optional i18n/404 warnings remain nonblocking. The new C++17 harness compiles all six actual snippets with warnings as errors, checks every initialized-value checkpoint, unchanged operands, alternate zero/full withdrawals, the nonzero reset contrast and the comprehension result 11. Execution has no output. Public SVGs match authoritative generated snapshots byte for byte.

Chrome regression passes at 1440/390/320px, including six cards on the new route, keyboard focus, close behavior, animation and no-JS disclosures. The mobile discrepancy card was visually inspected: its expected/actual explanation is readable, with scrollable content. The local development server was restarted on port 4322; the lesson returns HTTP 200. These checks establish technical consistency, not measured learner comprehension. No remaining blocking finding in the local review. README availability and explorer coverage descriptions were refreshed while adding the test command.


## First boolean values

Implemented option A approved on 2026-10-13: six independent examples introducing bool, true and false through known initialization, assignment and copying. Five authoritative activities back six cards. The last example deliberately repeats the valid true initialization under a different requirement and explicitly compares actual true against expected false. The source diagram describes the expected requirement, not the erroneous execution.

Editorial rereading checked true versus favorable outcome, false versus unknown, supplied information versus physical detection, independent copy versus automatic binding, and refresh versus retained initial history. All examples state the requirement before code; traces cover every instruction. No numeric conversions, hardware IO, comparisons, decisions, loops, new UI or speculative patterns were introduced. Complementary explorer content remains a future authoring gap, with no empty control or invented practice link.

Verification: all six actual excerpts compile in C++17 with warnings as errors. The new harness checks bool types, every initialized-value checkpoint, preserved copies, explicit refresh, the wrong-value contrast, empty output and byte-identical public/generated SVGs. Astro check reports zero errors/warnings/hints. Build produces 19 pages and all six Node tests pass; existing nonblocking MDX directive and optional i18n/404 warnings remain.

Chrome regression passes at 1440/390/320px, including all six new cards, closing/focus behavior and no-JS disclosures. Mobile discrepancy-card rendering was visually inspected. The running development server initially returned 500 because its content catalog lacked the new slug after hot reload; restarting it restored HTTP 200 on /notions/premiers-booleens/ without source changes. Local consistency is verified; learner mastery has not been measured. No deployment or practice repository changes.


## First strict comparison

Implemented approved option A: five independent snippets covering count 2/3/4 against the fixed fictional limit 3, reversed operands, and explicit recomputation after a count update. Four authoritative activities back five cards; the deliberately reversed snippet explicitly compares actual false to expected true. Updated the sidebar, prior boolean lesson, roadmap and availability count.

Editorial review checked the distinction between reaching/exceeding, comparison result type versus storage type, unchanged operands, observation versus enforcement, and a stored answer versus a live formula. The refresh trace includes the intermediate stale false at count four, not just the final true result. The reversed-operand table demonstrates that equality alone masks the bug. Diagrams model sequential evaluation/storage without fictional branches, temporaries or hardware actions.

Verification: the new harness extracts all five actual lesson snippets, compiles C++17 with warnings as errors, checks each initialized-value checkpoint, bool types, unchanged inputs, alternate counts 0/2/3/4/5, reversed-operand masking and empty output. Public SVGs match their authoritative rendered snapshots. Astro check reports zero errors/warnings/hints; the build produces 20 pages and six Node tests pass. Existing nonblocking MDX directive and optional i18n/404 warnings remain.

Chrome regression passes at 1440/390/320px, including all five new cards, keyboard/closing behavior, the discrepancy label and no-JS reading. Mobile discrepancy and scrolled refresh cards were visually inspected; the longer diagram retains its full-size SVG link for close reading. The local development server was restarted after content updates and /notions/premiere-comparaison/ returns HTTP 200. No shared UI, deployment or practice-repository change. Technical consistency is verified; learner mastery remains unmeasured.


## Strict versus inclusive comparison

Implemented owner-approved option A: five independent snippets compare the same two questions at counts 2, 3 and 4 against limit 3, then deliberately substitute each operator for the other at equality. Three authoritative activity models back five cards. Both discrepancy cards distinguish expected false/true from the actual false/false or true/true result. Sidebar, previous lesson, roadmap and introductory availability count are updated.

Editorial review checked inclusive meaning versus exact equality, initialization versus comparison, unchanged operands, stored answers versus physical enforcement, and consistent result order. Each excerpt includes requirements, UML correspondence and an instruction-by-instruction trace. The closing comparison table demonstrates why off-boundary inputs mask these substitutions, while equality alone masked the preceding lesson's operand reversal. No new shared UI or unrelated syntax was introduced.

Verification: all five actual snippets compile in C++17 with warnings as errors; the extraction harness checks every initialized-value checkpoint, bool types, unchanged operands, both substitutions at counts 2/3/4, empty output and byte-identical public/source SVGs. Astro check has zero diagnostics. The build produces 21 pages and six Node tests pass; existing nonblocking MDX directive and optional i18n/404 warnings remain.

Chrome regression passes at 1440/390/320px, including five new cards, focus/closing behavior and no-JS disclosures. Mobile checks verify both discrepancy labels and expected/actual text, with no page-wide horizontal overflow. The discrepancy and scrolled equality cards were visually inspected. The restarted local server returns HTTP 200 for /notions/atteindre-ou-depasser/. Technical consistency is verified; learner comprehension has not been measured. Deployment, practice publication, assessments and downloads remain outside this change.


## Less-than and at-most comparisons

Implemented refined option A approved on 2026-10-13: three boundary cases, a full-box transfer, then a deliberately reversed comparison. Five excerpts match the approved specification exactly in content and order; four authoritative activities back their cards. The transfer precedes diagnosis, and the equivalent swapped greater-than formulation is explained explicitly.

Editorial review checked independent snippets, initialization versus comparison, strict versus inclusive meaning, nonnegative-count assumptions, room for one item versus respecting current capacity, and observation versus enforcement. The error trace records actual false/true while the UML card explicitly states intended true/true. Published first/second-result trace rows were checked against the five expected cases. The four-operator recap is restricted to the integer domain. Companion explorer sheets remain a documented authoring gap; no empty control or invented practice link was added.

Verification: the new C++17 harness extracts all five actual snippets and checks every initialized-value checkpoint, bool types, unchanged inputs, reversed comparisons at 0/2/3/4/20, equivalent swapped expressions, box counts 7/8/9, silent execution and exact public/source SVG correspondence. Compilation uses -Wall -Wextra -Werror. Astro check reports zero errors/warnings/hints; build produces 22 pages and all six Node tests pass. Existing nonblocking MDX directive and optional i18n/404 warnings remain.

Chrome regression passes at 1440/390/320px, including all five cards, keyboard/focus/closing behavior and no-JS disclosures. Mobile checks confirm discrepancy text, transfer identifiers and no page-wide horizontal overflow. Transfer and discrepancy screenshots were visually inspected. The restarted local server returns HTTP 200 for /notions/en-dessous-ou-au-maximum/. No shared UI, deployment, practice repository or deferred assessment/download changes. Technical consistency is verified; learner mastery has not been measured.


## Exact equality and difference

Implemented owner-approved option A: exact target, lower value, higher value, integer-identifier transfer and a deliberate >= substitution. Five excerpts match the approved specification in content and order; four authoritative activities back their cards. The target name explicitly replaces the earlier upper-limit requirement. The lesson distinguishes declaration initialization from comparison, and difference from direction or distance.

Editorial review checked exact integer assumptions, input preservation, paired results versus automatic binding, supplied identifiers versus acquisition/authentication, and expected design versus faulty execution. All five first/second-result trace rows were checked against the intended actual outcomes. The compact final table shows that 2 and 3 mask the >= substitution while 4 reveals it. No assignment-in-condition pitfall, conversion, floating-point comparison, control flow or new UI is introduced. Companion explorer sheets remain an authoring gap; practice availability remains explicit.

Verification: the extraction harness compiles all five actual excerpts in C++17 with -Wall -Wextra -Werror and checks every initialized-value checkpoint, bool types, unchanged inputs, alternate counts 0/2/3/4/20, identifier values 5/7/9, silent execution and public/source SVG byte equality. Astro check reports zero errors/warnings/hints. Build produces 23 pages and all six Node tests pass; existing nonblocking MDX directive and optional i18n/404 warnings remain.

Chrome regression passes at 1440/390/320px, including five new cards, focus/closing behavior and no-JS disclosures. Mobile checks verify explicit expected/actual discrepancy text, identifier mapping and no page-wide horizontal overflow. Identifier and discrepancy screenshots were visually inspected. The restarted local server returns HTTP 200 for /notions/egal-ou-different/. No deployment, practice repository or deferred quiz/download changes. Technical consistency is verified; learner mastery remains unmeasured.


## First if and common continuation

Implemented owner-approved option A: four complete console programs teach executing/skipping a block, common continuation, identifier transfer and a deliberately misplaced common write. Three authoritative activities back four cards. The roadmap separates this module from the future else lesson. Each program matches the approved source and order exactly; published stdout blocks and the explicit silent-error description were checked.

Editorial review checked condition evaluation versus reading a stored bool, braces versus indentation, skipped versus executed actions, a false condition versus program termination, and normal exit status versus requirement satisfaction. Decisions and merges introduce no parallel execution. Corrected an engineering-doc wording ambiguity: not is used as a UML guard predicate here, but C++ also provides it as an alternative token for !; the lesson neither denies that fact nor introduces logical operators. Models and code behavior are unchanged. Companion explorer sheets remain an authoring gap.

Verification: four actual C++17 programs and twelve input configurations compile with -Wall -Wextra -Werror and produce exact expected stdout, empty stderr and exit status 0. Separate instrumented copies check initialized inputs/bool and their preservation through either path. Tests expose the misplaced write for counts 2/4 and confirm masking at 3. Public SVG snapshots match authoritative renders byte for byte. Astro check has zero errors/warnings/hints; build produces 24 pages and all six Node tests pass. Existing nonblocking MDX directive and optional i18n/404 warnings remain.

Chrome regression passes at 1440/390/320px, including four new cards, focus/closing behavior and no-JS disclosures. The new page has no page-wide horizontal overflow; discrepancy text is checked. Mobile false-path and discrepancy screenshots were visually inspected: the branch bypasses its write and merges before the common write; detailed SVG viewing remains available through the full-size link. The restarted local server returns HTTP 200 for /notions/premiere-condition/. No shared UI, deployment, practice repository, quiz or download changes. Technical consistency is verified; learner mastery remains unmeasured.


## First explicit alternative with else

Implemented owner-approved option A: five complete programs show a matched count, both directions of mismatch, identifier transfer and a deliberately false directional message. Four authoritative activity diagrams back five cards. Exact published snippets match the approved specification. The two false numeric examples deliberately change only the input; other sections add distinct transfer and error-analysis roles.

Editorial review distinguishes false equality from below-target meaning, bool initialization from later condition use, exclusive branches from shared continuation, and normal exit from requirement satisfaction. At count 2, the wrong message describes the relation accurately but still violates the required output; at 4 it also asserts a false relation. The discrepancy diagram explicitly shows intended behavior. Prerequisites, unavailable practice projects, navigation and availability counts are current. Companion explorer sheets remain an authoring gap, with no empty controls added.

Verification: tests/first-else.py compiles five actual published C++17 programs over 15 input configurations, with separate instrumented copies (30 compilation/execution checks), using -Wall -Wextra -Werror. Exact stdout, empty stderr, status 0, initialized and preserved state, bool types, approved source equality, displayed output contracts and public SVG provenance pass. Astro check reports zero errors/warnings/hints; npm test builds 25 pages and passes six Node tests. Existing nonblocking MDX directive and optional i18n/404 build warnings remain.

Chrome regression passes at 1440/390/320px, covering all five new cards, keyboard/focus/closing and no-JavaScript disclosures. Mobile discrepancy and above-target screenshots were inspected: the expected/actual distinction is explicit and both branches meet before the common write. Diagram labels are compact on mobile; the full-size SVG link remains available. No page-wide overflow was found on the new page at the inspected 390px viewport. The restarted local server returns HTTP 200 for /notions/premiere-alternative/. No shared UI, CI, deployment or practice repository changes. Technical checks do not measure learner mastery.
