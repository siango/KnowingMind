# Public / Private Boundary V1

## Classification values

### PUBLIC
Approved for public repository and public documentation.

Examples:
- sanitized application code,
- public API schemas,
- UI source,
- tests with synthetic data,
- public architecture docs,
- translation strings,
- contributor documentation.

### RESTRICTED
Required for internal operation but not public.

Examples:
- internal operational evidence,
- non-public incident material,
- private deployment topology,
- sensitive admin procedures.

### PROHIBITED
Must not enter public source.

Examples:
- API keys,
- tokens,
- .env contents,
- private keys,
- webhook signing secrets,
- Cloudflare/FastAPI/Stripe credentials,
- private user/practice records,
- raw authentication data,
- payment credentials.

### SHARED
Potentially reusable infrastructure shared across projects. Must be explicitly classified before copying to public source.

### UNKNOWN
Not publishable until reviewed.

## Source-material rule

Raw Canon PDFs, books, translations, images, recordings, or third-party corpora require explicit redistribution rights. Indexing or internal lawful access does not automatically grant republication rights.

## Git-history rule

Deleting a secret from the current working tree does not prove it was never present in history.

Before public release:
1. scan current tree,
2. assess repository history,
3. rotate any exposed credential,
4. prefer clean public history when exposure cannot be confidently excluded.

## Runtime rule

Production configuration remains provider-native.

Public repository examples must use placeholders such as environment-variable names only, never real values.

## Public-data rule

Public contribution identity should be separable from private membership/payment identity.

A donor's public recognition requires explicit consent.

## Authority rule

Publication classification does not change DHAMMA authority. Public copies are projections/source distributions, not new Canon truth stores.
