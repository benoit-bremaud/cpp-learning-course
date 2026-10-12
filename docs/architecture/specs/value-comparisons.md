# Targeted value comparisons — CPP-01 and CPP-09

Status: proposed detailed conception for the requested expansion of code examples. Awaiting owner validation before new snippets enter lessons. No publication.

## Teaching scope

Add short, independently readable comparisons next to the explanations they substantiate. Existing primary examples and companion sheets stay unchanged. Every new fragment is scoped inside a function; every value is initialized. No sensor API, loop, arithmetic operator, class or new dependency is introduced.

| ID | Location and learning question | Exact ordered actions | Expected observations |
| --- | --- | --- | --- |
| VC-01 | CPP-01: does repeating assignment count arrivals? | Initialize measurement_count to 0; assign 1; assign 1 again | 0, 1, 1; repeating replacement does not increment |
| VC-02 | CPP-01: does a variable remember its old values? | Initialize measurement_count to 0; assign known total 2; assign known total 5 | 0, 2, 5; current value replaces the earlier value, no history is stored |
| VC-03 | CPP-01: why not repeat int to update a value? | Contrast existing valid MC-01 with declaring measurement_count twice in the same block, initialized to 0 and 1 | Valid baseline compiles; redeclaration is rejected, so no runtime values are attributed to it |
| VC-04 | CPP-09: does a constant limit enforce a maximum? | Initialize constant measurement_limit to 3; initialize measurement_count to 0; assign 4 to the mutable count | (3,0), then (3,4); compiles, const invariant holds, but a hypothetical count<=limit rule is not enforced |

VC-02 uses known totals supplied by the story, not an autonomous counter. VC-04 deliberately illustrates missing capacity enforcement: it must not be presented as a correct implementation of a maximum-count requirement. Teaching this observation does not authorize adding a conditional guard yet.

## Placement and explanation — superseding the original batch

The owner approved prerequisite-driven sequencing after the external-reference review. These comparisons are not one immediate implementation batch.

- VC-01 follows the primary assignment explanation, after the program/block orientation. It is the first candidate for a new snippet, subject to its detailed conception review.
- VC-02 is deferred: the current copy sheet already supports value tracking. Reconsider only for a distinct unmet learning need.
- VC-03 follows a concrete block explanation. Keep the invalid example separate from the first successful reading; it has no successful execution activity.
- VC-04 is deferred to the conditions module, where an unenforced limit can be contrasted with explicit enforcement. CPP-09 keeps the simple warning. The future guarded variant requires its own reviewed design; the old unguarded activity is not that design.

Use distinct pedagogical titles and stable snippet labels for extraction. Short inline comparisons share the existing course presentation; no additional explorer UI is required. Teaching diagram labels are French; code identifiers are English.

## Verification

Extract actual labelled snippets from the authored lessons into temporary C++17 programs. Assert all checkpoints, including intermediate ones. For VC-03 compile the correct baseline successfully, then require failure on the same-name declaration with a relevant diagnostic. Never execute the rejected fragment. Verify SVG provenance, local links, unique heading IDs and rendered page readability. Updating tests/example-code.py must replace its single-excerpt assumption with explicit labels before extra CPP-01 blocks are added.

## Files affected after approval

CPP-01 MDX, CPP-09 Markdown, generated public SVG snapshots, example extraction tests, validation record. No framework or dependency change. The historical action inventory remains a proposal; placement above takes precedence and each implemented subset must have its conception confirmed.

## Four-pass review

Requirements: each contrast resolves a different misconception, with a concrete observation; no numeric quota drives the choice. Dependencies: plain local integers only. Simplicity: reuse existing naming and prerequisite scope; no hardware simulation or new abstraction. Pattern fit: no pattern justified; three straight-line activities plus a documented compile rejection suffice. Risks: explicitly distinguish replacement from acquisition, and demonstrate missing enforcement without endorsing the faulty requirement implementation.


## Current development order

The approved first-program and ordered-output lessons are now implemented. Continue with VC-01's focused assignment comparison as the next conception to review, followed by the block-dependent VC-03 comparison. Do not implement the old batch wholesale. The newly suggested interactive assessments are explicitly deferred and do not belong to this work item. VC-02 remains deferred and VC-04 stays with conditions.


## VC-01 implementation follow-up

Owner requested integration with plentiful progressive examples. The focused repeated-assignment conception is now implemented in CPP-01: existing 0→1 baseline and new 0→1→1 fragment, with compact activity, card and all checkpoints checked. A comparison guide connects these to existing stock/copy sheets. Other inventory items remain deferred or subject to their own conception; this does not authorize the old batch wholesale.


## VC-03 implementation follow-up

The owner approved the valid/rejected complete-program pair in assignment-redeclaration.md. CPP-01 now shows the enclosing main block, expected activity, actual GCC 13.3.0 diagnostic and correction. Scope is explicitly limited to this ordinary local integer's two definitions in one block. The exact examples and instrumented checkpoints are verified by tests/assignment-redeclaration.py. No nested-scope or interactive-assessment feature was introduced.
