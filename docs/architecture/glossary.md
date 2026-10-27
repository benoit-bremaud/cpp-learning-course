# Architecture glossary

Status: owner-approved entries for #20; owner-approved arithmetic-update conception entries for #23; owner-approved equality-results conception entries for #26. This small index defines the terms used by its new activities; it does not claim to replace or retrospectively audit the definitions in earlier lesson specifications.

| Term | Meaning and source |
| --- | --- |
| Addition | Compute the sum of two small known integer operands; [accepted arithmetic contract](specs/arithmetic-update-lesson.md) |
| Arithmetic update | Read the current count, add 1, then replace its stored value in one assignment statement; approved #23 conception; [contract](specs/arithmetic-update-lesson.md) |
| Assignment | Replace the value of an already existing ordinary integer; [CPP-01](../../src/content/docs/notions/cpp-01.mdx) |
| Compile rejection | The complete source is ill-formed; no successful execution or output is claimed; [const contract CL-02](specs/constant-limit.md) |
| Constant integer | A local int object whose value cannot be modified after initialization through direct assignment; [CL-01](specs/constant-limit.md) |
| Count | Named integer total. CPP-01/CPP-09 store supplied totals; the proposed arithmetic lesson computes a next value from its prior value. Neither implies physical acquisition; [constant contract](specs/observable-constants-lesson.md), [accepted update](specs/arithmetic-update-lesson.md) |
| Initialization | Establish an object's initial value when it is created; [CPP-01](../../src/content/docs/notions/cpp-01.mdx) |
| Invariant | The limit remains unchanged during the modeled count update; the initial value may still be wrong for the requirement; [CL-03](specs/constant-limit.md) |
| Limit | Required fictional stable value 3, not automatically enforced capacity or allocated storage; [CL-01](specs/constant-limit.md) |
| Observation pair | Write the limit then the count, each followed by a newline: four statements grouped into one activity action; [proposed mapping](specs/observable-constants-lesson.md) |
| Operand | A value used by the addition; here the current count and literal 1; [proposed contract](specs/arithmetic-update-lesson.md) |
| Stored result | Value retained after assignment, not a formula that recomputes automatically; [proposed contract](specs/arithmetic-update-lesson.md) |
| Successful return | Return status 0 without an additional output write; [first-program conception](specs/program-skeleton.md) |

## Approved equality-results terms - #26

These new terms belong to the owner-approved [equality-results design](specs/equality-results-lesson.md). Earlier accepted entries retain their meaning and status.

| Term | Meaning and source |
| --- | --- |
| Boolean result | A true or false value produced by comparison and optionally stored in a bool object; accepted #26 contract |
| Default Boolean formatting | In the unchanged default stream state used here, stored true/false is printed as1/0; this is distinct from type identity or process status |
| Equality comparison | Evaluate == on two supplied small int values of the same type; a value computation, not branch selection |
| Inequality comparison | Evaluate != on those operands; false for equality, true for inequality, with no ordering conclusion |
| Reevaluation | Execute the comparison again at a later statement and assign its new result; not an autonomous event |
| Stored Boolean snapshot | Result retained from an earlier evaluation; changing the compared count alone does not modify that bool object |
| Target | Supplied constant integer3 used for exact comparison, not an automatically enforced capacity or hardware threshold |
