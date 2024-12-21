# D:\algorithms-and-data-structures\lab2\task3\tests\test.py

import unittest
import os
import random
import sys

sys.path.append(r"D:\algorithms-and-data-structures\lab2\task3\src")

from invertion_cnt import task, PATH, OUTPUT_PATH

class TestInversionCount(unittest.TestCase):

    def setUp(self):
        self.original_in = PATH
        self.original_out = OUTPUT_PATH
        self.test_in = r"D:\algorithms-and-data-structures\lab2\task3\txtf\test_input.txt"
        self.test_out = r"D:\algorithms-and-data-structures\lab2\task3\txtf\test_output.txt"

        import invertion_cnt
        invertion_cnt.PATH = self.test_in
        invertion_cnt.OUTPUT_PATH = self.test_out

    def tearDown(self):
        import invertion_cnt
        invertion_cnt.PATH = self.original_in
        invertion_cnt.OUTPUT_PATH = self.original_out

        if os.path.exists(self.test_in):
            os.remove(self.test_in)
        if os.path.exists(self.test_out):
            os.remove(self.test_out)

    def write_input_file(self, arr):
        with open(self.test_in, 'w', encoding='utf-8') as f:
            f.write(str(len(arr)) + "\n")
            if arr:
                f.write(" ".join(map(str, arr)) + "\n")

    def read_output_file(self):
        if not os.path.exists(self.test_out):
            return None
        with open(self.test_out, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]
            if not lines:
                return None
            return int(lines[-1])  # Читаем последнее значение как число инверсий

    def inversions_brute_force(self, arr):
        """
        Подсчёт инверсий грубой силой для проверки корректности
        """
        count = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] > arr[j]:
                    count += 1
        return count

    def test_empty_array(self):
        arr = []
        self.write_input_file(arr)
        task()
        result = self.read_output_file()
        self.assertEqual(result, 0)

    def test_single_element(self):
        arr = [42]
        self.write_input_file(arr)
        task()
        result = self.read_output_file()
        self.assertEqual(result, 0)

    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        self.write_input_file(arr)
        task()
        result = self.read_output_file()
        expected = self.inversions_brute_force(arr)
        self.assertEqual(result, expected)

    def test_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        self.write_input_file(arr)
        task()
        result = self.read_output_file()
        expected = self.inversions_brute_force(arr)
        self.assertEqual(result, expected)

    def test_random_arrays(self):
        for _ in range(5):
            arr = random.sample(range(-100, 100), 10)  # 10 distinct integers
            self.write_input_file(arr)
            task()
            result = self.read_output_file()
            expected = self.inversions_brute_force(arr)
            self.assertEqual(result, expected)

    def test_large_numbers(self):
        arr = [10**9, -10**9, 999999999, -999999999, 0]
        self.write_input_file(arr)
        task()
        result = self.read_output_file()
        expected = self.inversions_brute_force(arr)
        self.assertEqual(result, expected)

    def test_max_size(self):
        # Для демонстрации используем 2000 (не 100000)
        n = 2000
        arr = random.sample(range(-10**6, 10**6), n)
        self.write_input_file(arr)
        task()
        result = self.read_output_file()
        expected = self.inversions_brute_force(arr)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
