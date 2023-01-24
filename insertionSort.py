"""Having a list with 10 random numbers"""

def insertionSort(list): #for loop and while loop nested this time
    for index in range(1,len(list)): #the variable index first value is 1 since start parameter is 1 so it would pertain to the 1st index element
        value = list[index]
        i = index - 1 # left element of the current element in a horizontal or list visualization
        while i >= 0: # while true
            """just like bubble sort, would swap every comparison whenever the condition is satisfied but would not continuously iterate all elements and would
            immediately exit the inner loop or start off comparing another value element index to its left elements
            
            - to sort in descending order simply change the '<' to '>' then the higher value will be swapped towards the left"""
            if value < list[i]: # if current element starting from the 1st index element is less than the element on its left
                list[i+1] = list[i] # shift number in slot i right to slot i+1; then place the left index element to its right index
                list[i] = value # from the value stored on the variable(value) at the outer loop, replace the left index element
                i -= 1 # intended to continue comparisons of the left indexes

assignedNum = [76, 13, 88, 26, 9, 51, 62, 22, 63, 31]
print("Unsorted list:", assignedNum)

