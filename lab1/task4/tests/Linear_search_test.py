import unittest
from lab1.task1.src.insertion_sort_plus import insertion_sort


class TestCaesar(unittest.TestCase):

    def test_caesar(self):
        test_input = [
            []
        ]
        answers = []
        for i in range(len(test_input)):
            test = test_input[i]
            ans = answers[i]

            a, b = insertion_sort(test)
            self.assertEqual(a, ans)
            self.assertEqual(b, sorted(test))

if __name__ == "__main__":
    unittest.main()