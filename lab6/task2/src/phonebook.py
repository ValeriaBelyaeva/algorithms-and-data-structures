# lab5/task2/src/phonebook.py

import sys
import os

# Глобальные пути к входному/выходному файлам
PATH = r"D:\algorithms-and-data-structures\lab5\task2\txtf\input.txt"
OUTPUT_PATH = r"D:\algorithms-and-data-structures\lab5\task2\txtf\output.txt"

def task2():
    """
    Реализовать телефонную книгу с операциями:
      - add number name
      - del number
      - find number -> выводим имя или "not found"
    """
    phonebook = {}

    with open(PATH, 'r', encoding='utf-8') as fin:
        n = int(fin.readline().strip())
        commands = [fin.readline().strip() for _ in range(n)]

    results = []
    for cmd in commands:
        parts = cmd.split()
        if not parts:
            continue
        op = parts[0]
        if op == 'add':
            # add number name
            # number - строка из цифр (до 7 длиной)
            # name - строка (латинские буквы, до 15 длиной)
            number = parts[1]
            name = parts[2]
            phonebook[number] = name
        elif op == 'del':
            # del number
            number = parts[1]
            if number in phonebook:
                del phonebook[number]
        elif op == 'find':
            # find number
            number = parts[1]
            if number in phonebook:
                results.append(phonebook[number])
            else:
                results.append("not found")

    with open(OUTPUT_PATH, 'w', encoding='utf-8') as fout:
        for res in results:
            fout.write(res + '\n')

if __name__ == '__main__':
    task2()
