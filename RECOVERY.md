# Public Recovery Baseline

This fork-only branch provides a non-sensitive, reviewable CI baseline for
Dataline.

## Reproducible checks

- Python 3.11 and uv 0.8.14
- frozen backend dependency installation
- existing backend tests, excluding the explicitly gated expensive evaluation
- backend source compilation
- Node.js 20.19.5 and frozen npm installation
- TypeScript and Vite production build
- read-only GitHub Actions permissions and full commit SHA action pins

## Production boundary

Recovery CI does not read OpenAI or repository secrets, log in to Docker Hub,
build or publish release images, create platform bundles, deploy the
application, run database migrations, or access user data and hosted services.
The existing release, evaluation, and Docker workflows are outside this
branch's automated pull-request path.

This zero-Star fork does not inherit upstream Stars, users, releases, or
authorship. It is recovery evidence only and does not imply maintainer status.
