# Stripe and Sustainability V1

## Purpose

Fund recurring project costs transparently while keeping payment authority separate from knowledge, Canon, and community governance authority.

## Current account boundary

A Stripe account must be explicitly approved for KnowingMind before live integration. Do not silently reuse an account belonging to another project or brand.

## Environments

Use:
- Stripe sandbox for development,
- isolated CI/test configuration,
- Stripe live only after human go-live approval.

Separate keys and webhook endpoints per environment.

## Recommended payment surface

Initial support flow:
- Stripe Checkout Sessions,
- Stripe-hosted checkout,
- dynamic payment methods,
- verified webhooks,
- no fulfillment from success page.

Do not use legacy Charges or Sources APIs.

## Required webhook handling

At minimum:
- checkout.session.completed
- checkout.session.async_payment_succeeded
- checkout.session.async_payment_failed
- refund.created, refund.updated, and refund.failed
- charge.dispute.created, charge.dispute.updated, and charge.dispute.closed

Rules:
- verify Stripe signature before processing,
- enforce idempotency,
- record provider event ID,
- fulfill/credit only when payment state is eligible,
- never trust browser success redirect as payment authority,
- deduplicate webhook delivery by provider event ID, then deduplicate every financial side effect by provider object ID and normalized state-transition key,
- persist one unique adjustment for each refund/dispute transition that affects recognized support; event-delivery deduplication alone is not sufficient,
- cap cumulative refund and dispute-loss reversals for a payment at the original credited amount, so overlapping refund/dispute events cannot reverse support or contribution points twice,
- create a financial reversal only when a refund succeeds; pending, failed, or canceled refunds do not reverse recognized support,
- place recognition on hold while a dispute is open; release the hold if won, and record an auditable reversal if lost,
- apply partial refunds only to the refunded amount and calculate any contribution-points reversal deterministically under the recorded policy version.

## Secret policy

Preferred server credential:
- restricted API key with minimum permissions.

Runtime secrets:
- STRIPE_RESTRICTED_KEY
- STRIPE_WEBHOOK_SECRET

Configuration:
- STRIPE_MODE
- STRIPE_SUPPORT_PRODUCT_ID or equivalent catalog reference

Secrets belong in FastAPI Cloud/provider-native secret storage, never Git.

## Data separation

Private payment data:
- Stripe customer/payment identifiers as needed,
- reconciliation references,
- payment event payload subset required for audit.

Public sustainability data:
- aggregated support received,
- aggregated cost categories,
- monthly net support,
- runway estimate.

Do not expose donor identity without explicit consent.

## Expense categories

Suggested:
- AI_API
- DATABASE
- STORAGE
- CDN_EDGE
- MONITORING
- MEDIA_GENERATION
- DOMAIN
- SECURITY
- DEVELOPMENT_INFRA
- OTHER_APPROVED

## Reconciliation

Periodic process:
1. read Stripe payment totals,
2. read internal funding ledger,
3. compare by currency/date/event,
4. record discrepancies,
5. correct through auditable adjustment events,
6. publish only aggregates.

## Authority separation

Stripe payment success may authorize a funding event.
It must never authorize:
- Canon claims,
- Dhamma verification,
- reviewer override,
- spiritual-attainment status,
- moderation immunity.
