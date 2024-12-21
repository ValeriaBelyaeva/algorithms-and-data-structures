import unittest
import os

from lab3.task2.src.anti_quick_sort import (
    task2, generate_anti_quick_sort, read_from_file, write_to_file,
    PATH, OUTPUT_PATH
)

class TestAntiQuickSort(unittest.TestCase):

    def setUp(self):
        self.test_input_path = r"D:\algorithms-and-data-structures\lab3\task2\txtf\test_input.txt"
        self.test_output_path = r"D:\algorithms-and-data-structures\lab3\task2\txtf\test_output.txt"

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
        import lab3.task2.src.anti_quick_sort as aqs
        aqs.PATH = self.test_input_path
        aqs.OUTPUT_PATH = self.test_output_path

    def _restore_global_paths(self):
        import lab3.task2.src.anti_quick_sort as aqs
        aqs.PATH = self.original_input_path
        aqs.OUTPUT_PATH = self.original_output_path

    def write_test_file(self, n):
        with open(self.test_input_path, 'w', encoding='utf-8') as f:
            f.write(str(n))

    def read_test_output(self):
        if not os.path.exists(self.test_output_path):
            return []
        with open(self.test_output_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if content:
                return list(map(int, content.split()))
            return []

    def test_n_1(self):
        self.write_test_file(1)
        task2()
        out_data = self.read_test_output()
        self.assertEqual(out_data, [1])

    def test_n_5(self):
        self.write_test_file(5)
        task2()
        out_data = self.read_test_output()
        self.assertEqual(len(out_data), 5)
        self.assertEqual(set(out_data), {1, 2, 3, 4, 5})

    def test_n_10(self):
        self.write_test_file(10)
        task2()
        out_data = self.read_test_output()
        self.assertEqual(len(out_data), 10)
        self.assertEqual(set(out_data), set(range(1, 11)))

if __name__ == '__main__':
    unittest.main()
