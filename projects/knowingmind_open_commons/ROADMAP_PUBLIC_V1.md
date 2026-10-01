# KNOWINGMIND_OPEN_COMMONS — Public Roadmap V1

## OC-0 — Public Release Reconciliation

Goal: establish a correct baseline before publication.

Deliverables:
- authoritative state/readback reconciliation,
- file inventory,
- PUBLIC / RESTRICTED / PROHIBITED / SHARED / UNKNOWN classification,
- secret scan,
- Git-history exposure assessment,
- third-party licensing inventory,
- public dependency inventory,
- public-source manifest.

Exit gate:
- no unresolved secret or licensing blocker in the public manifest,
- source-state claims match current authority,
- public build candidate identified.

## OC-1 — Clean Public GitHub

Goal: create a sanitized public code surface.

Deliverables:
- clean public repository candidate,
- minimal clean history,
- README,
- CONTRIBUTING,
- CODE_OF_CONDUCT,
- SECURITY,
- issue and PR templates,
- public architecture documentation,
- synthetic examples.

Exit gate:
- no production secret/private-data dependency,
- public clone/build/test passes,
- security review passes.

## OC-2 — Open Licensing

Goal: make code/documentation legally reusable while preserving third-party rights.

Proposed baseline:
- Apache-2.0 for project-owned code,
- CC BY 4.0 for project-owned documentation,
- third-party sources retain original rights/licenses.

Exit gate:
- maintainer human decision recorded,
- copyright/source inventory complete,
- root public license files match decision.

## OC-3 — TH / EN / zh-Hans Foundation

Goal: first-class Thai, English, Simplified Chinese.

Deliverables:
- locale framework,
- terminology registry,
- translation states,
- reviewer attribution,
- fallback policy,
- machine-readable translation provenance.

Exit gate:
- critical public UI available in all three locales,
- no silent machine translation presented as verified human translation.

## OC-4 — Membership

Goal: create a general KnowingMind identity layer.

Deliverables:
- member profile,
- role model,
- GitHub developer identity connection,
- privacy and consent controls,
- moderation status,
- account export/delete process where applicable.

Exit gate:
- account lifecycle tested,
- private identity data separated from public contribution profile.

## OC-5 — Contribution Points

Goal: recognize useful contributions without claiming to measure religious merit.

Contribution classes:
- code,
- review,
- translation,
- source verification,
- documentation,
- community help,
- content production,
- infrastructure/compute support,
- financial support.

Exit gate:
- points only after verified/accepted contribution event,
- anti-spam and reversal rules exist,
- donations cannot purchase doctrinal/reviewer authority.

## OC-6 — Funding and Expense Ledger

Goal: support sustainable infrastructure transparently.

Deliverables:
- Stripe sandbox integration,
- verified webhook ingestion,
- contribution/funding ledger,
- expense categories,
- monthly summaries,
- separation of private payment identity from public totals.

Exit gate:
- sandbox end-to-end payment canary passes,
- idempotency and webhook signatures verified,
- reconciliation procedure documented.

## OC-7 — Public Sustainability Dashboard

Goal: show how the project is sustained.

Public aggregates may include:
- infrastructure costs,
- AI/API costs,
- storage/database costs,
- monitoring,
- media generation,
- domain/edge costs,
- support received,
- runway estimate.

Never expose:
- secret keys,
- full invoices with sensitive identifiers,
- payment credentials,
- private donor identity without consent.

## OC-8 — Contributor Workflow

Goal: make external contribution safe and efficient.

Deliverables:
- issue templates,
- PR templates,
- labels,
- contributor guide,
- Dhamma/domain-review routes,
- security reporting route,
- independent verification route.

Exit gate:
- test external contribution from fork to merged PR,
- contribution event reaches recognition ledger.

## OC-9 — Public Alpha

Goal: release a bounded public version.

Preconditions:
- OC-0 through OC-8 mandatory gates pass,
- live public frontend can be exercised,
- production authority and public projection are clearly separated,
- rollback plan exists,
- incident contact exists.

Public-alpha is not equivalent to production-complete Canon or universal spiritual authority.

## OC-10 — Interfaith Knowledge Domains

Goal: allow additional traditions and non-religious knowledge domains under a common provenance framework.

Requirements:
- each domain defines source authority and provenance,
- cross-domain comparison remains descriptive,
- disputed interpretation is attributed,
- no forced doctrinal unification,
- no domain inherits DHAMMA Canon authority automatically.

## Phase control

Each phase state must use evidence-backed states such as:

NOT_STARTED → SOURCE_IN_PROGRESS → SOURCE_COMPLETE_UNVERIFIED → VERIFIED_PASS

Requested or coded work alone must never be reported as verified public readiness.
