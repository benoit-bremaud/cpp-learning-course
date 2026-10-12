# Pedagogical review — introductory course and example pilots

Status: historical audit with implementation follow-ups. The original findings below describe the reviewed baseline, not the current state. See the current-status reconciliation at the end; do not reopen resolved observations without checking current sources.

## Scope and evidence limits

Read the source of TOOL-01, CPP-01, CPP-09, the build overview, home, progression, UML method, guided indicator and the four companion sheets, together with the activity sources and the excerpt test harness. This is an editorial/conception review, not a learner study. Passing code and browser tests establishes specific technical behavior, not comprehension, retention or transfer. No numeric pedagogical score is justified without a defined rubric and learner observations.

## Findings in priority order

### P1 — CPP-01 lacks a worked example in the main learning path

Evidence: src/content/docs/notions/cpp-01.mdx explains a measurement counter and vocabulary but contains no C++ block or concrete value trace; the first instructions are in the optional component-stock sheet.

Impact: a learner can finish the page without seeing what initialization and assignment look like. “Other contexts” is doing the work of the missing first context. The prerequisite TOOL-01 does not establish variable syntax.

Recommendation: introduce a minimal primary example with explicit initial and next values, a matching reviewed activity, and a direct mapping from int/name/initializer to the first action and assignment to the next. Keep the explorer supplementary. Reuse the approved stock example as the main worked example only if the owner accepts changing its role; otherwise design the measurement-counter example before adding code. Do not silently duplicate the same sheet as both primary and alternative context.

### P2 — The prerequisite chain hides language-reading demands

Evidence: CPP-01 discusses local integers and functions; CPP-09 discusses const without showing its syntax. The indicator and reservoir use int, bool, const, function parameters, return, branches and noexcept. The indicator provides a useful glossary, but novices still have to integrate many new elements at once.

Impact: understanding the scenario can be mistaken for understanding the C++ expression of it. The home page points beginners to the dense build overview rather than a single recommended first lesson.

Recommendation: distinguish “guided reading: terms explained here” from “independent practice: prerequisites required”. Give a default first route while keeping free navigation. Provide a small consistent reading key for excerpts; explain the essential syntax now and mark peripheral details once. Do not remove noexcept from the existing pinned reference or create a second untracked variant of that source.

### P3 — Copy is relevant, but its label and reading support can improve

Evidence: independent-copy demonstrates an ordinary integer value snapshot with correct outcomes 11 and 12, and explicitly excludes pointers/references. It says the third instruction changes only the named integer.

Assessment: this is the strongest new conceptual extension. Its conclusion is correct in the stated scope; do not classify it as a C++ bug. “Original” and “copy” can nevertheless imply an enduring special relationship unless the independent-variable model is made concrete.

Recommendation: explain the right-hand value being read before the left-hand initialization, then use a two-column trace. Keep the explicit limitation to independent ordinary integers. Define “bloc” when using the stock sheet's redeclaration counterexample; learners have not yet studied scope.

### P4 — Inclusive threshold repeats the core lesson without a clear added task

Evidence: the guided indicator already discusses 29/30/31, the equality boundary and a >= mutation rejected by tests. inclusive-threshold repeats those inputs and adds a second explicit contract, which is useful but not prominently framed as its added value.

Impact: length and duplicated diagrams/functions can suggest depth while mostly repeating familiar material.

Recommendation: retain the approved subject, but frame its purpose as comparing two legitimate specifications and choosing a discriminating input. Show why 29 and 31 cannot distinguish the contracts. Avoid presenting a new operator alone as a deeper lesson. Preserve separate UML/code correspondence and the original strict function unchanged.

### P5 — Reservoir precondition is stated but not operationally explained

Evidence: reservoir-level correctly limits inputs to integer percentages 0..100 and explicitly excludes invalid inputs. The C++ int parameter does not enforce that interval; no validation branch exists.

Assessment: no contract violation for valid inputs. This is a hidden learning distinction, not grounds to add defensive branches to the approved example.

Recommendation: explain that a precondition is what the caller must guarantee, and that choosing int alone does not check percentages. Distinguish the assumed valid domain from the function's actual comparison. Keep physical acquisition and invalid-input handling outside this simple example.

### P6 — UML adds reading work that is not consistently supported

Evidence: teaching prose is French, while diagram titles/actions are English. Stock explains initial/action/final nodes; later sheets assume more familiarity. Traceability is often narrative rather than the explicit mapping promised by the UML method.

Impact: learners must translate both a new graphical notation and a new programming notation. A detailed diagram can be technically aligned without being pedagogically explained.

Recommendation: use French explanatory labels in teaching diagrams while preserving exact English code identifiers; keep engineering documents English. Introduce symbols where first needed and explain one concrete path through each decision. Add compact mappings only where they clarify the transition to code. Regenerate SVGs from authoritative sources; never edit snapshots manually.

### P7 — Explained answers do not establish learner understanding

