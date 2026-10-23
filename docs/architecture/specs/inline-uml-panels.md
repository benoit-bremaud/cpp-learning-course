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
| CPP-01 measurement_count | measurement-count.svg | Creation with 0 then assignment to 1 |
| CPP-09 valid | constant-limit.svg | Fixed limit and independently mutable count |
| CPP-09 forbidden assignment | constant-limit.svg | Reference the invariant; the invalid fragment cannot execute successfully; count actions are outside this fragment |
| CPP-09 wrong initial value | constant-limit.svg | Requirement says 3, fragment initializes 30; only the first action is compared, later count actions are outside scope |
| Guided indicator | threshold-indicator.svg | Input, threshold, guard, two returns; preserve pinned source |
| Stock | 04-activity-stock.svg | Two actions and values 12 then 11 |
| Copy | 05-activity-copy.svg | Read initial integer value then modify only the original |
| Reservoir | 06-activity-reservoir.svg | Valid-input precondition, guard and returns |
| Strict threshold | 07-activity-strict.svg | Strict guard excludes equality |
| Inclusive threshold | 08-activity-inclusive.svg | Inclusive guard includes equality |

Do not describe the full reference activity as the exact executable model of either short faulty fragment. Label it “Conception attendue de référence” and explicitly identify omitted actions. No new algorithm or teaching-code change is required.

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
