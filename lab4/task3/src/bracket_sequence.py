# lab4/task3/src/bracket_sequence.py

import sys
import os

PATH = r"D:\algorithms-and-data-structures\lab4\task3\txtf\input.txt"
OUTPUT_PATH = r"D:\algorithms-and-data-structures\lab4\task3\txtf\output.txt"

def read_sequences(file_path):
    """
    Считывает из файла:
      - N: количество скобочных последовательностей
      - N строк со скобочными последовательностями.
    Возвращает список этих последовательностей.
    """
    sequences = []
    with open(file_path, 'r', encoding='utf-8') as file:
        N = int(file.readline().strip())
        for _ in range(N):
            seq = file.readline().strip()
            sequences.append(seq)
    return sequences


def is_correct_bracket_sequence(seq):
    """
    Проверяет, является ли seq правильной скобочной последовательностью
    из символов '(', ')', '[' и ']'.
    """
    stack = []
    pairs = {')': '(', ']': '['}
    for ch in seq:
        if ch in ('(', '['):
            stack.append(ch)
        elif ch in (')', ']'):
            if not stack:
                return False
            top = stack.pop()
            if pairs[ch] != top:
                return False
        else:
            # Недопустимые символы, по условию задачи не встречаются
            return False
    return len(stack) == 0


def task3():
    """
    Считывает N скобочных последовательностей, для каждой
    выводит YES или NO.
    """
    sequences = read_sequences(PATH)
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as out_file:
        for seq in sequences:
            if is_correct_bracket_sequence(seq):
                out_file.write("YES\n")
            else:
                out_file.write("NO\n")

if __name__ == '__main__':
    task3()
