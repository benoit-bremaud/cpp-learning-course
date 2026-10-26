# Arithmetic update - conception delivery review

Date: 2026-10-26. Issue: [#23](https://github.com/benoit-bremaud/cpp-learning-course/issues/23). Branch: codex/23-arithmetic-update-conception, from main 060c545. The owner explicitly approved A and weights 30/30/25/15: two independently copyable complete sources contrasting an arithmetic update with a supplied literal, 455/500. B scores 445/500 and C 400/500. The [accepted specification](../../architecture/specs/arithmetic-update-lesson.md) records per-cell reasons, sensitivity, fallback and concrete future file plan. Transfer five points from evidence to reading focus ties A/B at 450; ten favors B 455 against A 445. These are editorial decision judgments, not measured learning results. Activating B requires a revised approved plan.

## Scope and four-pass review

This separate conception delivery adds the specification, two activity triplets, scoped glossary/traceability entries and review/smoke evidence. No lesson, public asset, test, navigation, runtime, CSS, dependency, lockfile or workflow is changed. The new route remains a future implementation. Existing CPP-09 still displays its complete const sources; screenshots show current page context, not a shipped arithmetic lesson.

Requirements: initial 2 makes calculation 2 + 1 -> 3 observably different from literal replacement -> 1. Initial 0 would hide the distinction. A fixed literal 3 still matches baseline output, so future source-intent assertions and a fake-result mutation are explicit requirements. Five actions map seven statements per source; reading, adding and storing remain one assignment action. No algebraic-equality, retained-formula, autonomous recount or physical-event claim is allowed.

Dependencies/SOLID: authored content/model feeds the existing static reader, tests consume actual authored source and fixed observations. Another all-success lesson reuses the established program-output runner; diagnostic identity must follow expected keys rather than cardinality, preserving existing messages and contracts. The mixed const-rejection runner stays unchanged. No new infrastructure or domain/framework boundary is justified.

KISS/YAGNI/DRY: two short whole files make the contrast independently reproducible. Known wrapper repetition is the accepted reading cost. Reuse the current table class and cards; no helper, explorer, generic registry, style extension or design pattern has a present force.

Anti-patterns: zero-baseline ambiguity, fake literal output, update portrayed as algebraic equality, invented events, signed overflow, stale availability/navigation and false practice alignment are covered by the explicit plan. The practice workshop total initializes a separate sum and is not presented as a dedicated self-update exercise. New reading does not take CPP-02's reserved integer-representation identity. Homepage availability corrections are scoped to adding the sixth intro, not a redesign.

The initial local review identified no Must Have or Should Have finding; Codex subsequently found the traceability introduction error documented in Round 1 below. No new Nice to Have item. This is structured local self-review, not an independent reviewer claim. Source/companion/schema/runtime boundaries were read before proposing changes.

## Five local validation gates

1. Tests: CI Node 22.21.1, Astro check zero errors/warnings/hints, fresh 12-page production build, npm test 20/20. Existing eight executable complete programs, one complete rejected source and its successful controls retain their contracts. Six remaining fragments/intermediate/boundary checks and six invalid-content probes pass. Exact new specification sources match the separately executed strict C++17 studies: stdout 2\n3\n and 2\n1\n, empty stderr, exit 0. The two-update alternative produces 2\n3\n4\n; zero-start alternatives both 0\n1\n; fixed literal 3 matches 2\n3\n. No undefined/uninitialized case is executed. These are conception studies, not future lesson extraction tests.
2. Coverage: browser TypeScript 170/170 lines, 100%, existing 80% floor retained. Public TypeScript declarations documented 3/3; public program-harness functions documented 2/2. Contracts were read for freshness; presence ratios do not measure pedagogy. Twenty-eight axe scans report zero violations; six incomplete results retain 22 diagnostics resolved by the unchanged narrow contrast guard.
3. SonarQube: fresh lcov and a fresh exact-final-SCM-revision scanner run are required before publication authorization. Record the gate conditions, revision and compute task in the publication body and resume note after commit. No scan from #20 substitutes for this delivery's scan. Markdown/UML semantics receive manual review.
4. Secrets: full reachable-history and exact staged delivery snapshot Gitleaks before publication, plus QA evidence scan. No tracked env files or manually observed sensitive diff data. Generated SVG bytes are preserved; whitespace uses cr-at-eol handling.
5. Product QA: [dated smoke report](../../architecture/qa/2026-10-26-arithmetic-update-conception.md). Existing production Chrome/Firefox/WebKit regressions cover keyboard/focus, all card identities, narrow/tablet/desktop/theme/motion, text enlargement, reload and native fallbacks. A direct current CPP-09 Chrome path captures desktop/mobile context with zero all-level console/page/network failures. This routine regression/smoke evidence is not the deferred comprehensive QA campaign.

Both fresh headless activity renders equal their authoritative SVGs, with 16px labels and natural sizes 235x544 and 225x522. The PNG previews and smoke screenshots were visually inspected. Authored links and ASCII hyphens were checked. White-panel/intrinsic sizing remains unchanged reader behavior, not a newly implemented #23 layout.

CodeRabbit CLI is unavailable; no CodeRabbit or Copilot review is claimed. Existing nonblocking build notices remain. The known npm audit TLS-chain limitation is not reclassified as an audit pass; no manifest or lockfile changed. #7 remains separate. This docs-only smoke does not extend the #20 local-preview header waiver. The future implementation must perform the appropriate inspector/security applicability pass and obtain any needed disposition separately. The owner deferred a separate comprehensive QA campaign; no such campaign or automation was started.

## PR #24 - Round 1 traceability correction

Codex comment [4376466793](https://github.com/benoit-bremaud/cpp-learning-course/pull/24#discussion_r4376466793) was verified exact against the matrix and both specifications. The original file-level sentence said all requirements below were defined in the constants specification, while REQ-9..16/NFR-5..8 belong to the arithmetic specification. The owner validated Must Have (factual documentation error), weights 50/25/15/10 and correction A on 2026-10-26.

The correction makes the introduction feature-neutral, gives the original #20 table its own heading and scopes its specification statement to that section. The existing #23 heading/source remains distinct. No requirement ID, table row, mapping, code, model, test or public asset changes. The two authoritative sources are now unambiguous without duplicating their correspondence in a global index sentence.

| Criterion | Weight | A: section-scoped sources | C: both sources in global introduction | B: retain wording |
| --- | ---: | --- | --- | --- |
| Correctness | 50 | 5: each section names its source | 5: both sources named | 0: false attribution remains |
| Targeted correction | 25 | 5: headings only, mappings unchanged | 4: source correspondence repeated globally | 5: no edit |
| Readability | 15 | 4: one extra section heading | 5: references grouped at top | 1: ambiguous scope |
| Estimated maintenance | 10 | 5: each section owns its reference | 3: global list follows additions | 1: ambiguity retained |
| Total | 100 | 485/500 | 455/500 | 150/500 |

Scores are owner-validated decision judgments. Transfer all ten maintenance points to readability and A/C tie at 475/500. C is the valid compact fallback, requiring a revised wording choice; B's correctness zero blocks merge. The owner selected A despite that sensitivity.

Local correction read-through verifies both section scopes, all local links and unchanged table rows. The routine full test/coverage/production-browser gates are rerun for the corrected delivery, followed by exact-head Sonar and history/snapshot secrets checks. Their final head and scanner task are recorded in the PR description and resume note. The separate comprehensive QA campaign remains deferred. No independent reviewer or active security pass is claimed. After this correction, no known conception Must Have or Should Have remains locally; the new remote head still requires review. Inline reply, push and any review retry remain separately authorized; do not resolve the conversation.

## Owner dispositions and next gate

| Material point | Disposition |
| --- | --- |
| Two complete contrast programs with nonzero start | Keep - owner approved A 455/500 |
| Weights, close margin and fallback sensitivity | Keep - owner validated 30/30/25/15 |
| Five actions/seven statements and one read-compute-store assignment | Keep - accepted mapping and executed study |
| Reuse fixed success harness, preserve previous inventories/messages | Keep - approved proportional plan |
| Reader, CSS, schema, companions and separate practice repository | Keep - unchanged boundaries |
| +=, ++, other operators, input, loops, range study and dedicated exercise | Defer - future reviewed bricks |
| Comprehensive site QA campaign | Defer - explicit owner instruction; routine gates retained |

Request separate authorization to push the committed conception and create its documentation PR with Refs #23. Do not close the implementation issue in this PR. After a separately authorized conception merge, implement the approved plan on a fresh branch from updated main. Implementation publication, merge and deletion remain separate approvals. No matching course-specific GitHub Project is configured; no V-SEA routing is inferred.
