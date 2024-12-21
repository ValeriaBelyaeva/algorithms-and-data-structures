# D:\algorithms-and-data-structures\lab2\task4\tests\test.py

import unittest
import os
import sys

sys.path.append(r"D:\algorithms-and-data-structures\lab2\task4\src")
from bin_faind import task, PATH, OUTPUT_PATH

class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.original_in = PATH
        self.original_out = OUTPUT_PATH
        self.test_in = r"D:\algorithms-and-data-structures\lab2\task4\txtf\test_input.txt"
        self.test_out = r"D:\algorithms-and-data-structures\lab2\task4\txtf\test_output.txt"

        import bin_faind
        bin_faind.PATH = self.test_in
        bin_faind.OUTPUT_PATH = self.test_out

    def tearDown(self):
        import bin_faind
        bin_faind.PATH = self.original_in
        bin_faind.OUTPUT_PATH = self.original_out

        if os.path.exists(self.test_in):
            os.remove(self.test_in)
        if os.path.exists(self.test_out):
            os.remove(self.test_out)

    def write_input_file(self, arr, queries):
        """
        arr: отсортированный массив
        queries: список чисел для поиска
        """
        with open(self.test_in, 'w', encoding='utf-8') as f:
            # Первая строка: n и n чисел массива
            f.write(str(len(arr)))
            if arr:
                f.write(" " + " ".join(map(str, arr)))
            f.write("\n")
            # Вторая строка: k и k чисел
            f.write(str(len(queries)))
            if queries:
                f.write(" " + " ".join(map(str, queries)))
            f.write("\n")

    def read_output_file(self):
        if not os.path.exists(self.test_out):
            return []
        with open(self.test_out, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]
        if not lines:
            return []
        # Предполагаем, что вся одна строка - это результат
        return list(map(int, lines[-1].split()))

    def test_empty_array(self):
        # n=0, k=3
        arr = []
        queries = [1,2,3]
        self.write_input_file(arr, queries)
        task()
        result = self.read_output_file()
        # Во всех случаях должно быть -1
        self.assertEqual(result, [-1]*len(queries))

    def test_single_element_found(self):
        # n=1, arr=[5], k=1, queries=[5]
        arr = [5]
        queries = [5]
        self.write_input_file(arr, queries)
        task()
        result = self.read_output_file()
        self.assertEqual(result, [0])  # элемент по индексу 0

    def test_single_element_not_found(self):
        # n=1, arr=[5], k=1, queries=[7]
        arr = [5]
        queries = [7]
        self.write_input_file(arr, queries)
        task()
        result = self.read_output_file()
        self.assertEqual(result, [-1])

    def test_multiple_search(self):
        # n=5, arr=[1,5,8,12,13], k=5, queries=[8,1,23,1,11]
        arr = [1, 5, 8, 12, 13]
        queries = [8, 1, 23, 1, 11]
        self.write_input_file(arr, queries)
        task()
        result = self.read_output_file()
        # a2=8 => index=2, a0=1 => index=0, 23 => -1, a0=1 => index=0, 11 => -1
        self.assertEqual(result, [2, 0, -1, 0, -1])

    def test_random_array(self):
        import random
        arr = sorted(random.sample(range(1, 200), 10))  # 10 distinct sorted
        queries = [arr[0], arr[-1], 999, 1, 50]
        # arr[0] => index 0
        # arr[-1] => index 9
        # 999 => -1
        # 1 => index=0 if 1 in arr else -1
        # 50 => check if in arr or -1
        self.write_input_file(arr, queries)
        task()
        result = self.read_output_file()
        # validate each query by manual binsearch
        expected = []
        for q in queries:
            try:
                idx = arr.index(q)
            except ValueError:
                idx = -1
            expected.append(idx)
        self.assertEqual(result, expected)

    def test_larger_array(self):
        import random
        arr = sorted(random.sample(range(1, 2000), 100))  # 100 distinct
        queries = random.sample(range(1, 2000), 20)       # 20 queries
        self.write_input_file(arr, queries)
        task()
        result = self.read_output_file()
        expected = []
        for q in queries:
            try:
                idx = arr.index(q)
            except ValueError:
                idx = -1
            expected.append(idx)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
