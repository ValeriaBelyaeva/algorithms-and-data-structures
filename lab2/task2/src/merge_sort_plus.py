# D:\algorithms-and-data-structures\lab2\task2\src\merge_sort_plus.py

PATH = r"D:\algorithms-and-data-structures\lab2\task2\txtf\input.txt"
OUTPUT_PATH = r"D:\algorithms-and-data-structures\lab2\task2\txtf\output.txt"

def read_input(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
        if not lines:
            return []
        n = int(lines[0])
        if n == 0:
            return []
        arr = list(map(int, lines[1].split()))
        if len(arr) != n:
            raise ValueError("Количество элементов не совпадает с заявленным n.")
    return arr

def merge_sort(arr, L, R, output_file):
    if L < R:
        M = (L + R) // 2
        merge_sort(arr, L, M, output_file)
        merge_sort(arr, M + 1, R, output_file)
        merge(arr, L, M, R, output_file)

def merge(arr, L, M, R, output_file):
    # L, M, R - 1-based индексы
    left_part = arr[L - 1 : M]
    right_part = arr[M : R]
    i = j = 0
    k = L - 1  # текущая позиция в оригинальном массиве arr

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1
    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1
    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1

    If = L
    Il = R
    Vf = arr[L - 1]
    Vl = arr[R - 1]
    # По условию "Допускается не выводить информацию о слиянии для подмассива длиной 1"
    # Но при стандартном merge_sort, если L<R, длина подмассива >=2, значит выведем
    output_file.write(f"{If} {Il} {Vf} {Vl}\n")

def write_result(arr, output_file):
    output_file.write(' '.join(map(str, arr)) + '\n')

def task():
    arr = read_input(PATH)
    n = len(arr)

    # Очищаем выходной файл
    open(OUTPUT_PATH, 'w', encoding='utf-8').close()

    if n <= 1:
        # Если массив пустой или из 1 элемента, выводим его напрямую
        with open(OUTPUT_PATH, 'a', encoding='utf-8') as f:
            if n == 1:
                f.write(' '.join(map(str, arr)) + '\n')
            else:
                f.write('\n')
        return

    with open(OUTPUT_PATH, 'a', encoding='utf-8') as f:
        merge_sort(arr, 1, n, f)
        write_result(arr, f)

if __name__ == "__main__":
    task()