Evidence: sheets provide outcomes immediately and end with summaries. The progression promises a “proof of understanding”, but the pilot pages do not offer a clear criterion for deciding whether to proceed. Existing C++ tests verify final results; the stock test does not check its intermediate value 12.

Recommendation: propose a small optional mental prediction/self-explanation with an explained answer and a readiness criterion, if the owner agrees this fits the reading-only course. No compiler, scored quiz or browser execution is needed. Keep actual coding practice in its independent repository. Do not claim the current tests verify every intermediate state or that tests establish educational effectiveness.

### P8 — Availability and UI hierarchy need an editorial pass

Evidence: CPP-01 still states “study and exercise to come”, although complementary local sheets have approved UML studies. Home availability omits the four sheets. The component renders a sheet title as h3 before a body heading h2; repeated large introductory headings consume reading space.

Recommendation: distinguish available reading, approved local studies and unpublished practice. Use a consistent heading hierarchy and eliminate titles that repeat the objective rather than orient the reader. A readable dialog is useful infrastructure, not a substitute for this editorial work.

## Strengths worth preserving

- Small scalar examples with explicit outcomes and no forced class hierarchy or patterns.
- Boundary cases and the separation between deciding and controlling physical hardware.
- Explicitly fictional thresholds and honest statements about unpublished practice.
- Independent integer-copy example provides a useful new mental model.
- UML, snippets and tables broadly agree for the stated inputs.
- Two categories support transfer versus deeper reasoning, provided each sheet genuinely fulfills its assigned role.

## Recommended order of changes

1. Validate the main-example policy and repair CPP-01's primary learning path (P1).
2. Review terminology, declared prerequisites and default navigation (P2/P3).
3. Refocus threshold and clarify the reservoir contract without changing behavior (P4/P5).
4. Align teaching diagrams, traceability and heading hierarchy (P6/P8).
5. Agree on lightweight reading-comprehension checks (P7), then observe the owner reading the pilots before wider rollout.

Review each meaningful pedagogical decision with the owner rather than expanding the scope silently. No site-wide readiness claim until these gaps and the human reading review are addressed.

## P1 implementation follow-up

The owner selected the measurement-count context and approved its detailed conception. CPP-01 now provides the complete primary worked example, explains both instructions and their correspondence with the activity, distinguishes a count from a temperature, and explicitly excludes acquisition and automatic incrementing. Stock/copy remain optional complements. P1's missing-primary-example finding is addressed locally; human comprehension review remains pending. This does not close P2–P8 as a group.


## Deeper coverage analysis — systematic examples policy

Owner decision: systematic coverage, no arbitrary minimum snippet count. The charter records this decision. The proposals below are analysis, not approved new code contracts.

### Coverage by learning demand

| Section | Existing evidence | Remaining gap | Recommended addition and rationale |
| --- | --- | --- | --- |
| CPP-01 initialization/assignment | Primary 0→1 example with UML, syntax and trace; stock 12→11 transfer | Repeated assignment is asserted in prose only | A reviewed short trace of repeated assignment would distinguish replacement from incrementing without teaching arithmetic yet |
| CPP-01 redeclaration | Error described, block defined | The learner cannot visually contrast the two forms | A valid/invalid pair with expected compiler rejection; no fake successful execution diagram |
| CPP-01 initial value | Count zero contrasted with temperature 23 | Uninitialized-value warning remains abstract | Contrast an explicitly initialized local with a declaration lacking an initializer; never evaluate the latter; postpone advanced language-version terminology |
| CPP-09 const | Prose covers intention, forbidden assignment, runtime initialization | No actual declaration or concrete diagnostic | Highest coverage priority: one stable integer limit, one permitted evolving count, one rejected modification; later show a value supplied to a function and held constant during that call, with function prerequisites explicit |
| TOOL-01 compilation | Illustrative diagnostic, correct/incorrect arithmetic, stale firmware scenario | First heading says alarm although no alarm behavior is modeled; diagnostic not reproducible yet | Align the scenario vocabulary; retain honest illustrative status; future cloned reference should reproduce the intended error |
| Build overview | Definitions and stage table | Dense terminology without a continuous artifact example | Trace one tiny project through source/object/link/output/transfer; only name the stage-specific new information, and avoid adding a whole toolchain tutorial |
| Indicator | Complete worked rule and boundary trace | Many terms appear at once | Guided reading key and explicit “reading now / implementing later” distinction rather than removing parts of the pinned source |
| Reservoir | New context, opposite comparison, domain boundaries | Valid input assumption is not enforced by int | Explain the caller's obligation with a concrete out-of-domain scenario, without adding validation code to the approved contract |
| Inclusive threshold | Two correct specifications and boundary table | Most facts also appear in main lesson | Organize around selecting a distinguishing input: why 29 and 31 are insufficient, why 30 matters |
| UML method | View-selection table and process | Abstract method not anchored to the available worked reference | Walk through the existing indicator requirement, activity branch and corresponding test; no new fabricated architecture needed |

### Refinements to the recommendations

