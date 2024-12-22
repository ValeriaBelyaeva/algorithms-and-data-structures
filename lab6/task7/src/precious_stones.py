# lab5/task7/src/precious_stones.py

import sys
import os

PATH = r"D:\algorithms-and-data-structures\lab5\task7\txtf\input.txt"
OUTPUT_PATH = r"D:\algorithms-and-data-structures\lab5\task7\txtf\output.txt"

def task7():
    """
    Дано:
      - n, k
      - строка S (длина n)
      - k "красивых" пар (a_i, b_i)
    Нужно найти количество пар (i, j), i < j, таких что (S[i], S[j]) == (a_i, b_i)
    для некоторого i в [1..k].
    """
    with open(PATH, 'r', encoding='utf-8') as f:
        line = f.readline().strip()
        n, k = map(int, line.split())
        S = f.readline().strip()

        # pairs_for[b] = список (или множество) символов a, для которых (a,b) - красивая пара
        from collections import defaultdict
        pairs_for = defaultdict(list)

        for _ in range(k):
            pair_str = f.readline().strip()
            if len(pair_str) == 2:
                a = pair_str[0]
                b = pair_str[1]
                pairs_for[b].append(a)

    # Будем идти слева направо, хранить частоты символов (freq) - сколько раз мы видели каждый символ
    # Когда видим S[j] = c, суммируем freq[a] для всех a in pairs_for[c].
    # Затем freq[S[j]]++.
    freq = [0]*26
    def idx(ch):
        return ord(ch) - ord('a')

    result = 0
    for ch in S:
        b_index = idx(ch)
        if ch in pairs_for:
            # для каждой a in pairs_for[ch], прибавим freq[a]
            for a_char in pairs_for[ch]:
                result += freq[idx(a_char)]
        freq[b_index] += 1

    with open(OUTPUT_PATH, 'w', encoding='utf-8') as out_file:
        out_file.write(str(result))

if __name__ == '__main__':
    task7()
