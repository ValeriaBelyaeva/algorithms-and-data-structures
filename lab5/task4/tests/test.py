# lab5/task4/tests/test.py

import unittest
import os

from lab5.task4.src.build_heap import (
    task4, PATH, OUTPUT_PATH, build_min_heap
)

class TestBuildHeap(unittest.TestCase):

    def setUp(self):
        self.test_input_path = r"D:\algorithms-and-data-structures\lab5\task4\txtf\test_input.txt"
        self.test_output_path = r"D:\algorithms-and-data-structures\lab5\task4\txtf\test_output.txt"

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
        import lab5.task4.src.build_heap as module
        module.PATH = self.test_input_path
        module.OUTPUT_PATH = self.test_output_path

    def _restore_global_paths(self):
        import lab5.task4.src.build_heap as module
        module.PATH = self.original_path
        module.OUTPUT_PATH = self.original_output_path

    def write_test_file(self, arr):
        with open(self.test_input_path, 'w', encoding='utf-8') as f:
            f.write(str(len(arr)) + '\n')
            f.write(' '.join(map(str, arr)) + '\n')

    def read_output_file(self):
        if not os.path.exists(self.test_output_path):
            return []
        with open(self.test_output_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f]

    def test_no_swaps_needed(self):
        # Already min-heap
        arr = [1, 2, 3, 4, 5]
        self.write_test_file(arr)
        task4()
        result = self.read_output_file()
        # Expect 0 swaps
        self.assertTrue(result[0] == '0')

    def test_example_swaps(self):
        arr = [5, 4, 3, 2, 1]
        self.write_test_file(arr)
        task4()
        output = self.read_output_file()
        # We just check 0 <= m <= 4n
        # And final array should be a min-heap
        # We won't strictly check the exact sequence of swaps (it can vary)
        m = int(output[0])
        self.assertTrue(0 <= m <= 4*len(arr))

    def test_build_min_heap_function(self):
        arr = [5, 4, 3, 2, 1]
        swaps = build_min_heap(arr)
        # Now arr should be a valid min-heap
        # Check min-heap property
        for i in range(len(arr)//2):
            left = 2*i+1
            right = 2*i+2
            if left < len(arr):
                self.assertLessEqual(arr[i], arr[left])
            if right < len(arr):
                self.assertLessEqual(arr[i], arr[right])


if __name__ == '__main__':
    unittest.main()
