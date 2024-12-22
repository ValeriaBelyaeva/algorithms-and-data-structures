# lab7/task6/tests/test.py

import unittest
import os

from lab7.task6.src.lis import (
    task6, PATH, OUTPUT_PATH, lis
)

class TestLIS(unittest.TestCase):

    def setUp(self):
        self.test_input_path = r"D:\algorithms-and-data-structures\lab7\task6\txtf\test_input.txt"
        self.test_output_path = r"D:\algorithms-and-data-structures\lab7\task6\txtf\test_output.txt"

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
        import lab7.task6.src.lis as module
        module.PATH = self.test_input_path
        module.OUTPUT_PATH = self.test_output_path

    def _restore_global_paths(self):
        import lab7.task6.src.lis as module
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

    def test_small(self):
        lines = [
            "6",
            "3 2 9 5 5 2"
        ]
        # Одна из LIS: [3, 9], [3, 5], [2,5]... max length=2 or 3? Actually [2, 5, 5] is not strictly?
        # strictly increasing => 3 -> 9 is length=2, or 2->9->? or 2->5 -> length=2
        # let's see if 2->9->? There's a 5 after 9 which is not bigger. So likely length=2
        # We'll see what code does
        self.write_test_file(lines)
        task6()
        res = self.read_output_file()
        # first line is length, second line is subseq
        self.assertEqual(res[0], '2')

    def test_example_increasing(self):
        lines = [
            "4",
            "1 2 3 4"
        ]
        # obviously entire sequence is LIS => length=4, subsequence=1 2 3 4
        self.write_test_file(lines)
        task6()
        out = self.read_output_file()
        self.assertEqual(out[0], '4')
        self.assertEqual(out[1], '1 2 3 4')

    def test_single(self):
        lines = [
            "1",
            "100"
        ]
        self.write_test_file(lines)
        task6()
        out = self.read_output_file()
        self.assertEqual(out[0], '1')
        self.assertEqual(out[1], '100')


if __name__ == '__main__':
    unittest.main()
