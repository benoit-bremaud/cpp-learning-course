# Site-wide pedagogical example charter

Status: accepted editorial and interaction requirements. Implementation and publication remain separate, explicitly reviewed work.

## Scope and authority

This is the single source of truth for contextual example presentation across all course sections, modules and guided pages. Authors and reviewers must consult it before adding or changing examples. Link to this charter instead of maintaining competing copies. Changes to accepted requirements require explicit owner validation and a corresponding update here.

The approved pilot targets are the variables introduction and the guided indicator page. This is not a claim that either page has already been migrated or that every course page has been audited. Each teaching example is intended to offer an “Explorer d’autres exemples” control once relevant companion content exists. Never add an empty or misleading control; record missing companion content as an authoring gap.

## Accepted decisions

| ID | Requirement | Rationale |
| --- | --- | --- |
| EX-01 | Offer both “Autres contextes” and “Pour aller plus loin”. | Transfer understanding across situations and support deeper study without mixing those goals. |
| EX-02 | Use two tabs and display one selected example at a time. Selectors use explicit, descriptive titles. | Keep attention on one readable explanation. |
| EX-03 | Present a complete, concise, self-contained example with one learning objective. | Readers must be able to return after a break without reconstructing a previous lesson. |
| EX-04 | Keep the primary conception and essential teaching sequence visible. Additionally provide a compact UML button immediately after each teaching code block, opening a dismissible floating card; retain the disclosure as a no-script fallback. | The primary explanation remains complete; the optional panel supports local code/model comparison. |
| EX-05 | Provide a scrollable dialog with a single main reading area, readable diagrams, short paragraphs and spaced code. | Rich examples need room without nested vertical scrolling. |
| EX-06 | Keep closing available, support Escape and keyboard navigation, and restore focus to the opener and the course reading position. Use an almost full-screen layout on small screens. | Reading and returning to the course must remain straightforward across input methods and screen sizes. |
| EX-07 | Keep practice in the independent repository, cloned and run in a local IDE. | The site remains a reader, not an execution environment. |
| EX-08 | Use French teaching content and UI; English code and engineering documents. | Preserve the approved language separation. |
| EX-09 | Store example sheets as Markdown files with metadata in the course repository, without a database. | Support readable long-form explanations, code blocks and diagram references while retaining structured classification. |

## Accepted systematic example coverage

The owner selected systematic coverage without a fixed numeric quota. This applies to all instructional sections, not just the two explorer pilots. Four pilot sheets are an initial implementation scope, not a permanent ceiling or evidence of complete coverage.

- Each new concept receives a worked example in the main page; essential understanding must not depend on opening the explorer.
- Each new syntax element is explained on a concrete use. Important distinctions receive contrasted cases; misconceptions receive an explained counterexample and correction. Observable behavior receives a trace or result; meaningful boundaries receive boundary cases.
- Each notion should offer multiple relevant complementary contexts as content is developed. Missing coverage is recorded explicitly rather than concealed by empty buttons or artificial duplicates.
- Keep short examples close to the explanation they support. Use the shared explorer for complete supplementary sheets. Reusing one coherent study across explicitly mapped steps is allowed; a new behavior requires appropriate reviewed conception.
- Count an example's contribution by the question it resolves, not its snippet count. Renaming variables is not sufficient evidence of transfer. Repetition is useful when its comparison purpose is explicit.
- Code examples retain the UML-before-code requirement. An invalid-code counterexample describes an expected diagnostic, not an executable activity that successfully runs. Never execute undefined behavior to illustrate a misconception.

Review coverage using: explanation or difficulty → example → distinctive contribution → prerequisite → expected observation → UML/source reference → review status. This is an editorial review matrix, not a new mandatory content-schema implementation.

## Standard example structure

Use the following order consistently. Headings may be phrased naturally in French while retaining these responsibilities:

