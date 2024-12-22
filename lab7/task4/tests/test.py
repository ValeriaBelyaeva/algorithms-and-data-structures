# lab7/task4/tests/test.py

import unittest
import os

from lab7.task4.src.lcs_two_sequences import (
    task4, PATH, OUTPUT_PATH, read_sequences, lcs_length
)

class TestLCSTwoSequences(unittest.TestCase):

    def setUp(self):
        self.test_input_path = r"D:\algorithms-and-data-structures\lab7\task4\txtf\test_input.txt"
        self.test_output_path = r"D:\algorithms-and-data-structures\lab7\task4\txtf\test_output.txt"

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
        import lab7.task4.src.lcs_two_sequences as module
        module.PATH = self.test_input_path
        module.OUTPUT_PATH = self.test_output_path

    def _restore_global_paths(self):
        import lab7.task4.src.lcs_two_sequences as module
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
        # Пример из условия:
        # n=3, seqA=[2,7,5]
        # m=2, seqB=[2,5]
        # Одна общая подпоследовательность (2,5) => длина 2
        lines = [
            "3",
            "2 7 5",
            "2",
            "2 5"
        ]
        self.write_test_file(lines)
        task4()
        result = self.read_output_file()
        self.assertEqual(result, "2")

    def test_no_common(self):
        # n=1, seqA=[0], m=4, seqB=[1,2,3,4]
        # Нет общих элементов => LCS=0
        lines = [
            "1",
            "0",
            "4",
            "1 2 3 4"
        ]
        self.write_test_file(lines)
        task4()
        res = self.read_output_file()
        self.assertEqual(res, "0")

    def test_common_two(self):
        # n=4, seqA=[2,7,8,3], m=4, seqB=[5,2,8,7]
        # LCS could be length 2 (e.g. [2,8] or [2,7]) => 2
        lines = [
            "4",
            "2 7 8 3",
            "4",
            "5 2 8 7"
        ]
        self.write_test_file(lines)
        task4()
        res = self.read_output_file()
        self.assertEqual(res, "2")

if __name__ == '__main__':
    unittest.main()
