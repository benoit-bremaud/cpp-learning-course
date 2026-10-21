# Example reader and UML card pilot — local review

Date: 2026-10-21. Work item: [#6](https://github.com/benoit-bremaud/cpp-learning-course/issues/6). Branch: `codex/example-reader-pilot`, based on `main` revision `7dc6347` after PR #5. Status: local implementation under joint owner review; no push or PR authorized. The historical branch `codex/repeated-decision-design` remains intact.

## Implemented scope and traceability

| Contract | Local realization | Evidence |
| --- | --- | --- |
| EX-01/02 | Two categories, manual tabs, first-sheet reset, native selector for multiple sheets | Production browser checks and unpublished multi-sheet fixture |
| EX-03/04 | Four self-contained French sheets; primary UML before code; ten authored code-to-UML disclosures | Output tests, C++ harness, manual editorial review |
| EX-05/06 | Native modal, one reading scroller, persistent header/close controls, focus/position return | Desktop, 390px, 320px, keyboard and text-enlargement checks |
| EX-07/08 | French narrative/UI, English code, no browser execution; pinned practice reference unchanged | C++ extraction, link/asset checks, manual provenance review |
| EX-09 | Static Markdown collection and ordered host IDs | Six isolated invalid-content build probes |
| UML cards | Native auto-popovers, outside/Escape/Close dismissal, scoped content moved without cloning | Production smoke, source-mapped DOM tests, accessibility scans, opacity-frame checks |
| Fallback | Original disclosures and companion articles remain readable | No-JavaScript and unsupported-popover browser contexts |

CPP-01 introduces only the accepted `measurement_count` initialization at 0 and assignment to 1. The stock and copy sheets implement P1/P2. The guided indicator retains its published strict function and pinned links; P3/P4 are separate companion contracts. CPP-09 receives the three previously accepted mapping-inventory excerpts, without importing the historical branch's later lessons, prerequisites or progression changes.

No new runtime package, database, content request, persistence, browser compiler, class hierarchy or GoF pattern is introduced. The source files have separate responsibilities: collection metadata, static rendering, dialog navigation, card enhancement and presentation. The accepted conception remains in `docs/architecture/specs/`.

## Automated validation

- `npm run check`: zero errors, warnings or hints.
- `npm test`: production build plus eight output/content tests pass; ten static pages generated.
- `python3 tests/example-code.py`: all ten actual C++ excerpts checked, including intermediate values, independent copy, valid-domain reservoir boundaries, strict/inclusive boundaries, rejected const assignment and a boundary mutation that must fail.
- `python3 tests/explorer-invalid-content.py`: build rejects duplicate IDs, unknown category, missing prerequisite page, missing sheet, duplicate host reference and empty pilot category. Source mutations occur in a temporary copy.
- `npm run test:browser`: source-mapped V8 line coverage of the two authored browser modules is 170/170 (100%); the runner enforces an 80% floor. This measures line execution, not branch completeness, teaching quality or Astro rendering coverage. Build-time collection configuration is exercised by integration probes and excluded from the browser coverage denominator.
- Nine axe-core scans of course pages, dialogs and cards report no WCAG A/AA violations. Scans wait for the accepted fade to settle. Full incomplete-result diagnostics remain visible in `coverage/accessibility.json`. Review found and fixed an unnamed-role ARIA labeling issue by making the focusable reading container a named region. axe still reports a native-popover overlap uncertainty for two text nodes; the test resolves only this exact case by checking browser hit order, an opaque settled background and a contrast ratio of at least 4.5:1 using axe’s color calculation. Other serious/critical incomplete results fail the suite. This does not establish complete accessibility conformance or replace assistive-technology testing.
- Public TypeScript documentation presence: 3/3 exports, 100%, counted using the TypeScript AST. Contract quality/freshness also inspected manually.
- All ten local PlantUML sources render via `plantuml -tsvg -pipe`; seven copied snapshots are byte-identical to their authoritative local SVGs. The published strict indicator snapshot is unchanged.
- Gitleaks: no leaks in the full reachable history or in a temporary copy of the non-ignored working snapshot. No tracked `.env*` files. Manual source/diff inspection found no credentials or credential-bearing links.
- Local SonarQube project `cpp-learning-course`: quality gate passed after importing coverage and correcting excessive callback nesting. Analysis covers supported TS/CSS/Python/test files; Astro/MDX semantics still rely on Astro check and browser/output tests. This working-snapshot scan is not the final pre-merge gate on a future PR head SHA.

The build retains Starlight's optional missing-i18n/404 notices and emits generated MDX `use astro:head-inject` bundler warnings. The production browser suite verifies that the actual dialog script and scoped stylesheet load and work. No warning suppression was added.

## Product QA and retained screenshots

Chromium, Firefox and WebKit pass the production bundle suite: both pilot routes, all cards, desktop/390px/320px layouts, tabs, Tab/Shift+Tab containment, selection and reset, Escape/Close/outside dismissal, focus and course-scroll return, nested popovers, reload reset, dark mode, reduced motion, 200% text enlargement, multi-sheet/multi-instance fixtures and no-JavaScript/unsupported-popover fallbacks. No collected browser page, console or HTTP errors. Text enlargement is a reflow probe, not a claim of native browser zoom or screen-reader verification.

WebKit 27.2 passes using the matching Ubuntu 26.04 Playwright build, Python Playwright 1.64.0 and isolated `libmanette`/`libbacktrace` package extraction in a temporary directory. The prior cached browser targeted an older OS and could not launch; the prior Python driver also needed to match the browser protocol. No system package was installed or OS library replaced.

| View | Retained evidence |
| --- | --- |
| Desktop reader | [Desktop dialog](desktop-dialog.png) |
| Mobile reader | [390px dialog](mobile-dialog.png) |
| Mobile code/model comparison | [390px UML card](mobile-uml-card.png) |
| Narrow dark presentation | [320px card](narrow-dark-card.png) |
| Text reflow | [200% text](text-enlargement.png) |

Generated HTML sizes: CPP-01 51,982 bytes; guided indicator 69,208 bytes, uncompressed. These are local pilot measurements, not a measured growth comparison or a performance budget for wider rollout. Companion text is excluded from Pagefind indexing. No runtime teaching-content fetch occurs.

## Structured critical review

- Requirements/traceability: contracts, guards, branches and observations agree; essential explanation remains visible without opening the explorer. No future lesson is linked or imported.
- Dependencies/SOLID: content flows into the static build; enhancements depend on rendered markup. No speculative layer or interface is justified.
- KISS/YAGNI/DRY: native dialog/popover/disclosure behavior, one shared component and two small scripts. The common footer initializes the explorer before cards, preserving dialog ownership; initialization is idempotent.
- Pattern fit: no GoF pattern is needed. A small explicit state model implements the approved state diagram.
- Must Have, fixed: manual tabs now move their keyboard stop without activating; hidden cards are excluded from sequential focus; unsupported popover browsers avoid unsupported selectors; changing sheets closes a prior card; no-JavaScript selectors stay hidden.
- Should Have, fixed: source-mapped line coverage and settled-state accessibility checks; reproducible development-only tools; compatible lockfile fixes for three high-severity transitive advisories.
- Review tool limit: CodeRabbit CLI is absent; no CodeRabbit review ran. Structured self-review, compiler checks, SonarQube, C++ tests and browser verification are the local review evidence. Copilot was not requested.
- Tracking limit: the course repository has no associated GitHub Project. No unrelated board or new project was selected automatically.

## Approved decision: remaining dependency advisory

`npm audit` reports ten moderate dependency entries caused by one underlying `postcss-selector-parser` advisory through `postcss-nested` 6.2.0 and Expressive Code/Starlight. It reports no high or critical entries after compatible lockfile updates. These moderate entries existed before the new testing tools.

The [reviewed advisory](https://github.com/advisories/GHSA-rj75-hqrm-r3gf) concerns CPU exhaustion when parsing attacker-supplied selectors synchronously in a request path; it explicitly states that ordinary build-time use of trusted source is unaffected. This reader builds repository-authored CSS and publishes static files, with no selector-processing endpoint. That reachability conclusion is source-based, not an audit suppression. No override, suppression or forced downgrade has been applied.

Options:

- A: keep this pilot's compatible dependency fixes, record the unreachable advisory and defer migration to a focused upstream-compatible dependency change.
- B: investigate and validate a scoped major PostCSS dependency override in this brick.
- C: follow npm's forced Starlight downgrade to 0.21.5, requiring a separate compatibility review.

MCDA judgments (0–5; weights total 100; maximum 500), validated by the owner on 2026-10-21:

| Criterion | Weight | A | B | C |
| --- | --- | --- | --- | --- |
| Fidelity to this approved brick | 30 | 5: no extra migration | 3: adds cross-major tooling scope | 1: changes the reader framework baseline |
| Address current reachable exposure | 25 | 4: trusted build path is outside advisory exposure | 5: aims to remove affected parser | 5: npm proposes a dependency path avoiding it |
| Compatibility confidence | 30 | 5: current full suite is exercised | 3: override compatibility unverified | 1: large downgrade unverified |
| Maintenance cost | 15 | 4: track upstream-compatible fix | 2: own a transitive override | 1: own framework regression/migration work |
| **Weighted total** | **100** | **460/500 — recommended** | **335/500** | **200/500** |

A vs B: both address the actual exposure decision; A preserves the verified dependency contracts, while B removes the audit entry at the cost of a new cross-major compatibility obligation. B is the fallback if untrusted selector processing is introduced or the owner requires a zero-advisory audit. Activating B requires a dependency design change and rerunning the full suite; it is not a guaranteed drop-in replacement. A vs C: the downgrade changes substantially more than the affected parser.

The 125-point lead uses explicit judgments, not measured probabilities. Increasing the exposure criterion from 25 to 50 and proportionally reducing the others still leaves A ahead (450 vs 400). If audit-count elimination becomes a separate requirement, it must be added as a criterion and the matrix recomputed. The owner validated the weights and selected A on 2026-10-21. The deferred migration is tracked in [issue #7](https://github.com/benoit-bremaud/cpp-learning-course/issues/7). No override or audit suppression was introduced.

## Owner questionnaire and next gate

Review one material point at a time, classifying it as keep, improve, reject, defer or investigate:

1. Remaining dependency advisory: **approved — A, defer migration with recorded reachability**, tracked in #7; weights validated.
2. Teaching pilot: **approved — A, keep the current teaching pilot (475/500)**, including the reservoir invalid-input explanation; editorial weights validated. Alternative B, shorten that passage, scored 460/500. Criteria: accepted contract 35%, self-contained explanation 30%, single-difficulty focus 25%, change/verification cost 10%. No teaching content was changed.
3. Reader and cards: **approved — A, keep current reader and card timing (480/500)**; weights validated. Alternative B, immediate cards without delay/fades, scored 410/500. Criteria: approved presentation 40%, keyboard/motion support 30%, response latency 20%, change/verification cost 10%. The owner then requested natural-size diagrams inside full-width white paper: implemented with no SVG upscaling, centered diagrams and shrinking only when space is limited. CPP-01 measures 227px diagram width in 756px desktop paper and 358px mobile paper; SVG and prose labels both use 16px at the normal page size. Motion timing remains approved. The owner explicitly accepted the revised natural-size diagram presentation on 2026-10-21 after inspecting the local preview.
4. Evidence and limits: **approved — A, accept scoped evidence and limits (450/500)**; weights validated. Alternative B, additional assistive-technology acceptance work before PR, scored 410/500. Criteria: planned pilot verification 35%, accessibility evidence depth 25%, proportionality 30%, effort/setup readiness 10%. No full WCAG, native browser zoom, screen-reader or teaching-effectiveness claim is made. Tracking-board assignment remains unavailable because no GitHub Project is associated with this repository.
5. Final scope and PR authorization only after approved improvements and fresh checks.

No push, PR, deployment, Copilot request or merge has occurred. Final PR-head checks, individual review-comment handling and post-merge cleanup remain future gates.

## Owner-directed diagram sizing refinement

The former `width: 100%` stretched small SVGs and enlarged their text. The paper container now fills the content width independently from the centered image. Images use their intrinsic width and a 100% maximum, so they shrink only when necessary. SVG bytes and authoritative source diagrams are unchanged. Regression checks cover natural-size bounds in both the lesson and open cards.

[Desktop diagram sizing](desktop-diagram-sizing.png) · [Mobile diagram sizing](mobile-diagram-sizing.png)

## Deferred typography request

The owner requested a future cleanup replacing em dashes (U+2014) with simple ASCII hyphens (U+002D) in authored text and UI labels. This is tracked in [issue #8](https://github.com/benoit-bremaud/cpp-learning-course/issues/8); no bulk typography change is included in this pilot. Preserve programming syntax and authoritative diagram provenance when implementing it.
