# KnowingMind Public Demo

This is a deliberately small, dependency-free, public-safe runnable slice.

It uses only static/synthetic values and has no access to production PostgreSQL,
Dhamma MCP, credentials, private evidence, user practice records, payment data,
or private infrastructure.

Run:

```bash
python examples/public-demo/app.py --check
python -m unittest discover -s examples/public-demo -p 'test_*.py'
python examples/public-demo/app.py --port 8765
```

Then visit:

- http://127.0.0.1:8765/health
- http://127.0.0.1:8765/principles
