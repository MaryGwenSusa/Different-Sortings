"""Having a list with 10 random numbers

Quick Sort - Divide and Conquer Algorithm
- breaks down problem into multiple subproblems recursively until they become simple so solve; turn into a binary tree
- solutions are combined to solve original problem

*Big O - 0(n * log(n)) running time
*O(n^2) worst case

1) Choose pivot element (usually last or random)
2) Stores elements less than the pivot in left subarray
3) Stores elements greater than the pivot in right subarray
4) Call quicksort recursively on left subarray
    Call quicksort recursively on right subarray

this recursion goes on until the area size of a subarray is 1"""

def quickSort(arr, left, right): # left = 0; right = 9 on first call--refers to the index; serves as boundary
    # in this case, the element on the last index will be the first pivot
    if left < right: #subarray atleast contains two elements
        partition_pos = partition(arr, left, right)
        quickSort(arr, left, partition_pos - 1) # less of the pivot element; parameter continuously decrement
        quickSort(arr, partition_pos + 1, right) # subarrays contain > pivot; parameter continuously increment


# Print the array
def printList(lst):
    for i in range(len(lst)):
        print(lst[i], end=" ") # By default Python‘s print() function ends with a newline. The end parameter in the print function is used to add any string. 
        # At the end of the output of the print statement in python. Passing the whitespace to the end parameter (end=‘ ‘) indicates that the end character has to be 
        # identified by whitespace and not a newline.
    print()


# Driver program
if __name__ == '__main__': #executes coroutine on the default event loop
    assignedNum = [76, 13, 88, 26, 9, 51, 62, 22, 63, 31]
    print("Unsorted List:", end=" ")
    printList(assignedNum)

    

    print("Sorted Merged List:", end=" ")
    printList(assignedNum)