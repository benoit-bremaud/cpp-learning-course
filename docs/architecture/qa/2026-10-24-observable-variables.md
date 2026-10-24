# QA pass - observable variable values (2026-10-24)

| Level | Head | Environment | Targets | Agent |
| --- | --- | --- | --- | --- |
| pass | Delivery commit containing this report; exact SHA and final Sonar task recorded in the prepared PR body | local production build | Web, C++17 excerpts | Codex, manual review and Playwright |

Allowed security hosts: 127.0.0.1 and localhost only. The production-bundle suite and inspector use loopback static servers rooted at dist. No production or third-party host was probed; no redirect following, credentials, destructive payload or burst traffic was used. No staging host was supplied. Hosting remains explicitly deferred in README.

## Results

| ID | Check | Verdict | Evidence | Issue |
| --- | --- | --- | --- | --- |
| FON-01 | Read CPP-01, predict two values, compare source/result/model, inspect companions and continue | PASS | One marked program; stdout bytes 0\n1\n, empty stderr, exit 0; all seven statements mapped | #16 |
| FON-02 | Main card and companion dialog, keyboard closure, native and unsupported-script fallbacks | PASS | Three-engine production suite; loaded card usable offline | #16 |
| DAT-01 | Static route and SVG contracts | PASS | Existing reader navigation/asset tests; seven snapshot provenance pairs, exact accepted primary SVG | |
| DAT-02 | Persistence contract | N/A | No authored-data writes; transient reader selection resets on reload as specified | |
| UI-01 | Responsive reading and tables | PASS | Chrome 320x640, 390x844, 768x1024, 1024x768, 1440x900, 844x390; three-engine 320/390/1440 and 200% text; no page/card/table horizontal overflow | #16 |
| UI-02 | Inspector console and network | PASS | All console levels captured, zero messages/errors/failed requests; only loopback assets; 27 responses in inspector journey | |
| UI-03/04 | Engines, theme and motion | PASS | Chrome, Firefox, WebKit; dark scheme; normal card 80ms delay/160ms fade; reduced-motion zero duration | |
| A11Y-01 | Keyboard, escape, focus return and dialog containment | PASS | Production suite and source-mapped browser suite | |
| A11Y-02 | Semantics and names | PASS | lang=fr, one h1 and main; accessible-tree inspection; copy buttons named through their title attribute; unique IDs and relationships | |
| A11Y-03 | Form error announcement | N/A | No added form submission, validation error or error state | |
| A11Y-04 | Contrast | PASS | 20 axe scans, zero violations; three incomplete results contain 16 diagnostics resolved by the unchanged opaque-color/top-layer-hit guard at >=4.5:1 | |
| A11Y-05/06 | Touched controls and visible focus | PASS | Close target 70.5x36.78px; keyboard opener/close remain visible and focus returns; responsive suite checks close viewport bounds | |
| A11Y-07/08 | Drag alternatives and accessible authentication | N/A | No drag or authentication | |
| PERF-01 | Throttled mobile local production build | PASS | Chrome trace with 4x CPU, 150ms latency, 200000 bytes/s download; measured LCP about 1.2s, CLS 0, recorded event durations below 200ms | |
| ROB-01 | Network loss on the touched reading path | PASS | After load, card/text remain usable offline and recover without a write or spinner | |
| ROB-02 | Backend failure | N/A | No backend or server-side operation | |
| SEC-01 | Deployment security headers | BLOCKED | Local preview/static server supplies no CSP, frame restriction, nosniff, Referrer-Policy or Permissions-Policy. Deployment configuration is outside this approved lesson. No pass or owner waiver is assumed. | Owner disposition required |
| SEC-02 | Cookies | N/A | Zero cookies and no sessions | |
| SEC-03 | Origin/CORS | N/A | No API or WebSocket endpoint; static Origin probe returned 200 with no allow-origin or allow-credentials header | |
| SEC-04 | Search XSS | PASS | Two standard image/SVG handler payloads treated as inert search input, no dialog execution or injected handler element | |
| SEC-05 | Authn/authz | N/A | No accounts, protected routes, private data or identifiers | |
| SEC-06 | Server input limits | N/A | No server input handler; separate robustness observation: empty and 4096-character local search did not crash | |
| SEC-07 | Rate limits | N/A | No login/send endpoint; Pagefind queries a local client index, no server search operation or stated throttling contract | |
| SEC-08 | Error leaks | PASS | Deliberate local 404 without stack or local filesystem path; no 500/payload handler to exercise | |
| SEC-09 | Production bundle | PASS | No source maps in dist; Gitleaks dist and delivery snapshot; manual diff review. No credentials or browser compiler added | |
| SEC-10 | Third parties | PASS | Inspector requests only loopback assets; no tracker, external request or mixed content | |
| SEC-11/12/13 | Privileged routes, session invalidation and server injection | N/A | Static public reader; no sessions, backend query, template input or user-controlled file endpoint | |

## Inspector evidence and limits

All-level console, request/response headers, failures, WebSocket connections, storage keys and performance entries were observed. No WebSocket was created, so frames are N/A. Storage contains only starlight-theme; sessionStorage, IndexedDB and cookies are empty. A naive text-only button-name check initially flagged the two copy icons; accessible-tree inspection confirms their title-based names, and axe reports no name violation.

The Chrome trace and detailed inspector JSON are retained locally in `/tmp/cpp-observable-implementation-qa/`. Performance values are repeatable lab observations, not field INP certification. Native browser page zoom and a human screen-reader session were not performed; 200% text enlargement is explicitly a reflow probe. These P1 checks are outside this pass, not claimed as a full accessibility audit. API, native mobile, firmware, authenticated privacy and data-migration domains are N/A. No user study or learning-outcome measurement is claimed.

SEC-01 is an unresolved validation boundary of the local preview, not an assertion that a production host is vulnerable: no production deployment exists. The current gate stays blocked until the owner explicitly records a limited local-preview waiver or a separately reviewed hosting-security study resolves it. No infrastructure change or public security issue was created. A real production security finding would require owner/private-advisory handling.

## Findings and delta

The first implementation scan found table overflow and inaccessible scrollable regions at 320px. Tracked within this change's issue #16. The owner approved scoped reflow option A, its weights and extra CSS file on 2026-10-24. Fixed by the dedicated observable-values table class; the final scans pass with no weakened checks. Interim UML wrappers and keyboard-only workaround were removed.

The [conception smoke](2026-10-24-observable-variables-conception.md) showed the old primary fragment. This report shows its approved complete-program replacement. No previous report defect was silently marked fixed. Broader deployment, dependency advisory #7, punctuation #8 and future prerequisite work #3 remain separate.

## Screenshots

- [Complete program and exact result](2026-10-24-observable-program.png).
- [Five actions and all seven mapped statements](2026-10-24-observable-table.png).
- [Tablet, intrinsic diagram on full-width white paper](2026-10-24-observable-tablet.png).
- [320px dark, reduced-motion card](2026-10-24-observable-dark-320.png).

Screenshots were visually inspected. Final publication remains separately authorized.
