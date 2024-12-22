# lab6/task1/src/set.py

import sys
import os

# Глобальные пути к входному/выходному файлам
PATH = r"D:\algorithms-and-data-structures\lab6\task1\txtf\input.txt"
OUTPUT_PATH = r"D:\algorithms-and-data-structures\lab6\task1\txtf\output.txt"

def task1():
    """
    Реализовать множество с операциями:
     - A x: Добавить x в множество
     - D x: Удалить x из множества
     - ? x: Проверить, есть ли x в множестве -> вывести 'Y' или 'N'
    """
    # Для удобства и скорости используем встроенное множество Python
    s = set()

    with open(PATH, 'r', encoding='utf-8') as file_in:
        n = int(file_in.readline().strip())  # число операций
        commands = []
        for _ in range(n):
            line = file_in.readline().strip()
            commands.append(line)

    with open(OUTPUT_PATH, 'w', encoding='utf-8') as file_out:
        for cmd in commands:
            parts = cmd.split()
            if len(parts) < 2:
                continue
            op = parts[0]
            x_str = parts[1]
            if op == 'A':  # Добавить
                # x может быть очень большим (до 10^18 по модулю),
                # но Python int справится
                x = int(x_str)
                s.add(x)
            elif op == 'D':  # Удалить
                x = int(x_str)
                if x in s:
                    s.remove(x)
            elif op == '?':  # Проверить
                x = int(x_str)
                file_out.write('Y\n' if x in s else 'N\n')

if __name__ == '__main__':
    task1()
