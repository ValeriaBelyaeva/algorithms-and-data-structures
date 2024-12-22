# lab7/task5/tests/test.py

import unittest
import os

from lab7.task5.src.lcs_three_sequences import (
    task5, PATH, OUTPUT_PATH, lcs_three_length
)

class TestLCSThreeSequences(unittest.TestCase):

    def setUp(self):
        self.test_input_path = r"D:\algorithms-and-data-structures\lab7\task5\txtf\test_input.txt"
        self.test_output_path = r"D:\algorithms-and-data-structures\lab7\task5\txtf\test_output.txt"

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
        import lab7.task5.src.lcs_three_sequences as module
        module.PATH = self.test_input_path
        module.OUTPUT_PATH = self.test_output_path

    def _restore_global_paths(self):
        import lab7.task5.src.lcs_three_sequences as module
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

    def test_example1(self):
        # Пример: n=3 A=[1,2,3], m=3 B=[2,1,3], l=3 C=[1,3,5]
        # Одна общая подпоследовательность (1,3) => длина 2
        lines = [
            "3",
            "1 2 3",
            "3",
            "2 1 3",
            "3",
            "1 3 5"
        ]
        self.write_test_file(lines)
        task5()
        res = self.read_output_file()
        self.assertEqual(res, "2")

    def test_no_common(self):
        # Нет общих
        lines = [
            "3",
            "8 3 2",
            "3",
            "1 1 1",
            "3",
            "5 5 5"
        ]
        self.write_test_file(lines)
        task5()
        res = self.read_output_file()
        self.assertEqual(res, "0")

    def test_some_common(self):
        # A=[8,2,1,3,8,1,0,7]
        # B=[8,2,1,3,8,1,0]
        # C=[6,8,3,1,4,7]
        # LCS might be something like (8,3,1) or (8,2,1) if 2 is in C? No, 2 not in C => (8,3,1)
        # Let's see length=3
        lines = [
            "8",
            "8 2 1 3 8 1 0 7",
            "7",
            "8 2 1 3 8 1 0",
            "6",
            "6 8 3 1 4 7"
        ]
        self.write_test_file(lines)
        task5()
        res = self.read_output_file()
        # Possibly "8,3,1" => length=3
        self.assertEqual(res, "3")

if __name__ == '__main__':
    unittest.main()
