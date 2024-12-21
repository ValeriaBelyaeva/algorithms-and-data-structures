import sys
import bisect

PATH = r"D:\algorithms-and-data-structures\lab3\task4\txtf\input.txt"
OUTPUT_PATH = r"D:\algorithms-and-data-structures\lab3\task4\txtf\output.txt"

def read_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        s, p = map(int, f.readline().split())
        intervals = []
        for _ in range(s):
            a, b = map(int, f.readline().split())
            intervals.append((a, b))
        points = list(map(int, f.readline().split()))
    return s, p, intervals, points

def write_to_file(counts, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(' '.join(map(str, counts)))

def points_and_segments(s, p, intervals, points):
    starts = sorted(iv[0] for iv in intervals)
    ends = sorted(iv[1] for iv in intervals)
    result = []
    for x in points:
        c_in = bisect.bisect_right(starts, x)
        c_out = bisect.bisect_left(ends, x)
        result.append(c_in - c_out)
    return result

def task4():
    s, p, intervals, points = read_from_file(PATH)
    res = points_and_segments(s, p, intervals, points)
    write_to_file(res, OUTPUT_PATH)

if __name__ == '__main__':
    task4()
