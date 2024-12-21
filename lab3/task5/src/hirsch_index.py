import sys

PATH = r"D:\algorithms-and-data-structures\lab3\task5\txtf\input.txt"
OUTPUT_PATH = r"D:\algorithms-and-data-structures\lab3\task5\txtf\output.txt"

def read_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        line = f.read().strip()
    # Заменим запятые на пробелы
    line = line.replace(',', ' ')
    arr = list(map(int, line.split()))
    return arr

def write_to_file(value, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(value))

def hirsch_index(citations):
    citations.sort(reverse=True)
    h = 0
    for i, c in enumerate(citations):
        if c >= i + 1:
            h = i + 1
        else:
            break
    return h

def task5():
    citations = read_from_file(PATH)
    h = hirsch_index(citations)
    write_to_file(h, OUTPUT_PATH)

if __name__ == '__main__':
    task5()
