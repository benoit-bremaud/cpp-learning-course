# Conception traceability matrix

Status: owner-approved conception IDs for [#20](https://github.com/benoit-bremaud/cpp-learning-course/issues/20). Existing specifications keep their legacy scoped IDs; this is not a retrospective coverage claim. All requirements below are defined in [observable-constants-lesson](specs/observable-constants-lesson.md). Tests are proposed future verification, not implemented results.

| Source / requirement | Realization | Proposed verification |
| --- | --- | --- |
| #20 -> REQ-1 | REQ-1 -> [ACT-stable-limit](diagrams/observable-constants/07-activity-stable-limit.md) | tests/constant-limit.py fixed values and narrative review |
| #20 -> REQ-2 | Three labelled source/card contracts in specification | tests/constant-limit.test.mjs fixed inventory and HTML mappings |
| #20 -> REQ-3 | REQ-3 -> ACT-stable-limit and [ACT-wrong-limit](diagrams/observable-constants/07-activity-wrong-limit.md) | tests/constant-limit.py actual extraction, C++17, exact output/stderr/status |
| #20 -> REQ-4 | Compile-only contract; no runtime activity for the invalid translation unit | tests/constant-limit.py rejection plus mutable and removed-assignment controls |
| #20 -> REQ-5 | REQ-5 -> ACT-stable-limit and ACT-wrong-limit observation pairs | Source intent assertions and fake-literal-output mutation tests |
| #20 -> REQ-6 | REQ-6 -> both six-action activities; qualified five-statement invalid mapping | tests/constant-limit.test.mjs twelve/five statement mapping checks |
| #20 -> REQ-7 | Existing static reader/card/progression architecture, no new component | tests/reader.test.mjs and production browser regression |
| #20 -> REQ-8 | Fixed valid/invalid/wrong contracts and meaningful mutation inventory | tests/constant-limit.test.mjs and compiler controls |
| #20 -> NFR-1 | NFR-1 -> both authoritative activity triplets | Snapshot provenance and production browser bounds |
| #20 -> NFR-2 | Existing validation/security/coverage pipeline | Full local tests, public-doc audit, exact-head Sonar and Gitleaks |
| #20 -> NFR-3 | Existing browser-owned card behavior and current QA policy | Three engines, accessibility, inspector/security report and inspected screenshots |
| #20 -> NFR-4 | Separate reviewed conception and owner approval gates | Recorded approvals, distinct conception/implementation PRs, preserved deferrals |
