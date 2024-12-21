# D:\algorithms-and-data-structures\lab2\task5\src\representative_of_the_majority.py

PATH = r"D:\algorithms-and-data-structures\lab2\task5\txtf\input.txt"
OUTPUT_PATH = r"D:\algorithms-and-data-structures\lab2\task5\txtf\output.txt"

def read_input(file_path):
    """
    Считывает данные из input.txt:
    - Первая строка: n (количество элементов)
    - Вторая строка: n целых чисел
    Возвращает список считанных чисел arr.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    if len(lines) < 2:
        return []
    n = int(lines[0].split()[0])
    arr = list(map(int, lines[1].split()))
    if len(arr) != n:
        raise ValueError("Количество чисел не совпадает с заявленным n.")
    return arr

def majority_element_divide_conquer(arr):
    """
    Определяет, есть ли в массиве arr элемент, который встречается
    более чем n/2 раз, используя divide & conquer (O(n log n)).
    Возвращает сам элемент, если он есть, иначе None.
    """
    def get_majority_element(l, r):
        # База: если в подмассиве один элемент, он "кандидат" (но не факт, что мажоритарный)
        if l == r:
            return arr[l]

        mid = (l + r) // 2
        left_candidate = get_majority_element(l, mid)
        right_candidate = get_majority_element(mid + 1, r)

        # Если оба кандидата совпадают, возвращаем одного из них
        if left_candidate == right_candidate:
            return left_candidate

        # Иначе подсчитываем, сколько раз каждый кандидат встречается в [l..r]
        left_count = sum(1 for i in range(l, r + 1) if arr[i] == left_candidate)
        right_count = sum(1 for i in range(l, r + 1) if arr[i] == right_candidate)

        # Возвращаем того, у кого больше вхождений (он потенциальный кандидат)
        if left_count > right_count:
            return left_candidate
        else:
            return right_candidate

    n = len(arr)
    if n == 0:
        return None

    candidate = get_majority_element(0, n - 1)
    # Проверяем, действительно ли candidate мажоритарен
    count_candidate = sum(1 for x in arr if x == candidate)
    if count_candidate > n // 2:
        return candidate
    else:
        return None

def task():
    """
    Основная функция:
    - Считывает массив из input.txt
    - Проверяет, есть ли элемент, встречающийся более n/2 раз
    - Выводит 1, если такой элемент есть, иначе 0, в output.txt
    """
    arr = read_input(PATH)
    elem = majority_element_divide_conquer(arr)
    result = 1 if elem is not None else 0
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        f.write(str(result) + "\n")

if __name__ == "__main__":
    task()
