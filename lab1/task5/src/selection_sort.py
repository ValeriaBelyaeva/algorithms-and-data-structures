def selection_sort(arr):
    """
    Sorts an array using selection sort.
    Args: arr: The array to be sorted.
    Returns:The sorted array.
    """

    n = len(arr)
    for i in range(n - 1):
        # Find the index of the minimum element in the remaining unsorted part of the array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the minimum element with the current element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr
