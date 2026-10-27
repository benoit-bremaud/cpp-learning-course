# QA pass - arithmetic update

Date: 2026-10-27. Level: pass, local production build, branch codex/23-arithmetic-update-lesson from main37d4b8c (conception PR24 merged). Exact delivery revision and Sonar task are recorded in the publication body after commit. The owner deferred the separate comprehensive QA campaign. This report covers routine delivery gates only. Allowed security hosts: 127.0.0.1 and localhost, loopback-only static servers rooted at dist. No production or third-party probe, credentials, destructive payload, burst or redirect following. No staging host supplied.

## Results

| ID | Check | Verdict | Evidence / limit |
| --- | --- | --- | --- |
| FON-01 | Predict, copy and compare both complete programs | PASS | Actual extracted C++17 stdout 2\n3\n and 2\n1\n, empty stderr, exit0; source intent rejects fake fixed3 despite matching baseline output |
| FON-02 | Cards, keyboard, dismissal, reload, native fallback | PASS | Chrome/Firefox/WebKit, both identities, six rows including header, Escape/focus return, no-JavaScript and no-popover fallbacks |
| DAT-01 | Source/model/public provenance | PASS | Ten existing-plus-new provenance pairs; two new renders deterministic; all seven statements mapped in five actions each |
| DAT-02 | Persistent authored data | N/A | No backend or authored-data writes |
| UI-01 | Responsive geometry and reflow | PASS | Three engines at320/390/768/1440; additional Chrome1024x768 and844x390; both cards at200% text; no page/card/table horizontal overflow |
| UI-02 | Inspector | PASS | Zero all-level console messages, page errors and failed requests;25 successful loopback responses |
| UI-03/04 | Theme and motion | PASS | Dark theme,80ms delay/160ms fades; zero duration under reduced motion, unchanged animation regression |
| A11Y-01/02 | Keyboard, semantics, identity | PASS | French document, one main/h1, unique IDs, DOM popover target relationship, keyboard dismissal/focus return |
| A11Y-03 | Submission error announcement | N/A | No submission flow |
| A11Y-04 | Automated accessibility | PASS | 34 axe scans, zero violations;8 incomplete results contain26 contrast diagnostics handled by the unchanged opaque-color/top-layer-hit guard |
| A11Y-05/06 | Controls and focus | PASS | Close control in viewport at200% text, keyboard reachability and return |
| A11Y-07/08 | Drag and authentication alternatives | N/A | Neither interaction exists |
| PERF-01 | Throttled mobile sample | PASS | Chrome4xCPU,150ms latency,200000bytes/s download: LCP1160ms, CLS0, maximum observed event duration32ms |
| ROB-01 | Offline after load | PASS | Loaded reading and primary card stay usable offline; network restoration requires no data write |
| ROB-02 | Backend outage | N/A | No backend |
| SEC-01 | Deployment headers/banner | BLOCKED | Local Python static server lacks CSP, frame restriction, nosniff, Referrer-Policy and Permissions-Policy, and exposes its generic preview banner; new owner disposition required |
| SEC-02 | Cookies | N/A | Zero cookies, no sessions |
| SEC-03 | Origin/CORS | N/A | No API/WebSocket; static requests with foreign/null Origin expose no allow-origin/allow-credentials headers |
| SEC-04 | Search XSS | PASS | Two image/SVG event-handler payloads inert; no dialog or injected handler element |
| SEC-05 | Authn/authz | N/A | Public static reader, no accounts or protected data |
| SEC-06 | Server input limits | N/A | No server input handler; empty and4096-character local search do not crash |
| SEC-07 | Rate limits | N/A | Client Pagefind index, no server-search/login/send endpoint |
| SEC-08 | Error leaks | PASS | Deliberate local404 has no stack trace or local filesystem path |
| SEC-09 | Bundle/sensitive data | PASS | Full reachable history, exact delivery snapshot, dist and retained QA evidence scanned; no tracked env file or served source map |
| SEC-10 | Third parties | PASS | Only loopback responses; no tracker or mixed content |
| SEC-11/12/13 | Privileges, sessions, server injection | N/A | No privileged route, session, backend query or user-controlled server template/path |
| SEC-18 | Dependency audit | BLOCKED / unchanged | Fresh npm audit fails trusted TLS chain; verification not weakened, no dependency changes; advisory7 remains deferred |
| PRI-01/02/03 | Privacy and consent | N/A / PASS | No personal-data flow or third party; only starlight-theme localStorage key |
| Native/mobile/firmware | N/A | Web reader only |

## Inspector and limits

No WebSocket was observed, so frames are N/A. Session storage and IndexedDB empty; cookies zero. Local inspector JSON and real Chrome performance trace are in /tmp/cpp23-implementation-qa. Performance numbers are one lab sample, not field INP certification. Native browser zoom and a human screen-reader session were not performed;200% text is a reflow probe. No learner-effectiveness claim.

SEC-01 describes a local preview boundary, not a production vulnerability. Hosting is outside this approved lesson scope. No earlier waiver, including20, is inherited. A new limited owner decision is required before publication; future hosting must separately validate headers and remove preview banners. No public security issue/advisory was created for this local-only validation boundary. The audit TLS failure is disclosed infrastructure evidence, not a clean advisory result.

## Findings and evidence

An initial mutation fixture changed an asset URL instead of the marker; the fixture now targets the full marker comment. An existing ordered-output test hardcoded the global five-page inventory; its single assertion now expects six. Neither correction changes earlier program contracts. The temporary inspector originally enumerated a disappearing card table and captured stale scroll coordinates; waiting for the fade and resetting scroll corrected evidence capture. No shared reader change was needed. No remaining functional/layout defect or new Nice finding was found in this reviewed scope; SEC-01 remains blocked pending owner disposition.

All four screenshots were visually inspected:

- [Complete arithmetic source and both expected output lines](2026-10-27-arithmetic-update-arithmetic-program.png).
- [Complete literal-replacement source and both actual output lines](2026-10-27-arithmetic-update-replacement-program.png).
- [Tablet, full-width white paper and natural-size centered model](2026-10-27-arithmetic-update-tablet.png).
- [320px dark/reduced-motion card, scrollable top only](2026-10-27-arithmetic-update-dark-320.png).

The narrow screenshot does not claim to show the full tall card or its complete mapping table. Automated assertions verify all mapping rows. Comprehensive QA, dependencies7, punctuation8 and later prerequisites3 stay separate.
