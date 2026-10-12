# Assignment versus a second local definition

Status: focused VC-03 conception approved by the owner and implemented locally.

## Need and boundaries

After CPP-01 initialization/assignment and the main/block orientation, explain why repeating int does not update the same ordinary local integer. Limit the rule to two initialized definitions of measurement_count in the same main body. Do not claim all C++ redeclarations are forbidden; declarations, function overloads and nested scope require separate treatment.

## Proposed examples and UML

Show two complete independent programs. Both begin with int main(), initialize measurement_count to zero and end with return 0. The valid program assigns one to the existing variable. The invalid variant replaces only that assignment with a second int measurement_count initialized to one in the same block. Neither prints a result. Valid checkpoints: zero then one. Invalid variant: compilation rejection, no executed trace.

Use a compact valid activity: initialize to zero, assign one, return zero, end. Invalid card references this expected design and identifies the conflicting second definition; do not model compiler rejection as an executed branch in the learner program. Keep full braces visible to make same-block scope concrete. Reuse existing main/return knowledge without adding cout, nested blocks, ++ or renaming as a supposed fix.

## Verification and files after approval

CPP-01 section Modifier n’est pas redéclarer, one authoritative activity and rendered SVG, per-snippet UML cards, tests/assignment-redeclaration.py and browser counts, validation log. Label snippets distinctly. Compile the valid full source in C++17; check zero exit and no output, with a separately instrumented extraction checking the two values. A set-but-unused warning is expected for a deliberately non-observable local; suppress only that warning in the valid harness rather than teaching irrelevant casts. Compile invalid source with syntax-only and assert the actual redeclaration diagnostic; do not run it. Report compiler/version when showing exact wording.

## Four-pass review

Traceability: same intended update, one syntax difference and explicit shared block. Dependencies: main, blocks and initialized integers already taught. Simplicity: valid/faulty pair only; no additional language mechanism or pattern. Risks: overgeneralizing redeclaration prohibition, attributing runtime values to invalid code, and confusing table observations with stdout. State these boundaries explicitly.

## References and evidence limits

- https://isocpp.org/std/the-standard — intended standards information entry point; retrieval returned HTTP 403 in this review, so it is not evidence for the rule. Distinguish the paid ISO publication from a public draft.
- https://eel.is/c++draft/basic.def.odr — public HTML rendering of the working draft, not the purchased ISO edition. Duplicate definitions rule supports this particular initialized-variable case.
- https://www.learncpp.com/cpp-tutorial/local-variables/ — pedagogical treatment of local scope. Borrow progression principles, not lesson text.

The lesson uses C++17. Verify the actual pair with a C++17 compiler; do not introduce newer draft exceptions or imply this current draft is the C++17 publication.
