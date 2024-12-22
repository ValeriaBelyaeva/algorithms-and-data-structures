# lab4/task9/src/clinic_queue.py

import sys
import os

PATH = r"D:\algorithms-and-data-structures\lab4\task9\txtf\input.txt"
OUTPUT_PATH = r"D:\algorithms-and-data-structures\lab4\task9\txtf\output.txt"

def task9():
    """
    Реализует очередь по особым правилам:
      + i  -> пациент i встает в конец очереди
      * i  -> пациент i встает в середину очереди
      -    -> из головы очереди пациент заходит к врачу (выводим его номер)
    Правило "середины":
      - при нечетной длине очереди вставать сразу за центром
      - при четной длине вставать в точный центр
    """
    with open(PATH, 'r', encoding='utf-8') as f:
        n = int(f.readline().strip())
        # Используем 2 deques для эффективной вставки в середину
        from collections import deque
        left = deque()
        right = deque()

        with open(OUTPUT_PATH, 'w', encoding='utf-8') as out_file:
            for _ in range(n):
                cmd = f.readline().strip()
                if cmd.startswith('+'):
                    # формат "+ i"
                    _, val = cmd.split()
                    val = int(val)
                    # в конец -> right
                    right.append(val)
                    # Поправим баланс, чтобы длины отличались не более чем на 1
                    if len(right) > len(left):
                        left.append(right.popleft())

                elif cmd.startswith('*'):
                    # формат "* i"
                    _, val = cmd.split()
                    val = int(val)
                    # вставка в середину
                    # хотим, чтобы элемент попал в конец левой части
                    left.append(val)
                    # баланс
                    if len(left) > len(right) + 1:
                        right.appendleft(left.pop())

                elif cmd == '-':
                    # извлекаем из головы
                    # голова очереди — это left[0], если left не пуст
                    if left:
                        popped = left.popleft()
                        # балансируем
                        if len(right) > len(left):
                            left.append(right.popleft())
                    else:
                        popped = right.popleft()
                    out_file.write(str(popped) + '\n')

if __name__ == '__main__':
    task9()
