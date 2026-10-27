# Conception traceability matrix

Each feature section names its authoritative specification. Existing specifications retain their legacy scoped IDs; this matrix does not claim a retrospective audit. Verification columns record conception contracts rather than a current execution report.

## Observable-constants conception - #20

Status: owner-approved conception IDs for [#20](https://github.com/benoit-bremaud/cpp-learning-course/issues/20). Existing specifications keep their legacy scoped IDs; this is not a retrospective coverage claim. Requirements in this #20 section are defined in [observable-constants-lesson](specs/observable-constants-lesson.md). Tests are proposed future verification, not implemented results.

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

## Approved arithmetic-update conception - #23

Conception A and its file plan explicitly approved on 2026-10-26. Requirements below are defined in [arithmetic-update-lesson](specs/arithmetic-update-lesson.md). Tests/implementation remain proposed; no earlier IDs are reused.

| Source / requirement | Realization | Proposed verification |
| --- | --- | --- |
| #23 -> REQ-9 | Narrow integer update contract | Source intent and French-content review |
| #23 -> REQ-10 | Two complete source/card contracts | tests/arithmetic-update.test.mjs fixed inventory |
| #23 -> REQ-11 | [ACT-arithmetic-update](diagrams/arithmetic-update/07-activity-arithmetic-update.md) and [ACT-literal-replacement](diagrams/arithmetic-update/07-activity-literal-replacement.md) | tests/program-output.py arithmetic-update mode, actual C++17 extraction |
| #23 -> REQ-12 | REQ-12 -> ACT-arithmetic-update old-value read | Source-intent and fixed-result/fake-output mutations |
| #23 -> REQ-13 | REQ-13 -> both five-action/seven-statement activities | Exact ordered mapping/card assertions |
| #23 -> REQ-14 | Distinct actual literal behavior, required arithmetic result | Output contracts and manual explanation review |
| #23 -> REQ-15 | Existing static reading progression plus new route | tests/arithmetic-update.test.mjs, reader and production navigation |
| #23 -> REQ-16 | Fixed lesson and preserved prior inventories | Meaningful safe mutation suite |
| #23 -> NFR-5 | NFR-5 -> both authoritative triplets | Deterministic render, snapshots, intrinsic geometry and mappings |
| #23 -> NFR-6 | Existing validation/coverage pipeline | Full local checks, doc audit, exact-head Sonar and Gitleaks |
| #23 -> NFR-7 | Existing reader/card architecture | Proportionate production QA with inspector/security applicability |
| #23 -> NFR-8 | Separate reviewed conception and owner approvals | Approval records and distinct conception/implementation PRs |

## Approved equality-results conception - #26

The owner approved concrete conception A and weights35/30/20/15 on2026-10-27. Requirements below are defined only in the accepted [equality-results specification](specs/equality-results-lesson.md). Realizations are accepted formal models; all lesson/test implementation and verification remains proposed. No prior scoped or normalized ID is reused.

| Source / requirement | Proposed realization | Proposed verification |
| --- | --- | --- |
| #26 -> REQ-17 | Same-int equality/inequality and bool contract | Scope/prerequisite review, no CPP-04 completion claim |
| #26 -> REQ-18 | Two fixed source/card contracts | tests/equality-results.test.mjs inventory and exact outputs |
| #26 -> REQ-19 | [ACT-equality-pair](diagrams/equality-results/07-activity-equality-pair.md) and [ACT-equality-snapshot](diagrams/equality-results/07-activity-equality-snapshot.md) | Actual C++17 extraction plus independent safe2/3/4 truth probes |
| #26 -> REQ-20 | REQ-20 -> both comparison-evaluation activities | Exact source intent, wrong-operator/fixed-result/fake-output mutations |
| #26 -> REQ-21 | REQ-21 -> five-action/nine-statement pair and eight-action/twelve-statement snapshot | Exact ordered mappings, no invented decision diamond |
| #26 -> REQ-22 | REQ-22 -> ACT-equality-snapshot evaluation moments | Stored/reevaluated output trace and semantic review |
| #26 -> REQ-23 | Existing reading progression plus one new page | Seven-introduction links/counts, honest practice/catalog scope |
| #26 -> REQ-24 | Fixed baseline and safe mutations | New test file, prior68 probes retained |
| #26 -> NFR-9 | NFR-9 -> both authoritative triplets | Deterministic render/public snapshot and intrinsic paper geometry |
| #26 -> NFR-10 | Existing validation/coverage pipeline | Full local gates, documentation audit, exact-head Sonar and Gitleaks |
| #26 -> NFR-11 | Existing static reader/card architecture | Three engines, accessibility, inspector/security and inspected screenshots |
| #26 -> NFR-12 | Separate conception/implementation and owner gates | Explicit approvals/publication boundaries, no Copilot |
