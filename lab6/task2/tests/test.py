# lab5/task2/tests/test.py

import unittest
import os

from lab5.task2.src.phonebook import task2, PATH, OUTPUT_PATH

class TestPhonebook(unittest.TestCase):

    def setUp(self):
        self.test_input_path = r"D:\algorithms-and-data-structures\lab5\task2\txtf\test_input.txt"
        self.test_output_path = r"D:\algorithms-and-data-structures\lab5\task2\txtf\test_output.txt"

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
        import lab5.task2.src.phonebook as module
        module.PATH = self.test_input_path
        module.OUTPUT_PATH = self.test_output_path

    def _restore_global_paths(self):
        import lab5.task2.src.phonebook as module
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
            "add 911 police",
            "add 76213 Mom",
            "add 17239 Bob",
            "find 76213",
            "find 910",
            "find 911",
            "del 910",
            "find 911",
        ]
        # find 76213 -> Mom
        # find 910 -> not found
        # find 911 -> police
        # del 910 (none)
        # find 911 -> police
        self.write_test_file(lines)
        task2()
        result = self.read_output_file()
        self.assertEqual(result, ["Mom", "not found", "police", "police"])

    def test_overwrite(self):
        lines = [
            "5",
            "add 100 xyz",
            "add 100 abc",
            "find 100",
            "del 100",
            "find 100"
        ]
        # Перезапись на "abc"
        # find 100 -> abc
        # del 100 -> {}
        # find 100 -> not found
        self.write_test_file(lines)
        task2()
        result = self.read_output_file()
        self.assertEqual(result, ["abc", "not found"])

    def test_del_non_existing(self):
        lines = [
            "4",
            "del 123",
            "add 555 me",
            "del 123",
            "find 555"
        ]
        # del 123 -> нет ничего
        # add 555 me -> phonebook["555"] = "me"
        # del 123 -> ничего
        # find 555 -> me
        self.write_test_file(lines)
        task2()
        result = self.read_output_file()
        self.assertEqual(result, ["me"])

if __name__ == '__main__':
    unittest.main()
