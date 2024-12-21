# D:\algorithms-and-data-structures\lab2\task4\src\bin_faind.py

PATH = r"D:\algorithms-and-data-structures\lab2\task4\txtf\input.txt"
OUTPUT_PATH = r"D:\algorithms-and-data-structures\lab2\task4\txtf\output.txt"


def read_input(file_path):
    """
    Считывает данные из input.txt.
    Формат:
    1-я строка: n (размер массива), затем n возрастающих положительных целых чисел
    2-я строка: k (количество искомых чисел), затем k чисел.
    Возвращает (arr, queries).
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    if len(lines) < 2:
        return [], []
    # Первая строка: n и сам массив
    first_line = list(map(int, lines[0].split()))
    n = first_line[0]
    arr = first_line[1:]  # должны быть n чисел
    if len(arr) != n:
        raise ValueError("Количество чисел в первой строке не совпадает с заявленным n.")

    # Вторая строка: k и k чисел
    second_line = list(map(int, lines[1].split()))
    k = second_line[0]
    queries = second_line[1:]
    if len(queries) != k:
        raise ValueError("Количество чисел в поиске не совпадает с заявленным k.")

    return arr, queries


def bin_search(arr, x):
    """
    Бинарный поиск числа x в отсортированном массиве arr.
    Возвращает индекс (0-based), если элемент найден, или -1 в противном случае.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def write_output(results, file_path):
    """
    Записывает результаты (k чисел-ответов) в одну строку output.txt,
    разделяя их пробелом.
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(' '.join(map(str, results)) + '\n')


def task():
    """
    Основная функция:
    - Считывает данные из input.txt
    - Для каждого искомого числа выполняет бинарный поиск
    - Записывает результаты поиска в output.txt
    """
    arr, queries = read_input(PATH)
    results = []
    for q in queries:
        idx = bin_search(arr, q)
        results.append(idx)
    write_output(results, OUTPUT_PATH)


if __name__ == "__main__":
    task()
