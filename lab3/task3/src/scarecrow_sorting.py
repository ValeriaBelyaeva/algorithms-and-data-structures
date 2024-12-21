import sys

PATH = r"D:\algorithms-and-data-structures\lab3\task3\txtf\input.txt"
OUTPUT_PATH = r"D:\algorithms-and-data-structures\lab3\task3\txtf\output.txt"

def read_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        first_line = f.readline().split()
        n, k = int(first_line[0]), int(first_line[1])
        arr = list(map(int, f.readline().split()))
    return n, k, arr

def write_to_file(answer, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(answer)

def can_scarecrow_sort(n, k, arr):
    from collections import defaultdict
    groups = defaultdict(list)
    for i in range(n):
        groups[i % k].append(arr[i])
    for g in groups:
        groups[g].sort()
    result = []
    indices = {g: 0 for g in groups}
    for i in range(n):
        g = i % k
        result.append(groups[g][indices[g]])
        indices[g] += 1
    for i in range(1, n):
        if result[i] < result[i - 1]:
            return False
    return True

def task3():
    n, k, arr = read_from_file(PATH)
    if can_scarecrow_sort(n, k, arr):
        write_to_file("ДА", OUTPUT_PATH)
    else:
        write_to_file("НЕТ", OUTPUT_PATH)

if __name__ == '__main__':
    task3()
