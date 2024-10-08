# Линейный поиск
### Описание
Этот код на Python реализует алгоритм линейного поиска — простой алгоритм поиска в листе.
Выводит индексы искомого эл-та в листе

## Структура проекта
  - `src/` — исходные коды и файлы ввода/вывода.
  - `tests/` — тесты.

## Запуск задачи
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ValeriaBelyaeva/algorithms-and-data-structures
   ```
2. Раскомментируйте код в файле Linear_search.py:
   ```Python
    inp_file = open("input")  # Open input file
    search_list = list(map(int, inp_file.readline().split()))  # Read the first line as a list of integers
    target = int(inp_file.readline())  # Read the second line as an integer
    inp_file.close()  # Close input file
    out_file = open("output", 'w')  # Open output file in write mode
    try:
        ans = linear_search(target, search_list)  # Call linear_search function
        out = ''  # Initialize an empty string for output
        for e in ans:  # Iterate through the result list
            out = out + str(e) + ' '  # Append each index to the output string
        out_file.write(out)  # Write the output string to the output file
    except:
        print('we have egor :(')  # Handle potential exceptions
    out_file.close()  # Close output file
   ```
   
3. Введите входные данные в 
   ```bash
   lab1/task4/src/input
   ```
4. Запустите:
   ```bash
   lab1/task4/src/Linear_search.py
   ```

## Тестирование

Для каждой задачи написаны тесты с использованием библиотеки `unittest`. 
Для запуска:

1. Запустите файл для тестирования:
   ```bash
   lab1/task4/tests/Linear_search_test.py
   ```