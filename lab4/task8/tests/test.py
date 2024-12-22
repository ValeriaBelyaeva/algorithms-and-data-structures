# lab4/task8/tests/test.py

import unittest
import os

from lab4.task8.src.postfix_notation import (
    task8, PATH, OUTPUT_PATH, evaluate_postfix
)

class TestPostfixNotation(unittest.TestCase):

    def setUp(self):
        self.test_input_path = r"D:\algorithms-and-data-structures\lab4\task8\txtf\test_input.txt"
        self.test_output_path = r"D:\algorithms-and-data-structures\lab4\task8\txtf\test_output.txt"
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
        import lab4.task8.src.postfix_notation as module
        module.PATH = self.test_input_path
        module.OUTPUT_PATH = self.test_output_path

    def _restore_global_paths(self):
        import lab4.task8.src.postfix_notation as module
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

    def test_evaluate_postfix_basic(self):
        # 2 3 + -> 5
        expr = ["2", "3", "+"]
        self.assertEqual(evaluate_postfix(expr), 5)
        # 2 3 * -> 6
        expr = ["2", "3", "*"]
        self.assertEqual(evaluate_postfix(expr), 6)
        # 5 2 - -> 3
        expr = ["5", "2", "-"]
        self.assertEqual(evaluate_postfix(expr), 3)

    def test_task8(self):
        # (8 + 9) * (1 - 7) = 17 * (-6) = -102
        # Постфикс: 8 9 + 1 7 - *
        N = 5
        expr = "8 9 + 1 7 - *"
        lines = [
            str(N),
            expr
        ]
        self.write_test_file(lines)
        task8()
        result = self.read_output_file()
        self.assertEqual(result, "-102")

if __name__ == '__main__':
    unittest.main()
