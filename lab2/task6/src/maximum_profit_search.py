# D:\algorithms-and-data-structures\lab2\task6\src\maximum_profit_search.py

PATH = r"D:\algorithms-and-data-structures\lab2\task6\txtf\input.txt"
OUTPUT_PATH = r"D:\algorithms-and-data-structures\lab2\task6\txtf\output.txt"


def read_input(file_path):
    """
    Считывает данные из input.txt.
    Формат (пример):
    1-я строка: Название фирмы (строка)
    2-я строка: Интервал времени анализа (строка)
    3-я строка: n (количество цен)
    4-я строка: n целых чисел (цены акции в день i)

    Возвращает (company, date_range, prices).
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    if len(lines) < 4:
        # Можно обработать по-разному, для простоты вернём пустые значения
        return "", "", []

    company = lines[0]
    date_range = lines[1]
    n = int(lines[2])
    prices = list(map(int, lines[3].split()))
    if len(prices) != n:
        raise ValueError("Количество считанных цен не совпадает с заявленным n.")

    return company, date_range, prices


def find_max_subarray(prices, low, high):
    """
    Находит максимальный подмассив (с точки зрения суммы приращений)
    с использованием divide & conquer.
    Возвращает (left_index, right_index, sum).
    """
    if low == high:
        # Если один элемент, максимум - этот элемент
        return low, high, prices[low]

    mid = (low + high) // 2
    left_low, left_high, left_sum = find_max_subarray(prices, low, mid)
    right_low, right_high, right_sum = find_max_subarray(prices, mid + 1, high)
    cross_low, cross_high, cross_sum = find_max_crossing_subarray(prices, low, mid, high)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum


def find_max_crossing_subarray(prices, low, mid, high):
    """
    Находит максимальный подмассив, пересекающий середину (low..mid..high).
    Возвращает (max_left, max_right, sum).
    """
    left_sum = float('-inf')
    sum_ = 0
    max_left = mid
    for i in range(mid, low - 1, -1):
        sum_ += prices[i]
        if sum_ > left_sum:
            left_sum = sum_
            max_left = i

    right_sum = float('-inf')
    sum_ = 0
    max_right = mid + 1
    for j in range(mid + 1, high + 1):
        sum_ += prices[j]
        if sum_ > right_sum:
            right_sum = sum_
            max_right = j

    return max_left, max_right, left_sum + right_sum


def compute_profit_and_days(prices):
    """
    Принимает список цен акций по дням (prices[0] - цена в день 1, ...)
    Ищет максимальную прибыль (разницу) с помощью Find Maximum Subarray.

    Для применения 'maximum subarray' нам нужны приращения между днями.
    Если P[i] - цена на i-й день, то дельта d[i] = P[i] - P[i-1].
    Тогда задача поиска максимального подмассива d решает "купить в начале подмассива,
    продать в конце" для максимальной прибыли.

    Возвращает (buy_day, sell_day, max_profit).
    Если прибыль неотрицательна, считаем, что buy_day < sell_day.
    Если вся прибыль <= 0, значит выгоды нет, но возвращаем max_profit и
    buy_day == sell_day по условной логике.
    """
    n = len(prices)
    if n < 2:
        # Если всего 0 или 1 цена, нет нормальной сделки
        return 1, 1, 0

    # Формируем массив приращений d[i], i=1..n-1
    # d[0] соответствует приращению между днем 2 и днем 1
    deltas = []
    for i in range(1, n):
        deltas.append(prices[i] - prices[i - 1])

    # Ищем максимальный подмассив в deltas (индексы 0..n-2)
    low, high, max_sum = find_max_subarray(deltas, 0, len(deltas) - 1)
    # low..high в deltas => это соотв. покупка в day=low, продажа в day=high+1 (т.к. deltas[i] = P[i+1] - P[i])
    # Нужно преобразовать индексы обратно к дням [1..n]
    buy_day = low + 1  # в prices, это (low + 1)
    sell_day = high + 1  # т.к. разница между day+1 и day
    # Но покупка - это (low+1)-й день, а продажа - это (high+1+1)-й день
    # Для удобства:
    buy_day_in_prices = low + 1  # покупка
    sell_day_in_prices = high + 1 + 1  # продажа

    # Если max_sum <= 0, значит нет выгоды, вернём 1,1,0
    if max_sum <= 0:
        return 1, 1, 0

    return buy_day_in_prices, sell_day_in_prices, max_sum


def task():
    """
    Основная функция:
    - Считывает данные (название фирмы, интервал времени, цены)
    - Вычисляет лучший день покупки, день продажи, максимальную прибыль
    - Записывает результаты в output.txt
    Формат выхода (пример):
        <company>
        <date_range>
        Buy day: <buy_day>
        Sell day: <sell_day>
        Max profit: <profit>
    """
    company, date_range, prices = read_input(PATH)
    buy_day, sell_day, max_profit = compute_profit_and_days(prices)

    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        f.write(f"{company}\n")
        f.write(f"{date_range}\n")
        f.write(f"Buy day: {buy_day}\n")
        f.write(f"Sell day: {sell_day}\n")
        f.write(f"Max profit: {max_profit}\n")


if __name__ == "__main__":
    task()
