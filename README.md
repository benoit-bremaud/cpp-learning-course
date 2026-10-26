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

`npm test` builds fresh production output before running the reader checks and compiling eight executable complete programs across the first-program, ordered-output, observable-variable and observable-constant lessons as C++17, plus checking one complete intentionally rejected source. These checks require Python 3 and g++. A failed build stops the command before tests run. Use `npm run build` when only a build is needed.

Open the printed local address. Search is indexed during production builds.

## Scope and decisions

Five introductory theory pages, the proposed progression, the UML method, and local practice instructions are available. The threshold-indicator worked reference is published in the independent practice repository and linked from a guided course page. The 121-module planning catalog is published in the practice repository; its detailed pedagogical content still requires joint review.

Teaching content and UI are French by explicit owner approval. Engineering documents and code are English. The owner approved a default export only in `astro.config.mjs`, as required by standard Astro configuration; other authored code uses named exports.

Validation and security workflows run on pull requests and `main`. They do not deploy the site. GitHub Pages is explicitly excluded. `cpp.benoitbremaud.fr` is the accepted future Cloudflare target, but the course remains local until a separate deployment change is reviewed and approved.

## Architecture

Markdown content and Starlight produce static HTML and a local Pagefind search index. No backend, browser compiler, user account, or exercise execution is present. See `docs/design.md` for the accepted implementation boundaries.

## Example reader validation

The local pilot uses CPP-01 and the guided indicator, with four Markdown companion sheets. Runtime enhancements have no additional production dependency. The charter and accepted architecture remain authoritative; owner review and publication are separate gates.

After `npm test`, run `npm run test:browser` with Google Chrome installed, or set `COURSE_BROWSER_EXECUTABLE` to a Chromium executable. This command checks WCAG rules with axe-core, exercises real DOM interactions, writes source-mapped TypeScript coverage to `coverage/`, and enforces an 80% line floor. Its server replaces only the two interaction entrypoints with source-mapped equivalents; the independent production smoke suite exercises the actual bundles.

```sh
python3 tests/program-output.py
python3 tests/program-output.py --lesson ordered-output
python3 tests/program-output.py --lesson observable-variables
python3 tests/constant-limit.py
python3 tests/example-code.py
python3 tests/explorer-invalid-content.py
python3 tests/explorer-browser.py
```

The C++ checks require g++ with C++17 support. The unchanged all-success program harness validates six programs. The dedicated `tests/constant-limit.py` validates two more executable complete programs and one complete rejected source, with two test-only successful rejection controls. `tests/example-code.py` retains the six other authored fragments, their intermediate observations and boundary mutation. There are still fifteen teaching C++ fences; compiler controls are not teaching examples. The invalid-content suite uses an isolated source/dependency copy. The production browser suite requires Python Playwright (tested with 1.64.0); choose other engines using `COURSE_BROWSER_ENGINE` and `COURSE_BROWSER_EXECUTABLE`. It covers desktop/mobile reading, keyboard/focus, cards, reloading, text enlargement and fallbacks; screenshots go to `COURSE_QA_DIR` or a temporary directory. Install the matching browser and its host libraries before using Firefox or WebKit.

See [pilot review evidence](docs/reviews/example-reader-pilot/README.md) for measured results, provenance, remaining limits and the owner questionnaire.
