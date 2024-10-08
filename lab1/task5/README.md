#Сортировка выбором.
###Описание
Этот код на Python реализует алгоритм сортировки выбором — простой алгоритм сортировк.
Упорядочивает элементы по возрастанию 

##Структура проекта
  - `src/` — исходные коды и файлы ввода/вывода.
  - `tests/` — тесты.

##Запуск задачи
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ValeriaBelyaeva/algorithms-and-data-structures
   ```
2. Раскомментируйте код в файле selection_sort.py:
   ```Python
   inp_file = open("input")  # Open input file
   inp = list(map(int, inp_file.readline().split()))  # Read the first line as a list of integers
   inp_file.close()  # Close input file
   out_file = open("output", 'w')  # Open output file in write mode
   try:
      ans = selection_sort(inp)  # Call selection_sort function
      out = ''  # Initialize an empty string for output
      for e in ans:  # Iterate through the result list
         out = out + str(e) + ' '  # Append each element to the output string
      out_file.write(out)  # Write the output string to the output file
   except:
      print('we have egor :(')  # Handle potential exceptions
   out_file.close()  # Close output file
   ```
3. Введите входные данные в 
   ```bash
   lab1/task5/src/input
   ```
4. Запустите:
   ```bash
   lab1/task5/src/selection_sort.py
   ```

## Тестирование

Для каждой задачи написаны тесты с использованием библиотеки `unittest`. 
Для запуска:

1. Запустите файл для тестирования:
   ```bash
   lab1/task5/tests/selection_sort.py
   ```