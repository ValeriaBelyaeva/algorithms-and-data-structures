import unittest
from lab1.task4.src.Linear_search import linear_search


class TestCaesar(unittest.TestCase):
    def test_caesar(self):
        test_input = [
            (1000, list(range(-1000, -800))+list(range(800, 1001))),
            (3, list(range(-1000, 4))+[3, 3, 3, 3]+list(range(600, 700))+list(range(3, 650))),
            (250, list(range(200, 400))+list(range(100, 300))+list(range(300, -150, -1))),
            (-500, list(range(-550, -450))+list(range(-550, -450))+list(range(-550, -450))),
            (100, [100 for i in range(100)]),
            (0, [3, 2, 4, 0] * 5),
            (-2, [3, 2, 4, 0] * 5)
        ]
        answers = [
            [400],
            [1003, 1004, 1005, 1006, 1007, 1108],
            [50, 350, 450],
            [50, 150, 250],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
             21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
             40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58,
             59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77,
             78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99],
            [3, 7, 11, 15, 19],
            [-1]
        ]
        for i in range(len(test_input)):
            test = test_input[i]
            ans = answers[i]

            self.assertEqual(linear_search(test[0], test[1]), ans)

if __name__ == "__main__":
    unittest.main()