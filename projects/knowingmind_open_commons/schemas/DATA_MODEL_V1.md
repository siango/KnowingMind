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
- event_type
- payment_state
- currency
- gross_amount
- occurred_at
- processed_at
- payload_hash

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

External events such as Stripe webhooks and GitHub contribution sync must store stable external IDs or hashes sufficient to prevent duplicate effects.
