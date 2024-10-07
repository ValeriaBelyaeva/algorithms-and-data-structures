def insertion_sort(to_sort: list) -> (list, list):
  """
  Sorts a list using insertion sort and returns the sorted list along with a list
  containing the indices where swaps occurred during the sorting process.

  Args:
    to_sort: The list to be sorted.

  Returns:
    A tuple containing:
      - swap_id: A list of indices where swaps occurred during sorting.
      - to_sort: The sorted list.
  """
  n = len(to_sort)  # Get the length of the input list
  swap_id = [1]  # Initialize a list to store swap indices, starting with 1 (assuming the first element is already in place)
  for i in range(1, n):  # Iterate through the list starting from the second element
    key = to_sort[i]  # Store the current element as the "key"
    j = i - 1  # Initialize `j` to the index of the element before the current one
    while j >= 0 and key < to_sort[j]:  # While `j` is within the list bounds and the `key` is less than the element at index `j`
      to_sort[j + 1] = to_sort[j]  # Shift the element at index `j` one position to the right
      j -= 1  # Move `j` one position to the left
    swap_id.append(j + 2)  # Append the index of the swap (j + 2) to the `swap_id` list
    to_sort[j + 1] = key  # Insert the `key` at the correct position

  return (swap_id, to_sort)  # Return the list of swap indices and the sorted list

'''
inp_file = open("input")  # Open input file
inp = list(map(int, inp_file.readline().split()))  # Read the first line as a list of integers
inp_file.close()  # Close input file
out_file = open("output", 'w')  # Open output file in write mode
try:
    ans1, ans2 = insertion_sort(inp)  # Call insertion_sort function
    out1 = ''  # Initialize an empty string for the first output
    for e in ans1:  # Iterate through the first result list (swap indices)
        out1 = out1 + str(e) + ' '  # Append each swap index to the first output string
    out2 = ''  # Initialize an empty string for the second output
    for e in ans2:  # Iterate through the second result list (sorted list)
        out2 = out2 + str(e) + ' '  # Append each sorted element to the second output string
    out_file.write(out1 + '\n' + out2)  # Write both output strings to the file, separated by a newline
except:
    print('we have egor :(')  # Handle potential exceptions
out_file.close()  # Close output file
'''