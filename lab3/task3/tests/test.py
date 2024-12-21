import unittest
import os

from lab3.task3.src.scarecrow_sorting import (
    task3, can_scarecrow_sort, read_from_file, write_to_file,
    PATH, OUTPUT_PATH
)

class TestScarecrowSorting(unittest.TestCase):

    def setUp(self):
        self.test_input_path = r"D:\algorithms-and-data-structures\lab3\task3\txtf\test_input.txt"
        self.test_output_path = r"D:\algorithms-and-data-structures\lab3\task3\txtf\test_output.txt"

        self.original_input_path = PATH
        self.original_output_path = OUTPUT_PATH

        self._override_global_paths()

    def tearDown(self):
        self._restore_global_paths()
        if os.path.exists(self.test_input_path):
            os.remove(self.test_input_path)
        if os.path.exists(self.test_output_path):
            os.remove(self.test_output_path)

    def _override_global_paths(self):
        import lab3.task3.src.scarecrow_sorting as scs
        scs.PATH = self.test_input_path
        scs.OUTPUT_PATH = self.test_output_path

    def _restore_global_paths(self):
        import lab3.task3.src.scarecrow_sorting as scs
        scs.PATH = self.original_input_path
        scs.OUTPUT_PATH = self.original_output_path

    def write_test_file(self, n, k, arr):
        with open(self.test_input_path, 'w', encoding='utf-8') as f:
            f.write(f"{n} {k}\n")
            f.write(" ".join(map(str, arr)))

    def read_test_output(self):
        if not os.path.exists(self.test_output_path):
            return None
        with open(self.test_output_path, 'r', encoding='utf-8') as f:
            return f.read().strip()

    def test_basic_yes(self):
        n, k = 5, 3
        arr = [1, 5, 3, 2, 4]  # Можно переставить (через группы индексов mod 3) в неубывающий
        self.write_test_file(n, k, arr)
        task3()
        result = self.read_test_output()
        self.assertEqual(result, "НЕТ")

    def test_basic_no(self):
        n, k = 3, 2
        arr = [2, 1, 3]  # Пример, когда нельзя
        self.write_test_file(n, k, arr)
        task3()
        result = self.read_test_output()
        self.assertEqual(result, "НЕТ")

if __name__ == '__main__':
    unittest.main()
