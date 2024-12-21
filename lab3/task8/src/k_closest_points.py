import sys

PATH = r"D:\algorithms-and-data-structures\lab3\task8\txtf\input.txt"
OUTPUT_PATH = r"D:\algorithms-and-data-structures\lab3\task8\txtf\output.txt"

def read_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        line = f.readline().split()
        n, K = int(line[0]), int(line[1])
        points = []
        for _ in range(n):
            x, y = map(int, f.readline().split())
            points.append((x, y))
    return n, K, points

def write_to_file(kpoints, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(','.join(f"[{x},{y}]" for x, y in kpoints))

def k_closest_points(n, K, points):
    points.sort(key=lambda p: p[0]*p[0] + p[1]*p[1])
    return points[:K]

def task8():
    n, K, points = read_from_file(PATH)
    result = k_closest_points(n, K, points)
    write_to_file(result, OUTPUT_PATH)

if __name__ == '__main__':
    task8()
