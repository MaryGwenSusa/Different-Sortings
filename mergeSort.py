"""Having a list with 10 random numbers

Merge Sort - Divide and Conquer Algorithm
- breaks down problem into multiple subproblems recursively until they become simple so solve; turn into a binary tree
- solutions are combined to solve original problem

*Big O - 0(n * log(n)) running time"""

def mergeSort(lst):
    if len(lst) > 1:
        # split array in half; [:] python slices array
        # leftList = lst[0:len(lst)//2]
        leftList = lst[:len(lst)//2] # integer division so no remainder; goes from the first to the middle element
        rightList = lst[len(lst)//2:] # goes from the middle to the last element
        # rightList = lst[len(lst)//2:len(lst)]

        #  this will print out every division of the list until having 1 element each
        #print("Left leaf: ", leftList)
        #print("Right leaf: ", rightList)

        # recursion: continuously divide the list until there will be one/two child nodes at the last level
        mergeSort(leftList)
        mergeSort(rightList)


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