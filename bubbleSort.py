"""Having a list with 10 random numbers"""

def bubbleSort(num):
    """using the argument for the range parameters so the number of the elements in the list can be easily changed and considering the 0 index value by '-1'
    plus since the last comparison between the last and second to the last position will satisfy the order already"""
    for i in range(len(num)-1, 0, -1): 
        for j in range(i):
            """this time i will be the last element index (since the step is negative); for this reason, the unsorted range will be lessening upto 0 index to 1 
            index elements unlike in Selection Sort where its last unsorted range is the last index element and its adjacent"""
            if num[j] > num[j+1]: # will compare adjacent elements (this will implement putting the biggest quantity value at the last index first upon ordering)
                temp = num[j]
                num[j] = num[j+1]
                num[j+1] = temp

list = [76, 13, 88, 26, 9, 51, 62, 22, 63, 31]
print("Unsorted list: ", list)