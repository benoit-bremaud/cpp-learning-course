# Arithmetic update - implementation delivery review

Date: 2026-10-27. Issue: [23](https://github.com/benoit-bremaud/cpp-learning-course/issues/23). Branch codex/23-arithmetic-update-lesson from main37d4b8cb38c40d07544c419de718ad122e169bf0, after owner-authorized squash merge of conception PR24. [Approved A conception](../../architecture/specs/arithmetic-update-lesson.md):455/500, evidence30/focus30/continuity25/maintenance15. Local implementation approved; publication, merge and deletion are separate permissions.

## Implemented scope

The new French page /notions/premiers-calculs/ teaches one central operation: read an initialized small int, add1, then assign the result to that same object. Its independently copyable programs start2 and produce2/3 versus2/1. Both return0 with empty stderr. Literal replacement is valid C++ with a different outcome, not a compiler error. The page explains RHS read/LHS store, one assignment statement, no algebraic equation or retained formula, no autonomous event, why starting0 hides the distinction and why fixed3 can fake one baseline. Overflow/type representation and +=/++ are deferred. No input, hardware, helpers or loops are introduced.

Both five-action activities map all seven statements; two writes form each observation and read/add/store remains one assignment. Sources exactly match the approved conception. Public SVGs exactly match authoritative deterministic renders,235x544 and225x522 with16px labels. Content-wide white panels preserve intrinsic centered diagrams, shrinking only to fit. Existing cards,80ms delay/160ms fades, reduced motion, native fallback and companion schema are preserved.

Navigation adds the sixth introduction after CPP-09, with direct CPP-01 prerequisite. CPP-09 only gains the next link; earlier source contracts remain unchanged. Home/progression availability and architecture mappings agree. CPP-02 remains reserved for integer representation. The separate workshop-total initialization is not claimed as published self-update practice.

The fixed all-success harness adds two contracts without a registry or runtime compiler. Expected markers derive from actual fixed keys while existing diagnostics remain identical. Exact intent rejects fake literal3 and fake observations. Twenty new safe mutation cases join48 previous probes. No undefined/uninitialized mutation executes. Total17 teaching fences:10 complete successes,1 complete rejected source,6 fragments. The existing invalid-source runner and fragment harness are unchanged.

One necessary file-plan consequence: tests/ordered-output.test.mjs has a single global availability assertion changed five->six, matching the approved navigation addition. No older behavior assertion is removed. No CSS, component, runtime script, schema, companion, dependencies, lockfile, workflow or practice edit.

## Five local gates

1. Tests: Node22.21.1, Astro check0 errors/warnings/hints; fresh13-page production build; npm test23/23. Actual lesson excerpts compile GCC15.2.0 C++17 with Wall/Wextra/Werror/pedantic-errors, bounded execution/closed stdin, exact bytes/empty stderr/status0. Ten successes, compile-only rejection and paired successful controls pass. Six fragments/intermediate assertions/boundary mutation and six invalid-content build probes pass. Chrome/Firefox/WebKit production regression passes: identities, mappings, keyboard/focus, dismissal/reload,320/390/768/1440, dark/reduced-motion,200% text, fallbacks, CPP-09 next/new previous, search and original SVG links.
2. Coverage: browser TypeScript170/170 lines=100%, existing80% floor retained. Public production TypeScript doc blocks3/3; public functions in the two complete-program validation modules2/2. Private test helpers excluded; contracts read for freshness. This is not C++ branch or learning coverage.34 axe scans have zero violations;8 incomplete results contain26 contrast diagnostics resolved by the unchanged narrow guard.
3. SonarQube: fresh lcov and exact final committed SCM revision scanned before publication approval. Returned gate conditions and CE task go in the publication body/resume note; no old scan substitutes. Markdown/UML semantics are manually reviewed.
4. Secrets: full reachable public history, exact staged delivery snapshot, production dist and retained QA evidence scanned with Gitleaks before publication. No tracked env files/served source maps; full manual diff read found no sensitive material. SVG bytes preserved, cr-at-eol whitespace check used.
5. Product QA: [dated pass and inspected screenshots](../../architecture/qa/2026-10-27-arithmetic-update.md).25 successful loopback responses, zero all-level console messages/page errors/failed requests; no WebSocket/cookies/third party. Search payloads inert, offline card usable. Mobile4xCPU/150ms latency: LCP1160ms, CLS0, event durations<=32ms. SEC-01 BLOCKED pending fresh owner disposition; whole gate not yet claimed green.

npm audit remains unavailable because of a self-signed TLS chain; TLS is retained and no advisory-clean result is claimed. No dependency change;7 stays deferred. Optional CodeRabbit/CodeQL/act CLIs absent; this is structured self-review with available checks, not an independent reviewer claim. No Copilot requested. The separate comprehensive QA campaign remains deferred.

## Structured full-diff review

Requirements: REQ9..16 realized by two actual-source contracts, source-intent/fake-result mutations, seven-statement mappings, French reasoning and honest availability. NFR5 provenance/layout and NFR6 available gates pass, with exact-head Sonar recorded after commit; NFR7 security boundary requires disposition. NFR8 publication boundaries remain separate.

Dependency direction/SOLID: authored page/model feeds the existing static build; tests consume actual source and fixed expectations. No new runtime dependency, framework layer or API. KISS/YAGNI/DRY: independently copyable repetition is intentional approved contrast; reuse existing fixed harness and table styling, no helper/registry/pattern without a present force.

Anti-pattern review: nonzero baseline distinguishes calculation/replacement; exact intent blocks hardcoded3/fake observations; literal1 remains actual legal behavior against required3. Observing does not change the object, elapsed time triggers nothing, one arithmetic update executes. No unbounded-int promise or published-practice claim.

Must Have: SEC-01 local-preview disposition before publication. Test-only marker targeting, global count and temporary capture defects corrected and reverified. No remaining functional Must/Should or new Nice finding in the scoped review. Earlier48 mutations and runtime coverage guard are retained.

## Final owner review and SEC-01 proposal

| Material point | Proposed disposition |
| --- | --- |
| Two complete programs and current-value dependency | Keep: approved A, actual outputs2/3 and2/1 |
| Five-action/seven-statement diagrams and cards | Keep: exact mappings, deterministic provenance and browser checks |
| Prerequisite, navigation, six introductions and practice boundary | Keep: checked current progression, no CPP-02 identity claim |
| Local deployment headers/banner | New limited waiver requires owner approval |
| Input, other operators, representation, hosting and comprehensive QA | Defer: outside approved brick |

Scores below are decision judgments, maintenance estimates, not measured risk probabilities. Weights sum100. A accepts absent deployment headers/generic banner only for this local-preview delivery; future hosting must independently validate them. B expands into a separate hosting-security study now. C holds the lesson until future hosting. No choice is already authorized.

| Criterion | Weight | A: local-only waiver | B: hosting now | C: hold delivery |
| --- | ---: | --- | --- | --- |
| Approved lesson scope |35|5: no infrastructure change|1: expands scope|4: preserves code scope but couples completion|
| Evidence clarity |30|4: explicit local gap and future obligation|5: actual hosting can be validated after study|3: known gap stays unresolved|
| Deliverable continuity |20|5: reviewed lesson can proceed|1: new prerequisite|1: no delivery progress|
| Estimated maintenance |15|4: bounded dated waiver|2: new host/policy work|3: deferred coordination|
| Total |100|455/500|235/500|295/500|

A vs C: A permits the reviewed lesson delivery with an explicit boundary; C leaves the same known local gap and stalls the lesson. A vs B: B can prove real hosting policy but introduces unapproved infrastructure work. Transfer20 points scope->evidence: A435/B315/C275. A remains preferred. Runner-up C295 is a workflow hold, requiring no code change but delaying completion. Hosting work B235 needs a separately reviewed scope. No production safety/exposure conclusion is inferred.

Explicit owner approval is required for the concrete final delivery, the new limited waiver, and push/PR. No merge, deletion, discussion resolution or external review request follows from local completion.
