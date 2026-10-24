# Observable variables - conception delivery review

Date: 2026-10-24. Issue: [#16](https://github.com/benoit-bremaud/cpp-learning-course/issues/16). Branch: `codex/16-observable-variables-conception`, from main `8712767`. The owner explicitly approved option A, its weights and concrete implementation plan: replace the primary CPP-01 fragment with one complete observed program, 460/500. Fallback C adds a missing-assignment program, 440/500; B retains both fragment and wrapper, 355/500. The [accepted specification](../../architecture/specs/observable-variables.md) records the matrix, sensitivity and full future file plan.

## Delivery and four-pass review

This separate conception delivery adds the specification, one activity source/render/note triplet and verification evidence. No lesson, public diagram, compiler harness, browser runtime, schema, navigation, package, lockfile or CI workflow changes are included. The existing CPP-01 page still contains its two-instruction fragment; the new complete program is a reviewed future contract.

Requirements and traceability: initialize measurement_count to 0, observe it, assign the supplied total 1, observe it again, then return success. The five conceptual activity actions cover all seven C++ statements explicitly: each observation consists of a value write followed by a newline write. The per-statement trace distinguishes current value, accumulated stdout and return status. No arithmetic, acquisition, input, redeclaration, conditions or helper functions are introduced.

Dependency direction and SOLID: authored content feeds the existing static reader; the future tests consume the authored source. The stock/copy sheets remain scoped fragments. The compiler harness must distinguish complete programs from fragments and retain existing fixed lesson inventories. No new runtime boundary or infrastructure coupling is needed.

KISS/YAGNI/DRY: one complete primary program replaces the fragment rather than repeating it. An inline identifier-versus-quoted-text comparison explains integer output without another full example or a syntax family. No pattern, class hierarchy, service or generalized test registry is justified.

Pattern/anti-pattern review: the principal risks are false acquisition semantics, hard-coded fake observations, stale two-action provenance, nesting a complete main inside the old fragment wrapper and weakened prior inventories. The concrete plan requires correcting the story, checking mapped variable reads, updating one public-source provenance pair, preserving nine other fragments and retaining the first-program and ordered-output exact contracts. These are tracked implementation responsibilities within #16, not claims that the current lesson has already changed. No remaining conception Must Have or Should Have finding was identified; no new Nice to Have item.

The original fragment conception and model remain historical/current-published evidence until the accepted implementation replaces that primary example. The extension governs the future complete program and requires explicit supersession of old framing at delivery. This avoids silently redefining earlier published evidence.

## Local verification

1. Tests: Astro check reports 0 errors, warnings and hints. The unchanged production site builds 12 pages and npm test passes 14/14 tests, including five complete programs and fourteen mutation probes. The ten current excerpts and six invalid-content probes pass. The exact future C++ program was separately extracted from the new specification, compiled with C++17/Wall/Wextra/Werror/pedantic-errors and executed with closed stdin and a timeout: stdout exactly `b'0\n1\n'`, empty stderr, exit 0. That study is not a replacement for future lesson extraction tests.
2. Coverage: browser runtime TypeScript coverage is 170/170 (100%), with the existing 80% floor enforced. Audited public TypeScript declarations have documentation 3/3 (100%); the public compiler-harness function is documented 1/1. Eighteen axe scans report zero violations; three incomplete contrast results contain sixteen diagnostics checked by the existing narrow top-layer/opaque-color/contrast guard. These denominators do not measure C++ coverage, all content semantics or complete accessibility conformance.
3. SonarQube: the committed delivery head receives a fresh scanner run with its exact SCM revision and current lcov before publication authorization. Record the result and compute task in the accompanying chat/PR body. A scan of the previous brick is not substituted for that evidence. Markdown pedagogy and UML are reviewed manually.
4. Secrets: full reachable-history and exact staged delivery-snapshot Gitleaks are required and checked before publication; no env files are tracked. Manual read found no credentials or sensitive data. Preserve generated SVG source-comment bytes, using Git's cr-at-eol whitespace check rather than editing generator output.
5. Product QA: [dated smoke report](../../architecture/qa/2026-10-24-observable-variables-conception.md). The production reader passes its existing Chrome, Firefox and WebKit suite, with keyboard/focus/dismissal, responsive/theme/motion, enlarged text, reload and native fallbacks. A direct Chrome path through the unchanged CPP-01 primary card also passes with zero page, console or failing HTTP responses. Screenshots show the existing fragment and card, not an implemented future program.

The new model uses 16px labels and natural dimensions 225px by 544px. Fresh PlantUML output equals the committed SVG bytes. The render was visually inspected; authored links, ASCII hyphens and whitespace were checked. The full-width paper and intrinsic sizing remain reader behavior and are unchanged by this delivery.

Existing build notices about head-inject, optional i18n content and default 404 remain nonblocking. CodeRabbit CLI is unavailable; structured local review and available checks provide the evidence. No independent CodeRabbit or Copilot review is claimed. Inspector/security-probe pass-level requirements are part of the accepted implementation acceptance; this documentation-only delivery uses smoke scope.

## Owner review and next gate

| Material point | Disposition |
| --- | --- |
| One complete primary program, no duplicate fragment | Keep - owner approved A on 2026-10-24 |
| Weights and fallback sensitivity | Keep - owner validated 25/30/30/15 and A 460/500 |
| One variable, supplied total, exact two observations | Keep - approved contract; compiled study matches |
| Five model actions covering seven statements | Keep - explicit grouping and fine-grained trace |
| Existing companions, reader, prerequisite links and lesson count | Keep - preserve existing implementation boundaries |
| Redeclaration, arithmetic, dependencies, punctuation sweep and practice publishing | Defer - separate future bricks or existing #7/#8/#3 scope |

Request separate authorization to push this committed conception and create its documentation PR with Refs #16. Do not close #16 in that PR. After its separately authorized merge, implement the accepted file plan on a fresh branch from updated main. Implementation publication, merge and branch deletion remain separately authorized. No course-specific GitHub Project is available from the existing routing; do not use V-SEA.
