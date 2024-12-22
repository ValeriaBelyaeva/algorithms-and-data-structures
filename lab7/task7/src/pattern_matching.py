# lab7/task7/src/pattern_matching.py

import sys
import os

PATH = r"D:\algorithms-and-data-structures\lab7\task7\txtf\input.txt"
OUTPUT_PATH = r"D:\algorithms-and-data-structures\lab7\task7\txtf\output.txt"

def match_pattern(pattern, text):
    """
    Проверка, подходит ли text под pattern, где:
      '?' соответствует ровно одному символу,
      '*' соответствует произвольной (включая пустую) подстроке,
      остальные символы - точное совпадение.
    """
    # Реализуем классический алгоритм с динамическим программированием
    # dp[i][j] = подходит ли pattern[:i] к text[:j]
    # размеры (len(pattern)+1) x (len(text)+1)
    p = len(pattern)
    t = len(text)
    dp = [[False]*(t+1) for _ in range(p+1)]

    # Пустой шаблон соотв. пустой строке
    dp[0][0] = True

    # Если в начале идут '*', они могут соответствовать пустой подстроке
    for i in range(1, p+1):
        if pattern[i-1] == '*':
            dp[i][0] = dp[i-1][0]
        else:
            break

    for i in range(1, p+1):
        for j in range(1, t+1):
            if pattern[i-1] == text[j-1] or (pattern[i-1] == '?' and text[j-1] != ''):
                dp[i][j] = dp[i-1][j-1]
            elif pattern[i-1] == '*':
                # '*' может соответствовать нулю или многим символам
                dp[i][j] = dp[i-1][j] or dp[i][j-1]
            else:
                dp[i][j] = False

    return dp[p][t]

def task7():
    with open(PATH, 'r', encoding='utf-8') as f:
        pattern = f.readline().rstrip('\n')
        text = f.readline().rstrip('\n')

    result = match_pattern(pattern, text)

    with open(OUTPUT_PATH, 'w', encoding='utf-8') as out:
        out.write("YES\n" if result else "NO\n")

if __name__ == '__main__':
    task7()
