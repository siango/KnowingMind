# KnowingMind Synthetic Provenance & Citation Fixtures

A small, dependency-free, public-safe example of how **provenance** and
**citation** metadata are represented in this project.

Every value here is **invented**. There are no private evidence records, no
user data, and no copyrighted source dumps — only stable identifiers, locators,
and review states. The fixtures demonstrate shape, not real content.

## Files

| File | What it shows |
| --- | --- |
| `sources.fixture.json` | The public source registry: a source id, a stable title, license, classification, and a content hash. |
| `provenance.fixture.json` | How a statement records *what it is derived from* and *where to verify it*, including a model-assisted record that still names its underlying source. |
| `citations.fixture.json` | How a public citation names a source and a stable locator — never a private path, endpoint, or credential. |
| `check.py` | A stdlib-only validator for the three fixtures above. |
| `test_check.py` | `unittest` tests over that validator. |

## Authority rule

The fixtures honour the project's `SOURCE > MODEL` principle: a model-assisted
record (`ai_generated: true`) still carries `derived_from` references to the
underlying source, so the source remains the authority and the model output is
never treated as canon or spiritual authority.

## Run

```bash
python examples/synthetic-provenance/check.py --check
python examples/synthetic-provenance/test_check.py -v
```

(`unittest discover` with a dashed directory name does not pick these up in this repo; running the test module directly, as above, is the reliable form.)

## What the fixtures do not do

They do not add secrets, private paths, or production endpoint details. They do
not claim Canon verification. They are a public-shape reference for a future
real provenance/citation API, not the runtime itself.
