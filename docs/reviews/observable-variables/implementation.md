# Observable variables - implementation delivery review

Date: 2026-10-24. Issue: #16. Branch: `codex/16-observable-variables-lesson`, from conception merge `0c2a81bf3a339648c5aec61461cab4c7595d5546`. Conception PR #17 was squash-merged after explicit owner authorization. This report records the local implementation and its unresolved local-preview gate; it is not a publication or merge approval.

## Implemented approved scope

CPP-01 now has one complete hosted C++17 program, reading measurement_count before and after literal assignment. Its exact stdout is `0\n1\n`, stderr is empty and exit status is 0. Five UML actions map all seven statements. The public snapshot matches the accepted observed-values model. Stock/copy companion sources, CPP-09, navigation, runtime scripts, dependencies and CI are unchanged.

The fixed compiler harness adds an explicit observable-variables mode. Its source contract rejects hard-coded output even when stdout matches. Twelve new mutations cover initial/assigned values, early assignment, quoted identifier, newline, stderr, status, missing/wrong/duplicate markers, extra fences and fake observations. The previous two- and three-program contracts remain fixed. The replaced fragment is removed from the generated wrapper; the other nine excerpts remain checked.

The MDX marker uses its required JSX comment syntax, retaining the accepted program identifier. Tests accept Markdown and MDX comment syntax. The first build exposed the unsupported HTML-comment form; the actual lesson now builds successfully.

## Local verification

1. Tests: CI Node 22.21.1, Astro check 0 errors/warnings/hints, production build 12 pages, full Node suite 17/17. Six complete programs meet their independent C++17 contracts. Twelve new mutations plus the fourteen earlier probes pass. Nine remaining excerpts retain their intermediate-value/negative controls. Six invalid-content build probes pass. Fifteen teaching fences remain fifteen.
2. Coverage: source-mapped browser runtime 170/170 lines (100%), 80% floor unchanged. Public TypeScript declarations documented 3/3 (100%); public compiler-harness function 1/1 (100%), module docstring present. Documentation contracts were read for freshness. These figures exclude test helpers and do not measure C++ branch coverage or pedagogical effectiveness. Twenty axe scans have zero violations; three incomplete results contain sixteen contrast diagnostics resolved by the unchanged narrow guard.
3. SonarQube: fresh lcov and an exact-SCM-revision scanner run are required on the final committed head. Its authoritative scanner result, compute-task ID and returned gate conditions are recorded in the prepared PR body and continuity file after commit. No prior brick's scan substitutes for this evidence. The optional sonar/CodeRabbit/CodeQL/act CLIs are absent; the established sonar-scanner is used without changing integration or credentials.
4. Secrets: full reachable history (42 commits before this delivery), exact delivery snapshot and production dist scanned with Gitleaks; no tracked env files, source maps or manually observed credentials. SVG generator bytes are preserved and checked using cr-at-eol whitespace handling. Final committed history is scanned again before any authorized push.
5. Product QA: [dated pass report](../../architecture/qa/2026-10-24-observable-variables.md). Production Chrome, Firefox and WebKit validate reading, main card, companion explorer, keyboard/focus, dismissals, 320/390/1440, theme/motion, 200% text, reload and native fallbacks. Additional Chrome tablet/landscape, inspector and safe local security probes are recorded there. **SEC-01 remains BLOCKED pending owner disposition of the local-preview-only header boundary.** The whole gate is not yet green, despite passing functional and accessibility checks.

The accepted source/render/public snapshot are byte-identical after a fresh PlantUML render: natural 225x544, labels 16px. The white panel spans content width, image is centered and never enlarged. All seven statements map in execution order. Main page objectives are understandable without companions; stock/copy and CPP-09 are byte-unchanged from main. Direct prerequisites and navigation remain unchanged. The scoped CSS extension changes no colors, runtime script, diagram geometry, card delay/fade or reduced-motion behavior.

Existing build notices about head-inject, optional i18n and default 404 remain nonblocking. npm audit could not reach a trusted registry audit endpoint because of a self-signed certificate chain; no advisory count or audit pass is claimed and TLS was not weakened. No manifest/lockfile changes; dependency issue #7 remains deferred.

## Structured local diff review

