# Public Release Gates V1

Repository visibility and live public-alpha launch require all mandatory gates to pass.

## G0 — Authority Reconciliation

PASS when:
- public docs reflect current authority,
- PostgreSQL/Dhamma MCP remains clear for DHAMMA truth,
- stale source snapshots are labelled non-authoritative.

## G1 — Public Classification

PASS when:
- every candidate file is PUBLIC,
- no UNKNOWN item enters release,
- RESTRICTED/PROHIBITED items are excluded.

## G2 — Secret and History Audit

PASS when:
- tree scan passes,
- history assessment passes,
- any previously exposed credential is rotated,
- no production credential is in public history.

## G3 — Rights and Licensing

PASS when:
- project-owned code license approved,
- documentation license approved,
- third-party rights inventory complete,
- non-redistributable source material excluded.

## G4 — Clean Public Build

PASS when:
- clean clone,
- dependency install,
- tests,
- build,
- minimal local run
succeed without private source files.

## G5 — Security & Privacy

PASS when:
- security reporting path exists,
- private identity/payment/practice data excluded,
- privileged role controls tested,
- no environment-dump/debug secret exposure.

## G6 — Multilingual Baseline

PASS when critical public UI is available in:
- Thai,
- English,
- Simplified Chinese.

Translation status/provenance must be visible where relevant.

## G7 — Membership

PASS when:
- sign-in/account lifecycle works,
- public/private profile separation works,
- role grants are auditable.

## G8 — Funding Sandbox

PASS when:
- Stripe sandbox Checkout succeeds,
- webhook signature verification passes,
- duplicate webhook does not duplicate ledger effects,
- failed/async payment paths behave correctly,
- ledger reconciliation passes.

## G9 — Contribution Recognition

PASS when:
- merged/test contribution produces one auditable contribution event,
- accepted translation/review path works,
- points reversal is possible,
- donation does not grant governance authority.

## G10 — FastAPI/GitHub Deployment

PASS when:
- existing FastAPI Cloud deploy path is used/reconciled,
- deployment credential gate passes,
- health endpoint passes,
- authoritative readback boundary is preserved.

## G11 — Public Sustainability

PASS when:
- aggregated expense/support view works,
- sensitive donor/payment details remain private.

## G12 — Independent Verification

PASS when an independent readback verifies:
- source release commit,
- deployment/runtime state,
- security/public-boundary assertions,
- authority separation.

## Go-live

Only after G0–G12 mandatory gates pass:
PUBLIC_ALPHA_READY

Visibility change and Stripe live enablement remain explicit human-gated actions.
