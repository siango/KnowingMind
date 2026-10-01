from __future__ import annotations

import argparse
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PRINCIPLES = {
    "project": "KnowingMind",
    "authority_rule": "SOURCE > MODEL",
    "ai_is_canon": False,
    "ai_is_spiritual_authority": False,
    "public_runtime_dependency": False,
}


class Handler(BaseHTTPRequestHandler):
    def _json(self, payload: dict, status: int = 200) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        if self.path == "/health":
            self._json({"ok": True, "service": "knowingmind-public-demo"})
            return
        if self.path == "/principles":
            self._json(PRINCIPLES)
            return
        self._json(
            {
                "name": "KnowingMind public demo",
                "message": "Public-safe demo with synthetic/static data only.",
                "endpoints": ["/health", "/principles"],
            }
        )

    def log_message(self, _format: str, *_args: object) -> None:
        return


def self_check() -> None:
    assert PRINCIPLES["authority_rule"] == "SOURCE > MODEL"
    assert PRINCIPLES["ai_is_canon"] is False
    assert PRINCIPLES["ai_is_spiritual_authority"] is False
    assert PRINCIPLES["public_runtime_dependency"] is False


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    if args.check:
        self_check()
        print("PUBLIC_DEMO_CHECK_PASS")
    else:
        self_check()
        ThreadingHTTPServer(("127.0.0.1", args.port), Handler).serve_forever()
