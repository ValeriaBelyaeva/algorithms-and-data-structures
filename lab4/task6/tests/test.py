# lab4/task6/tests/test.py

import unittest
import os

from lab4.task6.src.queue_with_minimum import (
    task6, PATH, OUTPUT_PATH, MinQueue
)

class TestQueueWithMin(unittest.TestCase):

    def setUp(self):
        self.test_input_path = r"D:\algorithms-and-data-structures\lab4\task6\txtf\test_input.txt"
        self.test_output_path = r"D:\algorithms-and-data-structures\lab4\task6\txtf\test_output.txt"

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
        import lab4.task6.src.queue_with_minimum as module
        module.PATH = self.test_input_path
        module.OUTPUT_PATH = self.test_output_path

    def _restore_global_paths(self):
        import lab4.task6.src.queue_with_minimum as module
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

    def test_min_queue_class(self):
        q = MinQueue()
        q.push(3)
        q.push(1)
        self.assertEqual(q.get_min(), 1)
        q.push(2)
        self.assertEqual(q.get_min(), 1)
        q.pop()  # removes 3
        self.assertEqual(q.get_min(), 1)
        q.pop()  # removes 1
        self.assertEqual(q.get_min(), 2)

    def test_task_basic(self):
        lines = [
            "7",
            "+ 10",
            "+ 5",
            "?",
            "+ 7",
            "-",
            "?",
            "+ 2"
        ]
        # После "+10", "+5", get_min -> 5
        # потом "+7", "-" (удаляется 10), get_min -> 5
        # "+2" не меняет вывод, т.к. нет последующей '?'
        self.write_test_file(lines)
        task6()
        result = self.read_output_file()
        self.assertEqual(result, ["5", "5"])

    def test_task_more(self):
        lines = [
            "9",
            "+ 5",
            "+ 6",
            "+ 2",
            "?",
            "-",
            "?",
            "-",
            "?",
            "-"
        ]
        # Операции:
        # +5, +6, +2 => очередь [5,6,2], min=2 => при '?': вывод "2"
        # '-' => удаляем 5 => очередь [6,2], min=2 => при '?': вывод "2"
        # '-' => удаляем 6 => очередь [2],  min=2 => при '?': вывод "2"
        # '-' => удаляем 2 => очередь []
        self.write_test_file(lines)
        task6()
        result = self.read_output_file()
        self.assertEqual(result, ["2", "2", "2"])


if __name__ == '__main__':
    unittest.main()
