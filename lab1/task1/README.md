#Insertion Sort Algorithm
This Python code implements the insertion sort algorithm, a simple sorting algorithm that builds a sorted array one element at a time.

##How it works:
**Initialization:**  
The algorithm iterates through the list starting from the second element. The first element is considered already sorted.  
**Key Selection:**  
The current element is selected as the “key”.  
**Finding the Insertion Point:**  
The code compares the key with the elements in the sorted portion of the list, shifting elements to the right to make space for the key until the correct position is found.  
**Insertion:**   
The key is inserted at the correct position in the sorted portion.  
This process repeats for each element in the list, building a sorted array.  

##Example Usage:
The commented code demonstrates how to use the insertion_sort function to process input and output files:  

Reads a list of integers from an “input” file.
Sorts the list using insertion_sort.
Writes the sorted list to an “output” file.