import importlib.util
import pathlib
import unittest

MODULE_PATH = pathlib.Path(__file__).with_name("app.py")
SPEC = importlib.util.spec_from_file_location("public_demo_app", MODULE_PATH)
APP = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(APP)


class PublicDemoTests(unittest.TestCase):
    def test_source_over_model(self):
        self.assertEqual(APP.PRINCIPLES["authority_rule"], "SOURCE > MODEL")

    def test_ai_not_authority(self):
        self.assertFalse(APP.PRINCIPLES["ai_is_canon"])
        self.assertFalse(APP.PRINCIPLES["ai_is_spiritual_authority"])

    def test_no_private_runtime_dependency(self):
        self.assertFalse(APP.PRINCIPLES["public_runtime_dependency"])


if __name__ == "__main__":
    unittest.main()
