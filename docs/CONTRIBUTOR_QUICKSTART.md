# Contributor quickstart

This page lets a new volunteer clone the public repository, run the
public-safe demo, run its tests, and open a pull request — using only this
repository and the public internet. No private infrastructure, credentials,
databases, Dhamma MCP servers, or donor/payment data are ever required.

The invariant to keep in view the whole way: **SOURCE > MODEL**. Dhamma
content and cited source are authoritative; AI output is a tool, not an
authority. Everything below stays inside the public boundary described in
`docs/PUBLIC_PRIVATE_BOUNDARY.md`.

## Prerequisites

- Python 3.10 or newer. The public demo uses the standard library only, so
  there are no packages to install.
- `git` and a GitHub account.

## 1. Clone and orient

```bash
git clone https://github.com/siango/KnowingMind.git
cd KnowingMind
```

Start with `README.md`, then `CONTRIBUTING.md`. The public demo lives in
`examples/public-demo/`.

## 2. Run the public-safe demo

From the repository root:

```bash
python examples/public-demo/app.py --check
```

Prints `PUBLIC_DEMO_CHECK_PASS` when the demo's invariants hold. To serve it:

```bash
python examples/public-demo/app.py --port 8765
```

Then open:

- `http://127.0.0.1:8765/health`
- `http://127.0.0.1:8765/principles`

The demo is dependency-free by design: it only imports standard-library
modules and carries no private-runtime markers.

## 3. Run the demo tests

Run the test module directly from the repository root:

```bash
python -m unittest examples/public-demo/test_app.py
```

Expected result: `Ran 8 tests ... OK`.

Note: `python -m unittest discover -s examples/public-demo` prints "OK" but
discovers **0** tests, because that directory is not an importable package
(it has no `__init__.py`). Use the direct-module invocation above to actually
exercise the suite.

## 4. Open your first pull request

1. Open a short issue first when the change is more than a trivial fix
   (see `CONTRIBUTING.md`).
2. Create a branch from `main`:

   ```bash
   git checkout main
   git pull
   git checkout -b docs/my-first-change
   ```

3. Make a small, scoped change and add tests or docs where applicable.
4. Commit with a clear message and push:

   ```bash
   git add <changed files>
   git commit -m "docs: add a short contributor note"
   git push -u origin docs/my-first-change
   ```

5. Open the pull request against `main` from the branch.

## What to include and what to leave out

Every contribution must stay on the public side of the boundary:

- Include: public application code, public contracts with no secrets,
  documentation, synthetic fixtures, tests, localization files, and
  contribution templates.
- Leave out (fail-closed): credentials or secrets, production environment
  dumps, private runtime evidence, private user practice records,
  donor/payment details, and any file whose classification or rights are
  unclear. If a file's status is unknown, keep it out until it is reviewed.
- Examples and tests must use mock or synthetic data only.
- Never claim Canon verification from source code or an automated test;
  Dhamma-content changes require a Dhamma review issue.

Small, reviewable, reproducible-from-this-repo changes are the best fit for
a first contribution.
