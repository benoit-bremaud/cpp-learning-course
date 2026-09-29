# GitHub Pages deployment proposal

Status: proposed; owner approval required before workflow or hosting mutations.

## Goal and target

Publish the independent French static course at `https://benoit-bremaud.github.io/cpp-learning-course/`. This is the expected URL, not a deployed endpoint. GitHub Actions is enabled; the Pages API currently returns 404. Verify authorization if enabling Pages fails rather than assuming the endpoint is accessible.

Astro already uses site `https://benoit-bremaud.github.io` and base `/cpp-learning-course`. No custom domain, backend, account, new paid service or practice-repository deployment is needed.

## Proposed files and behavior

- `.github/workflows/validate.yml`: pull requests and pushes to main run npm ci, npm run check and npm test. The test command builds output itself; do not build twice.
- `.github/workflows/pages.yml`: on main or a manual dispatch restricted to main, install locked dependencies, check, build/test, upload dist and deploy the validated artifact with official Pages actions. Grant pages:write and id-token:write only to the deployment job; other jobs have contents:read. Serialize production deployments and never deploy PR code with write permissions.
- `.github/workflows/gitleaks.yml`: secret scanning on pushes, PRs and weekly; findings fail validation; upload SARIF where available.
- `.github/workflows/codeql.yml`: analyze JavaScript/TypeScript using CodeQL with security-events permission limited to reporting jobs.
- `.github/workflows/dependency-review.yml`: review dependency changes on PRs and fail on actionable known vulnerabilities under the chosen policy.
- `README.md` and `docs/validation.md`: explain actual hosting, required checks, commands and measured verification results after deployment.

Resolve supported action versions and pin immutable commit SHAs during implementation. Use Node compatible with the pinned Astro engine (minimum 22.12), not an unverified default runner version. Do not add personal access tokens to workflow files.

## Environments

Use local preview for current review and a protected `prod` GitHub environment for Pages deployment, restricted to main. No QA environment is justified for a static reader with no data. Disposable hosted staging previews are deferred; initial review remains local plus downloadable build artifacts. This is an explicit limited initial scope, not a claim that hosted previews exist.

## Repository settings

Enable Pages with GitHub Actions as source. Restrict production environment deployment branches to main. Review the workflow PR before merging. Branch protection/required-check changes are a separate decision after initial checks exist; do not silently enable bypasses or overwrite existing rules.

## Acceptance

1. Workflow syntax validated; action SHAs and their provenance checked.
2. PR jobs validate code without publishing the site; build/test failure prevents deployment.
3. Main deployment succeeds through the official Pages artifact mechanism.
4. Public home, guided example, local SVG, styles and search work under the project base.
5. Mobile navigation works; published practice links retain the accepted revision.
6. No deployment is reported complete until the live URL and workflow result are verified.

## Review and scope

Content feeds a static build, the build feeds Pages, and practice remains independent. No application architectural change or new framework is required. Security checks are separate workflows and minimal permissions are job-scoped. Main deployment follows reviewed changes; the workflow must first pass its own PR review. No merge or branch deletion is authorized by this proposal alone.

Reference: https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages
