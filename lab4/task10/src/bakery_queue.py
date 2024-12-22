# lab4/task10/src/bakery_queue.py

import sys
import os

PATH = r"D:\algorithms-and-data-structures\lab4\task10\txtf\input.txt"
OUTPUT_PATH = r"D:\algorithms-and-data-structures\lab4\task10\txtf\output.txt"

def to_minutes(h, m):
    return h * 60 + m

def to_hm(minutes):
    # Возвращает (часы, минуты)
    return (minutes // 60, minutes % 60)

def task10():
    """
    В пекарне один продавец, тратит ровно 10 минут на покупателя.
    - Читаем N, затем N строк: часы, минуты, нетерпение
    - Если при приходе покупателя в очереди больше людей, чем его нетерпение,
      он уходит, и время ухода = время прихода.
    - Иначе он становится в очередь, дожидается, обслуживается 10 минут.
    - Вывести время ухода каждого покупателя (часы, минуты).
    """
    with open(PATH, 'r', encoding='utf-8') as f:
        N = int(f.readline().strip())
        customers = []
        for _ in range(N):
            line = f.readline().strip().split()
            h = int(line[0])
            mn = int(line[1])
            impatience = int(line[2])
            customers.append((h, mn, impatience))

    # Очередь будет хранить моменты начала обслуживания
    # Для каждого покупателя хранить время окончания обслуживания
    results = [None]*N

    # Время, когда освободится продавец (минуты от 0:00)
    # Если нет очереди, продавец ждет до прихода покупателя
    seller_free_at = 0

    # Будем хранить (индекс покупателя, время начала обслуживания) в очереди
    queue = []

    for i, (h, mn, imp) in enumerate(customers):
        arrive_time = to_minutes(h, mn)
        # Удалим из очереди всех, кто уже обслужен к моменту arrive_time
        # Но сервис заканчивается последовательно,
        # фактически будем проверять, сколько в очереди на момент прихода
        # queue содержит только тех, кто не обслужен + обслуживаемый
        # для упрощения можно просто смотреть длину очереди
        # (тот, кто обслуживается, тоже считается в очереди).
        queue_len = len(queue)

        if queue_len > imp:
            # Уходит
            # время ухода = время прихода
            results[i] = (h, mn)  # тот же момент
            continue

        # Иначе становится в очередь
        # Рассчитаем время начала обслуживания этого покупателя
        if not queue:
            # Продавец либо уже освободился, либо освободится раньше прихода
            start_service = max(seller_free_at, arrive_time)
        else:
            # Начнет обслуживаться после последнего в очереди
            # Последний в очереди начнет обслуживание: queue[-1][1]
            last_idx, last_start = queue[-1]
            # Его обслуживание закончится = last_start + 10
            # Значит наш покупатель сможет начать = last_start + 10
            start_service = last_start + 10

        # Добавляем в очередь
        queue.append((i, start_service))
        # Обновляем время, когда освободится продавец
        seller_free_at = start_service + 10

    # Теперь у нас в queue есть все покупатели, которые остались
    # (i, start_service). Их время завершения = start_service + 10
    for (i, start) in queue:
        finish = start + 10
        results[i] = to_hm(finish)

    # Запишем результаты
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as out_file:
        for (h, m) in results:
            out_file.write(f"{h} {m}\n")

if __name__ == '__main__':
    task10()
