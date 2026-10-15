from __future__ import annotations

import argparse
import json
import pathlib
from typing import Dict

HERE = pathlib.Path(__file__).resolve().parent


def _load(name: str) -> dict:
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def source_ids() -> Dict[str, dict]:
    rows = json.loads((HERE / "sources.fixture.json").read_text(encoding="utf-8"))
    assert isinstance(rows, list), "sources.fixture.json must be a list"
    out: Dict[str, dict] = {}
    for row in rows:
        assert "source_id" in row, "every source needs a source_id"
        out[row["source_id"]] = row
    return out


def check_sources() -> None:
    for sid, row in source_ids().items():
        for field in ("title", "kind", "classification", "content_sha256"):
            assert field in row, f"{sid} missing {field!r}"
        assert sid == row["source_id"]


def check_provenance() -> None:
    doc = _load("provenance.fixture.json")
    known = set(source_ids())
    ids = set()
    for rec in doc["records"]:
        assert rec["provenance_id"] not in ids, f"duplicate provenance_id {rec['provenance_id']}"
        ids.add(rec["provenance_id"])
        for ref in rec["derived_from"]:
            assert ref["source_id"] in known, f"{rec['provenance_id']} cites unknown source {ref['source_id']!r}"
            assert "retrieval_state" in ref
        # a model-assisted record must still name its underlying source(s)
        if rec.get("ai_generated") is True:
            assert ref_count(rec) >= 1, f"{rec['provenance_id']} is model-assisted but cites no source"


def ref_count(rec: dict) -> int:
    return len(rec.get("derived_from", []))


def check_citations() -> None:
    doc = _load("citations.fixture.json")
    known = set(source_ids())
    for cite in doc["citations"]:
        assert "citation_id" in cite and "display" in cite, "citation needs id and display"
        refs = cite.get("references", [])
        assert refs, f"{cite['citation_id']} must reference at least one source"
        for ref in refs:
            assert ref["source_id"] in known, f"{cite['citation_id']} cites unknown source {ref['source_id']!r}"
            assert "locator" in ref, f"{cite['citation_id']} reference needs a locator"


def self_check() -> None:
    check_sources()
    check_provenance()
    check_citations()
    print("SYNTHETIC_PROVENANCE_CHECK_PASS")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    self_check()
