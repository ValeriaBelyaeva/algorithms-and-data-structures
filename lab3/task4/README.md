##  Точки и отрезки
 Допустим, вы организовываете онлайн-лотерею. Для участия нужно сделать
 ставку на одно целое число. При этом у вас есть несколько интервалов после
довательных целых чисел. В этом случае выигрыш участника пропорционален
 количеству интервалов, содержащих номер участника, минус количество интер
валов, которые его не содержат. (В нашем случае для начала- подсчет только
 количества интервалов, содержащих номер участника). Вам нужен эффективный
 алгоритм для расчета выигрышей для всех участников. Наивный способ сделать
 это- просто просканировать для всех участников список всех интевалов. Однако
 ваша лотерея очень популярна: у вас тысячи участников и тысячи интервалов. По
 этой причине вы не можете позволить себе медленный наивный алгоритм.
 