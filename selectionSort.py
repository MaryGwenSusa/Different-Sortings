"""Having a list with 10 random numbers"""

def selectionSort (nums):
    # for multiple iteration - nested loops
    """only until the 9th position (which is index 8) since the last comparison between the last and second to the last position will satisfy the order 
    alreaady and there is no need to loop for another placeholder to determine which is last"""
    for  i in range(9): 
        # variable will hold minimum index (position); initially, assume the first element of the unsorted part as the minimum
        minIndex = i

        for j in range(i, 10): # for loop the incrementing index j in the range of i index (which is also an incrementing value) to range 10
            """select the minimum element in every iteration
            
            - to sort in descending order simply change the '<' to '>'; then the placeholder will be for the maximum element"""
            if nums[j] < nums[minIndex]: # if the element at value of j index is less than the first element of the unsorted part (which is the minIndex)
                minIndex = j # then j is the new index position of minimum element






list = [76, 13, 88, 26, 9, 51, 62, 22, 63, 31]
print(list)