# lab6/task8/tests/test.py

import unittest
import os

from lab6.task8.src.almost_interactive_hashtable import task8, PATH, OUTPUT_PATH

class TestAlmostInteractiveHashTable(unittest.TestCase):

    def setUp(self):
        self.test_input_path = r"D:\algorithms-and-data-structures\lab6\task8\txtf\test_input.txt"
        self.test_output_path = r"D:\algorithms-and-data-structures\lab6\task8\txtf\test_output.txt"

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
        import lab6.task8.src.almost_interactive_hashtable as module
        module.PATH = self.test_input_path
        module.OUTPUT_PATH = self.test_output_path

    def _restore_global_paths(self):
        import lab6.task8.src.almost_interactive_hashtable as module
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

    def test_small(self):
        # N=4, X=0, A=0, B=0
        # AC=1, BC=1, AD=0, BD=0
        # step by step
        # i=0: X=0 not in set => add => A=0+0=0, B=0+0=0 => X=(0*0+0)=0
        # i=1: X=0 in set => A=0+1=1 mod 1000, B=0+1=1 mod 10^15 => X=(0*1+1)=1
        # i=2: X=1 not in set => add => A=1+0=1, B=1+0=1 => X=(1*1+1)=2
        # i=3: X=2 not in set => add => A=1+0=1, B=1+0=1 => X=(2*1+1)=3
        # final => X=3, A=1, B=1
        lines = [
            "4 0 0 0",
            "1 1 0 0"
        ]
        self.write_test_file(lines)
        task8()
        result = self.read_output_file()
        self.assertEqual(result, ["3 1 1"])

    def test_another(self):
        # N=3, X=1, A=1, B=0
        # AC=0, BC=1, AD=0, BD=100
        # i=0: X=1 not in set => add => A=1+0=1, B=0+100=100 => X=(1*1+100)=101
        # i=1: X=101 not in set => add => A=1+0=1, B=100+100=200 => X=(101*1+200)=301
        # i=2: X=301 not in set => add => A=1+0=1, B=200+100=300 => X=(301*1+300)=601
        # final => X=601, A=1, B=300
        lines = [
            "3 1 1 0",
            "0 1 0 100"
        ]
        self.write_test_file(lines)
        task8()
        result = self.read_output_file()
        self.assertEqual(result, ["601 1 300"])

if __name__ == '__main__':
    unittest.main()
