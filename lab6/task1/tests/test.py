# lab5/task1/tests/test.py

import unittest
import os

from lab5.task1.src.set import task1, PATH, OUTPUT_PATH

class TestSet(unittest.TestCase):

    def setUp(self):
        """
        Переопределяем пути к input.txt и output.txt на тестовые
        """
        self.test_input_path = r"D:\algorithms-and-data-structures\lab5\task1\txtf\test_input.txt"
        self.test_output_path = r"D:\algorithms-and-data-structures\lab5\task1\txtf\test_output.txt"

        self.original_path = PATH
        self.original_output_path = OUTPUT_PATH

        self._override_global_paths()

    def tearDown(self):
        """
        Восстанавливаем пути и удаляем тестовые файлы
        """
        self._restore_global_paths()

        if os.path.exists(self.test_input_path):
            os.remove(self.test_input_path)
        if os.path.exists(self.test_output_path):
            os.remove(self.test_output_path)

    def _override_global_paths(self):
        import lab5.task1.src.set as module
        module.PATH = self.test_input_path
        module.OUTPUT_PATH = self.test_output_path

    def _restore_global_paths(self):
        import lab5.task1.src.set as module
        module.PATH = self.original_path
        module.OUTPUT_PATH = self.original_output_path

    def write_test_file(self, lines):
        with open(self.test_input_path, 'w', encoding='utf-8') as f:
            for line in lines:
                f.write(line + '\n')

    def read_output_file(self):
        if not os.path.exists(self.test_output_path):
            return []
        with open(self.test_output_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f]

    def test_example(self):
        lines = [
            "8",
            "A 2",
            "? 2",
            "? 4",
            "A 2",
            "D 2",
            "? 2",
            "A 5",
            "? 5"
        ]
        # Пошагово:
        # A 2 -> {2}
        # ? 2 -> Y
        # ? 4 -> N
        # A 2 -> {2} (без изменений)
        # D 2 -> {}
        # ? 2 -> N
        # A 5 -> {5}
        # ? 5 -> Y
        self.write_test_file(lines)
        task1()
        result = self.read_output_file()
        self.assertEqual(result, ["Y", "N", "N", "Y"])

    def test_add_and_query(self):
        lines = [
            "5",
            "A 10",
            "A 10",
            "? 10",
            "D 10",
            "? 10"
        ]
        # {10}, ? 10 -> Y, D 10 -> {}, ? 10 -> N
        self.write_test_file(lines)
        task1()
        result = self.read_output_file()
        self.assertEqual(result, ["Y", "N"])

    def test_large_values(self):
        lines = [
            "4",
            "A 1000000000000000000",
            "? 1000000000000000000",
            "D 999999999999999999",
            "? 999999999999999999"
        ]
        # добавляем 10^18, спрашиваем 10^18 -> Y
        # удаляем 999999999999999999 (нет в множестве), ? 999999999999999999 -> N
        self.write_test_file(lines)
        task1()
        result = self.read_output_file()
        self.assertEqual(result, ["Y", "N"])

if __name__ == '__main__':
    unittest.main()
