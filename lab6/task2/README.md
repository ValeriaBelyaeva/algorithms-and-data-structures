##  Телефонная книга
 В этой задаче ваша цель- реализовать простой менеджер телефонной книги.
 Он должен уметь обрабатывать следующие типы пользовательских запросов:
 • add number name– это команда означает, что пользователь добавляет в
 телефонную книгу человека с именем name и номером телефона number.
 Если пользователь с таким номером уже существует, то ваш менеджер дол
жен перезаписать соответствующее имя.
 • del number– означает, что менеджер должен удалить человека с номе
ром из телефонной книги. Если такого человека нет, то он должен просто
 игнорировать запрос.
 • find number– означает, что пользователь ищет человека с номером те
лефона number. Менеджер должен ответить соответствующим именем или
 строкой «not found» (без кавычек), если такого человека в книге нет.
 • Формат ввода / входного файла (input.txt). В первой строке входного
 файла содержится число N (1 ≤ N ≤ 105)- количество запросов. Далее
 следуют N строк, каждая из которых содержит один запрос в формате,
 описанном выше.
 Всеномерателефоновсостоятиздесятичныхцифр,внихнетнулейвначале
 номера, и каждый состоит не более чем из 7 цифр. Все имена представляют
 собой непустые строки из латинских букв, каждая из которых имеет длину
 не более 15. Гарантируется при проверке, что не будет человека с именем
 «not found».
 • Форматвывода/выходного файла (output.txt). Выведите результат каж
дого поискового запроса find– имя, соответствующее номеру телефона,
 или «not found» (без кавычек), если в телефонной книге нет человека с та
ким номером телефона. Выведите по одному результату в каждой строке в
 том же порядке, как были заданы запросы типа find во входных данных.
 • Ограничение по времени. 6 сек.
 • Ограничение по памяти. 512 мб.