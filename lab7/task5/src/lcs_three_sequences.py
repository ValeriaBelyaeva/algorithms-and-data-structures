# lab7/task5/src/lcs_three_sequences.py

import sys
import os

PATH = r"D:\algorithms-and-data-structures\lab7\task5\txtf\input.txt"
OUTPUT_PATH = r"D:\algorithms-and-data-structures\lab7\task5\txtf\output.txt"

def write_result(result, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(result))

def read_three_sequences(file_path):
    """
    Считывает три последовательности из файла:
      - n, затем n чисел (A)
      - m, затем m чисел (B)
      - l, затем l чисел (C)
    Возвращает (A, B, C)
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        n_line = f.readline().strip()
        n = int(n_line) if n_line else 0
        A = list(map(int, f.readline().strip().split())) if n>0 else []

        m_line = f.readline().strip()
        m = int(m_line) if m_line else 0
        B = list(map(int, f.readline().strip().split())) if m>0 else []

        l_line = f.readline().strip()
        l = int(l_line) if l_line else 0
        C = list(map(int, f.readline().strip().split())) if l>0 else []
    return A, B, C

def lcs_three_length(A, B, C):
    """
    Возвращает длину наибольшей общей подпоследовательности
    для трех последовательностей.
    """
    n = len(A)
    m = len(B)
    l = len(C)

    # dp[i][j][k] = LCS(A[:i], B[:j], C[:k])
    dp = [[[0]*(l+1) for _ in range(m+1)] for __ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            for k in range(1, l+1):
                if A[i-1] == B[j-1] == C[k-1]:
                    dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                else:
                    dp[i][j][k] = max(
                        dp[i-1][j][k],
                        dp[i][j-1][k],
                        dp[i][j][k-1]
                    )
    return dp[n][m][l]

def task5():
    A, B, C = read_three_sequences(PATH)
    result = lcs_three_length(A, B, C)
    write_result(result, OUTPUT_PATH)

if __name__ == '__main__':
    task5()
