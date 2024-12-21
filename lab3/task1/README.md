## Улучшение Quick sort
1. Используя псевдокод процедуры Randomized - QuickSort, а так же Partition
из презентации к Лекции 3 (страницы 8 и 12), напишите программу быстрой
сортировки на Python и проверьте ее, создав несколько рандомных массивов,
подходящих под параметры:
• Формат входного файла (input.txt). В первой строке входного файла
содержится число n (1 ≤ n ≤ 104
) — число элементов в массиве.
Во второй строке находятся n различных целых чисел, по модулю не
превосходящих 109
.
• Формат выходного файла (output.txt). Одна строка выходного файла
с отсортированным массивом. Между любыми двумя числами должен
стоять ровно один пробел.
• Ограничение по времени. 2 сек.
• Ограничение по памяти. 256 мб.
• Для проверки можно выбрать наихудший случай, когда сортируется
массив рамера 103
, 104
, 105 чисел порядка 109
, отсортированных в обратном порядке; наилучший, когда массив уже отсортирван, и средний
- случайный. Сравните на данных сетах Randomized-QuickSort и простой QuickSort. (А также есть Median-QuickSort, см. задание 10.2;
и Tail-Recursive-QuickSort, см. Кормен. 2013, стр. 217)