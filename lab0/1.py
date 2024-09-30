import time
from sys import getsizeof

while True:
    t_start = time.perf_counter()
    a, b = map(int, input().split())
    print(a+b)
    print (getsizeof(a), getsizeof(b))
    print(f"ремя работы кода:{time.perf_counter() - t_start}")
