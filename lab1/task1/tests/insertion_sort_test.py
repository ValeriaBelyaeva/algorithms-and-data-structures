import unittest
from lab1.task1.src import insertion_sort

class TestCaesar(unittest.TestCase):
    def test_encrypt_caesar(self):
        self.assertEqual(insertion_sort([3, 3, 1, 3, 3]), [1, 3, 3, 3, 3])
        self.assertEqual(insertion_sort([5, 4, 3, 2, -1]), [-1, 2, 3, 4, 5])
        self.assertEqual(insertion_sort([31, 41, 59, 26, 41, 58]), [26, 31, 41, 41, 58, 59])
        self.assertEqual(insertion_sort([1000000000, 1000000000, 50000000]), [50000000, 1000000000, 1000000000])
        self.assertEqual(insertion_sort([1 for i in range(1000)]), [1 for i in range(1000)])
        self.assertEqual(insertion_sort([i for i in range(1000, 0)]), [i for i in range(1, 1001)])

if __name__ == "__main__":
    unittest.main()