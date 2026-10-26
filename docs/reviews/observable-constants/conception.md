# Observable constants - conception delivery review

Date: 2026-10-26. Issue: [#20](https://github.com/benoit-bremaud/cpp-learning-course/issues/20). Branch: codex/20-observable-constants-conception, from main 40ea5e5. The owner explicitly approved option A and weights 35/25/25/15: three complete sources, including one compiler rejection, 445/500. B scores 425/500 and C 345/500. The [accepted specification](../../architecture/specs/observable-constants-lesson.md) contains per-cell reasons, sensitivity and the concrete future file plan. Moving ten points from independent evidence to reading focus ties A/B at 435; fifteen makes B lead. These are decision judgments, not measured learning outcomes. Activating B requires a revised approved plan.

## Four-pass review and scope

Requirements: two executable cases observe limit/count before and after a supplied assignment; one complete ill-formed source isolates forbidden const assignment. Successful status, output, const invariance and requirement correctness stay distinct. Six conceptual actions cover twelve statements in each executable case. The invalid case's five statements have qualified reference mappings, never an invented execution. Both derived compiler controls prevent unrelated broken syntax from serving as const evidence.

Dependencies/SOLID: authored lesson/model feeds the existing static renderer; future tests consume actual authored sources. A dedicated compile/run-or-reject runner keeps the existing all-success program harness unchanged. No runtime layer or framework dependency is introduced.

KISS/YAGNI/DRY: one existing page, three existing card identities, known output syntax and reused table styling. Repeated whole-file structure permits independent copying. No helper functions, browser compiler, generalized registry or new design pattern has a justified force.

Anti-pattern review: fake literal observations, compiler rejection for unrelated reasons, confusion between actual 30 and required 3, stale fragment wrappers/counts and clipped screenshots are explicitly addressed by future source assertions, controls, provenance, mappings and QA. No remaining conception Must Have or Should Have finding was identified; no new Nice to Have item. This is structured local review, not an independent reviewer claim.

This delivery contains only the specification, two source/render/note triplets, scoped glossary/traceability entries and review/QA evidence. The public CPP-09 lesson still has its three existing fragments. No source, test, runtime, public asset, navigation, dependency, lockfile or workflow changed. The historical constant-limit conception remains current published evidence until implementation explicitly supersedes its relevant parts.

## Local verification

- Astro check: zero errors, warnings or hints; production build succeeds; npm test passes 17/17. Nine current fragments and six invalid-content probes pass.
- Exact three sources extracted from this specification: C++17 with Wall/Wextra/Werror/pedantic-errors. Stable stdout is exactly 3\n0\n3\n1\n; wrong stdout is 30\n0\n30\n1\n. Both have empty stderr and exit 0. The invalid source fails compilation and is never executed. Removing const yields 4\n; removing only the forbidden assignment yields 3\n, both with empty stderr and exit 0. GCC 15.2.0. This is conception study evidence; future tests must extract the actual lesson.
- Runtime TypeScript coverage: 170/170 lines, 100%, with the existing 80% floor retained. Public TypeScript declarations documented 3/3; public program harness function documented 1/1. These presence counts do not measure pedagogical completeness.
- Accessibility: 20 axe scans, zero violations; three incomplete contrast results retain the existing narrow diagnostic guard. This is not a full accessibility conformance claim.
- Chrome, Firefox and WebKit production regressions pass keyboard/focus, dismissal, responsive/theme/motion, reload and native fallbacks. A direct current CPP-09 path passes desktop/mobile cards with zero console messages, page errors, HTTP errors or failed requests. [Dated smoke evidence](../../architecture/qa/2026-10-26-observable-constants-conception.md).
- Both 239x649 activity renders use 16px labels. Fresh headless PlantUML renders equal their SVG bytes; rendered diagrams were visually inspected. Links, new authored ASCII hyphens and generated-byte-aware whitespace are checked.
- Gitleaks full reachable history and exact staged snapshot are checked before publication; no env files are tracked. Exact committed-head Sonar runs with fresh lcov before publication authorization; its revision, compute task and gate verdict are recorded in the publication body and local resume note.

CodeRabbit CLI is unavailable; no CodeRabbit or Copilot review is claimed. Existing nonblocking build notices remain. This documentation-only delivery uses QA smoke scope. Full inspector/security-probe applicability belongs to the approved implementation pass; #16's local-preview header waiver does not extend to #20.

## Owner dispositions and next gate

| Material point | Disposition |
| --- | --- |
| Three complete sources on the existing CPP-09 page | Keep - explicit owner approval, option A |
| Weights, scores and sensitivity | Keep - owner validated 35/25/25/15 and 445/500 |
| Two six-action models and qualified rejected-source reference | Keep - exact statement scopes reviewed |
| Dedicated rejection runner, unchanged existing program harness | Keep - accepted proportional plan |
| Reader architecture, table styling, route and prerequisite | Keep - reuse existing contracts |
| Arithmetic, input, conditions, shared-runtime changes and deployment | Defer - separate bricks |

Publication requires separate authorization to push this local commit and create the conception documentation PR with Refs #20. It must not close the implementation issue. Merge and branch deletion remain separate approvals. After the separately authorized conception merge, implement the approved plan on a fresh branch from updated main.
