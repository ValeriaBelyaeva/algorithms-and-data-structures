##  В одной далекой восточной стране до сих пор по пустыням ходят караваны
 верблюдов, с помощью которых купцы перевозят пряности, драгоценности и до
рогие ткани. Разумеется, основная цель купцов состоит в том, чтобы подороже
 продать имеющийся у них товар. Недавно один из караванов прибыл во дворец
 одного могущественного шаха.
 Купцыхотят продать шаху nдрагоценных камней, которые они привезли с со
бой. Для этого они выкладывают их перед шахомвряд, после чего шахоценивает
 эти камни и принимает решение о том, купит он их или нет. Видов драгоценных
 камней на Востоке известно не очень много всего 26, поэтому мы будем обозна
чать виды камней с помощью строчных букв латинского алфавита. Шах обычно
 оценивает камни следующим образом. Он заранее определил несколько упоря
доченных пар типов камней: (a1,b1), (a2,b2), ..., (ak,bk). Эти пары он называет
 красивыми, их множество мы обозначим как P. Теперь представим ряд камней,
 которые продают купцы, в виде строки S длины n из строчных букв латинского
 алфавита. Шах считает число таких пар (i,j), что 1 ≤ i < j ≤ n, а камни Si и Sj
 образуют красивую пару, то есть существует такое число 1 ≤ q ≤ k, что Si = aq
 и Sj =bq.
 Если число таких пар оказывается достаточно большим, то шах покупает все
 камни. Однако в этот раз купцы привезли настолько много камней, что шах не
 может посчитать это число. Поэтому он вызвал своего визиря и поручил ему этот
 подсчет. Напишите программу, которая находит ответ на эту задачу.
 • Форматввода/входногофайла(input.txt).Перваястрокавходногофайла
 содержит целые числа n и k (1 ≤ n ≤ 100000,1 ≤ k ≤ 676)–числокамней,
 которые привезли купцы ичислопар,которыешахсчитаеткрасивыми.Вто
рая строка входного файла содержит строку S, описывающую типы камней,
 которые привезли купцы.
 Далее следуют k строк, каждая из которых содержит две строчных буквы
 латинского алфавита и описывает одну из красивых пар камней.
 • Формат вывода / выходного файла (output.txt). В выходной файл выве
дите ответ на задачу– количество пар, которое должен найти визирь.
 • Ограничение по времени. 1 сек.
 • Ограничение по памяти. 64 мб.