- Requirements/traceability: OV-01 through OV-06 verified by actual extraction, source-to-mapping assertions, provenance tests and manual French-content review. OV-07 through OV-09 functional/coverage/secrets checks are recorded above; exact-head Sonar follows commit. OV-08's SEC-01 needs explicit owner disposition. OV-10 publication remains pending.
- Dependency direction and SOLID: authored MDX and CSS feed the existing static reader; fixed contracts consume actual lesson source. No backend, schema, component, browser runtime, dependency, workflow or navigation change.
- KISS/YAGNI/DRY: one program replaces one fragment. Three fixed harness modes reuse the existing compiler loop. A source-token assertion is intentionally a fixed teaching contract, not a general C++ parser. Scoped table rules address an observed failure without generalizing the reader.
- Patterns/anti-patterns: no new pattern warranted. The fake-output mutation reads/discards the variable only to avoid the compiler's unused-variable warning, then demonstrates that matching stdout alone is insufficient. No mutation executes an uninitialized read.
- Must Have: table overflow/scrollability found by the new narrow scan, addressed by the explicitly approved scoped extension and regression assertions. SEC-01 remains a blocked validation decision, not silently waived.
- Should Have: none outstanding in the reviewed lesson/test diff. No new Nice to Have finding. External review tools unavailable are disclosed above; no independent review is invented.

## Final owner review

| Material item | Proposed disposition and evidence |
| --- | --- |
| One complete program reading the same variable before/after assignment | Keep - approved A, actual execution and fake-output rejection |
| Five actions, seven mapped statements and source provenance | Keep - exact mapping and fresh render equality |
| Supplied-total story, safe initialization, output versus exit status | Keep - reviewed French explanation and chronological trace |
| Reader/companions/navigation/practice boundaries | Keep - unchanged sources and existing tests |
| Scoped table reflow | Keep - extra file/weights/option A explicitly approved, 485/500, narrow scans pass |
| Local preview deployment-header check | Investigate/owner disposition - SEC-01 BLOCKED, no production deployment or policy configuration in scope |
| Dependencies, punctuation, future prerequisites and standalone practice | Defer - separate #7/#8/#3 or future reviewed bricks |

No push, implementation PR, merge or branch deletion is authorized by the conception or layout approvals. A concrete final review must resolve the local QA boundary and separately authorize publication. No Copilot review will be requested.

## Approved conception adjustment - table reflow

The approved file inventory excludes shared CSS. Browser measurements show Starlight's display:block tables ignore the intended fixed-column layout: at 320px, the main card table has client width 270px and scroll width 357px; two prose tables also overflow. Making the tables keyboard-focusable addresses one axe rule but leaves clipped-cell contrast diagnostics. This is not accepted as completion.

A temporary browser-only experiment applies three scoped rules: display:table/width:100%/table-layout:fixed on table.observable-values; overflow-wrap:anywhere on its header/data cells; white-space:normal on its inline code. All four table scroll widths then equal their client widths (card 270px, prose 288px), with zero axe violations or serious incomplete results. The owner then explicitly approved A and its weights. The three scoped rules are now implemented, with a dedicated class on all four tables.

Approved additional file: `src/styles/custom.css`. Option A applies the scoped class to only CPP-01's four tables, removes interim wrappers, and adds explicit table-overflow checks to the already-approved browser test files. Preserve card timing, reduced motion, diagram geometry and all other architecture. Rerun the full suites after approval.

| Criterion | Weight | A: scoped class | B: existing UML rules | C: keyboard scrolling |
| --- | ---: | --- | --- | --- |
| Reflow and accessibility | 35 | 5: experiment passes | 5: experiment passes | 2: sideways navigation remains |
| Regression exposure | 30 | 5: four tables only | 3: other UML panels affected | 5: local markup |
| Responsibility clarity | 20 | 5: explicit table styling | 3: prose uses UML styling | 4: native scrolling |
| Estimated maintenance | 15 | 4: three scoped rules | 5: two existing-rule edits | 4: keyboard/manual contrast checks |
| Total | 100 | 485/500 | 400/500 | 360/500 |

Scores are design judgments, not measured probabilities. A beats B by confining the correction to this lesson. Transfer 15 points from regression exposure to maintenance: A 470, B 430. B is the fallback and requires broader regression verification. The owner explicitly approved these weights and option A on 2026-10-24; the authoritative specification records the extension. No push, PR, merge or deletion is authorized.
