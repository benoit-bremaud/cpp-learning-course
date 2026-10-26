# Inline UML panels

Interaction superseded by [compact UML cards](uml-cards.md); this document retains the original content mapping and fallback specification.

Status: conception explicitly approved. Implementation remains a separately reviewed change.

## Scope and acceptance

Attach one local UML disclosure to every existing fenced C++ teaching excerpt: CPP-01 (1), CPP-09 (3), guided indicator (1), four companion sheets (5 blocks including two threshold functions): ten blocks total. Diagnostic text blocks are not executable C++ examples. Inline syntax mentions do not each receive a redundant control.

Each disclosure must immediately follow its code block, preserve the visible code, and contain a modeling question, reviewed diagram, exact scoped mapping and explanation. Primary diagrams remain visible. Panels start closed and work with keyboard and JavaScript disabled, including inside the existing example explorer. Opening one does not close another. No new modal, network request, data store, framework or client state.

## Implementation choice

Use native HTML details/summary embedded in Markdown and MDX, with shared styles in src/styles/custom.css. The summary is the keyboard-operable disclosure control; do not nest a button inside it or override its native semantics. Standard Markdown tables and images inside the disclosure provide content. Verify real rendered output in both loaders rather than assume parsing is identical. This keeps sheets plain Markdown as approved.

## Mapping inventory

| Excerpt | Reviewed diagram | Specific panel explanation |
| --- | --- | --- |
| CPP-01 measurement_count | measurement-count.svg, from measurement-count/02-activity-observed-values.svg | Initialize to 0, observe, assign 1, observe, return 0; five conceptual actions cover seven statements |
| CPP-09 valid | constant-limit.svg, observable-constants/07-activity-stable-limit.svg | Complete source, six actions covering twelve statements; limit/count observed twice |
| CPP-09 forbidden assignment | constant-limit.svg, expected reference only | Five authored statements; forbidden assignment rejected, writes/return never execute; count absent |
| CPP-09 wrong initial value | constant-wrong-limit.svg, observable-constants/07-activity-wrong-limit.svg | Actual faulty behavior: constant 30 against required 3; six actions cover twelve statements |
| Guided indicator | threshold-indicator.svg | Input, threshold, guard, two returns; preserve pinned source |
| Stock | 04-activity-stock.svg | Two actions and values 12 then 11 |
| Copy | 05-activity-copy.svg | Read initial integer value then modify only the original |
| Reservoir | 06-activity-reservoir.svg | Valid-input precondition, guard and returns |
| Strict threshold | 07-activity-strict.svg | Strict guard excludes equality |
| Inclusive threshold | 08-activity-inclusive.svg | Inclusive guard includes equality |

For the rejected source, do not describe the full reference activity as its executable model. Label it "Conception attendue de référence" and identify the absent count actions and nonexecuted writes/return. The wrong-initializer source has its own actual-behavior activity, explicitly contrasted with the requirement of 3.

## Files and verification

Edit the three host lessons, four Markdown sheets and shared CSS. Add output coverage tests counting ten code-to-panel associations and verifying the referenced SVG assets. Browser checks cover opening and closing with Enter/Space, visible code retained, panels inside both explorer categories, mobile overflow and no-JavaScript reading. Preserve C++ extraction markers and execute existing excerpt tests after content edits. Check generated SVG bytes are unchanged and no duplicate HTML IDs are introduced.

## Four-pass review

Requirements: per-excerpt access while retaining visible primary conception. Responsibilities: Markdown owns teaching mapping; shared CSS owns appearance; browser owns disclosure behavior. Simplicity: native details avoids custom state and nested-modal focus complexity. Patterns: none warranted. Principal risks are Markdown/MDX rendering differences, heading collisions and misleading attribution of a complete activity to an incomplete faulty fragment; explicit scope and output/browser checks address these.

## Interaction view

Reader activates summary → browser expands local panel → reader compares code and model → reader activates summary again → browser collapses panel. No cross-component sequence, class model or additional C++ activity is needed: native disclosure has two states and the existing reviewed activities already model the code.

## First-program mapping extension

The [approved first-program conception](program-skeleton.md) adds two mappings to the ten pilot excerpts above, for twelve teaching C++ fences in total. Both primary activities remain visible before code.

| Excerpt | Reviewed diagram | Specific panel explanation |
| --- | --- | --- |
| program-ready | program-skeleton/ready.svg | Write Ready and a newline with std::cout, then return 0; output and status are separate |
| program-silent | program-skeleton/silent.svg | Return 0 with no write action; stdout is empty |

Each source marker identifies one complete program, followed immediately by its uniquely keyed disclosure. Includes, signature, braces and activity initial/final nodes are not extra output statements. No companion sheets or explorer categories are added.

## Ordered-output mapping extension

The [approved ordered-output conception](ordered-output.md) adds three mappings, for fifteen teaching C++ fences in total. Each primary activity precedes its complete program; its uniquely keyed disclosure immediately follows the code. No companion sheets or explorer are added.

| Excerpt | Reviewed diagram | Specific panel explanation |
| --- | --- | --- |
| program-ordered | ordered-output/01-activity-ordered.svg | Write Program started and a newline, then Program finished and a newline, then return 0 |
| program-reversed | ordered-output/02-activity-reversed.svg | Same two literals in reversed statement order, then return 0 |
| program-joined | ordered-output/03-activity-joined.svg | Write System plus a significant space, then ready and a newline, then return 0 |

Each mapping has three action rows. Structural syntax and activity initial/final nodes are not extra statements.

## Observable-variable mapping update

The [accepted observable-variable extension](observable-variables.md) replaces the one CPP-01 fragment with one complete marked program, keeping `measurement-primary` and fifteen teaching fences in total. Each observation maps two separate statements: read/write the variable, then write a newline. The original two-action fragment model is historical. Stock and copy retain their existing mappings and scoped fragments.

## Observable-constant mapping update

The [accepted CPP-09 extension](observable-constants-lesson.md) replaces all three fragments with marked complete sources, retaining constant-valid/constant-rejected/constant-wrong and fifteen teaching fences overall. Both runtime cases map all twelve statements in six rows; each observation groups four writes. The rejected case maps all five statements with explicit compile-only qualifications. No shared reader behavior changes. The old constant-limit activity remains historical; published snapshot provenance follows the new stable-limit render, while the wrong case uses the new wrong-limit render.
