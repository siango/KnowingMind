import ast
import importlib.util
import io
import json
import pathlib
import unittest

MODULE_PATH = pathlib.Path(__file__).with_name("app.py")
SPEC = importlib.util.spec_from_file_location("public_demo_app", MODULE_PATH)
APP = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(APP)

# The public demo must stay dependency-free: only these standard-library
# modules are allowed. Anything outside this set is a private or third-party
# runtime dependency and a failure.
_STDLIB_OK = {"__future__", "argparse", "http", "json", "pathlib", "os", "sys", "typing"}

# Words that would mean the demo reached for private infrastructure. The app
# must never carry them.
_PRIVATE_MARKERS = ("postgres", "dhamma", "credential", "stripe", "payment")


def _fake_handler(path):
    """A stand-in request handler so do_GET can run without a real socket.

    It reuses the app's real do_GET/_json methods and only fakes the socket
    surface a BaseHTTPRequestHandler instance would provide.
    """

    class _Handler:
        do_GET = APP.Handler.do_GET
        _json = APP.Handler._json

        def __init__(self):
            self.path = path
            self.status = None
            self.wfile = io.BytesIO()

        def send_response(self, status):
            self.status = status

        def send_header(self, key, value):
            return

        def end_headers(self):
            return

    return _Handler()


class PublicDemoTests(unittest.TestCase):
    def test_source_over_model(self):
        self.assertEqual(APP.PRINCIPLES["authority_rule"], "SOURCE > MODEL")

    def test_ai_not_authority(self):
        self.assertFalse(APP.PRINCIPLES["ai_is_canon"])
        self.assertFalse(APP.PRINCIPLES["ai_is_spiritual_authority"])

    def test_no_private_runtime_dependency(self):
        self.assertFalse(APP.PRINCIPLES["public_runtime_dependency"])

    def test_principles_endpoint_returns_full_payload(self):
        handler = _fake_handler("/principles")
        APP.Handler.do_GET(handler)
        self.assertEqual(handler.status, 200)
        self.assertEqual(json.loads(handler.wfile.getvalue().decode("utf-8")), APP.PRINCIPLES)

    def test_health_endpoint_reports_ok(self):
        handler = _fake_handler("/health")
        APP.Handler.do_GET(handler)
        payload = json.loads(handler.wfile.getvalue().decode("utf-8"))
        self.assertTrue(payload["ok"])
        self.assertEqual(payload["service"], "knowingmind-public-demo")

    def test_unknown_endpoint_shows_demo_banner(self):
        handler = _fake_handler("/")
        APP.Handler.do_GET(handler)
        payload = json.loads(handler.wfile.getvalue().decode("utf-8"))
        self.assertEqual(payload["endpoints"], ["/health", "/principles"])
        self.assertIn("message", payload)

    def test_app_only_imports_stdlib_modules(self):
        source = MODULE_PATH.read_text(encoding="utf-8")
        imported = set()
        for node in ast.walk(ast.parse(source)):
            if isinstance(node, ast.Import):
                imported.update(name.name.split(".")[0] for name in node.names)
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imported.add(node.module.split(".")[0])
        self.assertEqual(
            [module for module in sorted(imported) if module not in _STDLIB_OK],
            [],
            "public demo must not import anything outside the stdlib allowlist",
        )

    def test_source_has_no_private_runtime_markers(self):
        source = MODULE_PATH.read_text(encoding="utf-8").lower()
        for marker in _PRIVATE_MARKERS:
            self.assertNotIn(marker, source)


if __name__ == "__main__":
    unittest.main()