1. More examples do not mean more popup openings. The main lesson must carry each indispensable explanation; an optional sheet provides transfer or depth.
2. Stabilize one worked context before changing context. Otherwise learners must learn scenario vocabulary and syntax simultaneously. Explain the invariant and the one changed dimension in each comparison.
3. Keep beginner contexts meaningful but honest. The current count assignment is not a working counter; presenting it as such would be worse than a simpler non-hardware context. Preserve the explicit simulation boundary.
4. Match every extra example to a distinct unresolved question. Retain useful repetition for comparison; reject repetition presented as unexplained depth.
5. Separate compile rejection, runtime result and violation of an input precondition. They require different evidence and should not all be illustrated with “run and see”.
6. UML should clarify the modeled behavior. Multiple equivalent inputs may share the same activity with explicit traces. A code fragment that fails to compile cannot have a truthful successful runtime trace; show the intended valid behavior and the diagnosed divergence.
7. Do not front-load technical exceptions to protect every sentence. State a precise beginner scope (ordinary local integers here), give a usable rule, then place exceptions with their real prerequisites.
8. Automated checks prove selected outputs and references, not educational quality. A reviewer should be able to state what misconception each example prevents; human reading still needs to establish whether the explanations work for this learner.

### Priority recommendation

Keep P2–P8 visible. First design concrete const examples for CPP-09, since it is the next linked lesson and lacks all code illustration. In parallel editorial planning, map small contrasts still missing in CPP-01. Then refocus the already implemented reservoir/inclusive sheets, and connect the build/UML overview to concrete existing references. Avoid filling every popup before repairing the primary learning path.

This is not a claim that additional examples have been implemented or that the course meets the new policy. No change to learning deadlines, independent practice, local-only operation or conception approval gates.

## CPP-09 coverage follow-up

The missing primary const illustration has been addressed locally with the approved graduated structure. The lesson now distinguishes allowed mutation, compile rejection and a valid declaration with a wrong requirement value. The existing indicator provides optional transfer. Runtime-initialization code and expanded contextual sheets remain deferred explicitly; this does not resolve the whole prerequisite-chain finding or establish learner comprehension.


## Current-status reconciliation after approved consolidation

The owner approved option A: clarify existing explanations and prerequisites before adding another batch of code. This pass edits the three lessons and four companion sheets without changing any C++ fence, accepted behavior or diagram. It does not approve the separate value-comparisons expansion.

| Finding | Current evidence and disposition |
| --- | --- |
| P1 | Addressed locally by the primary measurement example; retained. |
| P2 | Guided-reading expectations now explicit in CPP-01, CPP-09, the indicator and companion sheets. Function-writing independence is not implied. Default home navigation remains outside this pass. |
| P3 | The existing checkpoint table already addresses value tracking. Added explicit right-hand read/left-hand initialization explanation and a block reminder in stock. No additional duplicate trace is needed. |
| P4 | The existing comparison already identifies equality. Refined the explanation of why 29 and 31 are useful but cannot distinguish the contracts, while 30 can. |
| P5 | Main sheet now defines the caller's obligation and explains an out-of-domain input of −5: the comparison is true but establishes neither input validity nor a valid physical interpretation. No validation branch or new contract was introduced. |
| P6 | Inline panels already provide local mappings and paths. Full French-label alignment and narrow-screen diagram readability remain open. |
| P7 | No learner-comprehension claim. Optional prediction checks remain a separate proposal; not added in this pass. |
| P8 | CPP-01 availability already distinguishes reading from unpublished practice. Site-wide availability inventory and explorer heading hierarchy remain open. |

Review conclusion: essential explanations for this batch are visible outside optional UML panels; the sheets retain distinct purposes (transfer of initialization, independent values, opposite comparison direction, and discriminating boundary). Existing code/diagram contracts remain unchanged. Technical checks cannot establish retention or independent learner mastery.

## Sequential reading review after the first-program lessons

Scope: programme-minimal, premiers-affichages, CPP-01, CPP-09 and independent-copy; focused read of next comparison prerequisites. No whole-course completeness claim.

- Corrected CPP-01's overly broad definition of incrementing: adding one to the current counter is the intended operation, not any calculation from a previous total.
- Updated CPP-01 availability to two primary examples plus two companion sheets, and replaced the obsolete inline-panel wording with the UML card control.
- Replaced CPP-09's statement that main would be introduced later with a link to its now-earlier lesson.
- Removed consecutive duplicate explanations in independent-copy, a redundant post-table warning in CPP-09, and the doubled output/result label in the silent program.
- Kept deliberate repetition between primary text and optional cards: each card must remain understandable when opened independently. Kept contrasted examples that demonstrate different outcomes; removing those would weaken the lesson.

The approved C++ blocks are unchanged by an extraction comparison. No additional sample or interactive assessment was introduced. Next conception remains VC-03, distinguishing assignment from redeclaration within one explicitly shown block; it must avoid teaching nested-scope shadowing prematurely.
