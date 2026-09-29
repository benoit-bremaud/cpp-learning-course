# Course hosting and validation plan

Status: GitHub Pages explicitly rejected by the owner. CI validation/security workflows approved and prepared. Cloudflare hosting address and integration remain under discussion; no deployment or DNS mutation is authorized by this document.

## Existing personal site

Inspected `/home/vev/Documents/02_personal/portfolio/benoitbremaud.fr` (Git remote `benoit-bremaud/benoitbremaud.fr`). Its accepted ADR uses Cloudflare Pages Git integration and static HTML/CSS with no build command. The existing Projects section contains CAN Sniffer, BB Homelab and Kaggle Watcher. The adjacent `website` checkout is the separate StudioB22 commercial website and is not the personal portfolio. Untracked product documents were left untouched.

## Proposed integration

Prefer a separate Cloudflare Pages project for `cpp-learning-course`, linked from a new entry in the personal site's existing Projects section. Proposed host: `cpp.benoitbremaud.fr`; not accepted or provisioned yet. Alternative: `benoitbremaud.fr/cpp/`, requiring a combined publication pipeline or path routing. Both can keep separate repositories, but subdomain deployment minimizes release coupling.

For an accepted subdomain: change Astro site to the chosen canonical origin and base to `/`, update the diagram asset reference and tests, and configure the Pages output directory as `dist`. Build command should include `npm run check && npm test`; tests already build output. GitHub security checks do not automatically gate Cloudflare Git-integrated deployments: enforce PR checks before main merges or select an explicitly gated deployment mechanism. Do not claim that enabling CI alone guarantees this ordering.

Native Cloudflare branch previews can provide staging. Production comes from main. No QA data tier, backend or framework migration is required. DNS and custom-domain association are only configured after the hosting choice and implementation are validated. Existing apex and www routing must be preserved.

## Approved CI implementation

- validate.yml: PR/main install, type check and fresh production-output tests.
- dependency-review.yml: PR dependency vulnerability review, failure threshold low.
- codeql.yml: JavaScript/TypeScript analysis on PR/main and weekly.
- gitleaks.yml: secret scanning on PR/push/weekly, reports uploaded when produced.

Actions are pinned to verified upstream commit SHAs. Default permission is contents:read; security report upload jobs additionally use security-events:write. No pull_request_target, deployment token or hosting workflow. Node 22.21.1 matches the locally verified runtime.

## Remaining review

Validate the hosting address and portfolio entry content, implement the selected deployment design, then verify previews and live navigation/search/assets before reporting public availability. Current Astro GitHub-origin configuration is a legacy placeholder awaiting that decision, not an enabled GitHub Pages deployment.
