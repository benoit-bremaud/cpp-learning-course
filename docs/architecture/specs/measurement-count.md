# CPP-01 — Measurement count worked example

Status: context and pedagogical direction approved by the owner following finding P1. The owner explicitly approved the detailed conception before implementation. The worked example is implemented locally; no publication.

## Need and acceptance criteria

CPP-01 must teach initialization versus assignment without requiring the optional explorer. A novice who has read TOOL-01 should be able to identify the variable's meaning, its first value and a subsequent replacement. Companion stock/copy sheets keep their existing roles and contracts.

- MC-01: introduce the meaning of the data before syntax: number of measurements already received, not a measured temperature.
- MC-02: use one ordinary local integer named `measurement_count`, initialized to 0, then assigned the known total 1.
- MC-03: show both observable checkpoints, 0 then 1, with an exact mapping between the activity and the future two-instruction excerpt.
- MC-04: explain that these are two successive instructions in a function, not a complete standalone program. Explain a function minimally as a named group of instructions; writing one is not required here.
- MC-05: state that the second instruction executes unconditionally when reached. It neither waits for a measurement nor checks a sensor. The story supplies a known total; acquisition, event handling and incrementing are outside scope.
- MC-06: teach the normal explicit-initialization case before warning about uninitialized local integers. Never invite the reader to evaluate an uninitialized value.
- MC-07: keep the lesson self-contained; the explorer adds transfer and depth, not missing essential instruction.

## Behavioral contract

This is a straight-line state-update illustration, not an autonomous measurement counter. No inputs, outputs, sensor, I/O, loop, branch, class or persistent state are introduced. At the first checkpoint `measurement_count` equals 0. At the second it equals 1. The second operation assigns a literal known total; it does not compute previous value plus one. Running that assignment repeatedly would still store 1, so the lesson must not promise counting arbitrary arrivals.

The conceptual before/after moments of the story do not add an unrepresented waiting step. The diagram contains only the two actions performed by the excerpt. A complete function wrapper and observable checks belong to the validation harness, not to the beginner excerpt.

## Proposed lesson sequence

1. Situation: “Nous voulons représenter le nombre de mesures déjà reçues. Au départ, aucune : le total connu est 0. Pour illustrer une mise à jour, le total connu devient ensuite 1.”
2. Expected values: small table with two moments; distinguish a count of measurements from a temperature value.
3. UML: explain start, action and end symbols, then follow both actions. Notes show observations, not executable actions.
4. Matching excerpt: declare an ordinary integer `measurement_count` with initial value 0; subsequently assign 1 to that existing variable. No increment operator or sensor API.
5. Reading key: int is the integer type; measurement_count is the chosen identifier; 0 is the initial value; the later assignment replaces the value. Explain semicolons once. Avoid presenting initialization and assignment as semantically identical just because both spell '=' here.
6. Vocabulary: attach declaration, initialization and assignment to the two concrete actions just read. State that the first instruction also defines the variable; postpone the general declaration/definition distinction.
7. Pitfall: redeclaring the same name in the same block does not update it; define “same block” in plain language before using that term. Describe the error without adding an unreviewed executable counterexample.
8. Explicit initialization: an ordinary local integer is not automatically zero. Explain the chosen safe approach without reading an uninitialized variable or claiming one particular garbage value.
9. Summary and links: initial value vs replacement; zero is a valid empty count but does not stand for a missing sensor measurement. Stock transfers the concept; copy introduces a second independent value.

No scored quiz, browser execution or new exercise repository is added. A new general comprehension-check policy remains a separate review decision.

## Traceability and verification

| Requirement | Activity / lesson evidence | Planned verification |
| --- | --- | --- |
| MC-01 | Situation and count-versus-temperature distinction | Editorial review |
| MC-02/03 | Initialize to 0; assign 1; two observation notes | Compile actual excerpt with C++17; assert after each action, not only at the end |
| MC-04/05 | Excerpt framing and explicit acquisition exclusions | Review for false automatic-counting implications |
| MC-06 | Safe-case-first ordering | Check no uninitialized-value evaluation is proposed |
| MC-07 | Worked example before explorer | Read lesson without opening companion sheets |

The renderer must embed an unchanged SVG generated from the reviewed PlantUML source. The correspondence table must name both actual instructions once implementation is approved. No published-practice link until a corresponding target exists.

## Planned files

- `src/content/docs/notions/cpp-01.mdx`: revise the primary explanation, preserving slug and explorer references.
- `public/diagrams/examples/measurement-count.svg`: generated snapshot of this activity, with provenance.
- `tests/example-code.py`: extract the new excerpt and verify both intermediate and final values.
- `docs/validation.md` and the pedagogy review: record actual results and resolution of P1 after implementation, without marking other findings resolved.

## Four-pass conception review

1. Requirements: all MC requirements map above; both values are observable in tests. Acquisition is deliberately absent in both diagram and future code.
2. Dependencies and responsibilities: one local scalar, no infrastructure dependency; the course explains a value update rather than pretending to implement a sensor.
3. KISS/YAGNI/DRY: retain the two approved companion sheets. No shared C++ abstraction, new runtime component or device setup is justified.
4. Pattern fit: no design pattern or class diagram is needed. One activity answers the real question: which operation establishes the initial value and which replaces it?

Remaining risk: a reader can still interpret “measurement count” as a working event counter. The explicit known-total framing and unconditional assignment explanation are required, not optional footnotes. Human reading review remains necessary.
