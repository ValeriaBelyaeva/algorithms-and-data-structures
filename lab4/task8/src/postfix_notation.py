# lab4/task8/src/postfix_notation.py

import sys
import os

PATH = r"D:\algorithms-and-data-structures\lab4\task8\txtf\input.txt"
OUTPUT_PATH = r"D:\algorithms-and-data-structures\lab4\task8\txtf\output.txt"

def evaluate_postfix(expression):
    """
    Вычисляет значение выражения в обратной польской записи.
    expression — список элементов (числа или операторы '+', '-', '*').
    """
    stack = []
    for token in expression:
        if token.isdigit():
            # Однозначные неотрицательные числа (по условию)
            stack.append(int(token))
        else:
            # Операция
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                res = a + b
            elif token == '-':
                res = a - b
            elif token == '*':
                res = a * b
            else:
                # По условию других операций не бывает
                raise ValueError("Unknown operator")
            stack.append(res)
    return stack.pop()

def read_postfix(file_path):
    """
    Считывает из файла:
      - N: число элементов выражения
      - строку из N элементов (числа или '+', '-', '*'),
        разделённых пробелом.
    Возвращает список из этих N элементов (строк).
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        N = int(f.readline().strip())
        expression = f.readline().strip().split()
        # Проверим длину на всякий случай
        assert len(expression) == N
    return expression

def task8():
    """
    Считывает выражение в постфиксной записи, вычисляет и выводит результат.
    """
    expression = read_postfix(PATH)
    result = evaluate_postfix(expression)
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as out_file:
        out_file.write(str(result))

if __name__ == '__main__':
    task8()
