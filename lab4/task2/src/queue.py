# lab4/task2/src/queue.py

import sys
import os

# Глобальные пути к входному/выходному файлам
PATH = r"D:\algorithms-and-data-structures\lab4\task2\txtf\input.txt"
OUTPUT_PATH = r"D:\algorithms-and-data-structures\lab4\task2\txtf\output.txt"


def read_commands(file_path):
    """
    Считывает команды для очереди из файла.
    Первая строка: M — число команд.
    Далее M строк, каждая строка — команда.
    Команда может быть:
      '+ N' — добавить число N в очередь
      '-'   — извлечь элемент из очереди
    Возвращает список команд.
    """
    commands = []
    with open(file_path, 'r', encoding='utf-8') as file:
        M = int(file.readline().strip())
        for _ in range(M):
            line = file.readline().strip()
            commands.append(line)
    return commands


def task2():
    """
    Реализует работу обычной очереди.
    Для каждой операции '-' выводит результат изъятия элемента.
    """
    commands = read_commands(PATH)
    from collections import deque

    queue = deque()

    # Открываем файл для записи результатов
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as out_file:
        for cmd in commands:
            if cmd.startswith('+'):
                # Формат: "+ N"
                _, val = cmd.split()
                val = int(val)
                queue.append(val)
            elif cmd == '-':
                # Изъятие из очереди
                popped = queue.popleft()
                out_file.write(str(popped) + '\n')


if __name__ == '__main__':
    task2()
