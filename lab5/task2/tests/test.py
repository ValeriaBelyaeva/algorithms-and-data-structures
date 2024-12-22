# lab5/task2/tests/test.py

import unittest
import os

from lab5.task2.src.tree_height import (
    task2, PATH, OUTPUT_PATH, compute_height
)

class TestTreeHeight(unittest.TestCase):

    def setUp(self):
        self.test_input_path = r"D:\algorithms-and-data-structures\lab5\task2\txtf\test_input.txt"
        self.test_output_path = r"D:\algorithms-and-data-structures\lab5\task2\txtf\test_output.txt"

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
        import lab5.task2.src.tree_height as module
        module.PATH = self.test_input_path
        module.OUTPUT_PATH = self.test_output_path

    def _restore_global_paths(self):
        import lab5.task2.src.tree_height as module
        module.PATH = self.original_path
        module.OUTPUT_PATH = self.original_output_path

    def write_test_file(self, n, parents):
        with open(self.test_input_path, 'w', encoding='utf-8') as f:
            f.write(str(n) + '\n')
            f.write(' '.join(map(str, parents)) + '\n')

    def read_output_file(self):
        if not os.path.exists(self.test_output_path):
            return ""
        with open(self.test_output_path, 'r', encoding='utf-8') as f:
            return f.read().strip()

    def test_single_node(self):
        # Единственный узел, он же корень => высота = 1
        n = 1
        parents = [-1]
        self.write_test_file(n, parents)
        task2()
        result = int(self.read_output_file())
        self.assertEqual(result, 1)

    def test_example1(self):
        # n=5, parents=[4, -1, 4, 1, 1]
        # root=1, height=3
        n = 5
        p = [4, -1, 4, 1, 1]
        self.write_test_file(n, p)
        task2()
        result = int(self.read_output_file())
        self.assertEqual(result, 3)

    def test_example2(self):
        # n=5, parents=[4, -1, 0, 4, 0, 3] - but problem says n=5 only
        # Let's replicate example: n=5, parents=[4, -1, 0, 4, 0]
        # root=1 => node1 is root
        # Actually let's do a simpler example
        # We'll do n=5, parents=[-1, 0, 0, 1, 3]
        # root=0 => children(0)=[1,2], children(1)=[3], children(3)=[4]
        # height=4
        n = 5
        p = [-1, 0, 0, 1, 3]
        self.write_test_file(n, p)
        task2()
        result = int(self.read_output_file())
        self.assertEqual(result, 4)

    def test_compute_height_direct(self):
        # Test the function alone
        self.assertEqual(compute_height(1, [-1]), 1)
        # Chain: 0->1->2->3 => parents=[-1, 0, 1, 2], height=4
        self.assertEqual(compute_height(4, [-1, 0, 1, 2]), 4)

if __name__ == '__main__':
    unittest.main()
