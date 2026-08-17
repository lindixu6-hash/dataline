# Recovery Backlog Triage

Snapshot: 2026-08-18

This is a first-pass classification of the 30 open pull requests and 12 open
issues returned by the GitHub API. It is review guidance, not a merge or close
decision. Every item still requires conflict, test, security, and product-scope
verification against the current `main` branch.

## Pull Requests

### Human or product changes

| PR | Topic | Initial disposition |
|---|---|---|
| #407 | Dispose SQLAlchemy engines to prevent pool exhaustion | Highest-priority user reliability review; reproduce and test before merge |
| #393 | Hide SQL blocks by default from user preference | Close and replace: main already has the preference, while this PR regresses defined SQL dialects and misses async preference state |
| #187 | Frontend model selection | Close old PR, retain requirement: backend capability now exists, while the conflicting UI must wait for evaluation-backed provider/model design |

### Current dependency updates

| PRs | Area | Initial disposition |
|---|---|---|
| #414, #411, #410, #409, #408, #405 | Frontend runtime and transitive security updates | Rebase in small compatible groups; run frozen install and production build |
| #413, #412 | Backend security-sensitive dependencies | Review application compatibility and regenerate `uv.lock` independently |
| #402, #401 | Frontend build tooling | Rebase separately from runtime updates; verify Storybook/Vite compatibility |

### Older dependency updates needing supersedence checks

| PRs | Initial disposition |
|---|---|
| #394, #391, #389, #387, #371, #369, #366 | Compare with current lockfiles and newer open updates; close only when a specific replacement is identified |
| #363, #360, #358, #356, #355, #354, #348, #336, #317, #315 | Likely stale or superseded; verify advisory coverage and current resolved versions before replacing or closing |

## Issues

### User-facing bugs

| Issue | Initial disposition |
|---|---|
| #304 | Reproduce unsupported chart-type `KeyError`; candidate bounded patch |
| #279 | Reproduce graph recursion-limit failure and define a safe configurable bound |
| #263 | Reproduce stale query results after edited SQL; good first functional fix |
| #255 | Reproduce single-item layout and scrollbar defects on current frontend |
| #221 | Define error feedback contract for failed queries without exposing sensitive SQL/data |

### Product and model compatibility

| Issue | Initial disposition |
|---|---|
| #384 | Reconcile with PR #393 and the existing hide-SQL migration/settings implementation |
| #267 | Split provider/local-model support into a current compatibility matrix; retain blocked status until scope is agreed |
| #266 | Specify SQLite configuration behavior and migration compatibility |

### Evaluation and longer-term roadmap

| Issue | Initial disposition |
|---|---|
| #364 | Treat saved-query examples as a privacy-sensitive product feature requiring explicit data boundaries |
| #283 | Keep as roadmap milestone; decompose only after maintenance scope is confirmed |
| #282 | Define measurable anti-hallucination acceptance criteria before implementation |
| #272 | Keep expensive LLM evaluation separate from the no-secret pull-request gate |

## First Review Order

1. Validate the no-secret backend and frontend recovery checks.
2. Reproduce PR #407 and issues #304, #263, and #221.
3. Determine whether PR #393 is superseded by the current hide-SQL code.
4. Rebase only the newest dependency updates; map older PRs to explicit
   replacements before closing them.
5. Defer release credentials, hosted services, expensive LLM evaluation, and
   broad roadmap work until the owner approves scope.
