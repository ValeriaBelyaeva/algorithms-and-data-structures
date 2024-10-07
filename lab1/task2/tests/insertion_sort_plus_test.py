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
            [i for i in range(1000, 0, -1)]
        ]
        answers = [
            [1, 1, 1, 1, 1],
            [1, 2, 3, 1, 4, 5],
            [1, 2, 1],
            [1, 2, 3],
            [i for i in range(1, 1001)],
            [1 for i in range(1, 1001)]
        ]
        for i in range(len(test_input)):
            test = test_input[i]
            ans = answers[i]

            a, b = insertion_sort(test)
            self.assertEqual(a, ans)
            self.assertEqual(b, sorted(test))

if __name__ == "__main__":
    unittest.main()