# lab5/task1/src/is_heap.py

import sys
import os

# Глобальные пути к входному/выходному файлам
PATH = r"D:\algorithms-and-data-structures\lab5\task1\txtf\input.txt"
OUTPUT_PATH = r"D:\algorithms-and-data-structures\lab5\task1\txtf\output.txt"

def read_array(file_path):
    """
    Считывает:
      - n: размер массива
      - массив из n целых чисел
    Возвращает список чисел.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        n = int(f.readline().strip())
        arr = list(map(int, f.readline().split()))
    return arr

def check_if_min_heap(arr):
    """
    Проверяет, удовлетворяет ли массив свойству неубывающей пирамиды (min-heap).
    Для каждого i:
      - если 2i+1 < n, arr[i] <= arr[2i+1]
      - если 2i+2 < n, arr[i] <= arr[2i+2]
    """
    n = len(arr)
    for i in range(n):
        left = 2*i + 1
        right = 2*i + 2
        if left < n and arr[i] > arr[left]:
            return False
        if right < n and arr[i] > arr[right]:
            return False
    return True

def task1():
    """
    Определяет, является ли массив неубывающей пирамидой.
    Печатает "YES" или "NO" в выходной файл.
    """
    arr = read_array(PATH)
    result = check_if_min_heap(arr)

    with open(OUTPUT_PATH, 'w', encoding='utf-8') as out_file:
        if result:
            out_file.write("YES\n")
        else:
            out_file.write("NO\n")

if __name__ == '__main__':
    task1()
