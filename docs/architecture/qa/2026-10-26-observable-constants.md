# QA pass - observable constant values

Date: 2026-10-26. Level: pass (fixed core and applicable P0 domains). Environment: local production build; branch codex/20-observable-constants-lesson from 42c6422. Exact delivery head and scanner evidence are recorded in the publication body after commit. Allowed security hosts: 127.0.0.1 and localhost only. Servers are loopback-only and rooted at dist. No production/third-party host, credential, destructive payload, redirect following or burst was used. No staging host was supplied.

## Results

| ID | Check | Verdict | Evidence / limit |
| --- | --- | --- | --- |
| FON-01 | Predict, copy, compare three complete CPP-09 sources | PASS | Stable stdout 3\n0\n3\n1\n, wrong stdout 30\n0\n30\n1\n; empty stderr, exit 0. Invalid source rejected, never executed; paired controls pass |
| FON-02 | Cards, keyboard, dismissal, native fallbacks and restart | PASS | Chrome/Firefox/WebKit; all three identities, rows 7/6/7 including header, Escape/focus return, reload |
| DAT-01 | Sources and SVG contracts | PASS | Eight public/source provenance pairs, actual lesson extraction, twelve/five mapped statements |
| DAT-02 | Persistent authored data | N/A | No data writes or backend; transient reader state resets |
| UI-01 | Responsive reading and tables | PASS | Three engines at 320/390/768/1440; Chrome additional 1024x768 and 844x390. No page/card/table horizontal overflow; 200% text reflow |
| UI-02 | Inspector console/network | PASS | Zero all-level console messages, page errors or failed requests; 25 successful same-loopback responses |
| UI-03/04 | Theme and motion | PASS | Normal 80ms delay and 160ms fade; dark/reduced motion zero-duration; existing animation regression retained |
| A11Y-01/02 | Keyboard, semantics, names and relationships | PASS | lang=fr, one main/h1, named controls, unique IDs, actual popover target identity and focus return |
| A11Y-03 | Form error announcement | N/A | No form submission or new validation state |
| A11Y-04 | Automated accessibility | PASS | 28 axe scans, zero violations; six incomplete results contain 22 contrast diagnostics resolved by unchanged opaque-color/top-layer-hit guard |
| A11Y-05/06 | Operable controls and focus | PASS | Existing keyboard/viewport assertions; close control remains in view at 200% text; visible focus and return |
| A11Y-07/08 | Drag/authentication alternatives | N/A | Neither interaction exists |
| PERF-01 | Throttled mobile lab trace | PASS | Chrome 4x CPU, 150ms latency, 200000 bytes/s download: LCP 1264ms, CLS 0, recorded event durations at most 48ms |
| ROB-01 | Network loss after load | PASS | Current card/text remain usable offline; restoration requires no authored-data write |
| ROB-02 | Backend outage | N/A | No backend |
| SEC-01 | Deployment headers | BLOCKED | Local static server has no CSP, frame restriction, nosniff, Referrer-Policy or Permissions-Policy; generic Python preview banner present. Owner disposition required for this local-preview boundary only |
| SEC-02 | Cookies | N/A | Zero cookies, no sessions |
| SEC-03 | Origin/CORS | N/A | No API/WebSocket endpoint. Static requests with foreign and null Origin return no allow-origin/allow-credentials headers |
| SEC-04 | Search XSS | PASS | Two image/SVG event-handler payloads stay inert, no dialog or injected handler element |
| SEC-05 | Authn/authz | N/A | Public static reader, no protected data/accounts/IDs |
| SEC-06 | Server input limits | N/A | No server input handler; empty and 4096-character local search do not crash |
| SEC-07 | Rate limits | N/A | Client Pagefind index, no login/send/server-search endpoint or throttling contract |
| SEC-08 | Error leaks | PASS | Deliberate local 404 has no stack or local path. No 500/payload endpoint exists |
| SEC-09 | Bundle | PASS | Gitleaks dist and delivery snapshot; no served source maps or credential-bearing diff |
| SEC-10 | Third parties | PASS | Only loopback requests, no tracker or mixed content |
| SEC-11/12/13 | Privileges, sessions, server injection | N/A | No privileged route, session, backend query or user-controlled template/path |
| SEC-18 | Dependency audit | BLOCKED / unchanged | npm audit cannot establish a trusted TLS chain. Verification was not weakened. No dependency changes; existing advisory #7 remains separate |
| PRI-01/02/03 | Personal data, consent, third parties | N/A / PASS | No personal data or tracker observed; only theme preference stored |
| Native/mobile/firmware domains | N/A | Static desktop/mobile web reader only |

## Inspector and evidence limits

WebSocket count is zero; frames are N/A. Storage keys: localStorage starlight-theme only; sessionStorage and IndexedDB empty; cookies zero. No payload contains personal data. Inspector JSON and Chrome trace remain at /tmp/cpp20-implementation-qa. The performance figures are lab samples, not field INP certification. Native browser zoom and a human screen-reader session were not performed; 200% text enlargement is explicitly a reflow probe. No user-study or learning-effectiveness claim.

SEC-01 describes the local preview, not a production vulnerability: the course is not deployed and hosting configuration is explicitly outside this approved brick. The earlier #16 waiver is not extended. A new owner decision is required before publication. No public security issue or unapproved advisory was created for this local-only validation boundary. Future hosting must validate headers and remove the preview banner separately. The audit TLS limitation is inherited infrastructure evidence, not a new dependency change or a clean advisory result.

## Findings and delta

The initial new identity assertion incorrectly expected a serialized popovertarget ID. The approved reader uses the DOM popoverTargetElement relationship; the test now verifies that exact identity and the keyed open card. No reader change was needed. Initial screenshot coordinates were corrected in the temporary capture tool; committed captures were visually inspected and include full claimed outputs. No new product defect remains in the reviewed functional/layout scope. SEC-01 remains blocked pending the specific owner disposition above.

The [conception smoke](2026-10-26-observable-constants-conception.md) shows the old three fragments. This report shows the approved complete-source replacement. Dependencies #7, punctuation #8 and future prerequisites #3 remain separate.

## Inspected screenshots

- [Complete stable-limit source and all four expected output lines](2026-10-26-observable-constants-stable-program.png).
- [Complete wrong-initializer source and all four actual output lines](2026-10-26-observable-constants-wrong-program.png).
- [Complete invalid source and actual GCC diagnostic](2026-10-26-observable-constants-rejected-source.png).
- [Tablet, full-width white paper and intrinsic six-action diagram](2026-10-26-observable-constants-tablet.png).
- [320px dark/reduced-motion card, scrollable top portion](2026-10-26-observable-constants-dark-320.png).

All five screenshots were visually inspected. The dark screenshot does not claim to show the entire tall card. Publication remains separately authorized.
