"""Having a list with 10 random numbers"""

def selectionSort (nums):
    # for multiple iteration - nested loops
    """only until the 9th position (which is index 8) since the last comparison between the last and second to the last position will satisfy the order 
    alreaady and there is no need to loop for another placeholder to determine which is last"""
    for  i in range(9): 
        # variable will hold minimum index (position); initially, assume the first element of the unsorted range as the minimum
        minIndex = i

        for j in range(i, 10): # for loop the incrementing index j in the range of i index (which is also an incrementing value) to range 10
            """select the minimum element in every iteration
            
            - to sort in descending order simply change the '<' to '>'; then the placeholder will be for the maximum element"""
            if nums[j] < nums[minIndex]: # if the element at value of j index is less than the first element of the unsorted range (which is the minIndex)
                minIndex = j # then j is the new index position of minimum element

        """swap the minimum element with the first element of the unsorted part"""
        # since the parameter nums will be supplemented by a list argument and i is incrementing thru for loop--the first element of the unsorted part 
        # will be stored to a variable
        temp = nums[i] 
        nums[i] = nums[minIndex] # the new minimum element with determined index position will be the first element of the list (recognized as sorted); other elements to follow on index position with the help of i increment of the first for loop
        nums[minIndex] = temp # the old first element of the unsorted range will be swapped at the old index position of the new minimum element found

        # this will print out every determined minimum sequence for every index position
        print(nums)
        


list = [76, 13, 88, 26, 9, 51, 62, 22, 63, 31]
print(list)
selectionSort(list)
print("In ascending order", list)
#print("In descending order", list)


