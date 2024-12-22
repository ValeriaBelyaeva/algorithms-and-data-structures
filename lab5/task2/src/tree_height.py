# lab5/task2/src/tree_height.py

import sys
import os
import sys
sys.setrecursionlimit(10**7)

PATH = r"D:\algorithms-and-data-structures\lab5\task2\txtf\input.txt"
OUTPUT_PATH = r"D:\algorithms-and-data-structures\lab5\task2\txtf\output.txt"

def read_parents(file_path):
    """
    Считывает:
      - n: число узлов
      - список из n целых чисел parents[], где parents[i] - родитель i-го узла,
        -1, если i - корень
    Возвращает (n, parents).
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        n = int(f.readline().strip())
        parents = list(map(int, f.readline().split()))
    return n, parents

def compute_height(n, parents):
    """
    Вычисляет высоту дерева, заданного списком parents.
    parents[i] = -1 => i - корневой узел.
    Иначе parents[i] = parent_index.
    """
    # Строим список children: children[u] = список детей узла u
    children = [[] for _ in range(n)]
    root = None
    for i in range(n):
        p = parents[i]
        if p == -1:
            root = i
        else:
            children[p].append(i)

    # Считаем высоту дерева (глубина) - итеративно или рекурсивно
    # Чтобы избежать переполнения стека при глубоком дереве, можно
    # сделать итеративный DFS или BFS.

    # Реализуем BFS для вычисления высоты:
    from collections import deque
    q = deque()
    q.append((root, 1))  # (node, depth)
    max_depth = 1

    while q:
        node, depth = q.popleft()
        max_depth = max(max_depth, depth)
        for c in children[node]:
            q.append((c, depth + 1))

    return max_depth

def task2():
    """
    Считывает описание дерева, вычисляет его высоту,
    выводит это число.
    """
    n, parents = read_parents(PATH)
    h = compute_height(n, parents)
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as out_file:
        out_file.write(str(h) + '\n')

if __name__ == '__main__':
    task2()
