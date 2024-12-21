import unittest
import os

from lab3.task5.src.hirsch_index import (
    task5, hirsch_index, read_from_file, write_to_file,
    PATH, OUTPUT_PATH
)

class TestHirschIndex(unittest.TestCase):

    def setUp(self):
        self.test_input_path = r"D:\algorithms-and-data-structures\lab3\task5\txtf\test_input.txt"
        self.test_output_path = r"D:\algorithms-and-data-structures\lab3\task5\txtf\test_output.txt"

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
        import lab3.task5.src.hirsch_index as hi
        hi.PATH = self.test_input_path
        hi.OUTPUT_PATH = self.test_output_path

    def _restore_global_paths(self):
        import lab3.task5.src.hirsch_index as hi
        hi.PATH = self.original_input_path
        hi.OUTPUT_PATH = self.original_output_path

    def write_test_file(self, data):
        with open(self.test_input_path, 'w', encoding='utf-8') as f:
            f.write(data)

    def read_test_output(self):
        if not os.path.exists(self.test_output_path):
            return None
        with open(self.test_output_path, 'r', encoding='utf-8') as f:
            return f.read().strip()

    def test_example1(self):
        data = "3,0,6,1,5"
        self.write_test_file(data)
        task5()
        result = self.read_test_output()
        self.assertEqual(result, "3")

    def test_example2(self):
        data = "1,3,1"
        self.write_test_file(data)
        task5()
        result = self.read_test_output()
        self.assertEqual(result, "1")

    def test_large_values(self):
        data = "10,10,10,10,10"
        self.write_test_file(data)
        task5()
        result = self.read_test_output()
        # h-индекс здесь 5
        self.assertEqual(result, "5")

if __name__ == '__main__':
    unittest.main()
