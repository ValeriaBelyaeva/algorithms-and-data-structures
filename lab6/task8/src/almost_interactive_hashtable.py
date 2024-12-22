# lab5/task8/src/almost_interactive_hashtable.py

import sys
import os

PATH = r"D:\algorithms-and-data-structures\lab5\task8\txtf\input.txt"
OUTPUT_PATH = r"D:\algorithms-and-data-structures\lab5\task8\txtf\output.txt"

def task8():
    """
    Почти интерактивная хеш-таблица.
    Дано N, X, A, B, затем AC, BC, AD, BD.
    Нужно N раз:
      if X in table:
         A = (A + AC) mod 10^3
         B = (B + BC) mod 10^15
      else:
         add X to table
         A = (A + AD) mod 10^3
         B = (B + BD) mod 10^15
      X = (X*A + B) mod 10^15
    В конце вывести X, A, B.
    """
    with open(PATH, 'r', encoding='utf-8') as fin:
        line1 = fin.readline().strip().split()
        line2 = fin.readline().strip().split()
        # line1: N, X, A, B
        # line2: AC, BC, AD, BD
        N = int(line1[0])
        X = int(line1[1])
        A = int(line1[2])
        B = int(line1[3])

        AC = int(line2[0])
        BC = int(line2[1])
        AD = int(line2[2])
        BD = int(line2[3])

    modA = 10**3
    modB = 10**15

    # Храним посещенные X в set
    table = set()

    for _ in range(N):
        if X in table:
            A = (A + AC) % modA
            B = (B + BC) % modB
        else:
            table.add(X)
            A = (A + AD) % modA
            B = (B + BD) % modB
        X = (X * A + B) % modB

    with open(OUTPUT_PATH, 'w', encoding='utf-8') as fout:
        fout.write(f"{X} {A} {B}\n")

if __name__ == '__main__':
    task8()
