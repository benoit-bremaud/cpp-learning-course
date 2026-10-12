# Repeated assignment — focused CPP-01 extension

Status: owner authorized integration while emphasizing plentiful, progressive examples; implemented locally. Implements only VC-01 from value-comparisons.md after the program/block orientation; all other comparisons remain outside this batch.

## Need and exact contract

CPP-01 currently asserts in prose that repeating assignment leaves the value at one. Add a worked comparison immediately after the existing primary need/UML/result table. Reuse its variable and values: initialize measurement_count to zero, assign one, assign one again. The three observation checkpoints are zero, one, one. These are consecutive statements in one local function block, not a loop or independently executed snippets. No count of received events, sensor access, increment, output instruction or undefined behavior is implied.

The existing proposed activity at ../diagrams/value-comparisons/01-activity-repeat.puml already models exactly these three actions. Reformat it to the accepted compact French-label layout; place checkpoint observations in the lesson table. Preserve the primary example and introduce only one additional instruction. The table is an explanatory trace, not console output.

## Lesson and verification plan

Explain repeated recording of the same known total: assigning one twice does not count two arrivals. Present conception, actual three-line C++ fragment, UML card, three-row trace and the misconception's correction. Do not introduce ++, arithmetic, redeclaration or interactive assessment.

Files: CPP-01 MDX; authoritative repeat PlantUML and generated snapshot; public SVG; tests/example-code.py; browser route count; validation record. Add stable labels to the existing primary snippet and new repeated snippet. Replace the test's one-fence assumption with labelled extraction and assert each checkpoint for both snippets. Run Astro check, build/output tests, C++ extraction test and browser card checks.

## Four-pass review

Traceability: three UML actions match three instructions and three checkpoint values. Dependencies: only already-taught initialization/assignment; function/block context is explicitly recalled. Simplicity: one variation of the existing scenario, no extra abstraction or pattern. Teaching risk: reader might infer acquisition or counting from the identifier; explicitly state that the total is supplied directly and no event is detected.
