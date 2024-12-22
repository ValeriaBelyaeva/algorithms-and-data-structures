# lab4/task9/tests/test.py

import unittest
import os

from lab4.task9.src.clinic_queue import (
    task9, PATH, OUTPUT_PATH
)

class TestClinicQueue(unittest.TestCase):

    def setUp(self):
        self.test_input_path = r"D:\algorithms-and-data-structures\lab4\task9\txtf\test_input.txt"
        self.test_output_path = r"D:\algorithms-and-data-structures\lab4\task9\txtf\test_output.txt"

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
        import lab4.task9.src.clinic_queue as module
        module.PATH = self.test_input_path
        module.OUTPUT_PATH = self.test_output_path

    def _restore_global_paths(self):
        import lab4.task9.src.clinic_queue as module
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

    def test_example1(self):
        # Пример из условия:
        # 7
        # + 1
        # + 2
        # + 3
        # + 4
        # -
        # -
        # -
        # Вывод: 1, 2, 3
        lines = [
            "7",
            "+ 1",
            "+ 2",
            "+ 3",
            "+ 4",
            "-",
            "-",
            "-"
        ]
        self.write_test_file(lines)
        task9()
        result = self.read_output_file()
        self.assertEqual(result, ["1", "2", "3"])

    def test_example2(self):
        # Пример из условия:
        # 10
        # + 1
        # + 2
        # * 3
        # + 4
        # * 5
        # -
        # -
        # -
        # -
        # -
        # Ожидается: 1, 3, 2, 5, 4
        lines = [
            "10",
            "+ 1",
            "+ 2",
            "* 3",
            "+ 4",
            "* 5",
            "-",
            "-",
            "-",
            "-",
            "-"
        ]
        self.write_test_file(lines)
        task9()
        result = self.read_output_file()
        self.assertEqual(result, ["1", "3", "2", "5", "4"])

    def test_mixed(self):
        lines = [
            "6",
            "+ 10",
            "* 20",
            "+ 30",
            "* 40",
            "-",
            "-"
        ]
        # Шаги:
        # +10 => очередь [10]
        # *20 => очередь [10, 20] (середина при длине=1 => 10 уже слева, вставка 20 влево/право?
        #        Но алгоритм: left=[10], добавляем в left -> left=[10,20], баланс -> right=[]
        #        Это эквивалент [10,20])
        # +30 => хотим в конец => right=[30],
        #        баланс => len(right)=1, len(left)=2 -> left-> [10], right-> [20,30]
        # *40 => вставить в середину => добавляем в left -> left=[10, 40], right=[20,30]
        # - => извлекаем left[0]=10 => [40], right=[20,30], вывод 10
        # баланс => len(left)=1, len(right)=2 => left.append(right.popleft()) => left=[40,20], right=[30]
        # - => извлекаем left[0]=40 => left=[20], right=[30], вывод 40
        # Итог вывод: 10, 40
        self.write_test_file(lines)
        task9()
        result = self.read_output_file()
        self.assertEqual(result, ["10", "40"])


if __name__ == '__main__':
    unittest.main()
