# KnowingMind Open Commons Security & Privacy V1

## Security goals

1. public source contains no production secrets,
2. production credentials use provider-native secret storage,
3. least-privilege service credentials,
4. private user/payment/practice data stays outside public source,
5. public release history is reviewed for past exposure,
6. privileged actions are auditable.

## Mandatory secret classes

Never commit values for:
- FastAPI Cloud deploy tokens,
- Stripe restricted/secret keys,
- Stripe webhook signing secrets,
- Cloudflare tokens/secrets,
- OAuth client secrets,
- database credentials,
- private keys,
- Dhamma edge/access shared secrets,
- model-provider secret keys.

## CI controls

Before public release:
- current-tree secret scan,
- Git-history secret scan,
- dependency audit,
- license/source inventory,
- synthetic-data validation,
- forbidden-file pattern check.

## Runtime secrets

FastAPI Cloud:
- application runtime secrets,
- Stripe runtime secrets,
- service-to-service credentials.

GitHub Actions:
- deployment credentials only where required,
- no unnecessary runtime secrets.

## Stripe controls

- use restricted API keys where possible,
- separate sandbox/live keys,
- verify webhook signatures,
- never log keys or full sensitive event payloads,
- use strong dashboard authentication,
- rotate compromised credentials immediately.

## Privacy zones

### Public
- public profile fields with consent,
- accepted contribution records,
- aggregate project/funding statistics.

### Private
- email/auth identity,
- payment identity,
- private messages,
- practice records,
- security reports,
- moderation notes.

### Highly restricted
- credentials,
- authentication/session material,
- sensitive health/practice data where applicable,
- incident secrets.

## Logging

Logs must not dump:
- environment variables,
- authorization headers,
- cookies,
- Stripe secrets,
- private practice text by default.

## Vulnerability handling

Security vulnerabilities must use a private reporting channel.
Do not require a public GitHub issue for sensitive disclosures.

## Public release rule

Repository visibility must not be changed until RELEASE_GATES_V1 security gates pass.
