import unittest
from src.linux_lib_explainer import LinuxLibExplainer

class TestLinuxLibExplainer(unittest.TestCase):
    def setUp(self):
        self.explainer = LinuxLibExplainer()

    def test_explain_library(self):
        # Test with a known library
        lib_name = 'libc.so.6'
        explanation = self.explainer.explain_library(lib_name)
        self.assertIsNotNone(explanation)

        # Test with a non-existent library
        lib_name = 'non_existent_lib.so'
        with self.assertRaises(Exception):
            self.explainer.explain_library(lib_name)

if __name__ == '__main__':
    unittest.main()