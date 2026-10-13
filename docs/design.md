# Course reader design

Status: accepted by the owner in conversation, including Starlight, separate website/practice repositories, and the narrow Astro default-export exception.

## Requirements and implementation

- WEB-01/02: stable concept URLs and prerequisite links; native sidebar and local search.
- WEB-03/05: actual introductory theory distinguished from planned lessons and unpublished exercises. Full exercise studies are a subsequent authoring gate, not implied by introductory pages.
- WEB-04: one independent practice repository with module/project folders; no executable practice inside the reader.
- WEB-06: responsive Starlight navigation, production Pagefind search, keyboard-accessible framework controls.
- WEB-07: no deadlines; exercise UML studies must be approved before implementation.

## Files and dependencies

`src/content/docs/` owns French reader content. `src/content.config.ts` declares its schema. `astro.config.mjs` configures Starlight, French root locale, sidebar, and project base. `src/styles/custom.css` contains a small reading token system. Tests validate the built reader. Practice has no dependency on the website runtime.

No custom domain layer, database, shared package, or publishing synchronization service is justified. Framework components provide navigation and search; static content provides lessons. The initial framework-neutral website studies are retained in the practice repository at local design commit 53c627e. Current website feature and teaching specifications live in this repository under `docs/architecture/specs/`, with authoritative teaching diagrams under `docs/architecture/diagrams/`. Public SVGs are generated snapshots, not separately edited sources. The published indicator remains the explicit external-source exception described below.

## Visual direction

White paper (#ffffff), navy ink (#192e4d), blue links (#2856a5), pale blue emphasis (#e9f0fc), muted text (#53647b). System Segoe UI/Noto Sans gives readable documentation without remote font requests. Left-aligned content, restrained line lengths, persistent navigation and contextual outline. The course progression, not decorative cards or a marketing hero, organizes the opening page. Preserve native dark mode and mobile behavior.

## Review

Requirements map to content/navigation or explicit availability statements. Dependency direction is content into static build, with external practice independent. KISS/YAGNI: no custom client application or speculative abstraction. Patterns: no application pattern needed. CI validation/security workflows were subsequently approved and prepared; deployment remains deferred under the current local-only scope. See the [hosting plan](deployment-plan.md). Future workflow changes still require owner approval.

## Accepted teaching refinement

The owner approved situation-led teaching: concrete need, one question, progressive explanation, worked example, counterexample, independently cloned practice and a retrieval summary. TOOL-01 uses non-executable temperature scenarios and an explicitly illustrative diagnostic. No executable example or exercise implementation is implied before its own UML conception gate. Good practices start immediately; design-pattern modules require a concrete motivating force and a comparison with a simpler solution.

## Published example integration

The guided threshold page references practice revision `6f6da4c440153c0709e35b823a3ef5b85c6b6b68`. `public/diagrams/threshold-indicator.svg` is an unchanged snapshot of its generated SVG; the authoritative PlantUML stays exclusively in the practice repository. The code excerpt is verbatim from that revision. Update diagram, excerpt and pinned links together if the teaching reference changes. Practice is still exclusively local.

## Site-wide example requirements

The accepted [pedagogical example charter](example-charter.md) governs every course section. Consult its requirements and review checklist before authoring examples or implementing the explorer. The charter records accepted interaction/editorial choices separately from the accepted Markdown storage format and the approved schema/technical design. The shared explorer is implemented on CPP-01, the guided indicator page and the first-expressions lesson.


## Current design map

This document is the entry point for the site conception. Detailed specifications remain authoritative for their own behavior; the reader-facing [progression](../src/content/docs/parcours.md) owns teaching order and availability, while [validation evidence](validation.md) records completed checks.

| Concern | Authoritative design | Current implementation boundary |
| --- | --- | --- |
| Example pedagogy and authoring | [Example charter](example-charter.md) | French explanations, English code, explicit prerequisites, meaningful contrasts and exact code/UML correspondence. |
| Complementary examples | [Example explorer](architecture/specs/example-explorer.md) | Markdown sheets with validated metadata, a shared dialog, no database or execution service. Available on three host pages; remaining companion sheets are an authoring gap. |
| Code-to-UML mapping | [Inline UML content](architecture/specs/inline-uml-panels.md) | A mapping and intended diagram accompany each C++ excerpt; incorrect examples explicitly describe their divergence. |
| Current UML interaction | [Compact cards](architecture/specs/uml-cards.md) | Discreet UML/UML · écart buttons, scrollable native popovers, outside click/Escape/Close dismissal, focus restoration and no-JavaScript disclosure fallback. Supersedes expanded inline interaction. |
| Diagram readability | [Mobile diagrams](architecture/specs/mobile-diagrams.md) | Compact authoritative diagrams and a full-size SVG link at every occurrence. |
| Publication | [Hosting plan](deployment-plan.md) | Local only for now; future independent Cloudflare site. GitHub Pages is excluded. |

The example explorer dialog and UML popover have different dismissal contracts: the explorer deliberately does not close on backdrop click; UML cards do close on outside click. Closing a nested UML card preserves its containing explorer. `CourseFooter.astro` loads the shared enhancement; authored content remains readable without it. Accepted UML fades preserve position, honor reduced motion and avoid delaying focus restoration.

## Implemented teaching sequence and traceability

The introductory sequence currently reaches explicit alternatives with else. Each row links to the existing approved conception; it does not grant approval for new snippets or future modules.

| Teaching stage | Specifications |
| --- | --- |
| Complete program and successive output | [Program skeleton](architecture/specs/program-skeleton.md) |
| Variables, assignment and constant limits | [Measurement count](architecture/specs/measurement-count.md), [repeated assignment](architecture/specs/repeated-assignment.md), [assignment versus redeclaration](architecture/specs/assignment-redeclaration.md), [constant limit](architecture/specs/constant-limit.md) |
| Integer calculations | [Addition](architecture/specs/first-expressions.md), [subtraction](architecture/specs/first-subtractions.md), [multiplication](architecture/specs/first-multiplications.md), [grouping](architecture/specs/grouped-calculations.md), [division](architecture/specs/first-divisions.md) |
| State updates and answers | [Counter update](architecture/specs/counter-update.md), [boolean values](architecture/specs/boolean-values.md) |
| Comparisons | [Strict comparison](architecture/specs/first-comparison.md), [inclusive comparison](architecture/specs/inclusive-comparison.md), [lower comparisons](architecture/specs/lower-comparisons.md), [equality and difference](architecture/specs/equality-comparisons.md) |
| Conditional execution | [First if](architecture/specs/first-if.md): execute or skip a block, then continue. [First else](architecture/specs/first-else.md): choose one branch, then continue; a false equality includes both lower and higher values. |

The first-if module contains four complete programs and three activity models. The first-else module contains five complete programs and four models; its incorrect message reuses the intended above-target model with an explicit discrepancy explanation. Both retain named booleans to isolate execution control from new condition syntax. Direct comparisons inside conditions, nested alternatives and applications that enforce limits require their next proportionate conception review.

## Maintenance and deferred work

For each approved teaching increment, update its specification status, authoritative UML and public snapshots together; synchronize navigation, prerequisite/next links and availability. Update this design map when the sequence or site behavior changes, and record actual verification in validation.md. A successful build or compile check is evidence of technical consistency, not learner mastery.

Code-gap quizzes, scoring, personal strengths/gaps summaries and downloadable recap sheets remain deferred under the [charter](example-charter.md). Practice still belongs in separately cloned repositories. The next planned control applications, additional companion examples, publication and portfolio integration are not implemented by the latest if/else lessons.
