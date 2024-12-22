## Очередь с минимумом
 Реализуйте работу очереди. В дополнение к стандартным операциям очереди,
 необходимо также отвечать на запрос о минимальном элементе из тех, которые
 сейчас находится вочереди. Длякаждойоперациизапросаминимальногоэлемен
та выведите ее результат.
 На вход программе подаются строки, содержащие команды. Каждая строка
 содержит одну команду. Команда– это либо «+ N», либо «–», либо «?». Команда
 «+ N»означает добавление в очередь числа N, по модулю не превышающего 109.
 Команда«–»означает изъятие элемента из очереди. Команда «?» означает запрос
 на поиск минимального элемента в очереди.
 • Форматвходного файла (input.txt). В первой строке содержится M (1 ≤
 M≤106)–числокоманд.Впоследующихстрокахсодержатсякоманды,по
 одной в каждой строке.
 • Формат выходного файла (output.txt). Для каждой операции поиска ми
нимумавочередивыведитееёрезультат.Результатыдолжныбытьвыведены
 в том порядке, в котором эти операции встречаются во входном файле. Га
рантируется, что операций извлечения или поиска минимума для пустой
 очереди не производится.
 • Ограничение по времени. 2 сек.
 • Ограничение по памяти. 256 мб