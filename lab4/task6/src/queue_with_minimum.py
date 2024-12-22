# lab4/task6/src/queue_with_minimum.py

import sys
import os
from collections import deque

PATH = r"D:\algorithms-and-data-structures\lab4\task6\txtf\input.txt"
OUTPUT_PATH = r"D:\algorithms-and-data-structures\lab4\task6\txtf\output.txt"


def read_commands(file_path):
    """
    Считывает команды из файла.
    Первая строка: M — число команд
    Далее M строк.
    Команды:
      '+ N' — добавить N
      '-'   — извлечь из очереди
      '?'   — вывести текущий минимум
    """
    commands = []
    with open(file_path, 'r', encoding='utf-8') as f:
        M = int(f.readline().strip())
        for _ in range(M):
            line = f.readline().strip()
            commands.append(line)
    return commands


class MinQueue:
    """
    Очередь, поддерживающая операции:
      - push(x)
      - pop()
      - get_min()
    за амортизированное O(1) время.
    """
    def __init__(self):
        self.queue = deque()
        self.min_deque = deque()  # хранит кандидатов на минимум

    def push(self, x):
        self.queue.append(x)
        # Удаляем из min_deque все элементы, которые больше x
        # т.к. они не могут быть минимумом, если есть x
        while self.min_deque and self.min_deque[-1] > x:
            self.min_deque.pop()
        self.min_deque.append(x)

    def pop(self):
        val = self.queue.popleft()
        if self.min_deque and self.min_deque[0] == val:
            self.min_deque.popleft()
        return val

    def get_min(self):
        return self.min_deque[0] if self.min_deque else None


def task6():
    """
    Реализует работу очереди с минимумом.
    Для каждой операции '?' выводит текущий минимум в выходной файл.
    """
    commands = read_commands(PATH)
    q = MinQueue()

    with open(OUTPUT_PATH, 'w', encoding='utf-8') as out_file:
        for cmd in commands:
            if cmd.startswith('+'):
                # '+ N'
                _, val = cmd.split()
                val = int(val)
                q.push(val)
            elif cmd == '-':
                q.pop()
            elif cmd == '?':
                out_file.write(str(q.get_min()) + '\n')


if __name__ == '__main__':
    task6()
