import json
import pathlib
import unittest

FIXTURES = pathlib.Path(__file__).with_name("fixtures.json")


class ProvenanceCitationFixtureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(FIXTURES.read_text(encoding="utf-8"))

    def test_fixture_is_marked_synthetic(self):
        self.assertTrue(self.data["synthetic"])
        self.assertEqual(self.data["schema"], "KNOWINGMIND_PROVENANCE_CITATION_FIXTURE_V1")

    def test_provenance_uses_source_over_model(self):
        prov = self.data["provenance"]
        self.assertEqual(prov["authority_rule"], "SOURCE > MODEL")
        self.assertFalse(prov["ai_is_canon"])
        self.assertEqual(prov["classified_as"], "PUBLIC")

    def test_every_citation_points_at_the_provenance(self):
        prov_id = self.data["provenance"]["id"]
        for citation in self.data["citations"]:
            self.assertEqual(citation["provenance_id"], prov_id)

    def test_no_real_source_text_or_secret_strings(self):
        blob = json.dumps(self.data).lower()
        for marker in ("postgres", "stripe", "credential", "api_key", "sk-"):
            self.assertNotIn(marker, blob)

    def test_citations_carry_a_license_status(self):
        for citation in self.data["citations"]:
            self.assertIn("license_status", citation)
            self.assertIn("redistribution", citation)


if __name__ == "__main__":
    unittest.main()
