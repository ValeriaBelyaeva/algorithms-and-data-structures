def insertion_sort(to_sort: list) -> list:
  """
  Sorts a list in ascending order using insertion sort.

  Args:
    to_sort: The list to be sorted.

  Returns:
    The sorted list in ascending order.
  """
  for i in range(1, len(to_sort)):  # Iterate through the list starting from the second element
    key = to_sort[i]  # Store the current element as the "key"
    j = i - 1  # Initialize `j` to the index of the element before the current one
    while j >= 0 and key < to_sort[j]:  # While `j` is within the list bounds and the `key` is less than the element at index `j`
      to_sort[j + 1] = to_sort[j]  # Shift the element at index `j` one position to the right
      j -= 1  # Move `j` one position to the left
    to_sort[j + 1] = key  # Insert the `key` at the correct position

  return to_sort  # Return the sorted list

'''inp_file = open("input")  # Open input file
inp = list(map(int, inp_file.readline().split()))  # Read the first line as a list of integers
inp_file.close()  # Close input file
out_file = open("output", 'w')  # Open output file in write mode
try:
    ans = insertion_sort(inp)  # Call insertion_sort function
    out = ''  # Initialize an empty string for output
    for e in ans:  # Iterate through the result list
        out = out + str(e) + ' '  # Append each element to the output string
    out_file.write(out)  # Write the output string to the output file
except:
    print('we have egor :(')  # Handle potential exceptions
out_file.close()  # Close output file
'''