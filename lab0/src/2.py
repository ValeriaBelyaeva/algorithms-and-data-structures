import time
while True:
    a, b = map(int, input().split())
    t_start = time.perf_counter()
    print(a+b**2)

    print(f"ремя работы кода:{time.perf_counter() - t_start}")


'''
-1000000000 -1000000000
12 25
130 61
1000000000 1000000000
'''