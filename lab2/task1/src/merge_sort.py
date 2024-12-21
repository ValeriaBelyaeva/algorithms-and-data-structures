# merge_sort_task.py

import sys

# Глобальные пути к входному/выходному файлам
PATH = r"D:\algorithms-and-data-structures\lab2\task1\txtf\input.txt"
OUTPUT_PATH = r"D:\algorithms-and-data-structures\lab2\task1\txtf\output.txt"

def read_from_file(file_path):
    """
    Считывает данные из файла:
      - Первая строка: число n — количество элементов
      - Вторая строка: n целых чисел
    Возвращает: список считанных чисел
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        n = int(file.readline())
        arr = list(map(int, file.readline().split()))
    return arr

def write_to_file(arr, file_path):
    """
    Записывает отсортированный массив в файл,
    элементы разделяются одним пробелом
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(' '.join(map(str, arr)))

def merge_sort(arr):
    """
    Сортировка слиянием.
    Разделяем массив на левую и правую часть,
    рекурсивно сортируем каждую, затем сливаем.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Копируем оставшиеся элементы из левой части, если остались
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Копируем оставшиеся элементы из правой части, если остались
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def task1():
    """
    Основная функция для чтения входных данных,
    сортировки массива и записи результата в выходной файл.
    """
    data = read_from_file(PATH)   # Считываем массив
    merge_sort(data)              # Сортируем
    write_to_file(data, OUTPUT_PATH)  # Записываем результат

if __name__ == '__main__':
    task1()
