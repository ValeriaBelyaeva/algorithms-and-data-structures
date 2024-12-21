import unittest
import os

from lab3.task8.src.k_closest_points import (
    task8, k_closest_points, read_from_file, write_to_file,
    PATH, OUTPUT_PATH
)

class TestKClosestPoints(unittest.TestCase):

    def setUp(self):
        self.test_input_path = r"D:\algorithms-and-data-structures\lab3\task8\txtf\test_input.txt"
        self.test_output_path = r"D:\algorithms-and-data-structures\lab3\task8\txtf\test_output.txt"

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
        import lab3.task8.src.k_closest_points as kcp
        kcp.PATH = self.test_input_path
        kcp.OUTPUT_PATH = self.test_output_path

    def _restore_global_paths(self):
        import lab3.task8.src.k_closest_points as kcp
        kcp.PATH = self.original_input_path
        kcp.OUTPUT_PATH = self.original_output_path

    def write_test_file(self, n, K, points):
        with open(self.test_input_path, 'w', encoding='utf-8') as f:
            f.write(f"{n} {K}\n")
            for (x, y) in points:
                f.write(f"{x} {y}\n")

    def read_test_output(self):
        if not os.path.exists(self.test_output_path):
            return ""
        with open(self.test_output_path, 'r', encoding='utf-8') as f:
            return f.read().strip()

    def test_example1(self):
        n, K = 2, 1
        points = [(1, 3), (-2, 2)]
        self.write_test_file(n, K, points)
        task8()
        result = self.read_test_output()
        # Точка (-2,2) ближе, чем (1,3). Формат "[x,y]".
        # Возможный вывод: "[-2,2]"
        self.assertTrue("[-2,2]" in result)

    def test_example2(self):
        n, K = 3, 2
        points = [(3, 3), (5, -1), (-2, 4)]
        self.write_test_file(n, K, points)
        task8()
        result = self.read_test_output()
        # Проверим, что там действительно две точки, ближайшие к (0,0).
        # Могут быть "[-2,4]" и "[3,3]" (в любом порядке, но по условию сортировки - в порядке возрастания).
        self.assertIn("[-2,4]", result)
        self.assertIn("[3,3]", result)
        self.assertEqual(result.count('['), 2)

if __name__ == '__main__':
    unittest.main()
