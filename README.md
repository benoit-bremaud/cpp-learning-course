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

Open the printed local address at `/`. Search is indexed during production builds.

## Scope and decisions

Twelve introductory theory pages, the proposed progression, the UML method, and local practice instructions are available. The threshold-indicator worked reference is published in the independent practice repository and linked from a guided course page. The 121-module planning catalog is published in the practice repository; its detailed pedagogical content still requires joint review.

Teaching content and UI are French by explicit owner approval. Engineering documents and code are English. The owner approved a default export only in `astro.config.mjs`, as required by standard Astro configuration; other authored code uses named exports.

GitHub validation and security workflows are included. The accepted production address is `https://cpp.benoitbremaud.fr/`, on an independent Cloudflare Pages project. Hosting and DNS still require provisioning; this configuration is not evidence of a live deployment. See `docs/deployment-plan.md`.

## Architecture

Markdown content and Starlight produce static HTML and a local Pagefind search index. No backend, browser compiler, user account, or exercise execution is present. See `docs/design.md` for the accepted implementation boundaries.

## Authoring course examples

Read the [site-wide example charter](docs/example-charter.md) before adding or changing examples in any section. Its accepted requirements and review checklist are authoritative; Markdown with metadata is the accepted storage format; its schema and shared explorer are implemented on CPP-01, the guided indicator page and the first-expressions lesson.

### Local example verification

After `npm test`, run the following from the course root:

```sh
python3 tests/explorer-browser.py
python3 tests/example-code.py
python3 tests/assignment-redeclaration.py
python3 tests/first-expressions.py
python3 tests/first-subtractions.py
python3 tests/first-multiplications.py
python3 tests/grouped-calculations.py
python3 tests/first-divisions.py
python3 tests/counter-update.py
python3 tests/boolean-values.py
python3 tests/constant-limit.py
python3 tests/program-output.py
python3 tests/explorer-invalid-content.py
```

These additional checks require Python Playwright with Google Chrome at `/usr/bin/google-chrome`, g++ with C++17 support, and installed npm dependencies. They verify browser interaction, the actual teaching excerpts, and build rejection of invalid content in an isolated temporary copy. They are local checks, not currently part of the GitHub workflow.

Pilot URLs: `/notions/cpp-01/` and `/exemple-voyant/`. Each ends with “Explorer d’autres situations” and the explorer button. New companion practice projects remain unpublished.
