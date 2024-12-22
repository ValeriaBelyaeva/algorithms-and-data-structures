# lab4/task3/tests/test.py

import unittest
import os

from lab4.task3.src.bracket_sequence import (
    task3, PATH, OUTPUT_PATH, is_correct_bracket_sequence
)

class TestBracketSequence(unittest.TestCase):

    def setUp(self):
        self.test_input_path = r"D:\algorithms-and-data-structures\lab4\task3\txtf\test_input.txt"
        self.test_output_path = r"D:\algorithms-and-data-structures\lab4\task3\txtf\test_output.txt"

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
        import lab4.task3.src.bracket_sequence as module
        module.PATH = self.test_input_path
        module.OUTPUT_PATH = self.test_output_path

    def _restore_global_paths(self):
        import lab4.task3.src.bracket_sequence as module
        module.PATH = self.original_path
        module.OUTPUT_PATH = self.original_output_path

    def write_test_file(self, lines):
        with open(self.test_input_path, 'w', encoding='utf-8') as f:
            for line in lines:
                f.write(line + '\n')

    def read_output_file(self):
        if not os.path.exists(self.test_output_path):
            return []
        with open(self.test_output_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f]

    def test_function_basic(self):
        self.assertTrue(is_correct_bracket_sequence("()"))
        self.assertTrue(is_correct_bracket_sequence("([])"))
        self.assertFalse(is_correct_bracket_sequence("([)]"))
        self.assertFalse(is_correct_bracket_sequence("(((]"))

    def test_task_simple(self):
        lines = [
            "5",
            "()",
            "([])",
            "([)]",
            "((]]",
            "()[]"
        ]
        # Правильные: () -> YES
        # ([]) -> YES
        # ([)] -> NO
        # ((]] -> NO
        # ()[] -> YES
        self.write_test_file(lines)
        task3()
        result = self.read_output_file()
        self.assertEqual(result, ["YES", "YES", "NO", "NO", "YES"])

if __name__ == '__main__':
    unittest.main()
