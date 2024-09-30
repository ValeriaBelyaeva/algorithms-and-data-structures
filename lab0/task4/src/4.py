import time
t_start = time.perf_counter()
f = open("input")
fl = open("output", 'w')
for i in f.readlines():
    a, b = map(int, f.readline().split())
    fl.write(str(a+b**2))
    print(f"ремя работы кода:{time.perf_counter() - t_start}")