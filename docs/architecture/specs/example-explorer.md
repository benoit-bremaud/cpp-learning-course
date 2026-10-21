# Example explorer — accepted conception

Status: explicitly accepted by the owner before implementation. This specification defines the original two-page pilot; implementation and deployment remain deferred.

## Need and scope

Work item: implement EX-01 through EX-09 from [the charter](../../example-charter.md) on CPP-01 and the guided indicator page. Deliver four standalone sheets, two categories and a common accessible reading dialog. No database, API, browser execution, new framework or persistence. Existing indicator behavior and published practice revision remain unchanged.

## UC1 — Explore a complementary example and return to the course

Actor: Reader. Preconditions: a pilot page has validated companion content. Minimal guarantee: the original course remains readable. Success guarantee: the reader selects a category and sheet, reads its complete explanation, and closes the dialog without losing the original reading position.

1. Reader activates “Explorer d’autres exemples”.
2. ExampleExplorer opens the dialog on “Autres contextes”, first sheet, scroll position zero; focus moves to its titled reading container.
3. Reader activates a tab. Its first sheet replaces the current sheet; reading scroll resets, keyboard focus stays on the tab.
4. Reader uses the labelled native select when the category contains multiple sheets. Selection replaces only the article, resets reading scroll and leaves focus on the select.
5. Reader closes using the visible close button or Escape. Focus returns to the opener; the course position is restored.

Extensions: with one sheet, show its title instead of a redundant select. Do not close on backdrop click, preventing accidental loss of position. Reopening starts at step 2; no saved state. Without JavaScript, show the companion articles inline with their category headings rather than a nonfunctional button. Invalid references fail the build instead of producing empty UI.

## Content and files

Planned layout:

- `src/content/examples/variables/component-stock.md`
- `src/content/examples/variables/independent-copy.md`
- `src/content/examples/conditions/reservoir-level.md`
- `src/content/examples/conditions/inclusive-threshold.md`
- `src/components/ExampleExplorer.astro`: common rendered markup and scoped browser behavior; no application service layers.
- `src/content.config.ts`: separate examples collection and validated pilot-page references.
- `src/content/docs/notions/cpp-01.mdx`, `src/content/docs/exemple-voyant.mdx`: use the shared component at the relevant example location. Only host pages become MDX to import the component; example sheets remain plain Markdown. Preserve page slugs and content.
- `tests/`: build content-integrity checks and real-browser dialog interaction checks.

Each sheet has an explicit unique `id`, French `title`, `category` (`other-contexts` or `deeper`), and `prerequisites` (existing course page identifiers, possibly empty). Host pages reference an ordered list of sheet IDs once, in metadata, passing that list to the component. Directory names organize authorship, not category inference. Array order controls display order; each category must be populated for these pilots. Body follows the charter. Labels are mapped to French centrally.

Build validation rejects duplicate IDs, unknown categories, missing referenced sheets and broken prerequisite links. No client JSON fetch: render Markdown during the static build and only include the four pilots' relevant sheets in their respective pages. Hidden sheets remain outside the accessibility tree while the dialog is active. Mark supplemental dialog content out of the main Pagefind index to avoid search results landing on hidden text. Inline no-JS fallback remains available for direct reading.

## Reading and accessibility contract

Use a native modal dialog, labelled by its visible heading. Course background is inert while open. One main vertical reading area; header, close button and navigation remain available. Constrain width for prose; fit SVG diagrams to available width and provide meaningful alternative text. Code alone may scroll horizontally. Respect site theme tokens and zoom; near-full-screen on narrow viewports.

Tabs expose tablist/tab/tabpanel semantics, selected state and unique ID relationships. Arrow keys and Home/End move tab focus; Enter/Space activates (manual activation). Modal Tab/Shift+Tab stays inside. Each instance owns its state and IDs; no shared global selection. No mouse-only behavior, transitions or dependency on external assets. Browser verification must cover focus restoration, Escape, scroll preservation, mobile and zoom behavior rather than assuming native dialog solves everything.

