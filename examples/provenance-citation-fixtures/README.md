# Provenance and Citation Fixtures (synthetic)

Small, invented examples of how provenance and citation metadata are
represented in a public-safe way. The data is synthetic: no private
evidence, no user data, and no copyrighted source text appears here.

Each citation points at a provenance record through `provenance_id`. The
provenance record carries only public classification and the rule that a
source always outranks the model (`SOURCE > MODEL`). Excerpts are
placeholders, never real source text, and every citation states its
license/redistribution status.

Run the self-check (standard library only):

```bash
python examples/provenance-citation-fixtures/test_fixtures.py
```
