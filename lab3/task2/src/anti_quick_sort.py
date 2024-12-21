import sys

PATH = r"D:\algorithms-and-data-structures\lab3\task2\txtf\input.txt"
OUTPUT_PATH = r"D:\algorithms-and-data-structures\lab3\task2\txtf\output.txt"

def read_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        n = int(f.readline())
    return n

def write_to_file(arr, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(' '.join(map(str, arr)))

def generate_anti_quick_sort(n):
    arr = list(range(1, n + 1))
    for i in range(2, n):
        j = i // 2
        arr[i], arr[j] = arr[j], arr[i]
    return arr

def task2():
    n = read_from_file(PATH)
    permutation = generate_anti_quick_sort(n)
    write_to_file(permutation, OUTPUT_PATH)

if __name__ == '__main__':
    task2()
