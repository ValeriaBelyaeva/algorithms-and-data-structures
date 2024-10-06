import unittest
from lab1.task1.src.insertion_sort import insertion_sort

class TestCaesar(unittest.TestCase):

    def test_caesar(self):
        test_input = [
            [5, 4, 3, 2, -1],
            [31, 41, 59, 26, 41, 58],
            [1000000000, 1000000000, 50000000],
            [-1000000000, -1000000000, 50000000],
            [1 for i in range(1000)],
            [i for i in range(1000, 0)]
        ]
        for test in test_input:
            self.assertEqual(insertion_sort(test), sorted(test))

if __name__ == "__main__":
    unittest.main()