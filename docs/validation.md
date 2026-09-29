# Local validation

- `npm run check`: no errors, warnings or hints.
- `npm run build`: eight static pages generated and Pagefind indexed. Starlight emits non-blocking notices for the absent optional custom i18n collection and custom 404 entry; its built-in French UI and fallback page are used.
- `npm test`: two production-output tests pass, covering internal links, anchors, assets, project-base paths, French language metadata and search artifacts.
- Headless Chrome: desktop 1440px and mobile 390px inspected; no horizontal overflow or page errors on the home page. Search for `const` returns CPP-09 and opens its page. Mobile menu opens the progression successfully.
- npm install audit: no known dependency vulnerabilities reported.

Chrome DevTools MCP could not launch its graphical browser (no X server). Browser verification used the installed Python Playwright with headless Chrome instead. The initial browser test selected an input type not used by this search implementation; correcting that selector confirmed the search flow.

## Structured local review

Must Have: missing favicon found by output tests; added and verified. Default-export exception explicitly approved and limited to Astro configuration. Reader availability accurately distinguishes theory introductions from unpublished practice.

Should Have: ordered the three introductions by prerequisites rather than alphabetically. Done.

Nice to Have: custom 404/i18n overrides are unnecessary for this initial reader; retained framework defaults.

No push, PR, CI changes or deployment performed. Human push gate remains in effect.
