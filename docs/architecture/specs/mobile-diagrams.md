# Mobile teaching diagrams

Status: option A approved and implemented locally.

Need: improve readability without changing teaching contracts or adding a nested modal. Seven local activities use multiline French labels, preserved English identifiers and 16px source text. Observations formerly in side notes remain in lesson prose/tables; the reservoir input precondition remains explicit before its diagram. The published indicator snapshot is preserved according to design.md provenance rules.

Every diagram occurrence links to its own original SVG with an explicit new-tab label and noopener/noreferrer. Native anchor behavior needs no client state. Four-pass review: contract and traceability preserved; content owns labels, PlantUML owns rendering, browser owns navigation; no extra dependency or pattern justified. Keyboard navigation excludes descendants hidden by closed disclosures.

Validation covers source links, actual SVG assets, rendering in Markdown and MDX, popup destinations from the explorer, focus containment and narrow viewport overflow. Browser zoom usability on a physical phone remains a human review item.
