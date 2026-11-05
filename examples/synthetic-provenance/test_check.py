import importlib.util
import pathlib
import unittest

MODULE_PATH = pathlib.Path(__file__).with_name("check.py")
SPEC = importlib.util.spec_from_file_location("synthetic_provenance_check", MODULE_PATH)
CHECK = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(CHECK)


class SyntheticProvenanceTests(unittest.TestCase):
    def test_all_sources_have_required_fields(self):
        for sid, row in CHECK.source_ids().items():
            for field in ("title", "kind", "classification", "content_sha256"):
                self.assertIn(field, row)
            self.assertEqual(sid, row["source_id"])

    def test_provenance_cites_only_known_sources(self):
        CHECK.check_provenance()

    def test_citations_reference_only_known_sources(self):
        CHECK.check_citations()

    def test_self_check_passes(self):
        CHECK.self_check()


if __name__ == "__main__":
    unittest.main()
