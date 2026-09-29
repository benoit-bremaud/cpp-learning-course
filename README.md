# Embedded C++ course

French, self-paced reading website built with Astro and Starlight. Practice belongs to the separate [cpp-learning repository](https://github.com/benoit-bremaud/cpp-learning).

## Local development

Requires Node.js >=22.12.0 and npm >=9.6.5.

```sh
npm ci
npm run check
npm run build
npm test
npm run preview
```

Open the printed local address under `/cpp-learning-course/`. Search is indexed during production builds.

## Scope and decisions

Three introductory theory pages, the proposed progression, the UML method, and local practice instructions are available. No executable exercises are published yet. The 121-module planning catalog remains in the practice repository's local design branch pending joint review and publication.

Teaching content and UI are French by explicit owner approval. Engineering documents and code are English. The owner approved a default export only in `astro.config.mjs`, as required by standard Astro configuration; other authored code uses named exports.

No deployment or CI workflow is configured. The owner performs pushes. The configured project base anticipates GitHub Pages; it is not a claim of a deployed website.

## Architecture

Markdown content and Starlight produce static HTML and a local Pagefind search index. No backend, browser compiler, user account, or exercise execution is present. See `docs/design.md` for the accepted implementation boundaries.
