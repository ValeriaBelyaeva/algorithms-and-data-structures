# Сортировка вставкой+
### Описание
Этот код на Python реализует алгоритм сортировки вставками — простой алгоритм сортировк.
Также он возвращает лист индексов, на которые ставились 

## Структура проекта
  - `src/` — исходные коды и файлы ввода/вывода.
  - `tests/` — тесты.

## Запуск задачи
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ValeriaBelyaeva/algorithms-and-data-structures
   ```
2. Раскомментируйте код в файле insertion_sort_plus.py
   ```Python
    inp_file = open("input")  # Open input file
    inp = list(map(int, inp_file.readline().split()))  # Read the first line as a list of integers
    inp_file.close()  # Close input file
    out_file = open("output", 'w')  # Open output file in write mode
    try:
        ans1, ans2 = insertion_sort(inp)  # Call insertion_sort function
        out1 = ''  # Initialize an empty string for the first output
        for e in ans1:  # Iterate through the first result list (swap indices)
            out1 = out1 + str(e) + ' '  # Append each swap index to the first output string
        out2 = ''  # Initialize an empty string for the second output
        for e in ans2:  # Iterate through the second result list (sorted list)
            out2 = out2 + str(e) + ' '  # Append each sorted element to the second output string
        out_file.write(out1 + '\n' + out2)  # Write both output strings to the file, separated by a newline
    except:
        print('we have egor :(')  # Handle potential exceptions
    out_file.close()  # Close output file
   ```
3. Введите входные данные в 
   ```bash
   lab1/task2/src/input
   ```
4. Запустите:
      ```bash
      lab1/task2/src/insertion_sort_plus.py
      ```

## Тестирование

Для каждой задачи написаны тесты с использованием библиотеки `unittest`. 
Для запуска:

1. Запустите файл для тестирования:
   ```bash
   lab1/task2/tests/insertion_sort_plus_test.py
   ```