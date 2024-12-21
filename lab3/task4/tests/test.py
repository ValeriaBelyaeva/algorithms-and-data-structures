import unittest
import os

from lab3.task4.src.points_and_segments import (
    task4, points_and_segments, read_from_file, write_to_file,
    PATH, OUTPUT_PATH
)

class TestPointsAndSegments(unittest.TestCase):

    def setUp(self):
        self.test_input_path = r"D:\algorithms-and-data-structures\lab3\task4\txtf\test_input.txt"
        self.test_output_path = r"D:\algorithms-and-data-structures\lab3\task4\txtf\test_output.txt"

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
        import lab3.task4.src.points_and_segments as pas
        pas.PATH = self.test_input_path
        pas.OUTPUT_PATH = self.test_output_path

    def _restore_global_paths(self):
        import lab3.task4.src.points_and_segments as pas
        pas.PATH = self.original_input_path
        pas.OUTPUT_PATH = self.original_output_path

    def write_test_file(self, s, p, intervals, points):
        with open(self.test_input_path, 'w', encoding='utf-8') as f:
            f.write(f"{s} {p}\n")
            for a, b in intervals:
                f.write(f"{a} {b}\n")
            f.write(' '.join(map(str, points)))

    def read_test_output(self):
        if not os.path.exists(self.test_output_path):
            return []
        with open(self.test_output_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if content:
                return list(map(int, content.split()))
            return []

    def test_example(self):
        s = 2
        p = 3
        intervals = [(0, 5), (7, 10)]
        points = [1, 6, 11]
        self.write_test_file(s, p, intervals, points)
        task4()
        out_data = self.read_test_output()
        self.assertEqual(out_data, [1, 0, 0])

    def test_all_contained(self):
        s = 1
        p = 3
        intervals = [(0, 10)]
        points = [0, 5, 10]
        self.write_test_file(s, p, intervals, points)
        task4()
        out_data = self.read_test_output()
        self.assertEqual(out_data, [1, 1, 1])

if __name__ == '__main__':
    unittest.main()
