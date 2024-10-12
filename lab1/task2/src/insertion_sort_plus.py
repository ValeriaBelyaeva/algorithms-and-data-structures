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
  n = len(to_sort)
  swap_id = [1]
  for i in range(1, n):
    key = to_sort[i]  # Store the current element as the "key"
    j = i - 1
    while j >= 0 and key < to_sort[j]:
      to_sort[j + 1] = to_sort[j]
      j -= 1
    swap_id.append(j + 2)  # Append the new index
    to_sort[j + 1] = key  # Insert the `key` at the correct position

  return (swap_id, to_sort)

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