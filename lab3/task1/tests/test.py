# test_merge_sort.py

import unittest
import random
import os

# Импортируем всё необходимое из файла merge_sort
from lab2.task1.src.merge_sort import (
    merge_sort, read_from_file, write_to_file,
    task1, PATH, OUTPUT_PATH
)

class TestMergeSort(unittest.TestCase):

    def setUp(self):
        """
        Этот метод вызывается перед каждым тестом.
        Создаём временные пути для входного и выходного файлов,
        чтобы не перезаписывать реальные input.txt и output.txt.
        """
        self.test_input_path = r"D:\algorithms-and-data-structures\lab2\task1\txtf\test_input.txt"
        self.test_output_path = r"D:\algorithms-and-data-structures\lab2\task1\txtf\test_output.txt"

        # Сохраняем оригинальные пути
        self.original_input_path = PATH
        self.original_output_path = OUTPUT_PATH

        # Меняем глобальные пути на тестовые
        self._override_global_paths()

    def tearDown(self):
        """
        Этот метод вызывается после каждого теста.
        Удаляем временные файлы, если они существуют.
        Возвращаем глобальные переменные на место.
        """
        self._restore_global_paths()

        if os.path.exists(self.test_input_path):
            os.remove(self.test_input_path)
        if os.path.exists(self.test_output_path):
            os.remove(self.test_output_path)

    def _override_global_paths(self):
        """
        Вспомогательный метод, который позволяет временно
        переопределить глобальные переменные PATH и OUTPUT_PATH
        для тестов.
        """
        import lab2.task1.src.merge_sort as mst
        mst.PATH = self.test_input_path
        mst.OUTPUT_PATH = self.test_output_path

    def _restore_global_paths(self):
        """
        Возвращает PATH и OUTPUT_PATH к изначальным значениям.
        """
        import lab2.task1.src.merge_sort as mst
        mst.PATH = self.original_input_path
        mst.OUTPUT_PATH = self.original_output_path

    def write_test_file(self, arr):
        """
        Записывает тестовый массив в тестовый входной файл.
        """
        with open(self.test_input_path, 'w', encoding='utf-8') as file:
            file.write(f"{len(arr)}\n")
            file.write(' '.join(map(str, arr)))

    def read_test_output(self):
        """
        Считывает данные из тестового выходного файла.
        Возвращает список отсортированных чисел.
        """
        if not os.path.exists(self.test_output_path):
            return []
        with open(self.test_output_path, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            if content:
                return list(map(int, content.split()))
            else:
                return []

    def test_empty_array(self):
        """
        Тестирование пустого массива.
        """
        arr = []
        self.write_test_file(arr)
        task1()
        result = self.read_test_output()
        self.assertEqual(result, arr)

    def test_single_element(self):
        """
        Тестирование массива из одного элемента.
        """
        arr = [42]
        self.write_test_file(arr)
        task1()
        result = self.read_test_output()
        self.assertEqual(result, arr)

    def test_sorted_array(self):
        """
        Тест: массив уже отсортирован (наилучший случай).
        """
        arr = list(range(1, 101))  # 1..100
        self.write_test_file(arr)
        task1()
        result = self.read_test_output()
        self.assertEqual(result, arr)

    def test_reverse_sorted_array(self):
        """
        Тест: массив, отсортированный в обратном порядке (наихудший случай).
        """
        arr = list(range(100, 0, -1))  # 100..1
        expected = list(range(1, 101))
        self.write_test_file(arr)
        task1()
        result = self.read_test_output()
        self.assertEqual(result, expected)

    def test_random_array(self):
        """
        Средний случай: массив случайных уникальных элементов (размер до 20000).
        """
        arr = random.sample(range(-10**6, 10**6), 2000)  # Для демо используем 2000
        expected = sorted(arr)
        self.write_test_file(arr)
        task1()
        result = self.read_test_output()
        self.assertEqual(result, expected)

    def test_duplicates(self):
        """
        Проверка массива с дубликатами (по условию задачи все числа уникальны,
        но тестируем на устойчивость).
        """
        arr = [5, 3, 3, 2, 2, 1]
        expected = sorted(arr)
        self.write_test_file(arr)
        task1()
        result = self.read_test_output()
        self.assertEqual(result, expected)

    def test_large_numbers(self):
        """
        Проверка сортировки чисел с большими абсолютными значениями.
        """
        arr = [10**9, -10**9, 999999999, -999999999, 0]
        expected = sorted(arr)
        self.write_test_file(arr)
        task1()
        result = self.read_test_output()
        self.assertEqual(result, expected)

    def test_all_negative_array(self):
        """
        Дополнительный тест: массив, состоящий только из отрицательных чисел.
        """
        arr = [-5, -1, -100, -50, -9999]
        expected = sorted(arr)
        self.write_test_file(arr)
        task1()
        result = self.read_test_output()
        self.assertEqual(result, expected)

    def test_almost_sorted_array(self):
        """
        Дополнительный тест: «почти» отсортированный массив, где несколько
        элементов не на своих местах.
        """
        arr = [1, 2, 3, 10, 5, 6, 7, 4, 9, 8]
        expected = sorted(arr)
        self.write_test_file(arr)
        task1()
        result = self.read_test_output()
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
