# Architecture overview

The course is a statically built reader. French teaching content flows into Astro and Starlight at build time; the generated site does not require a database or teaching-content API. Practical exercises remain in independent repositories and run in the learner's local IDE.

## Contextual examples

The first shared interaction under conception is the contextual example explorer:

- [Editorial charter](../example-charter.md): site-wide teaching and review requirements.
- [Explorer specification](specs/example-explorer.md): pilot use case, accessibility contract, content schema and verification.
- [Inline UML specification](specs/inline-uml-panels.md): source-level association between every C++ block and its reviewed model.
- [Compact UML card specification](specs/uml-cards.md): progressive enhancement and motion behavior.
- [Explorer diagrams](diagrams/example-explorer/01-use-case.md): UML views and the four pilot teaching activities.
- [Measurement-count activity](diagrams/measurement-count/01-activity-update.md): initialization followed by assignment for CPP-01.
- [Constant-limit activity](diagrams/constant-limit/01-activity-values.md): stable limit and independently mutable count for CPP-09.

The static build depends on authored content. Browser enhancements depend on generated HTML. Teaching content and the independent practice repositories do not depend on browser scripts. This direction keeps every lesson readable when JavaScript is unavailable.

## Proportional UML views

The explorer uses a use-case view for the reader's goal, a state view for dialog navigation and a component view for build-time dependencies. Four activity views describe the pilot algorithms. A class diagram is not justified because the feature introduces no domain object model; a sequence diagram would duplicate the state transitions without clarifying a cross-component protocol.

Implementation evidence belongs to the implementation pull request. These documents define accepted intent and do not claim that the components are already shipped.

## Local implementation review

The example reader and compact-card pilot has local implementation and verification evidence in [the pilot review](../reviews/example-reader-pilot/README.md). Owner acceptance, publication and the final PR-head merge gate remain separate steps; this link does not mark the conception or course as deployed.
