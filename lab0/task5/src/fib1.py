
from sys import getsizeof
import time
t_start = time.perf_counter()
f = open("input")
fl = open("output", 'w')
for i in f.readlines():
    n = int(i)
    fib = [0 for i in range(n+2)]
    fib[1] = 1
    for i in range(2, n+1):
        fib[i] = fib[i-1]+fib[i-2]

    fl.write(str(fib[n])+"\n")
    print(getsizeof(fib) + getsizeof(n)+ getsizeof(t_start))
    print(f"ремя работы кода:{time.perf_counter() - t_start}")