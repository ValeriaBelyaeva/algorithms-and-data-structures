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