# D:\algorithms-and-data-structures\lab2\task3\src\invertion_cnt.py

PATH = r"D:\algorithms-and-data-structures\lab2\task3\txtf\input.txt"
OUTPUT_PATH = r"D:\algorithms-and-data-structures\lab2\task3\txtf\output.txt"


def read_input(file_path):
    """
    Считывает данные из input.txt:
    - Первая строка: n (количество элементов)
    - Вторая строка: n целых чисел
    Возвращает список считанных чисел.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
        if len(lines) < 2:
            return []
        n = int(lines[0])
        arr = list(map(int, lines[1].split()))
        if len(arr) != n:
            raise ValueError("Количество элементов не совпадает с заявленным n.")
        return arr


def merge_count_inversions(arr):
    """
    Считает количество инверсий в массиве arr, используя
    модифицированный merge sort. Возвращает (sorted_arr, inv_count).
    """
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, left_inv = merge_count_inversions(arr[:mid])
    right, right_inv = merge_count_inversions(arr[mid:])

    merged, split_inv = merge_and_count(left, right)
    total_inv = left_inv + right_inv + split_inv

    return merged, total_inv


def merge_and_count(left, right):
    """
    Сливает два отсортированных массива left и right,
    возвращая (merged_list, count_inversions_на_слиянии).
    """
    i = j = 0
    merged = []
    inv_count = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            # Все оставшиеся элементы left[i:] больше right[j],
            # значит они образуют инверсии.
            inv_count += len(left) - i
            j += 1

    merged += left[i:]
    merged += right[j:]
    return merged, inv_count


def write_output(result, file_path):
    """
    Записывает результат (число инверсий) в выходной файл output.txt
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(result) + "\n")


def task():
    """
    Основная функция:
    - Считывает массив из input.txt
    - Вычисляет количество инверсий
    - Записывает результат в output.txt
    """
    arr = read_input(PATH)
    _, inv_count = merge_count_inversions(arr)
    write_output(inv_count, OUTPUT_PATH)


if __name__ == "__main__":
    task()
