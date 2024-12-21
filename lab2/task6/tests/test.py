# D:\algorithms-and-data-structures\lab2\task6\tests\test.py

import unittest
import os
import sys
import random

sys.path.append(r"D:\algorithms-and-data-structures\lab2\task6\src")
from maximum_profit_search import (
    PATH, OUTPUT_PATH, task
)

class TestMaximumProfitSearch(unittest.TestCase):

    def setUp(self):
        self.test_in = r"D:\algorithms-and-data-structures\lab2\task6\txtf\test_input.txt"
        self.test_out = r"D:\algorithms-and-data-structures\lab2\task6\txtf\test_output.txt"
        self.original_in = PATH
        self.original_out = OUTPUT_PATH

        import maximum_profit_search
        maximum_profit_search.PATH = self.test_in
        maximum_profit_search.OUTPUT_PATH = self.test_out

    def tearDown(self):
        import maximum_profit_search
        maximum_profit_search.PATH = self.original_in
        maximum_profit_search.OUTPUT_PATH = self.original_out

        if os.path.exists(self.test_in):
            os.remove(self.test_in)
        if os.path.exists(self.test_out):
            os.remove(self.test_out)

    def write_input_file(self, company, date_range, prices):
        with open(self.test_in, 'w', encoding='utf-8') as f:
            f.write(company + "\n")
            f.write(date_range + "\n")
            f.write(str(len(prices)) + "\n")
            if prices:
                f.write(" ".join(map(str, prices)) + "\n")

    def read_output_file(self):
        if not os.path.exists(self.test_out):
            return []
        with open(self.test_out, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f]

    def parse_output(self, lines):
        """
        Ожидаем формат:
        0: company
        1: date_range
        2: Buy day: x
        3: Sell day: y
        4: Max profit: z
        """
        if len(lines) < 5:
            return {}, False
        try:
            out_data = {
                'company': lines[0],
                'date_range': lines[1],
                'buy_day': int(lines[2].split(":")[1].strip()),
                'sell_day': int(lines[3].split(":")[1].strip()),
                'max_profit': int(lines[4].split(":")[1].strip())
            }
            return out_data, True
        except:
            return {}, False

    def test_single_price(self):
        company = "OnlyOneDayCo"
        date_range = "2021-01-01"
        prices = [100]
        self.write_input_file(company, date_range, prices)
        task()
        lines = self.read_output_file()
        out_data, ok = self.parse_output(lines)
        self.assertTrue(ok)
        self.assertEqual(out_data['company'], company)
        self.assertEqual(out_data['date_range'], date_range)
        # С 1 ценой нельзя заработать
        self.assertEqual(out_data['buy_day'], 1)
        self.assertEqual(out_data['sell_day'], 1)
        self.assertEqual(out_data['max_profit'], 0)

    def test_two_days_increasing(self):
        company = "TestInc"
        date_range = "2021-01-01 to 2021-01-02"
        prices = [100, 120]
        # Покупаем день 1, продаём день 2, profit=20
        self.write_input_file(company, date_range, prices)
        task()
        lines = self.read_output_file()
        out_data, ok = self.parse_output(lines)
        self.assertTrue(ok)
        self.assertEqual(out_data['buy_day'], 1)
        self.assertEqual(out_data['sell_day'], 2)
        self.assertEqual(out_data['max_profit'], 20)

    def test_two_days_decreasing(self):
        company = "TestDec"
        date_range = "2021-01-01 to 2021-01-02"
        prices = [120, 100]
        # Нет выгоды => buy_day=1, sell_day=1, profit=0
        self.write_input_file(company, date_range, prices)
        task()
        lines = self.read_output_file()
        out_data, ok = self.parse_output(lines)
        self.assertTrue(ok)
        self.assertEqual(out_data['buy_day'], 1)
        self.assertEqual(out_data['sell_day'], 1)
        self.assertEqual(out_data['max_profit'], 0)

    def test_sample_scenario(self):
        company = "SampleCorp"
        date_range = "2021-01-01 to 2021-01-06"
        prices = [100, 105, 102, 110, 108, 120]
        # deltas= [5, -3, 8, -2, 12], sum subarray
        # Best subarray? day 2..6 => subarray(1..5) in deltas? Let's see:
        #  5 + (-3) + 8 + (-2) + 12 = 20, buy=1, sell=6 => profit=prices[5]-prices[0]=120-100=20
        # indeed we expect buy_day=1, sell_day=6, profit=20
        self.write_input_file(company, date_range, prices)
        task()
        lines = self.read_output_file()
        out_data, ok = self.parse_output(lines)
        self.assertTrue(ok)
        self.assertEqual(out_data['company'], company)
        self.assertEqual(out_data['date_range'], date_range)
        self.assertEqual(out_data['buy_day'], 1)
        self.assertEqual(out_data['sell_day'], 6)
        self.assertEqual(out_data['max_profit'], 20)

    def test_random(self):
        random.seed(42)
        company = "RandomInc"
        date_range = "2023-01-01 to 2023-01-10"
        prices = []
        cur_price = 100
        for _ in range(10):
            # колебания
            change = random.randint(-10, 10)
            cur_price = max(1, cur_price + change)
            prices.append(cur_price)
        self.write_input_file(company, date_range, prices)
        task()
        lines = self.read_output_file()
        out_data, ok = self.parse_output(lines)
        self.assertTrue(ok)
        # Проверим, что buy_day и sell_day в корректных пределах
        self.assertTrue(1 <= out_data['buy_day'] <= len(prices))
        self.assertTrue(1 <= out_data['sell_day'] <= len(prices))
        # profit>=0
        self.assertTrue(out_data['max_profit'] >= 0)

    def test_larger(self):
        # Более крупный тест для проверки производительности
        company = "BigCo"
        date_range = "2022-01-01 to 2022-12-31"
        n = 2000
        # Генерируем случайные цены (возможно есть возможность заработать)
        random_prices = []
        cur_price = 1000
        for _ in range(n):
            change = random.randint(-50, 50)
            cur_price = max(1, cur_price + change)
            random_prices.append(cur_price)
        self.write_input_file(company, date_range, random_prices)
        task()
        lines = self.read_output_file()
        out_data, ok = self.parse_output(lines)
        self.assertTrue(ok)
        self.assertTrue(1 <= out_data['buy_day'] <= n)
        self.assertTrue(1 <= out_data['sell_day'] <= n)
        # profit>=0
        self.assertTrue(out_data['max_profit'] >= 0)

if __name__ == "__main__":
    unittest.main()
