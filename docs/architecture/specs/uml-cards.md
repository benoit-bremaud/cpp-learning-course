# Compact UML cards

Status: option A approved by the owner. Supersedes the expanded inline interaction; teaching content and primary diagrams are unchanged.

Use case: activate a small UML (or UML · écart) control below code, read its diagram/mapping, dismiss by outside click, Escape or Close. Only one native auto popover is shown. Inside the example dialog, dismissing the card preserves the dialog. Keep SVG links. Native details remain the fallback without JavaScript or popover support.

Implementation: CourseFooter loads the common progressive enhancement on every lesson. Authored details own teaching content; uml-cards.ts moves it once into a native popover inside the same subtree. CSS owns presentation; bounded runtime coordinates keep the card near its invoker within the viewport. No clone of teaching content, new dependency or modal layer.

Four-pass review: requirements match approved behavior; content, enhancement and styles have separate responsibilities; use native light-dismiss and single-popover behavior rather than custom overlay management; no pattern or additional UML diagram justified for this simple browser-owned interaction. Tests must cover both loaders, nested dialog Escape/outside click, focus return, mobile bounds, mutual exclusion and no-script fallback.

## Owner-requested opening refinement

The owner requested a smoother appearance with slight latency, to assess visually after implementation. Hide the card until its viewport coordinates are assigned; then use an 80ms delay and 160ms opacity-only fade. Never animate position. Reduced-motion preference disables both delay and animation. This initial trial kept closing immediate; the accepted refinement below supersedes that closing behavior.

The owner subsequently requested a symmetric transparency fade on dismissal. Replace the entry-only animation with opacity transitions: retain the 80ms opening delay and 160ms fade, and use a 160ms exit without delay. Native discrete display/overlay transitions retain the closing card long enough to paint the exit; no timer delays dismissal or focus restoration. Reduced-motion disables transitions. Browsers lacking discrete transitions may dismiss immediately.

The owner validated the resulting opening and closing fades. These are the current shared site behavior, including the first-if and first-else cards; the earlier opening-only trial is retained above only to explain the superseded decision.