1. Objective and prerequisites: one learning objective, prerequisite links and what this example adds.
2. Concrete situation: explain the need, inputs and assumptions. Identify fictional or simplified hardware values explicitly.
3. Expected behavior: state the contract, including relevant boundary behavior, before implementation.
4. UML conception: use only the views needed to explain the actual decision, interaction or structure.
5. Code: a short, readable implementation matching the accepted conception exactly.
6. Explanation and outcomes: connect significant code to UML and show representative results, including meaningful boundary cases.
7. Takeaway and practice reference: summarize the transferable idea and link to the corresponding published practice reference when available. Do not invent links or imply unpublished practice exists.

“Self-contained” means understandable with the stated prerequisites, not repeating the whole language curriculum. Explain the lines that carry the concept, not every brace. Split an example that introduces multiple objectives; move additional difficulty into the deepening category. Optional reminders must not hide essential conception or reasoning.

## Category rules

**Autres contextes:** retain comparable difficulty and the same core concept. Explicitly identify what changes and what stays the same. Different hardware vocabulary alone is not sufficient: explain why the same reasoning applies.

**Pour aller plus loin:** identify the additional difficulty and prerequisites before the reader starts. Link to the required notions so readers can postpone the example without losing their place in the course.

## UML and code consistency

Conception precedes implementation and remains subject to the established owner validation gate. Choose diagrams proportionally: an activity diagram can explain a decision; interaction or structure may require other views. Do not force class diagrams, patterns or inheritance onto a simple function.

Maintain traceability between behavior, diagram branches, code and illustrated results. For published practice examples, keep authoritative UML and executable source in the practice repository; course excerpts and rendered diagrams must reference the same source revision and be updated together. Respect the provenance approach documented in design.md.

## Accepted storage approach

The owner selected Markdown with metadata over JSON and MDX. Metadata describes classification and references; Markdown carries the French pedagogical narrative, code excerpts and diagram references. Presentation belongs to a common site component, not custom interactive code in each sheet. Authoritative executable sources and UML for practice remain in the independent practice repository.

The approved schema uses id, title, category and prerequisites; host pages reference ordered example IDs. Structural validation should complement, not replace, editorial and UML/code consistency review.

## Accepted pilot scope

The owner selected both the variables introduction (`notions/cpp-01`) and the guided threshold indicator (`exemple-voyant`). The first iteration contains four authored sheets total: one “Autres contextes” and one “Pour aller plus loin” for each pilot. Both pilots use the same presentation and editorial structure.

This validates introductory reading as well as richer UML/code explanations. Multiple-example selection within one category should be exercised with test fixtures rather than extra published teaching sheets in this iteration. The four subjects and their detailed UML studies were approved before implementation.

## Implementation boundary

The [accepted conception](architecture/specs/example-explorer.md) defines the planned schema, directory tree and interaction. It does not authorize implementation, wider migration, publication or new independent practice projects. Each implementation increment must pass the repository's review gate.

## Required authoring and review checklist

For every new or revised example, record a review against the applicable EX requirements and verify:

- One objective, explicit prerequisites and correct category.
- Concrete context and expected behavior understood before reading code.
- Essential sequence visible and concise; no dependence on vague “as above” references.
- UML, code, outcomes and source revision agree, including boundary cases.
- Practice links are accurate and point to independent local-IDE work.
- Explorer content is meaningful; no empty categories or placeholder controls are presented as working features.
- Once implemented: keyboard/focus/closing behavior, mobile readability, diagram readability and overflow are verified.

A failing item is a review finding to address or explicitly discuss with the owner, not an implicit exception. This checklist defines acceptance criteria; it does not claim an automated enforcement mechanism already exists.

## Accepted pilot subjects

- Variables / other contexts: component stock initialized to 12, then assigned 11.
- Variables / deeper: initialize an independent integer copy, then modify the original.
- Indicator / other contexts: signal a reservoir level strictly below a threshold.
- Indicator / deeper: compare strict and inclusive temperature thresholds as separate requirements; preserve the existing strict reference.

