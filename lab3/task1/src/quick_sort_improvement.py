import sys
import random

# Глобальные пути (пример; скорректируйте при необходимости)
PATH = r"D:\algorithms-and-data-structures\lab3\task1\txtf\input.txt"
OUTPUT_PATH = r"D:\algorithms-and-data-structures\lab3\task1\txtf\output.txt"

def read_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        n = int(file.readline())
        arr = list(map(int, file.readline().split()))
    return arr

def write_to_file(arr, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(' '.join(map(str, arr)))

def partition3(arr, left, right):
    pivot_index = random.randint(left, right)
    arr[left], arr[pivot_index] = arr[pivot_index], arr[left]
    pivot = arr[left]
    lt = left
    gt = right
    i = left

    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1
    return lt, gt

def quick_sort_3way(arr, left, right):
    if left >= right:
        return
    m1, m2 = partition3(arr, left, right)
    quick_sort_3way(arr, left, m1 - 1)
    quick_sort_3way(arr, m2 + 1, right)

def quick_sort_improvement(arr):
    quick_sort_3way(arr, 0, len(arr) - 1)

def task1():
    data = read_from_file(PATH)
    quick_sort_improvement(data)
    write_to_file(data, OUTPUT_PATH)

if __name__ == '__main__':
    task1()
