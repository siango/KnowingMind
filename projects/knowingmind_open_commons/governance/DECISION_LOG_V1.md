# KnowingMind Open Commons Decision Log V1

## 2026-09-29 — Subproject creation approved

Decision:
Create KNOWINGMIND_OPEN_COMMONS as a controlled subproject under DHAMMA_GROUNDED_AI.

Approved scope:
- public/open-source roadmap,
- community membership,
- contribution recognition,
- transparent sustainability/funding,
- Thai/English/Simplified Chinese,
- interfaith/non-religious access,
- GitHub/FastAPI Cloud/Stripe integration planning.

Non-decisions:
- repository visibility has not been changed,
- Apache-2.0/CC BY 4.0 have not yet been legally granted,
- Stripe live has not been enabled,
- existing private production history has not been declared safe for publication.

## Architecture decisions

1. DHAMMA_GROUNDED_AI remains a bounded knowledge domain; KnowingMind Open Commons is broader than Buddhism.
2. Public release should use a sanitized clean public source/history rather than blindly exposing the current private production repository.
3. Community points recognize contribution only; they are not a measurement of religious merit or attainment.
4. Donations cannot purchase truth/review authority.
5. GitHub = source/CI, FastAPI Cloud = runtime, Stripe = payment provider, PostgreSQL/Dhamma MCP = DHAMMA authority/readback.
6. Existing FastAPI deploy workflow should be reused instead of creating a duplicate pipeline.
7. Initial locales are th, en, zh-Hans.
8. PUBLIC visibility and Stripe live remain human-gated.