Subject selection, detailed contracts and technical choices were explicitly approved by the owner. Visual and pedagogical acceptance of the rendered local pilot is the next human review.

## Accepted inline UML access

The owner chose option A: a disclosure under each teaching code excerpt, not a second modal or a code/UML toggle. Opening it preserves the visible code. It contains the modeling question, the relevant reviewed diagram, a concise code-to-model mapping and a narrated path or observation. Correct examples use “Voir la conception UML”; deliberately faulty examples use “Comprendre l’écart avec la conception”.

UML represents the intended design, not an automatic translation of syntax. Compilation failures have no successful execution trace. A valid-but-wrong fragment must identify the specific divergence from the required model. Reuse authoritative diagrams with explicit scope; do not create copies of their sources per excerpt. Primary diagrams remain visible before code. This decision refines EX-04; it does not hide essential teaching content.

Implementation conception: [inline UML panels](architecture/specs/inline-uml-panels.md). The interaction and the ten-excerpt pilot inventory are approved; implementation evidence belongs to the later implementation pull request.


## Accepted mobile diagram presentation

Owner-approved option A: compact teaching layouts plus an explicit “Ouvrir le diagramme en grand — nouvel onglet” link to the same SVG after every diagram occurrence. Links work without JavaScript. Keep identifiers, actions, order and guards unchanged; put observation commentary in adjacent lesson tables rather than wide side notes. Generate snapshots from PlantUML sources, never edit SVG geometry manually. Opening the original is an optional complement, not a guarantee of mobile zoom behavior. The pinned published indicator retains its authoritative snapshot; seven local teaching activities use compact French labels.


## Accepted compact UML cards — superseding the inline interaction

The owner approved option A after reviewing the inline panels: use a discreet UML button (UML · écart for intentionally faulty excerpts), with an accessible full label. Open a native auto-popover card near the trigger, constrained to the viewport and scrollable on small screens. Outside click, Escape and Close dismiss it; closing the card must preserve an enclosing explorer dialog. Close and keyboard dismissal restore trigger focus. Only one card is visible. Preserve original SVG links, primary diagrams and all authored mappings. Native disclosures remain the no-JavaScript/unsupported-browser fallback. This decision supersedes the earlier visible inline-panel interaction, not its teaching content requirements. See [card conception](architecture/specs/uml-cards.md).


## Accepted prerequisite-driven progression

The owner approved the revised course progression after reviewing LearnCpp, the publisher contents for Stroustrup PPP3 and Arduino built-in examples. The reader-facing order and availability are maintained in src/content/docs/parcours.md. Introduce one main learning difficulty at a time: worked case, one changed dimension, transfer context, then a meaningful boundary or error. Do not turn this into a fixed example quota.

Each module declares direct prerequisites, observable learning outcomes and honest availability. Keep IDs stable independently of reading order. The indicator remains optional guided discovery until conditions/functions are taught. Teach the minimal program and block orientation before expanding redeclaration examples; defer capacity-enforcement comparisons to conditions. Introduce hardware before advanced ownership while retaining lifespan/shared-state prerequisites for concurrency. UML vocabulary grows with the modeled behavior. New code still requires its accepted conception; roadmap approval alone does not approve all future snippets.


## Deferred interactive assessment idea

The owner requested recording, then explicitly postponing, code-gap questions with selectable answers, scoring and a personal strengths/gaps overview. This is a future proposal, not approval to implement assessments or change EX-07. Training versus assessment, feedback timing, concept-level evidence, retry handling, persistence, accounts and scoring thresholds remain undecided. The suggested browser-local pilot was not selected. No current module depends on assessment completion. Continue the prerequisite-driven course plan; revisit this idea only when the owner resumes it.


## Deferred downloadable course summaries

The owner requested downloadable recap sheets for later. Record the feature in the roadmap, but do not implement downloads or generate documents now. File format, module/theme grouping, content template and synchronization with the lessons remain undecided. This does not change the current teaching sequence or priorities.
