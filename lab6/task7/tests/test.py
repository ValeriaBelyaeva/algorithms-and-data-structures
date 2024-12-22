# lab5task7teststest.py

import unittest
import os

from lab5.task7.src.precious_stones import task7, PATH, OUTPUT_PATH

class TestPreciousStones(unittest.TestCase)

    def setUp(self)
        self.test_input_path = rDalgorithms-and-data-structureslab5task7txtftest_input.txt
        self.test_output_path = rDalgorithms-and-data-structureslab5task7txtftest_output.txt

        self.original_path = PATH
        self.original_output_path = OUTPUT_PATH
        self._override_global_paths()

    def tearDown(self)
        self._restore_global_paths()
        if os.path.exists(self.test_input_path)
            os.remove(self.test_input_path)
        if os.path.exists(self.test_output_path)
            os.remove(self.test_output_path)

    def _override_global_paths(self)
        import lab5.task7.src.precious_stones as module
        module.PATH = self.test_input_path
        module.OUTPUT_PATH = self.test_output_path

    def _restore_global_paths(self)
        import lab5.task7.src.precious_stones as module
        module.PATH = self.original_path
        module.OUTPUT_PATH = self.original_output_path

    def write_test_file(self, lines)
        with open(self.test_input_path, 'w', encoding='utf-8') as f
            for line in lines
                f.write(line + 'n')

    def read_output_file(self)
        if not os.path.exists(self.test_output_path)
            return 
        with open(self.test_output_path, 'r', encoding='utf-8') as f
            return f.read().strip()

    def test_example1(self)
        # 7 stones, 1 pair
        # S= abacaba
        # pair= aa
        lines = [
            7 1,
            abacaba,
            aa
        ]
        # S= a b a c a b a
        # indices0 1 2 3 4 5 6
        # пара (a,a), считаем кол-во пар (ij) S[i]=='a' and S[j]=='a'
        # символ 'a' встречается на позициях [0,2,4,6]
        # кол-во пар = 6 (C(4,2)=6)
        self.write_test_file(lines)
        task7()
        res = self.read_output_file()
        self.assertEqual(res, 6)

    def test_example2(self)
        # 7 3
        # abacaba
        # ab
        # ac
        # bb
        # S= a b a c a b a
        # pairs (a,b), (a,c), (b,b)
        # 1) (a,b) ij, S[i] ='a', S[j] ='b'
        #     a on [0,2,4,6], b on [1,5]
        #     кол-во (a,b) пар (0,1), (2,5), (4,5), итого 3 + (0,5) wait ij = (0,1),(0,5),(2,5),(4,5), (6,) no j6 = 4
        # 2) (a,c) a in [0,2,4,6], c in [3], пары (0,3),(2,3),(4,3),(6,3) j=3  i=6 no ij = i=63, skip = (0,3),(2,3),(4,3) = 3
        # 3) (b,b) b in [1,5], пары (1,5) = 1
        # total= 4+3+1=8
        lines = [
            7 3,
            abacaba,
            ab,
            ac,
            bb
        ]
        self.write_test_file(lines)
        task7()
        res = self.read_output_file()
        self.assertEqual(res, 8)

    def test_single_char(self)
        # n=5, k=1, S=aaaaa, pair=aa
        # number of pairs (ij) = C(5,2)=10
        lines = [
            5 1,
            aaaaa,
            aa
        ]
        self.write_test_file(lines)
        task7()
        res = self.read_output_file()
        self.assertEqual(res, 10)

if __name__ == '__main__'
    unittest.main()
