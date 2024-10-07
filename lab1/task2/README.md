#insertion sort +
The task code implements an insertion sorting algorithm. The function also displays the numbers of the positions on which the items were placed during the sorting process

##How it works:

**Initialization:**  
The algorithm initializes a list swap_id to store the indices where swaps occur. It also initializes a counter n to store the length of the input list.  
**Iteration:**  
The algorithm iterates through the list, starting from the second element (index 1). The first element is considered already sorted.  
**Key Selection:**   
The current element is selected as the “key”.  
**Finding the Insertion Point:**  
The code compares the key with the elements in the sorted portion of the list, shifting elements to the right to make space for the key until the correct position is found.  
**Shifting and Swap Tracking:**  
Each time an element is shifted to the right, the index where the shift occurred (j + 2) is appended to the swap_id list.
**Insertion:**  
The key is inserted at the correct position in the sorted portion.  
**Returning Results:**  
The function returns a tuple containing the swap_id list and the sorted list.  