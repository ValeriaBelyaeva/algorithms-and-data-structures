# D:\algorithms-and-data-structures\lab2\task5\tests\test.py

import unittest
import os
import sys
import random

sys.path.append(r"D:\algorithms-and-data-structures\lab2\task5\src")
from representative_of_the_majority import task, PATH, OUTPUT_PATH

class TestRepresentativeOfTheMajority(unittest.TestCase):
    def setUp(self):
        self.test_in = r"D:\algorithms-and-data-structures\lab2\task5\txtf\test_input.txt"
        self.test_out = r"D:\algorithms-and-data-structures\lab2\task5\txtf\test_output.txt"
        self.original_in = PATH
        self.original_out = OUTPUT_PATH

        import representative_of_the_majority
        representative_of_the_majority.PATH = self.test_in
        representative_of_the_majority.OUTPUT_PATH = self.test_out

    def tearDown(self):
        import representative_of_the_majority
        representative_of_the_majority.PATH = self.original_in
        representative_of_the_majority.OUTPUT_PATH = self.original_out

        if os.path.exists(self.test_in):
            os.remove(self.test_in)
        if os.path.exists(self.test_out):
            os.remove(self.test_out)

    def write_input_file(self, arr):
        with open(self.test_in, 'w', encoding='utf-8') as f:
            f.write(str(len(arr)) + "\n")
            if len(arr) > 0:
                f.write(" ".join(map(str, arr)) + "\n")

    def read_output_file(self):
        if not os.path.exists(self.test_out):
            return ""
        with open(self.test_out, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]
        return lines[-1] if lines else ""

    def test_empty_array(self):
        # n=0 => нет мажоритарного элемента
        arr = []
        self.write_input_file(arr)
        task()
        result = self.read_output_file()
        self.assertEqual(result, "0")

    def test_single_element(self):
        # n=1 => элемент является мажоритарным
        arr = [42]
        self.write_input_file(arr)
        task()
        result = self.read_output_file()
        self.assertEqual(result, "1")

    def test_no_majority(self):
        # n=5 => [1,2,3,2,1] => каждый по два раза макс, больше 5//2=2 никто
        arr = [1, 2, 3, 2, 1]
        self.write_input_file(arr)
        task()
        result = self.read_output_file()
        self.assertEqual(result, "0")

    def test_majority_simple(self):
        # n=5 => [2,3,9,2,2] => "2" встречается 3 раза (>5/2=2)
        arr = [2, 3, 9, 2, 2]
        self.write_input_file(arr)
        task()
        result = self.read_output_file()
        self.assertEqual(result, "1")

    def test_all_same(self):
        # n=5 => [7,7,7,7,7], очевидно мажоритарный
        arr = [7, 7, 7, 7, 7]
        self.write_input_file(arr)
        task()
        result = self.read_output_file()
        self.assertEqual(result, "1")

    def test_large(self):
        # Для проверки производительности
        n = 2000
        arr = [random.randint(1, 100) for _ in range(n)]
        # Принудительно сделаем часть элементов одним и тем же числом,
        # чтобы получить мажоритарный
        majority_value = 999
        for i in range(n//2 + 1):
            arr[i] = majority_value
        random.shuffle(arr)
        self.write_input_file(arr)
        task()
        result = self.read_output_file()
        self.assertEqual(result, "1")

    def test_large_no_majority(self):
        # Случайный массив, в котором нет элемента более n/2
        n = 2000
        arr = [random.randint(1, 2000) for _ in range(n)]
        # Убедимся, что не будет явно мажоритарного (заставим сделать уникальным)
        arr = list(set(arr))  # уникальные
        # если получилось меньше 2000, дополнить недостающими (уникальными) числами
        # хотя бы, чтобы гарантированно нет majority
        while len(arr) < 2000:
            val = random.randint(1, 10**6)
            if val not in arr:
                arr.append(val)
        random.shuffle(arr)
        self.write_input_file(arr[:2000])  # берем ровно 2000
        task()
        result = self.read_output_file()
        # Почти невозможно случайно получить мажоритарный => проверяем 0
        self.assertEqual(result, "0")

if __name__ == '__main__':
    unittest.main()