## Four teaching contracts

### P1 — Component stock (other contexts, CPP-01)

One integer `component_count` starts at 12, then receives 11. After initialization it is 12; after assignment it is 11. Explain that the assignment replaces the value and does not represent a sensor action or a subtraction instruction. No input, arithmetic, hardware or classes. Explain the syntax of type, name and assignment locally; no requirement to write a function independently.

### P2 — Independent copy (deeper, CPP-01)

Initialize integer `component_count` to 12. Initialize independent integer `snapshot_count` from it. Assign 11 to `component_count`. Final values: 11 and 12 respectively. Explain value copying at that instant and explicitly limit the conclusion to these ordinary integer variables; references and pointers are outside scope. Prerequisite: CPP-01, with a link back to that page.

### P3 — Reservoir level (other contexts, indicator)

Pure function `should_warn_low_level(int level_percent) noexcept`, fixed local `const int threshold_percent = 20`, returns true strictly below 20, otherwise false. Domain precondition: supplied level is an integer from 0 to 100. Physical measurement and invalid-input handling are excluded and explicitly stated; the caller supplies a valid value. Expected cases: 0/19 true, 20/21/100 false. UML uses both explicit return branches. The fictional threshold is a teaching choice.

### P4 — Inclusive threshold (deeper, indicator)

Compare the existing strict rule (>30) with a separately named function `should_light_indicator_inclusive(int temperature_celsius) noexcept` implementing >=30. Both use local threshold 30 and explicit true/false branches. For 29,30,31 the strict outcomes are false,false,true and inclusive outcomes false,true,true. Each function has its own contract and activity view; do not modify the published strict reference. Prerequisite: the guided indicator page. Explain that tests follow the requirement, not a preferred operator.

## Source ownership

These approved teaching contracts are planned as course excerpts and must be checked with a temporary C++17 compilation harness during implementation. New standalone practice projects are not yet published. Diagram sources here support this conception review. Before publishing new executable practice, establish their authoritative studies and source in the separate practice repository, validate them there, and reference one matching revision from the course. Relocate the accepted teaching diagram sources at that stage rather than creating competing authoritative copies; retain course render snapshots and provenance. No new practice links until those targets exist. The existing strict example remains pinned to its published revision.

## Acceptance and traceability

| Requirement | Realization | Verification |
| --- | --- | --- |
| EX-01/02 | UC1, dialog state diagram, category/select behavior | Real-browser tabs and a multiple-sheet fixture; one-sheet pilot labels |
| EX-03/04 | P1–P4, complete Markdown body | Editorial review and visible UML-to-code sequence |
| EX-05/06 | Dialog layout and focus contract | Desktop/mobile, zoom, Escape, Tab, arrows, closing and reopening |
| EX-07/08 | Independent practice, French content | Source provenance, link checks and language review |
| EX-09 | Separate Markdown collection | Invalid-metadata and missing-reference build failures |
| P1/P2 | Ordered activity actions | Observe every intermediate and final integer value |
| P3/P4 | Decision guards and returns | Boundary tables plus min/max valid reservoir inputs |

## Four-pass conception review

1. Requirements: every charter requirement maps above. Single-sheet categories avoid useless controls; multi-sheet fixtures cover the selection path. No claims of implemented behavior.
2. Dependencies/SOLID: content is independent of UI. Build consumes content; UI controls reading, never C++ execution. No inheritance or injectable repository needed. A shared component is justified by the approved common behavior across two pilots and the site-wide requirement.
3. KISS/YAGNI/DRY: static rendering, native controls, no database, runtime fetch, persistent state or speculative layers. Trade-off: rendered companion content increases page size; measure the two pilot outputs before wider rollout.
4. Pattern fit: no GoF pattern justified. A small explicit state description documents behavior without introducing State classes. No classes or patterns are forced into the learning examples.

The owner approved the no-JS fallback, host-page MDX use, schema and selection reset behavior with this conception. Automated, visual and pedagogical implementation evidence must be recorded in the later implementation pull request.
