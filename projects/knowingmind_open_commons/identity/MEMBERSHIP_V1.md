# KnowingMind Membership V1

## Objective

Provide one general KnowingMind identity layer for members, contributors, reviewers, and supporters without making GitHub the only login path.

## Identity principles

- a normal user must not need a GitHub account,
- developer identity may link to GitHub,
- public contribution identity is separable from private account identity,
- payment identity is never automatically public,
- religious belief is not required profile data,
- do not infer religion, spiritual attainment, or political belief from behavior.

## Minimum account model

identity.users
- user_id
- status
- preferred_locale
- created_at
- updated_at

identity.identities
- identity_id
- user_id
- provider
- provider_subject
- verified_at

identity.public_profiles
- user_id
- display_name
- bio
- public_contribution_visibility
- public_supporter_visibility

identity.role_grants
- user_id
- role
- scope
- granted_by
- granted_at

## Roles

- MEMBER
- CONTRIBUTOR
- REVIEWER
- DOMAIN_REVIEWER
- MAINTAINER
- INDEPENDENT_VERIFIER

Role grants are auditable and must not be derived from donation amount.

## Authentication roadmap

Public alpha baseline:
1. email/passkey or equivalent general-user authentication,
2. GitHub identity link for developers,
3. additional identity providers only when needed.

## Privacy

Private:
- login identifiers,
- email,
- payment-customer identifiers,
- moderation notes,
- consent history.

Potentially public with explicit consent:
- display name,
- merged contributions,
- translation/review attribution,
- supporter acknowledgement.

## Account lifecycle

Required flows:
- create,
- authenticate,
- link/unlink provider,
- update profile,
- export applicable user data,
- deactivate/delete according to policy and legal requirements,
- revoke public-recognition consent.

## Security requirements

- no production secret in browser/mobile client,
- session/token expiry,
- rate limiting,
- audit privileged role changes,
- strong authentication for maintainers,
- no donation-based privilege escalation.
