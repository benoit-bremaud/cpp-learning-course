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
