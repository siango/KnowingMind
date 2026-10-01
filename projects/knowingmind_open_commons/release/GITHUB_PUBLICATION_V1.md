# GitHub Publication Strategy V1

## Current controlled source

Private source repository:
- siango/KnowingMindApp

This repository remains controlled during public-alpha preparation.

## Preferred public strategy

Do not simply flip the private production repository to public.

Preferred route:
1. produce a reviewed PUBLIC source manifest,
2. exclude RESTRICTED/PROHIBITED/UNKNOWN material,
3. create a clean public repository/history,
4. validate public clone/build/tests,
5. verify no private runtime dependency is required for development,
6. publish only after human release gate.

Candidate public repository name:
- siango/KnowingMind

Final repository naming remains a maintainer decision.

## Required public files

- README.md
- LICENSE
- NOTICE where required
- CONTRIBUTING.md
- CODE_OF_CONDUCT.md
- SECURITY.md
- GOVERNANCE.md
- public architecture docs
- issue templates
- pull-request template
- public roadmap
- localization guide

## Contribution flow

Fork/branch
→ issue or scoped proposal where needed
→ PR
→ CI
→ technical review
→ domain/Dhamma review if applicable
→ independent verification for high-impact changes
→ merge
→ contribution event

## Branch protections

Public main should require:
- pull request,
- required checks,
- review,
- no direct unreviewed force push,
- security-sensitive changes to receive appropriate review.

## Public-source verification

A public release candidate is valid only if:
- checked-out from the candidate public repository,
- build/test executes from that checkout,
- no private file is required to make tests pass,
- public docs correctly describe authority boundaries.

## Existing production repository

Production workflows may remain private even when application code becomes open source.
Open source does not require publishing credentials or private infrastructure details.
