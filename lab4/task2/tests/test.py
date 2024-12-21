# lab4/task2/tests/test.py

import unittest
import os

from lab4.task2.src.queue import (
    task2, PATH, OUTPUT_PATH
)

class TestQueue(unittest.TestCase):

    def setUp(self):
        """
        Перед каждым тестом переопределяем пути к input.txt и output.txt.
        """
        self.test_input_path = r"D:\algorithms-and-data-structures\lab4\task2\txtf\test_input.txt"
        self.test_output_path = r"D:\algorithms-and-data-structures\lab4\task2\txtf\test_output.txt"

        # Сохраняем исходные пути
        self.original_path = PATH
        self.original_output_path = OUTPUT_PATH

        # Переопределяем пути
        self._override_global_paths()

    def tearDown(self):
        """
        После каждого теста восстанавливаем пути и удаляем тестовые файлы.
        """
        self._restore_global_paths()

        if os.path.exists(self.test_input_path):
            os.remove(self.test_input_path)
        if os.path.exists(self.test_output_path):
            os.remove(self.test_output_path)

    def _override_global_paths(self):
        import lab4.task2.src.queue as module
        module.PATH = self.test_input_path
        module.OUTPUT_PATH = self.test_output_path

    def _restore_global_paths(self):
        import lab4.task2.src.queue as module
        module.PATH = self.original_path
        module.OUTPUT_PATH = self.original_output_path

    def write_test_file(self, lines):
        """
        Записывает тестовые команды в тестовый входной файл.
        lines — список строк (включая первую строку M).
        """
        with open(self.test_input_path, 'w', encoding='utf-8') as f:
            for line in lines:
                f.write(line + '\n')

    def read_output_file(self):
        """
        Считывает результат из тестового выходного файла.
        Возвращает список строк.
        """
        if not os.path.exists(self.test_output_path):
            return []
        with open(self.test_output_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f]

    def test_simple(self):
        """
        Простой тест с несколькими операциями.
        """
        lines = [
            "5",
            "+ 10",
            "+ 20",
            "-",
            "+ 30",
            "-"
        ]
        self.write_test_file(lines)
        task2()
        result = self.read_output_file()
        # Первое извлечение: 10
        # Второе извлечение: 20
        self.assertEqual(result, ["10", "20"])

    def test_only_pushes(self):
        """
        Проверка: когда нет извлечений, файл выхода должен быть пустым.
        """
        lines = [
            "3",
            "+ 1",
            "+ 2",
            "+ 3"
        ]
        self.write_test_file(lines)
        task2()
        result = self.read_output_file()
        self.assertEqual(result, [])

    def test_multiple_pops(self):
        """
        Проверка множественных извлечений.
        """
        lines = [
            "4",
            "+ 1",
            "+ 2",
            "-",
            "-"
        ]
        self.write_test_file(lines)
        task2()
        result = self.read_output_file()
        self.assertEqual(result, ["1", "2"])

    def test_mixed_commands(self):
        """
        Смешанные операции.
        """
        lines = [
            "6",
            "+ 10",
            "+ 100",
            "-",
            "+ 200",
            "-",
            "-"
        ]
        self.write_test_file(lines)
        task2()
        result = self.read_output_file()
        # Первое '-' -> 10
        # Второе '-' -> 100
        # Третье '-' -> 200
        self.assertEqual(result, ["10", "100", "200"])


if __name__ == '__main__':
    unittest.main()
