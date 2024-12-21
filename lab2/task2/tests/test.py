# D:\algorithms-and-data-structures\lab2\task2\tests\test.py

import unittest
import os
import sys
import random

sys.path.append(r"D:\algorithms-and-data-structures\lab2\task2\src")
from merge_sort_plus import task, PATH, OUTPUT_PATH

class TestMergeSortPlus(unittest.TestCase):
    def setUp(self):
        self.original_path = PATH
        self.original_out = OUTPUT_PATH
        self.test_in = r"D:\algorithms-and-data-structures\lab2\task2\txtf\test_input.txt"
        self.test_out = r"D:\algorithms-and-data-structures\lab2\task2\txtf\test_output.txt"

        # Переопределяем пути
        import merge_sort_plus
        merge_sort_plus.PATH = self.test_in
        merge_sort_plus.OUTPUT_PATH = self.test_out

    def tearDown(self):
        import merge_sort_plus
        merge_sort_plus.PATH = self.original_path
        merge_sort_plus.OUTPUT_PATH = self.original_out

        if os.path.exists(self.test_in):
            os.remove(self.test_in)
        if os.path.exists(self.test_out):
            os.remove(self.test_out)

    def write_input_file(self, arr):
        n = len(arr)
        with open(self.test_in, 'w', encoding='utf-8') as f:
            f.write(str(n) + '\n')
            if n > 0:
                f.write(' '.join(map(str, arr)) + '\n')

    def read_output_file(self):
        if not os.path.exists(self.test_out):
            return [], []
        with open(self.test_out, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]
        if not lines:
            return [], []
        merges = []
        # Предпоследние строки - шаги слияния, последняя строка - итоговый массив
        # Но может быть только одна строка (если n<=1)
        if len(lines) == 1:
            # либо это пустая или итоговый массив
            try:
                arr = list(map(int, lines[0].split()))
                return [], arr
            except ValueError:
                return [], []
        # Всё, кроме последней, считаем слияниями
        for line in lines[:-1]:
            parts = line.split()
            if len(parts) == 4:
                If, Il, Vf, Vl = map(int, parts)
                merges.append((If, Il, Vf, Vl))
        # Последняя строка - отсортированный массив
        sorted_arr = list(map(int, lines[-1].split()))
        return merges, sorted_arr

    def test_empty_array(self):
        arr = []
        self.write_input_file(arr)
        task()
        merges, sorted_arr = self.read_output_file()
        self.assertEqual(merges, [])
        self.assertEqual(sorted_arr, [])

    def test_single_element(self):
        arr = [42]
        self.write_input_file(arr)
        task()
        merges, sorted_arr = self.read_output_file()
        self.assertEqual(merges, [])
        self.assertEqual(sorted_arr, [42])

    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        self.write_input_file(arr)
        task()
        merges, sorted_arr = self.read_output_file()
        self.assertEqual(sorted_arr, sorted(arr))
        # Проверим, что хотя бы одно слияние записано, кроме случая n<=1
        self.assertTrue(len(merges) > 0)

    def test_reverse_array(self):
        arr = [5, 4, 3, 2, 1]
        self.write_input_file(arr)
        task()
        merges, sorted_arr = self.read_output_file()
        self.assertEqual(sorted_arr, sorted(arr))
        self.assertTrue(len(merges) > 0)

    def test_random_array(self):
        arr = random.sample(range(-100, 100), 10)
        expected = sorted(arr)
        self.write_input_file(arr)
        task()
        merges, sorted_arr = self.read_output_file()
        self.assertEqual(sorted_arr, expected)

    def test_duplicates(self):
        arr = [5, 3, 3, 2, 2, 1]
        expected = sorted(arr)
        self.write_input_file(arr)
        task()
        merges, sorted_arr = self.read_output_file()
        self.assertEqual(sorted_arr, expected)

    def test_large_numbers(self):
        arr = [10**9, -10**9, 999999999, -999999999, 0]
        expected = sorted(arr)
        self.write_input_file(arr)
        task()
        merges, sorted_arr = self.read_output_file()
        self.assertEqual(sorted_arr, expected)

    def test_all_negative(self):
        arr = [-5, -1, -100, -50, -9999]
        expected = sorted(arr)
        self.write_input_file(arr)
        task()
        merges, sorted_arr = self.read_output_file()
        self.assertEqual(sorted_arr, expected)

    def test_almost_sorted(self):
        arr = [1, 2, 3, 10, 5, 6, 7, 4]
        expected = sorted(arr)
        self.write_input_file(arr)
        task()
        merges, sorted_arr = self.read_output_file()
        self.assertEqual(sorted_arr, expected)

    def test_large_array(self):
        n = 2000
        arr = random.sample(range(-10**6, 10**6), n)
        expected = sorted(arr)
        self.write_input_file(arr)
        task()
        merges, sorted_arr = self.read_output_file()
        self.assertEqual(sorted_arr, expected)

if __name__ == '__main__':
    unittest.main()
