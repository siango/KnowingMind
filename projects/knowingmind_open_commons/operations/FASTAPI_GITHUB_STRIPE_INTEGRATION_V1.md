# FastAPI Cloud + GitHub + Stripe Integration V1

## Existing infrastructure rule

Reuse existing KnowingMindApp GitHub/FastAPI deployment workflow where possible.

Known existing workflow:
- .github/workflows/dhamma-fastapi-cloud-deploy-verify-v1.yml

Do not create a duplicate deployment system merely for Open Commons.

## GitHub

Role:
- source and review,
- CI,
- controlled deployment trigger,
- contribution evidence.

Required separation:
- no Stripe/FastAPI production secret in source,
- deployment secrets stored as GitHub Actions secrets only when required.

## FastAPI Cloud

Role:
- public/runtime API host,
- membership/community API host as bounded modules,
- Stripe Checkout-session creation,
- Stripe webhook endpoint,
- public sustainability endpoints.

Known deployment variables:
- FASTAPI_CLOUD_TOKEN
- FASTAPI_CLOUD_APP_ID

Existing Dhamma runtime secrets/boundaries remain controlled separately.

## Stripe

Initial bounded API:

POST /v1/support/checkout
- create Checkout Session,
- use current Stripe SDK/API,
- add integration identifier,
- do not hardcode payment_method_types.

POST /v1/stripe/webhook
- verify signature,
- reject invalid signature,
- persist/idempotently process event,
- update funding ledger,
- create contribution event only when eligible.

GET /v1/support/status/{support_id}
- return application-level support status without exposing sensitive payment data.

GET /v1/public/sustainability
- return aggregate project-support/cost data only.

## Required runtime configuration

FastAPI Cloud secret/config:
- STRIPE_RESTRICTED_KEY
- STRIPE_WEBHOOK_SECRET
- STRIPE_MODE
- STRIPE_SUPPORT_PRODUCT_ID
- KNOWINGMIND_PUBLIC_ORIGIN

GitHub deployment:
- FASTAPI_CLOUD_TOKEN
- FASTAPI_CLOUD_APP_ID

No secret value belongs in this document or repository.

## Environments

DEV:
- local or isolated development,
- Stripe sandbox.

CI:
- isolated test configuration,
- synthetic users/events.

STAGING/PUBLIC-ALPHA:
- non-production or bounded deployment until release gates pass.

LIVE:
- explicit human approval,
- separate Stripe live credential,
- monitoring and rollback enabled.

## Verification sequence

1. GitHub source readback,
2. CI green,
3. FastAPI deploy,
4. /health,
5. Stripe sandbox Checkout canary,
6. webhook signature test,
7. duplicate webhook replay test,
8. PostgreSQL exact funding readback,
9. public sustainability aggregate readback,
10. Dhamma MCP readback for authority-boundary confirmation,
11. independent verification.

## Failure rules

One first failure point at a time.
Do not bypass a failed provider credential gate by hardcoding credentials.
Do not create another deployment/payment stack to avoid repairing the existing path.
