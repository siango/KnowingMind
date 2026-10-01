# KnowingMind Open Commons Architecture V1

## Logical layers

### 1. Public experience layer

- web UI,
- multilingual content,
- public documentation,
- contributor portal,
- public sustainability dashboard.

### 2. Application/API layer

FastAPI endpoints provide bounded services for:

- membership,
- support checkout creation,
- payment webhook ingestion,
- contribution events,
- public project summaries,
- knowledge-domain queries.

### 3. Domain authority layer

DHAMMA_GROUNDED_AI:
- PostgreSQL + pgvector is project SSOT,
- Canon authority remains VERIFIED_TIPITAKA,
- Dedicated Dhamma MCP remains controlled readback/access layer.

Future domains must declare their own source/provenance rules.

### 4. Community layer

Separate domains:
- identity,
- community contribution events,
- recognition/points,
- moderation,
- governance audit.

### 5. Funding layer

Stripe handles payment collection.

FastAPI receives verified Stripe webhook events.

PostgreSQL stores normalized payment/funding records and public aggregates, never Stripe secret keys.

### 6. Source and delivery layer

GitHub:
- source,
- PR review,
- CI,
- public contribution workflow.

FastAPI Cloud:
- runtime application hosting,
- runtime secrets,
- deployment target.

### 7. Security boundary

Public source must not contain:
- provider credentials,
- private endpoint secrets,
- user/practice private data,
- raw restricted evidence,
- payment secrets.

## Primary flows

### Code

Contributor → GitHub PR → CI → review → merge → deployment → runtime verification → contribution event

### Funding

Supporter → Stripe Checkout → Stripe event → FastAPI webhook → signature verification → idempotency → funding ledger → optional contribution recognition

### Knowledge

User question → domain router → bounded source retrieval → provenance/evidence → interpretation → AI response

## Authority rules

- GitHub is source, not runtime truth.
- FastAPI Cloud is runtime, not Canon/project authority.
- Stripe is payment-event authority for Stripe payment state, not community or religious authority.
- Community points are recognition metadata, not religious truth.
- D1/Kebunate remains execution-support only where explicitly delegated; it is not DHAMMA project truth.
