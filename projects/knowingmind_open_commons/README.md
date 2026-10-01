# KNOWINGMIND_OPEN_COMMONS

Status: SOURCE_STRUCTURE_CREATED_UNVERIFIED  
Parent authority: DHAMMA_GROUNDED_AI  
Project key: KNOWINGMIND_OPEN_COMMONS  
Source repository: siango/KnowingMindApp  
Source folder: projects/knowingmind_open_commons/  
Initial phase: OC-0  
Public release: NOT YET APPROVED  
Production truth: PostgreSQL + pgvector via Dedicated Dhamma MCP for DHAMMA authority

## Mission

KnowingMind Open Commons / เอไอตัวรู้ is the public, open-community layer for sharing knowledge and tools that help people investigate mind, meaning, practice, and human experience without requiring conversion to Buddhism or any other religion.

The system must support human agency. It should expose sources, traditions, evidence, interpretation boundaries, and AI analysis separately so users can consider and decide for themselves.

## Core principles

1. SOURCE > MODEL.
2. AI is not Canon and is not a spiritual authority.
3. No user is required to accept Buddhist doctrine or any religious belief.
4. Interfaith and non-religious access are first-class.
5. Sources and traditions must retain provenance.
6. Public code and documentation must be separated from production secrets and private user data.
7. Financial support must never purchase doctrinal authority or content-review authority.
8. Community points are recognition of contribution, not a measurement of religious merit, karma, holiness, or attainment.
9. Reuse existing infrastructure before creating a duplicate system.
10. Public release requires explicit release gates and independent readback.

## Repository strategy

The current private repository remains the controlled source/production repository during public-alpha preparation.

A future public repository should be generated from a sanitized, reviewed source set with clean public history rather than blindly exposing private repository history.

## Folder map

- PROJECT_CHARTER_V1.md — mission, scope, principles, exclusions
- ROADMAP_PUBLIC_V1.md — OC-0 through OC-10
- PHASES_V1.json — machine-readable phase manifest; source-only until promoted/verified
- STATUS_V1.json — machine-readable project-source status
- architecture/ARCHITECTURE_V1.md — system layers and flows
- architecture/PUBLIC_PRIVATE_BOUNDARY_V1.md — publication classification
- governance/GOVERNANCE_V1.md — roles and decision classes
- governance/CONTRIBUTION_POINTS_POLICY_V1.md — contribution recognition
- governance/DECISION_LOG_V1.md — approved decisions and explicit non-decisions
- identity/MEMBERSHIP_V1.md — membership and identity model
- funding/STRIPE_AND_SUSTAINABILITY_V1.md — funding and Stripe architecture
- i18n/I18N_POLICY_V1.md — Thai/English/Simplified Chinese policy
- security/SECURITY_PRIVACY_V1.md — secret/privacy controls
- release/GITHUB_PUBLICATION_V1.md — public GitHub plan
- release/LICENSE_DECISION_RECORD_V1.md — approved Apache-2.0/CC-BY-4.0 model for project-owned material in the exact PUBLIC manifest; publication remains separately gated
- release/RELEASE_GATES_V1.md — mandatory go-live gates
- release/PUBLIC_SOURCE_MANIFEST_TEMPLATE_V1.json — fail-closed public file-classification manifest
- schemas/DATA_MODEL_V1.md — identity/community/funding/i18n data domains
- operations/FASTAPI_GITHUB_STRIPE_INTEGRATION_V1.md — existing-infrastructure integration plan

## Immediate first unfinished step

OC-0 PUBLIC RELEASE RECONCILIATION:

1. reconcile README/GOVERNANCE claims with current PostgreSQL/Dhamma MCP authority,
2. inventory and classify candidate public files,
3. perform secret/history/license scans,
4. define a clean public-source manifest,
5. verify that public code builds without private dependencies.

Nothing in this folder changes repository visibility or grants an open-source license by itself.
