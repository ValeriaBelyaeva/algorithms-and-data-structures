# lab5/task1/tests/test.py

import unittest
import os

from lab5.task1.src.is_heap import (
    task1, PATH, OUTPUT_PATH, check_if_min_heap
)

class TestIsHeap(unittest.TestCase):

    def setUp(self):
        self.test_input_path = r"D:\algorithms-and-data-structures\lab5\task1\txtf\test_input.txt"
        self.test_output_path = r"D:\algorithms-and-data-structures\lab5\task1\txtf\test_output.txt"

        # Сохраняем оригинальные пути
        self.original_path = PATH
        self.original_output_path = OUTPUT_PATH

        # Переопределяем пути
        self._override_global_paths()

    def tearDown(self):
        self._restore_global_paths()
        if os.path.exists(self.test_input_path):
            os.remove(self.test_input_path)
        if os.path.exists(self.test_output_path):
            os.remove(self.test_output_path)

    def _override_global_paths(self):
        import lab5.task1.src.is_heap as module
        module.PATH = self.test_input_path
        module.OUTPUT_PATH = self.test_output_path

    def _restore_global_paths(self):
        import lab5.task1.src.is_heap as module
        module.PATH = self.original_path
        module.OUTPUT_PATH = self.original_output_path

    def write_test_file(self, n, arr):
        """
        Записывает n и массив arr в test_input.txt.
        """
        with open(self.test_input_path, 'w', encoding='utf-8') as f:
            f.write(str(n) + '\n')
            f.write(' '.join(map(str, arr)) + '\n')

    def read_output_file(self):
        if not os.path.exists(self.test_output_path):
            return ""
        with open(self.test_output_path, 'r', encoding='utf-8') as f:
            return f.read().strip()

    def test_single_element(self):
        # n=1 => всегда YES
        self.write_test_file(1, [42])
        task1()
        output = self.read_output_file()
        self.assertEqual(output, "YES")

    def test_valid_heap(self):
        # [2, 3, 4, 5, 6] => min-heap check
        arr = [2, 3, 4, 5, 6]
        self.write_test_file(len(arr), arr)
        task1()
        output = self.read_output_file()
        self.assertEqual(output, "YES")

    def test_invalid_heap(self):
        # [9, 8, 7, 6, 5] => not a min-heap
        arr = [9, 8, 7, 6, 5]
        self.write_test_file(len(arr), arr)
        task1()
        output = self.read_output_file()
        self.assertEqual(output, "NO")

    def test_check_if_min_heap_function(self):
        self.assertTrue(check_if_min_heap([1]))  # single element
        self.assertTrue(check_if_min_heap([1, 2, 3]))
        self.assertFalse(check_if_min_heap([10, 5, 9]))

if __name__ == '__main__':
    unittest.main()
