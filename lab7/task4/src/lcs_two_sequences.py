# lab7/task4/src/lcs_two_sequences.py

import sys
import os

PATH = r"D:\algorithms-and-data-structures\lab7\task4\txtf\input.txt"
OUTPUT_PATH = r"D:\algorithms-and-data-structures\lab7\task4\txtf\output.txt"

def read_sequences(file_path):
    """
    Считывает две последовательности из файла:
      - n, затем n чисел (первая последовательность)
      - m, затем m чисел (вторая последовательность)
    Возвращает (listA, listB)
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        n_line = f.readline().strip()
        if not n_line:
            return [], []
        n = int(n_line)
        if n > 0:
            seqA = list(map(int, f.readline().strip().split()))
        else:
            seqA = []

        m_line = f.readline().strip()
        if not m_line:
            return seqA, []
        m = int(m_line)
        if m > 0:
            seqB = list(map(int, f.readline().strip().split()))
        else:
            seqB = []
    return seqA, seqB

def write_result(result, file_path):
    """
    Записывает целочисленный результат (длину LCS) в файл.
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(result))

def lcs_length(seqA, seqB):
    """
    Возвращает длину наибольшей общей подпоследовательности
    для двух последовательностей seqA и seqB.
    """
    n = len(seqA)
    m = len(seqB)

    # dp[i][j] = длина LCS(seqA[:i], seqB[:j])
    dp = [[0]*(m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if seqA[i-1] == seqB[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][m]

def task4():
    """
    Считывает данные, вычисляет длину наибольшей общей подпоследовательности
    и записывает результат.
    """
    seqA, seqB = read_sequences(PATH)
    result = lcs_length(seqA, seqB)
    write_result(result, OUTPUT_PATH)

if __name__ == '__main__':
    task4()
