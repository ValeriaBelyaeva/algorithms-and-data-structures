# lab7/task7/tests/test.py

import unittest
import os

from lab7.task7.src.pattern_matching import (
    task7, PATH, OUTPUT_PATH, match_pattern
)

class TestPatternMatching(unittest.TestCase):

    def setUp(self):
        self.test_input_path = r"D:\algorithms-and-data-structures\lab7\task7\txtf\test_input.txt"
        self.test_output_path = r"D:\algorithms-and-data-structures\lab7\task7\txtf\test_output.txt"

        self.original_path = PATH
        self.original_output_path = OUTPUT_PATH
        self._override_global_paths()

    def tearDown(self):
        self._restore_global_paths()
        if os.path.exists(self.test_input_path):
            os.remove(self.test_input_path)
        if os.path.exists(self.test_output_path):
            os.remove(self.test_output_path)

    def _override_global_paths(self):
        import lab7.task7.src.pattern_matching as module
        module.PATH = self.test_input_path
        module.OUTPUT_PATH = self.test_output_path

    def _restore_global_paths(self):
        import lab7.task7.src.pattern_matching as module
        module.PATH = self.original_path
        module.OUTPUT_PATH = self.original_output_path

    def write_test_file(self, lines):
        with open(self.test_input_path, 'w', encoding='utf-8') as f:
            for line in lines:
                f.write(line + '\n')

    def read_output_file(self):
        if not os.path.exists(self.test_output_path):
            return ""
        with open(self.test_output_path, 'r', encoding='utf-8') as f:
            return f.read().strip()

    def test_example_yes(self):
        # pattern = "k?t*n"
        # text = "kitten"
        # => YES
        lines = [
            "k?t*n",
            "kitten"
        ]
        self.write_test_file(lines)
        task7()
        out = self.read_output_file()
        self.assertEqual(out, "YES")

    def test_example_no(self):
        # pattern = "k?t?n"
        # text = "kitten"
        # => NO
        lines = [
            "k?t?n",
            "kitten"
        ]
        self.write_test_file(lines)
        task7()
        out = self.read_output_file()
        self.assertEqual(out, "NO")

    def test_empty(self):
        # pattern="", text=""
        # => match
        lines = [
            "",
            ""
        ]
        self.write_test_file(lines)
        task7()
        out = self.read_output_file()
        self.assertEqual(out, "YES")

if __name__ == '__main__':
    unittest.main()
