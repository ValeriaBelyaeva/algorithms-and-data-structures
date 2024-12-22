# lab7/task6/src/lis.py

import sys
import os
import bisect

PATH = r"D:\algorithms-and-data-structures\lab7\task6\txtf\input.txt"
OUTPUT_PATH = r"D:\algorithms-and-data-structures\lab7\task6\txtf\output.txt"

def read_sequence(file_path):
    """
    Считывает:
      - n: длина последовательности
      - строку из n целых чисел
    Возвращает список.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        line_n = f.readline().strip()
        n = int(line_n) if line_n else 0
        if n > 0:
            seq = list(map(int, f.readline().strip().split()))
        else:
            seq = []
    return seq

def write_result(length, subseq, file_path):
    """
    Записывает в файл:
      - длину LIS
      - саму LIS через пробел
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(length) + '\n')
        if length > 0:
            f.write(' '.join(map(str, subseq)) + '\n')
        else:
            f.write('\n')

def lis(seq):
    """
    Наибольшая возрастающая подпоследовательность (O(n log n)).
    Возвращает (длина, сама подпоследовательность).
    """
    if not seq:
        return (0, [])

    # tail[i] = последний элемент возрастающей подпоследовательности длины i+1
    tail = []
    # Для восстановления последовательности храним parent, где parent[i] = индекс предыдущего эл-та
    parent = [-1]*len(seq)
    # pos[i] = позиция в tail (длина подпоследовательности-1), где лежит seq[i]
    pos = [0]*len(seq)

    for i in range(len(seq)):
        # ищем место seq[i] в tail
        # index = левая граница, где seq[i] можно поставить
        index = bisect.bisect_left(tail, seq[i])
        # если index == len(tail), добавляем
        if index == len(tail):
            tail.append(seq[i])
        else:
            tail[index] = seq[i]
        # запоминаем pos
        pos[i] = index
        # если index>0, нужно parent[i] = индекс элемента, у которого pos = index-1
        if index > 0:
            # ищем среди ранее обработанных элементов i-1, i-2,... у кого pos=? index-1
            # но чтобы всё работало быстро, нам придется хранить какую-то структуру?
            # Или сделаем хитрее:
            # Мы можем хранить отдельный массив bestPosSize, где bestPosSize[len] = индекс
            # элемента, который стоит в конце подпоследовательности длины len
            # Вместо этого проще хранить ещё один массив ends: ends[length] = индекс эл-та
            pass
        # Но чтобы упростить, создадим ends: ends[length_of_subseq-1] = индекс
        if i == 0:
            ends = [0]
        if index == len(ends):
            ends.append(i)
        else:
            ends[index] = i
        if index > 0:
            parent[i] = ends[index-1]

    length = len(tail)
    # восстановим последовательность
    # последний элемент = ends[length-1]
    lis_index = ends[length-1]
    lis_sequence = []
    while lis_index != -1:
        lis_sequence.append(seq[lis_index])
        lis_index = parent[lis_index]
    lis_sequence.reverse()
    return (length, lis_sequence)

def task6():
    seq = read_sequence(PATH)
    length, subsequence = lis(seq)
    write_result(length, subsequence, OUTPUT_PATH)

if __name__ == '__main__':
    task6()
