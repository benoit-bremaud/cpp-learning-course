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

No custom domain layer, database, shared package, or publishing synchronization service is justified. Framework components provide navigation and search; static content provides lessons. Existing website UML studies are retained in the practice repository at local design commit 53c627e, with these implementation choices refining the framework-neutral static-reader architecture.

## Visual direction

White paper (#ffffff), navy ink (#192e4d), blue links (#2856a5), pale blue emphasis (#e9f0fc), muted text (#53647b). System Segoe UI/Noto Sans gives readable documentation without remote font requests. Left-aligned content, restrained line lengths, persistent navigation and contextual outline. The course progression, not decorative cards or a marketing hero, organizes the opening page. Preserve native dark mode and mobile behavior.

## Review

Requirements map to content/navigation or explicit availability statements. Dependency direction is content into static build, with external practice independent. KISS/YAGNI: no custom client application or speculative abstraction. Patterns: no application pattern needed. CI/deployment remains outside this accepted implementation; workflows need owner approval.

## Accepted teaching refinement

The owner approved situation-led teaching: concrete need, one question, progressive explanation, worked example, counterexample, independently cloned practice and a retrieval summary. TOOL-01 uses non-executable temperature scenarios and an explicitly illustrative diagnostic. No executable example or exercise implementation is implied before its own UML conception gate. Good practices start immediately; design-pattern modules require a concrete motivating force and a comparison with a simpler solution.
