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

        # merging part
        # initialized variables for iterators; compare leftmost indexes and stores accordingly to the leftmost
        i = 0
        j = 0
        k = 0
        while i < len(leftList) and j < len(rightList): # while the divided lists still has comparable element each
            if leftList[i] < rightList[j]: # then if leftList element is less than rightList element
                lst[k] = leftList[i] # assign the element of the leftList as an element to the sorted list parameter
                i += 1 # increment leftList element indexs

            else:
                lst[k] = rightList[j] # else assign the element of the rightList as an element to the sorted list parameter
                j += 1 # increment rightlist element index
            k += 1 # increment sorted list or the merged list parameter element index

            #print("Merged & Sorted leaf/branch: ", lst)
        
        while i < len(leftList): # but if only the left list still has an element--exectute the same code above
            lst[k] = leftList[i]
            i += 1
            k += 1

            #print("Merged & Sorted LEFT leaf/branch: ", lst) 

        while j < len(rightList): # but if only the right list still has an element--exectute the same code above
            lst[k] = rightList[j]
            j += 1
            k += 1

            #print("Merged & Sorted RIGHT leaf/branch: ", lst) 

        # this will print out every sorted and merged final list division composing of 2 elements minimum
        print(lst)

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

    mergeSort(assignedNum)

    print("Sorted Merged List:", end=" ")
    printList(assignedNum)