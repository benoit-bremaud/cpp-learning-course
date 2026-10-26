# Observable constants - implementation delivery review

Date: 2026-10-26. Issue: [#20](https://github.com/benoit-bremaud/cpp-learning-course/issues/20). Branch: codex/20-observable-constants-lesson, from main 42c6422 after the owner-authorized squash merge of conception PR #21. Conception A, weights 35/25/25/15 and concrete file plan were explicitly approved: 445/500. [Accepted specification](../../architecture/specs/observable-constants-lesson.md).

## Implemented scope

CPP-09 replaces its three scoped fragments with three complete marked sources. The primary program observes (limit 3, count 0), stores supplied count 1 and observes (3,1). The wrong program differs only at initialization, preserving constant 30 against required 3. Their exact outputs are 3\n0\n3\n1\n and 30\n0\n30\n1\n, empty stderr, status 0. The invalid file attempts direct constant assignment; it is compiled only and rejected. Two independently successful controls remove const or remove only the forbidden assignment. No localized compiler message is used as the test oracle. The actual GCC 15.2.0 diagnostic was verified under LC_ALL=C and its filename sanitized in teaching text.

Two accepted six-action activities map twelve statements each. The rejected card qualifies all five statements against expected conception and marks writes/return nonexecuted; no successful rejected execution is invented. Public/source snapshots match exactly. The original activity stays historical. The lesson distinguishes unchanged value, correct initial requirement, output and process status, without acquisition, arithmetic or capacity enforcement. Optional threshold transfer remains nonessential guided reading.

The dedicated constant-limit runner avoids changing the existing three-mode all-success program harness. Actual page extraction and 22 mutations protect fixed inventory, values, update timing, const, quoted names, fake literal observations, newline, stderr, status and compiler rejection for the intended reason. The six prior executable programs stay checked. Three CPP-09 fragments leave the wrapper, preserving all six remaining excerpts and the existing boundary mutation. Fifteen teaching fences remain fifteen: eight executable complete sources, one complete rejected source and six fragments.

No component, script, CSS, content schema, navigation, package, lockfile or workflow changed. Existing observable-values table styling is reused through plain HTML class attributes. Reader/card timing, reduced motion and native fallbacks are unchanged. Companion sheets are unchanged. No standalone practice or deployment is implied.

## Local verification - five gates

1. Tests: CI Node 22.21.1; Astro check zero errors/warnings/hints; fresh 12-page build; npm test 20/20. Eight executable complete programs and one compile-only rejected source meet their contracts. The new 22 mutations join the 26 prior probes. Six remaining fragments, intermediate assertions and boundary mutation pass. Six invalid-content build probes pass. Chrome/Firefox/WebKit cover the current production bundles, all three CPP-09 card identities, rows, keyboard/focus, dismissal/reload, 320/390/768/1440, dark/reduced-motion, 200% text, native/no-JavaScript fallbacks, actual CPP-01 -> CPP-09 progression and original SVG links.
2. Coverage: browser TypeScript 170/170 lines (100%), existing 80% floor retained. Public TypeScript declarations documented 3/3; public program harness functions 2/2, with module/doc contracts read for freshness. These counts exclude private test helpers and do not measure pedagogy or C++ branch coverage. Twenty-eight axe scans have zero violations; six incomplete results contain 22 contrast diagnostics resolved by the unchanged narrow guard.
3. SonarQube: fresh lcov and the exact final committed SCM revision are scanned before publication authorization. Record returned gate conditions and compute task in the publication body and resume note; no previous scan substitutes for that evidence. Markdown pedagogy and UML are reviewed manually.
4. Secrets: full reachable history, exact staged delivery snapshot, production dist and QA evidence scanned with Gitleaks before publication. No tracked env files or served source maps; manual diff read found no credential or personal-data exposure. Preserve generated SVG bytes, with cr-at-eol whitespace checking.
5. Product QA: [dated pass report](../../architecture/qa/2026-10-26-observable-constants.md). Inspector captures all console levels, request/response metadata, failures, WebSockets and storage. Twenty-five loopback responses, zero console messages/page errors/failed requests; no WebSocket, cookie or third-party request. Search XSS stays inert; loaded reading/cards work offline. Throttled mobile trace: LCP1264ms, CLS0, event durations <=48ms. SEC-01 remains BLOCKED pending a new local-preview-only owner disposition; the whole validation gate is not claimed green yet.

New models remain 239x649 with 16px labels, centered without enlargement on content-wide white paper. Provenance is exact, all twelve/five statements map in order, and valid/invalid/wrong interpretations remain explicit. Screenshots show the full claimed code/result or diagnostic; the narrow card image is labelled as its scrollable top only.

Existing nonblocking build notices remain. npm audit failed because of a self-signed certificate chain; no audit pass or advisory count is claimed and TLS verification was retained. No dependency changes; #7 is deferred. Optional CodeRabbit/CodeQL/act CLIs are unavailable; structured local review and available checks are recorded, with no independent reviewer claim. No Copilot review is requested.

## Structured full-diff review

Requirements: REQ-1..8 are covered by actual-source execution, source-intent assertions, isolated compiler controls, meaningful mutations and exact rendered mappings. NFR-1..3 provenance, regression, coverage, security/QA evidence are above, with SEC-01 explicitly pending. NFR-4 approval boundaries remain separate.

Dependency direction/SOLID: authored content/model feeds the existing static build; tests consume actual sources and fixed observations. The compile-rejection runner has one bounded responsibility, without generalizing the established all-success runner. No domain/framework seam is manufactured.

KISS/YAGNI/DRY: one existing page, three existing card keys, no new runtime pattern. Known whole-file syntax repeats only to permit independent copying. Existing table reflow rules solve layout without a CSS extension. No helper function enters teaching code.

Anti-patterns: matching output cannot excuse fake observations or missing const; compiler failure cannot excuse malformed baseline; actual wrong behavior cannot redefine required 3; diagrams cannot portray a rejected translation unit as executing. The tests and French explanations preserve these boundaries. No undefined/uninitialized mutation is executed.

Must Have: the local-preview header boundary needs owner disposition before publication. The test-only identity assertion and temporary screenshot clipping defects are corrected and reverified. No remaining functional Must Have or Should Have finding; no new Nice to Have item. Reader/runtime/CI changes are not needed.

## Final owner review and local-preview disposition

| Material point | Proposed disposition |
| --- | --- |
| Three complete sources with independent outcomes | Keep - approved A, actual C++17 observations |
| Both six-action models and qualified compile-only reference | Keep - exact mappings/provenance |
| Constant semantics, supplied count and requirement correctness | Keep - reviewed French story and trace |
| Existing reader, tables, progression and practice boundary | Keep - unchanged architecture, measured regressions |
| Local preview deployment headers | Investigate/owner waiver required - specific #20 decision, no inherited waiver |
| Arithmetic, input, dependencies, punctuation and deployment | Defer - separate future bricks or #7/#8/#3 |

Recommended SEC-01 disposition A: accept only the absent deployment headers/generic server banner on this local-preview lesson delivery; future hosting must independently validate security policy. B expands into a separately conceived hosting-security brick before publication. C holds this lesson until that future work. No option is already authorized. Proposed weights total100; scores0..5 are decision judgments, not measured risk reductions.

| Criterion | Weight | A: limited local waiver | B: hosting work now | C: hold delivery |
| --- | ---: | --- | --- | --- |
| Approved lesson scope | 35 | 5: no infrastructure change | 1: expands scope | 4: preserves code scope but couples completion |
| Evidence clarity | 30 | 4: explicit local gap, future hosting remains open | 5: can verify actual hosting after a new study | 3: known gap stays unresolved |
| Deliverable continuity | 20 | 5: reviewed lesson can proceed | 1: separate infrastructure prerequisite | 1: no delivery progress |
| Estimated maintenance | 15 | 4: bounded dated waiver | 2: new host/policy work | 3: deferred coordination |
| Total | 100 | 455/500 | 235/500 | 295/500 |

Sensitivity: move20 points from scope to evidence: A435, B315, C275. A remains preferred under this scope-based judgment. B is a separate reviewed fallback if the owner requires deployment policy now; it cannot be implemented under the current lesson plan. No production exposure or host safety is inferred from the local waiver.

Publication requires explicit final owner approval of this concrete delivery, its limited SEC-01 disposition and push/PR. Merge/deletion remain separately authorized. The inherited npm audit infrastructure limitation is disclosed, not silently counted as a successful audit.
