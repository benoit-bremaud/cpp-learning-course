# Course hosting and validation plan

Status: Local-only work at the owner’s latest request. Cloudflare provisioning, DNS changes, portfolio integration and publication are deferred. The domain below remains a future target, not an active deployment.

GitHub Pages explicitly rejected by the owner. CI validation/security workflows approved and prepared. The owner accepted an independent Cloudflare Pages site at cpp.benoitbremaud.fr, linked from the personal portfolio. Provisioning remains pending.

## Existing personal site

Inspected `/home/vev/Documents/02_personal/portfolio/benoitbremaud.fr` (Git remote `benoit-bremaud/benoitbremaud.fr`). Its accepted ADR uses Cloudflare Pages Git integration and static HTML/CSS with no build command. The existing Projects section contains CAN Sniffer, BB Homelab and Kaggle Watcher. The adjacent `website` checkout is the separate StudioB22 commercial website and is not the personal portfolio. Untracked product documents were left untouched.

## Proposed integration

Prefer a separate Cloudflare Pages project for `cpp-learning-course`, linked from a new entry in the personal site's existing Projects section. Accepted host: `cpp.benoitbremaud.fr`; not provisioned yet. Alternative: `benoitbremaud.fr/cpp/`, requiring a combined publication pipeline or path routing. Both can keep separate repositories, but subdomain deployment minimizes release coupling.

For the accepted subdomain, Astro uses the canonical origin and base `/`; configure the Pages output directory as `dist`. Build command should include `npm run check && npm test`; tests already build output. GitHub security checks do not automatically gate Cloudflare Git-integrated deployments: enforce PR checks before main merges or select an explicitly gated deployment mechanism. Do not claim that enabling CI alone guarantees this ordering.

Native Cloudflare branch previews can provide staging. Production comes from main. No QA data tier, backend or framework migration is required. DNS and custom-domain association are only configured after the hosting choice and implementation are validated. Existing apex and www routing must be preserved.

## Approved CI implementation

- validate.yml: PR/main install, type check and fresh production-output tests.
- dependency-review.yml: PR dependency vulnerability review, failure threshold low.
- codeql.yml: JavaScript/TypeScript analysis on PR/main and weekly.
- gitleaks.yml: secret scanning on PR/push/weekly, reports uploaded when produced.

Actions are pinned to verified upstream commit SHAs. Default permission is contents:read; security report upload jobs additionally use security-events:write. No pull_request_target, deployment token or hosting workflow. Node 22.21.1 matches the locally verified runtime.

## Remaining review

Validate the hosting address and portfolio entry content, implement the selected deployment design, then verify previews and live navigation/search/assets before reporting public availability. Astro now uses the accepted canonical origin with root-relative assets; reader tests verify navigation, assets, canonical URL and the portfolio backlink.

## Post-merge cleanup

After confirming a PR is merged, synchronize local main using a fast-forward update, verify the merged result, remove its completed local and remote feature branches, and prune stale remote references. Preserve active branches, uncommitted files and unrelated worktrees. Squash merges require verifying the PR head and merged content before deleting the source branch.
