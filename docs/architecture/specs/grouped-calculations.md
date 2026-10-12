# Grouped calculations: combine kit counts before multiplying

Status: enriched option A approved by the owner and implemented locally; verification recorded in docs/validation.md.

## Need and boundaries

Extend first-multiplications with a single new difficulty: grouping a sum as an operand of multiplication. Need: three existing kits plus two additional kits, each containing four components, total twenty components. Distinguish logical grouping from operand execution order. Inputs are known counts in 0..10; sum at most 20 and product at most 200. These are teaching assumptions, not guards. No division, loops, self-update, operator table or hardware.

## Proposed independent fragments, in reading order

G1 — make the intermediate quantity explicit using familiar declarations:
```cpp
int existing_kit_count = 3;
int additional_kit_count = 2;
int components_per_kit = 4;
int total_kit_count = existing_kit_count + additional_kit_count;
int component_count = total_kit_count * components_per_kit;
```
Trace inputs 3,2,4, then total_kit_count=5 and component_count=20. Add counts in the same unit (kits), then multiply by components per kit. This establishes the requirement before any precedence discussion.

G2 — group the sum in one initializer, same final total:
```cpp
int existing_kit_count = 3;
int additional_kit_count = 2;
int components_per_kit = 4;
int component_count = (existing_kit_count + additional_kit_count) * components_per_kit;
```
Parentheses delimit the sum used as one multiplication operand. Intermediate value five exists in the explanation, but no total_kit_count variable is declared here. Explicit intermediate form remains a valid readability choice; shorter is not inherently better.

G3 — deliberately omitted parentheses, valid C++ but result eleven:
```cpp
int existing_kit_count = 3;
int additional_kit_count = 2;
int components_per_kit = 4;
int component_count = existing_kit_count + additional_kit_count * components_per_kit;
```
Explain * binds more tightly than +: the product is 2*4=8 and the sum is 3+8=11. Does not satisfy required twenty. The operands now combine kits with a component quantity; names do not provide unit checking. Correct by restoring the grouped sum. Do not say C++ always executes from left to right or that parentheses sequence arbitrary operand effects.

G4 — outer parentheses alone do not repair the formula, still eleven:
```cpp
int existing_kit_count = 3;
int additional_kit_count = 2;
int components_per_kit = 4;
int component_count = (existing_kit_count + additional_kit_count * components_per_kit);
```
One changed dimension relative to G3. Enclosing the whole expression leaves its internal grouping unchanged. Discrepancy card reuses expected grouped design with explicit actual eleven versus expected twenty. No blanket claim that parentheses always change a result.

G5 — transfer to a different requirement: three loose components plus two kits of four, correctly eleven:
```cpp
int loose_component_count = 3;
int kit_count = 2;
int components_per_kit = 4;
int component_count = loose_component_count + kit_count * components_per_kit;
```
Same numeric expression as G3 but a different valid contract. The multiplication produces eight components; the addition combines component quantities, three plus eight. Missing parentheses is not intrinsically an error. The names reflect the new requirement; this is not renaming G3 to claim its original five-kit requirement was met. This full snippet gets its own valid UML and a normal UML button. Read only after the four same-requirement comparisons, separated by an explicit heading announcing a changed need.

## UML and presentation

Three authoritative activities: explicit intermediate (G1), grouped expression (G2), loose components plus kits (G5). G1 and G2 initialize the same three inputs; G5 initializes its own role-specific inputs. Explicit version creates total_kit_count; grouped version calculates a sum without inventing that variable, multiplies its value by components_per_kit, then initializes component_count. Actions are conceptual dependencies, not guaranteed machine instruction order. G3/G4 use the grouped expected model, explicitly labelled expected20/actual11 before the image, not claimed as actual execution.

All five fragments independent inside main with no output. Visible conception precedes code; existing discreet cards and no-script fallback remain. No new explorer, interactive assessment or downloadable sheet. Include short traces (5→20, 8→11) and input values unchanged. A first table compares the four forms under the five-kit requirement. A separate transfer case G5 changes the requirement, retaining 3,2,4 to isolate meaning rather than arithmetic difficulty. Never label all appearances of eleven as wrong.

