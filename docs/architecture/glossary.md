# Architecture glossary

Status: owner-approved conception entries for #20's observable-constants conception. This small index defines the terms used by its new activities; it does not claim to replace or retrospectively audit the definitions in earlier lesson specifications.

| Term | Meaning and source |
| --- | --- |
| Assignment | Replace the value of an already existing ordinary integer; [CPP-01](../../src/content/docs/notions/cpp-01.mdx) |
| Compile rejection | The complete source is ill-formed; no successful execution or output is claimed; [const contract CL-02](specs/constant-limit.md) |
| Constant integer | A local int object whose value cannot be modified after initialization through direct assignment; [CL-01](specs/constant-limit.md) |
| Count | Supplied known total represented by measurement_count, not physical acquisition or an arithmetic update; [proposed contract](specs/observable-constants-lesson.md) |
| Initialization | Establish an object's initial value when it is created; [CPP-01](../../src/content/docs/notions/cpp-01.mdx) |
| Invariant | The limit remains unchanged during the modeled count update; the initial value may still be wrong for the requirement; [CL-03](specs/constant-limit.md) |
| Limit | Required fictional stable value 3, not automatically enforced capacity or allocated storage; [CL-01](specs/constant-limit.md) |
| Observation pair | Write the limit then the count, each followed by a newline: four statements grouped into one activity action; [proposed mapping](specs/observable-constants-lesson.md) |
| Successful return | Return status 0 without an additional output write; [first-program conception](specs/program-skeleton.md) |
