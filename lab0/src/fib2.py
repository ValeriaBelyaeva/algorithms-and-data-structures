import time
from sys import getsizeof
f = open("input")
fl = open("output", 'w')
for i in f.readlines():

    t_start = time.perf_counter()
    n = int(i)

    a, b = 0, 1
    for i in range(2, n+1):
        a, b = b, (a+b)%100

    fl.write(str(b%10)+'\n')
    print(f"ремя работы кода:{time.perf_counter() - t_start}")