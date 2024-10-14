import sys


def selection_sort(to_sort: list) -> list:
    """
    Sorts an to_sortay using selection sort.
    Args: to_sort: The to_sortay to be sorted.
    Returns:The sorted to_sortay.
    """
    n = len(to_sort)
    for i in range(n - 1):
        # Find the index of the minimum element in the remaining unsorted part of the to_sortay
        min_index = i
        for j in range(i + 1, n):
            if to_sort[j] < to_sort[min_index]:
                min_index = j

        # Swap the minimum element with the current element
        to_sort[i], to_sort[min_index] = to_sort[min_index], to_sort[i]
    return to_sort


'''inp_file = open("input")  # Open input file
inp = list(map(int, inp_file.readline().split()))  # Read the first line as a list of integers
inp_file.close()  # Close input file
out_file = open("output", 'w')  # Open output file in write mode
try:
    ans = selection_sort(inp)  # Call selection_sort function
    out = ''  # Initialize an empty string for output
    for e in ans:  # Iterate through the result list
        out = out + str(e) + ' '  # Append each element to the output string
    out_file.write(out)  # Write the output string to the output file
except:
    print('we have egor :(')  # Handle potential exceptions
out_file.close()  # Close output file
'''