## Planned files and acceptance checks after approval

- src/content/docs/notions/parentheses-calculs.md, five fragments and mapping tables.
- Three public/diagrams/examples/grouping-{intermediate,grouped,loose}.svg snapshots.
- Sidebar, multiplication continuation, parcours.md and homepage availability/count.
- tests/grouped-calculations.py: extract all five actual snippets, C++17 compilation, initialized-input and intermediate/final assertions, 20/20/11/11/11 outcomes and SVG provenance.
- Browser route coverage: five cards, including both discrepancy cards, mobile/desktop/no-JS; existing structural/link tests. Update README command and docs/validation evidence.

## Four-pass conception review

Requirements: sum kit quantities first in the mathematical model, then convert to components. Results discriminating (20 versus11). G4 resolves a distinct misconception about where parentheses belong.
Dependencies: all operators and declarations known; only grouping is new. No new code component/framework layer. Full-expression sequencing in G1 is distinct from conceptual calculation dependencies in G2.
Simplicity: three models, expected-design reuse for both wrong-but-valid cases. Do not compress identifiers or introduce a helper merely to shorten a line; horizontal scrolling for the bounded code line follows existing site behavior.
Pattern fit: no design pattern justified. Check absence of fictitious variables in grouped UML, conflation of precedence with evaluation order, or a claim that fewer lines are necessarily superior.

## Deeper review findings and revised alternatives

The original pair of wrong formulas could teach a false rule: always add parentheses. Add G5 to show when precedence already expresses the correct need. Keep G4: it diagnoses a different misconception, that enclosing the whole expression repairs its internal grouping. Do not merge these questions.

Keep G1 before G2: arithmetic dependency is understood before compact syntax. Do not claim fewer variables mean faster code or less runtime memory; no optimization comparison is taught. A staged implementation remains valid and readable.

Parentheses bind a subexpression; they do not generally order evaluation of arbitrary operands or function calls. The lesson has no calls/side effects in these expressions. The diagram describes arithmetic dependencies, not a processor schedule. State the bounded distinction once, rather than introducing advanced sequencing vocabulary into every explanation.

Check quality of input choice. For the original requirement, grouped and ungrouped results coincide if existing_kit_count is zero or components_per_kit is one. Retain 3,2,4 to discriminate. Verify these masking cases in conception review; do not add another learner table repeating the previous multiplication lesson's testing lesson. No extra subtraction/associativity example: that is a separate question and not required to understand this sum/product.

Revised weights: progression30%, misconception/transfer coverage30%, reading load25%, simplicity15%. Internal judgment, not measured learning gains.
A — Four same-need cases plus the valid loose-components transfer: 5,5,4,4 = 4.60.
B — Original four same-need cases: 5,3,5,5 = 4.40.
C — Literal-only comparison: 4,2,5,5 = 3.80.
D — Full operator-priority/associativity table: 2,4,2,2 = 2.60.
E — Defer until after division: 2,2,4,4 = 2.80.

A adds one short study and diagram, but prevents treating a requirement-relative error as an intrinsically invalid syntax choice. B is shorter but leaves that transfer untested. C suits an arithmetic reminder, not this design-oriented course. D overloads prerequisites; E adds division before resolving the already promised grouping topic. Scores were recomputed because the original coverage score of five omitted transfer.

Confidence high: language rules and exact numerical distinctions verified from primary draft text and C++17 compilation. Confidence moderate: added transfer is preferable for this learner; its actual effectiveness requires feedback. Parentheses-only diagrams are not automatic syntax translations: named intermediates and expected-versus-actual distinction remain explicit.

## Primary sources checked

- https://eel.is/c++draft/expr.prim.paren — parenthesized expression preserves inner expression meaning.
- https://eel.is/c++draft/expr.add — grammar embeds multiplicative expressions in additive expressions.
- https://eel.is/c++draft/intro.execution — sequencing terminology distinct from grouping.

Public HTML working draft, not the published ISO C++17 edition. Validate concrete results in C++17; keep advanced sequencing out of the beginner lesson except a bounded clarification. Confidence high on these results, moderate on relative pedagogical effectiveness until learner feedback.
