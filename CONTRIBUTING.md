# Contributing

## Pull request review gate

Every pull request must be preceded by a joint critical review with the owner. Do not create the pull request until the owner explicitly approves it.

The review must cover:

1. the requested outcome and final scope;
2. pedagogical progression, examples, prerequisites and repetition;
3. exact correspondence between requirements, UML, code and observed results;
4. architecture, simplicity, accessibility, responsive behavior and security;
5. automated checks and their known limits;
6. a questionnaire that classifies each material point as keep, improve, reject, defer or investigate further;
7. an explicit recommendation, using weighted MCDA when alternatives have meaningful trade-offs.

Apply approved improvements and rerun the relevant checks before requesting final authorization to create the pull request. A green build does not replace the pedagogical or conception review.

## Pull request content

Use a Conventional Commit-style title and describe the final result for a reviewer who has not seen the working conversation.

```md
## Summary

- Describe the concrete behavior or content added.
- Explain why it belongs in this pull request.

## Validation

- [ ] Pedagogical and conception review approved
- [ ] UML, code and results agree
- [ ] `npm run check` passes
- [ ] `npm test` passes
- [ ] Relevant C++ and browser checks pass
- [ ] Security checks pass

## Limits

- State deferred work and validation limits without claiming unmeasured learning outcomes.
```

Link the relevant issue with `Closes #<number>` when one exists. Apply the appropriate assignee, labels and project metadata after creation.
