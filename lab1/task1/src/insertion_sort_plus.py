def insertion_sort(to_sort: list)-> (list, list):
    n = len(to_sort)
    swap_id = [1]
    for i in range(1, n):
        key = to_sort[i]
        j = i - 1
        while j >= 0 and key < to_sort[j]:
            to_sort[j + 1] = to_sort[j]
            j -= 1
        swap_id.append(j+2)
        to_sort[j + 1] = key

    return swap_id, to_sort


test_input = [
    [5, 4, 3, 2, -1],
    [31, 41, 59, 26, 41, 58],
    [1000000000, 1000000000, 50000000],
    [-1000000000, -1000000000, 50000000],
    [1, 8, 4, 2, 3, 7, 5, 6, 9, 0],
    [i for i in range(1000)],
    [i for i in range(1000, 0, -1)]
]
for test in test_input:
    print(insertion_sort(test))

'''
1 2 2 2 3 5 5 6 9 1
0 1 2 3 4 5 6 7 8 9
'''