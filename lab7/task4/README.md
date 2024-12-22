## Скобочная последовательность. Версия 1
 Последовательность A, состоящую из символов из множества «(», «)», «[» и
 «]», назовем правильной скобочной последовательностью, если выполняется
 одно из следующих утверждений:
 • A–пустая последовательность;
 • первыйсимволпоследовательностиA–это«(»,ивэтойпоследовательности
 существует такой символ «)», что последовательность можно представить
 как A =(B)C,где B иC–правильные скобочные последовательности;
 • первыйсимволпоследовательностиA–это«[»,ивэтойпоследовательности
 существует такой символ «]», что последовательность можно представить
 как A =(B)C,где B иC–правильные скобочные последовательности.
 Так, например, последовательности «(())» и «()[]» являются правильными ско
бочными последовательностями, а последовательности «[)» и «((» таковыми не
 являются.
 Входной файл содержит несколько строк, каждая из которых содержит после
довательность символов «(», «)», «[» и «]». Для каждой из этих строк выясните,
 является ли она правильной скобочной последовательностью.
 • Формат входного файла (input.txt). Первая строка входного файла со
держит число N (1 ≤ N ≤ 500)– число скобочных последовательностей,
 которые необходимо проверить. Каждая из следующих N строк содержит
 скобочную последовательность длиной от 1 до 104 включительно. В каж
дой из последовательностей присутствуют только скобки указанных выше
 видов.
 3
• Форматвыходногофайла(output.txt).Длякаждойстрокивходногофайла
 (кроме первой, в которой записано число таких строк) выведите в выходной
 файл «YES», если соответствующая последовательность является правиль
ной скобочной последовательностью, или «NO», если не является.
 • Ограничение по времени. 2 сек.
 • Ограничение по памяти. 256 мб