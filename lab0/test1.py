from sys import getsizeof
import time
f = open("input")
fl = open("output", 'w')
for i in f.readlines():
    t_start2 = time.perf_counter()
    t_start = time.perf_counter()
    n = int(i)

    fib = [0 for i in range(n+2)]
    fib[1] = 1
    for i in range(2, n+1):
        fib[i] = fib[i-1]+fib[i-2]

    fl.write(str(fib[n]))
    print(f"ремя работы кода:{time.perf_counter() - t_start}")
    print(f"ремя работы кода:{time.perf_counter() - t_start2}")
    print(getsizeof(fib) + getsizeof(n)+ getsizeof(t_start))