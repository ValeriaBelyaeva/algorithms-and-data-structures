# lab5/task3/src/network_packets.py

import sys
import os
from collections import deque

PATH = r"D:\algorithms-and-data-structures\lab5\task3\txtf\input.txt"
OUTPUT_PATH = r"D:\algorithms-and-data-structures\lab5\task3\txtf\output.txt"

def read_packets(file_path):
    """
    Считывает:
      - S, n
      - далее n строк: время прибытия Ai, время обработки Pi
    Возвращает (S, packets), где packets - список (Ai, Pi).
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        line = f.readline().strip().split()
        S = int(line[0])
        n = int(line[1])
        packets = []
        for _ in range(n):
            A, P = map(int, f.readline().split())
            packets.append((A, P))
    return S, packets

def simulate_network(S, packets):
    """
    Моделирует обработку пакетов:
      - Размер буфера = S
      - Если буфер полон при приходе пакета, пакет отбрасывается (res=-1)
      - Иначе помещаем в очередь (finish_time)
      - Для каждого пакета вычислить время начала обработки или -1
    Возвращает список времен начала обработки в том же порядке.
    """
    # finish_time будет хранить время, когда завершится пакет
    # который в данный момент в буфере.
    from collections import deque
    finish_times = deque()
    results = [-1]*len(packets)

    # Время окончания обработки последнего пакета в очереди
    # (будем хранить для каждого пакета)
    for i, (arrival, processing) in enumerate(packets):
        # Удаляем из начала finish_times пакеты, которые завершатся раньше arrival
        while finish_times and finish_times[0] <= arrival:
            finish_times.popleft()

        # Если буфер полон, пакет отбрасывается
        if len(finish_times) == S:
            results[i] = -1
            continue

        # Если буфер пуст, начинаем обрабатывать пакет в момент arrival
        if not finish_times:
            start = arrival
        else:
            # Иначе начинаем после последнего в finish_times
            start = finish_times[-1]

        results[i] = start
        finish_times.append(start + processing)

    return results

def task3():
    """
    Читает входные данные, моделирует обработку, выводит время начала обработки
    или -1.
    """
    S, packets = read_packets(PATH)
    results = simulate_network(S, packets)
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as out_file:
        for r in results:
            out_file.write(str(r) + '\n')

if __name__ == '__main__':
    task3()
