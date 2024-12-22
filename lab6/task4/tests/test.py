# lab6/task4/tests/test.py

import unittest
import os

from lab6.task4.src.threaded_map import task4, PATH, OUTPUT_PATH

class TestThreadedMap(unittest.TestCase):

    def setUp(self):
        self.test_input_path = r"D:\algorithms-and-data-structures\lab6\task4\txtf\test_input.txt"
        self.test_output_path = r"D:\algorithms-and-data-structures\lab6\task4\txtf\test_output.txt"

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
        import lab6.task4.src.threaded_map as module
        module.PATH = self.test_input_path
        module.OUTPUT_PATH = self.test_output_path

    def _restore_global_paths(self):
        import lab6.task4.src.threaded_map as module
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
        # Пример (частично):
        # 14
        # put zero a
        # put one b
        # put two c
        # put three d
        # put four e
        # get two -> c
        # prev two -> b (key=one)
        # next two -> d (key=three)
        # delete one
        # delete three
        # get two -> c
        # prev two -> <none> (since 'one' was removed and it was left to 'two')
        # next two -> <none> (since 'three' was removed and it was right to 'two')
        # next four -> <none> (since 'four' is tail, no next)
        lines = [
            "14",
            "put zero a",
            "put one b",
            "put two c",
            "put three d",
            "put four e",
            "get two",
            "prev two",
            "next two",
            "delete one",
            "delete three",
            "get two",
            "prev two",
            "next two",
            "next four"
        ]
        self.write_test_file(lines)
        task4()
        result = self.read_output_file()
        # Ожидается:
        # c
        # b
        # d
        # c
        # <none>
        # <none>
        # <none>
        self.assertEqual(result, ["c", "b", "d", "c", "<none>", "<none>", "<none>"])

    def test_put_update(self):
        lines = [
            "5",
            "put key1 val1",
            "put key2 val2",
            "put key1 val3",  # update
            "get key1",
            "prev key2"
        ]
        # put key1 val1 -> head=key1=tail, val1
        # put key2 val2 -> tail=key2, prev-> key1
        # put key1 val3 -> update key1, does not change order
        # get key1 -> val3
        # prev key2 -> key1 => val3
        self.write_test_file(lines)
        task4()
        result = self.read_output_file()
        self.assertEqual(result, ["val3", "val3"])

    def test_delete_non_existent(self):
        lines = [
            "4",
            "delete q",
            "put a x",
            "delete z",
            "get a"
        ]
        # delete q -> ничего
        # put a x -> a( x ), head=tail='a'
        # delete z -> ничего
        # get a -> x
        self.write_test_file(lines)
        task4()
        result = self.read_output_file()
        self.assertEqual(result, ["x"])


if __name__ == '__main__':
    unittest.main()
