import unittest
from lab1.task1.src.insertion_sort_plus import insertion_sort


class TestCaesar(unittest.TestCase):

    def test_caesar(self):
        test_input = [
            [5, 4, 3, 2, -1],
            [31, 41, 59, 26, 41, 58],
            [1000000000, 1000000000, 50000000],
            [-1000000000, -1000000000, 50000000],
            [i for i in range(1000)],
            [i for i in range(1000, 0)]
        ]
        answers = [
            [1, 1, 1, 1, 1],
            [1, 2, 3, 1, 4, 5],
            [1, 2, 1],
            [1, 2, 3],
            [1, 2, 2, 2, 3, 5, 5, 6, 9, 1],
            [i for i in range(1, 1000)],
            [1 for i in range(1, 1000)]
        ]
        for test in test_input:
            print(insertion_sort(test))
            # self.assertEqual(insertion_sort(test), sorted(test, reverse=True))

if __name__ == "__main__":
    unittest.main()