# Embedded C++ course

French, self-paced reading website built with Astro and Starlight. Practice belongs to the separate [cpp-learning repository](https://github.com/benoit-bremaud/cpp-learning).

## Local development

Requires Node.js >=22.12.0 and npm >=9.6.5.

```sh
npm ci
npm run check
npm test
npm run preview
```

`npm test` builds fresh production output before running the reader checks. A failed build stops the command before tests run. Use `npm run build` when only a build is needed.

Open the printed local address under `/cpp-learning-course/`. Search is indexed during production builds.

## Scope and decisions

Three introductory theory pages, the proposed progression, the UML method, and local practice instructions are available. The threshold-indicator worked reference is published in the independent practice repository and linked from a guided course page. The 121-module planning catalog is published in the practice repository; its detailed pedagogical content still requires joint review.

Teaching content and UI are French by explicit owner approval. Engineering documents and code are English. The owner approved a default export only in `astro.config.mjs`, as required by standard Astro configuration; other authored code uses named exports.

No deployment or CI workflow is configured. The owner performs pushes. The configured project base anticipates GitHub Pages; it is not a claim of a deployed website.

## Architecture

Markdown content and Starlight produce static HTML and a local Pagefind search index. No backend, browser compiler, user account, or exercise execution is present. See `docs/design.md` for the accepted implementation boundaries.
