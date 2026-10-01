# KnowingMind Open Commons Data Model V1

This is a logical schema plan. It does not create database objects by itself.

## identity

### identity.users
Core private account record.

### identity.identities
External/login identities linked to user.

### identity.public_profiles
Explicitly public profile attributes.

### identity.role_grants
Auditable scoped roles.

## community

### community.contributions
Normalized accepted contribution.

Fields may include:
- contribution_id
- user_id
- contribution_type
- external_ref
- state
- accepted_at
- reviewer_ref

### community.contribution_events
Append-oriented event stream for contribution lifecycle.

### community.points_ledger
Append-oriented points ledger:
- ledger_id
- user_id
- contribution_id
- points_delta
- reason_code
- policy_version
- created_at
- reversal_of

### community.badges
Non-authoritative community recognition.

## funding

### funding.payment_events
Provider-normalized payment events.

Suggested fields:
- provider_event_id
- provider
- provider_object_id
- payment_ref
- event_type
- status_transition_key
- payment_state
- currency
- gross_amount
- occurred_at
- processed_at
- payload_hash

### funding.payment_adjustments
Append-only, auditable refund/dispute effects linked to the original payment.

Required uniqueness: `(provider, provider_object_id, status_transition_key)` so separate webhook event IDs cannot apply the same business effect twice. Track adjustment amount/currency and policy version; cumulative reversals for a payment must never exceed its original credited amount.

### funding.contributions
Normalized financial-support record.

### funding.expenses
Project cost ledger.

### funding.cost_centers
Cost categories/providers/projects.

### funding.monthly_summary
Derived aggregate for public sustainability display.

## i18n

### i18n.translations
Content-to-locale translations.

### i18n.terminology
Domain-specific terminology registry.

### i18n.translation_reviews
Review trail.

## governance

### governance.review_events
Technical/domain/independent review history.

### governance.release_gates
Evidence-backed release-gate status.

### governance.audit_log
Privileged operational changes.

## Hard separations

Do not merge community/funding tables into:
- canon authority tables,
- evidence authority tables,
- practice private records.

Payment/provider IDs are not Canon identifiers.

## Idempotency

Stripe ingress deduplicates by `(provider, provider_event_id)`. Refund/dispute ledger effects also use `(provider, provider_object_id, status_transition_key)` because one Stripe object can emit multiple event IDs for a single terminal outcome. Enforce a cumulative reversal cap at the original credited payment amount. GitHub contribution sync also stores stable external IDs or hashes sufficient to prevent duplicate effects.
