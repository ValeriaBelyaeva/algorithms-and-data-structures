# lab6/task4/src/threaded_map.py

import sys
import os

PATH = r"D:\algorithms-and-data-structures\lab6\task4\txtf\input.txt"
OUTPUT_PATH = r"D:\algorithms-and-data-structures\lab6\task4\txtf\output.txt"

class Node:
    """
    Узел 'ключ-значение' со ссылками на "соседей" в порядке вставки.
    """
    __slots__ = ['key', 'value', 'left_key', 'right_key']

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left_key = None
        self.right_key = None

def task4():
    """
    Прошитый ассоциативный массив.
    Операции:
      get x    -> вывести value или <none>
      prev x   -> вывести value ключа, вставленного "позже всех, но до x", или <none>
      next x   -> вывести value ключа, вставленного "раньше всех, но после x", или <none>
      put x y  -> если x не было, вставляем как последний, иначе обновляем значение
      delete x -> удалить x
    """
    # Словарь: key -> Node(key, value, left_key, right_key)
    store = {}
    # Два "указателя" на голову и хвост двусвязного списка вставленных ключей
    head_key = None
    tail_key = None

    with open(PATH, 'r', encoding='utf-8') as fin:
        n = int(fin.readline().strip())
        commands = [fin.readline().strip() for _ in range(n)]

    results = []
    for cmd in commands:
        parts = cmd.split()
        if not parts:
            continue
        op = parts[0]

        if op == 'put':
            # put x y
            x = parts[1]
            y = parts[2]
            if x in store:
                # обновляем значение, порядок не меняется
                store[x].value = y
            else:
                # вставляем новый узел
                node = Node(x, y)
                store[x] = node
                # Вставляем в конец
                if tail_key is None:
                    # список пуст
                    head_key = x
                    tail_key = x
                else:
                    # привязываем
                    store[tail_key].right_key = x
                    node.left_key = tail_key
                    tail_key = x

        elif op == 'delete':
            # delete x
            x = parts[1]
            if x in store:
                node = store[x]
                leftk = node.left_key
                rightk = node.right_key
                # Удаляем x из двусвязного списка
                if leftk is None:
                    # x был head
                    head_key = rightk
                else:
                    store[leftk].right_key = rightk
                if rightk is None:
                    # x был tail
                    tail_key = leftk
                else:
                    store[rightk].left_key = leftk
                # Удаляем из store
                del store[x]

        elif op == 'get':
            # get x
            x = parts[1]
            if x in store:
                results.append(store[x].value)
            else:
                results.append("<none>")

        elif op == 'prev':
            # prev x
            x = parts[1]
            if x not in store:
                results.append("<none>")
            else:
                leftk = store[x].left_key
                if leftk is None:
                    results.append("<none>")
                else:
                    results.append(store[leftk].value)

        elif op == 'next':
            # next x
            x = parts[1]
            if x not in store:
                results.append("<none>")
            else:
                rightk = store[x].right_key
                if rightk is None:
                    results.append("<none>")
                else:
                    results.append(store[rightk].value)

    with open(OUTPUT_PATH, 'w', encoding='utf-8') as fout:
        for r in results:
            fout.write(str(r) + '\n')

if __name__ == '__main__':
    task4()
