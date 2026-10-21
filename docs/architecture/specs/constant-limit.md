# CPP-09 — Stable limit and evolving count

Status: detailed conception and graduated organization explicitly approved by the owner. Implementation and publication remain separate reviewed work.

## Need

Replace abstract explanations of const with concrete comparisons in the main lesson. Prerequisite: CPP-01's ordinary local integers, initialization and assignment. One new central idea: prohibit modification of a particular integer after its initialization. No array, loop, device API or exception mechanism is required.

## Teaching contracts and examples

### CL-01 — Valid primary example

The stated requirement is a fixed limit of 3 measurements for a session. Declare an ordinary local constant integer named `measurement_limit`, initialized to 3. Initialize a separate mutable integer `measurement_count` to 0, then assign the known total 1 to it. At the final checkpoint the pair is (3, 1); before the assignment it is (3, 0).

Explain the choice of 3 as a fictional requirement, not a hardware capacity. This excerpt neither allocates storage nor checks or enforces the count against the limit. As in CPP-01, assigning 1 is not acquisition or incrementing. The constant is fixed for the lifetime of this local object, not across all program executions.

### CL-02 — Modification rejected at compilation

Starting from the constant declaration in CL-01, add a direct assignment of 4 to `measurement_limit`. This is an intentionally ill-formed comparison, not an executable alternative. Its expected observation is compiler rejection. Present valid mutable-count assignment beside invalid constant-limit assignment, with a precise explanation of the different declared objects.

Do not draw a successful runtime path for the rejected fragment. Reference the primary conception's invariant and identify the violating assignment. A compiler diagnostic must be captured from an actual compilation and labelled with tool/version; do not imply exact text is portable. Compile only; no executable should be run for this case.

### CL-03 — Stable does not mean correct

Keep the original requirement of 3 and contrast initialization of the constant to 30. The alternative compiles but violates the requirement immediately. It is a labelled faulty variant of the primary initialization, not a newly approved requirement. The activity's first action is the exact point of divergence. Show expected 3 versus actual 30; const prevents subsequent mutation but cannot validate the chosen requirement value.

### CL-04 — Same principle in a second context

Use the already published strict temperature-indicator reference as a short narrated transfer: its threshold is 30 while the supplied temperature varies. Reference its existing lesson/UML instead of adding a new executable program. State both invariant and context change. Do not require the learner to understand conditions or functions to finish the core const explanation; the complete indicator is optional guided reading.

## Runtime initialization nuance

Retain the precise qualification that const does not necessarily mean compile-time-known, but do not inject input APIs or unexplained function calls into this beginner lesson. Give an explicitly conceptual scenario: a setting supplied for a session, then kept fixed for that session. A code-based runtime-initialization sheet is deferred until function inputs have been introduced. Do not call it completed example coverage or teach constexpr as a prerequisite here.

## Proposed lesson order

1. Situation and table identifying which value changes and why.
2. Expected checkpoints (limit 3/count 0, then limit 3/count 1).
3. The primary activity and symbol recap.
4. Primary excerpt and line-to-action mapping; explain the role of const on the limit.
5. Side-by-side permitted and rejected assignment, with observed diagnostic.
6. Constant-but-wrong variant and the separation between language validity and requirement correctness.
7. Short transfer to the existing threshold reference.
8. Runtime-known qualification with its explicit later-study boundary.
9. Summary: what is fixed, for how long, who checks the prohibition, what is not guaranteed.

The main page remains readable without a dialog. Do not add an empty explorer or manufacture four extra sheets to satisfy a quota. Record further contextual-sheet coverage as pending under the charter.

## UML and evidence mapping

| Contract | Conception evidence | Planned verification |
| --- | --- | --- |
| CL-01 | Three ordered actions; constant invariant | Compile actual excerpt in C++17; assert each initialized value and pair before/after assignment |
| CL-02 | Invariant violation, no valid runtime | Compile baseline successfully, then reject isolated forbidden assignment; record real diagnostic |
| CL-03 | Deliberate divergence at first action | Compile faulty variant; check resulting value differs from required 3; label fault explicitly |
| CL-04 | Existing threshold study, no new algorithm | Verify reference and wording; keep source revision unchanged |

Code fragments and tables will be connected to the activity explicitly. The UML is not a diagram of the compiler's type-checking implementation.

## Files and limits

- `src/content/docs/notions/cpp-09.md`: revise lesson; preserve route and prerequisite link.
- `public/diagrams/examples/constant-limit.svg`: generated snapshot of reviewed activity.
- `tests/constant-limit.py`: extract labelled examples from the lesson and compile in isolated temporary files; successful baseline prevents unrelated compiler failures being mistaken for the intended rejection.
- Update validation and pedagogical audit with actual outcomes only.

No new dependency, application component, CI change, publication or standalone exercise repository. Additional illustrative code remains course reading; executable learner practice remains a separate repository.

## Four-pass review

1. Requirements: each example answers a different question (allowed evolution, forbidden mutation, wrong initial requirement, transfer). Results and limits are explicit.
2. Responsibilities/dependencies: scalar-only examples separate stated domain requirement from compiler enforcement. No framework or hardware dependency.
3. Simplicity: reuse CPP-01's count and existing indicator reference. No arrays, capacity enforcement or event handling is implied by the word limit.
4. Patterns: no pattern, class or sequence diagram is justified. One activity explains the valid updates; invalid code is diagnosed, not falsely animated as execution.

Human review must still check whether switching between compilation rejection and wrong-but-valid initialization is understandable. Human reading review remains pending.

## Accepted organization decision

Use one worked primary example followed by targeted contrasts in the main page. The weighted discussion rated this arrangement 96/100 as a subjective decision aid, not measured educational effectiveness. Runtime initialization code remains deferred until function parameters are available.
