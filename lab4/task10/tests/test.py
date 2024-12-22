# lab4/task10/tests/test.py

import unittest
import os

from lab4.task10.src.bakery_queue import (
    task10, PATH, OUTPUT_PATH, to_minutes, to_hm
)

class TestBakeryQueue(unittest.TestCase):

    def setUp(self):
        self.test_input_path = r"D:\algorithms-and-data-structures\lab4\task10\txtf\test_input.txt"
        self.test_output_path = r"D:\algorithms-and-data-structures\lab4\task10\txtf\test_output.txt"

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
        import lab4.task10.src.bakery_queue as module
        module.PATH = self.test_input_path
        module.OUTPUT_PATH = self.test_output_path

    def _restore_global_paths(self):
        import lab4.task10.src.bakery_queue as module
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

    def test_to_minutes(self):
        self.assertEqual(to_minutes(0, 0), 0)
        self.assertEqual(to_minutes(1, 0), 60)
        self.assertEqual(to_minutes(10, 30), 630)

    def test_to_hm(self):
        self.assertEqual(to_hm(0), (0, 0))
        self.assertEqual(to_hm(60), (1, 0))
        self.assertEqual(to_hm(63), (1, 3))

    def test_example1(self):
        # Пример из условия (упрощенный):
        # 3 покупателей:
        # (10:0, imp=0), (10:1, imp=1), (10:2, imp=1)
        # Предположим:
        #   1й приходит в 10:00, очередь пуста, сразу обслуживается 10:00..10:10
        #   2й приходит в 10:01, в очереди 1 человек (обслуживается), imp=1 -> ок остается
        #       обслужится после первого: 10:10..10:20
        #   3й приходит в 10:02, в очереди 2 (обслуживающийся + 2й), imp=1 -> 2 > 1 => уходит
        # Результаты:
        #   1й уходит в 10:10
        #   2й уходит в 10:20
        #   3й уходит в 10:02 (т.к. ушел сразу)
        lines = [
            "3",
            "10 0 0",
            "10 1 1",
            "10 2 1"
        ]
        self.write_test_file(lines)
        task10()
        result = self.read_output_file()
        # Ожидаем:
        # 10 10
        # 10 20
        # 10 2
        self.assertEqual(result, ["10 10", "10 20", "10 2"])

    def test_example2(self):
        # Допустим 2 покупателя:
        # 1) 10:00, imp=2 => приходит, пусто -> 10:00..10:10
        # 2) 10:10, imp=0 => приходит ровно в 10:10, 1й только что ушел, значит продавец свободен
        #    => обслуживается 10:10..10:20
        lines = [
            "2",
            "10 0 2",
            "10 10 0"
        ]
        self.write_test_file(lines)
        task10()
        result = self.read_output_file()
        # 1) уходит в 10:10
        # 2) уходит в 10:20
        self.assertEqual(result, ["10 10", "10 20"])

    def test_leave_immediately(self):
        # 1) 9:00, imp=0 => пусто, обслуживается 9:00..9:10
        # 2) 9:05, imp=0 => приходит, в очереди 1 человек (обслуживается), 1 > 0 => уходит в 9:05
        # 3) 9:10, imp=0 => приходит, продавец только освободился в 9:10 => обслуживается 9:10..9:20
        lines = [
            "3",
            "9 0 0",
            "9 5 0",
            "9 10 0"
        ]
        self.write_test_file(lines)
        task10()
        result = self.read_output_file()
        # 1) 9:10
        # 2) 9:5
        # 3) 9:20
        self.assertEqual(result, ["9 10", "9 5", "9 20"])


if __name__ == '__main__':
    unittest.main()
