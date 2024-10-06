def insertion_sort_reverse(to_sort):
    for i in range(1, len(to_sort)):
        key = to_sort[i]
        j = i - 1
        while j >= 0 and key > to_sort[j]:
            to_sort[j + 1] = to_sort[j]
            j -= 1
        to_sort[j + 1] = key

    return to_sort
