def linear_search(target: int, search_list: list) -> list:
  """
  Searches for a target value in a list using linear search.

  Args:
    target: The value to search for.
    search_list: The list to search in.

  Returns:
    A list of indices where the target value is found. If the target is not found,
    returns a list containing only -1.
  """
  to_return = []  # Initialize an empty list to store indices
  for i in range(len(search_list)):  # Iterate through each element in the list
    if search_list[i] == target:  # Check if the current element matches the target
      to_return.append(i)  # If found, append the index to the return list
  if len(to_return) == 0:  # If the target was not found
    return [-1]  # Return a list with -1
  return to_return  # Return the list of indices where the target was found


'''inp_file = open("input")  # Open input file
search_list = list(map(int, inp_file.readline().split()))  # Read the first line as a list of integers
target = int(inp_file.readline())  # Read the second line as an integer
inp_file.close()  # Close input file
out_file = open("output", 'w')  # Open output file in write mode
try:
    ans = linear_search(target, search_list)  # Call linear_search function
    out = ''  # Initialize an empty string for output
    for e in ans:  # Iterate through the result list
        out = out + str(e) + ' '  # Append each index to the output string
    out_file.write(out)  # Write the output string to the output file
except:
    print('we have egor :(')  # Handle potential exceptions
out_file.close()  # Close output file
'''