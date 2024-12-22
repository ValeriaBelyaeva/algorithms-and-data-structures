# lab5/task4/src/build_heap.py

import sys
import os

PATH = r"D:\algorithms-and-data-structures\lab5\task4\txtf\input.txt"
OUTPUT_PATH = r"D:\algorithms-and-data-structures\lab5\task4\txtf\output.txt"

def read_array(file_path):
    """
    Считывает:
      - n: число элементов
      - n целых чисел
    Возвращает список.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        n = int(f.readline().strip())
        arr = list(map(int, f.readline().split()))
    return arr

def sift_down(arr, i, swaps):
    """
    Просеивание вниз (min-heap).
    arr - массив
    i - текущий индекс
    swaps - список пар (i, j) для вывода
    Возвращает количество добавленных свопов (или меняет сам swaps).
    """
    n = len(arr)
    min_index = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[left] < arr[min_index]:
        min_index = left
    if right < n and arr[right] < arr[min_index]:
        min_index = right

    if i != min_index:
        arr[i], arr[min_index] = arr[min_index], arr[i]
        swaps.append((i, min_index))
        sift_down(arr, min_index, swaps)

def build_min_heap(arr):
    """
    Построение min-heap из массива.
    Возвращает список свопов.
    """
    swaps = []
    n = len(arr)

    # Строим кучу с помощью sift_down c середины массива
    # (последний неналоговый узел)
    for i in range(n//2 - 1, -1, -1):
        sift_down(arr, i, swaps)

    return swaps

def task4():
    """
    Считывает массив, строит min-heap,
    выводит число свопов и сами свопы.
    """
    arr = read_array(PATH)
    swaps = build_min_heap(arr)

    with open(OUTPUT_PATH, 'w', encoding='utf-8') as out_file:
        out_file.write(str(len(swaps)) + '\n')
        for i, j in swaps:
            out_file.write(f"{i} {j}\n")

if __name__ == '__main__':
    task4()
