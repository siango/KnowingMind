# KnowingMind I18N Policy V1

## Launch locales

- th — ไทย
- en — English
- zh-Hans — 简体中文

Prepare the architecture so zh-Hant can be added later without restructuring content IDs.

## Translation object

Each translatable knowledge/content object should preserve:

- content_id
- source_language
- target_locale
- source_reference
- source_hash/version
- translation_status
- translator identity or system
- reviewer identity
- reviewed_at
- terminology_version

## Translation states

DRAFT
→ AI_DRAFT
→ HUMAN_REVIEW
→ VERIFIED_TRANSLATION

AI-generated translation must not silently appear as verified human translation.

## Source-sensitive terms

Religious/philosophical terms require terminology records that can preserve:
- source-language term,
- transliteration,
- literal gloss,
- context-sensitive translation,
- domain/tradition,
- reviewer notes.

Do not force one English/Chinese/Thai term across traditions when meanings differ.

## UI requirements

Critical public-alpha surfaces must support all launch locales:
- landing page,
- sign-in/account,
- ask/search,
- source/evidence labels,
- contribution pages,
- support/donation pages,
- privacy/security notices,
- public status/sustainability page.

## Fallback

Fallback must be visible and deterministic.
Preferred:
target locale → English fallback → source language display.

Never fabricate a translation when no translation exists.

## Provenance

Translated claims retain original-source provenance.
Translation provenance is additional metadata; it does not replace source provenance.
