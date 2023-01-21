"""Having a list with 10 random numbers"""

def bubbleSort(num):
    """using the argument for the range parameters so the number of the elements in the list can be easily changed and considering the 0 index value by '-1'
    plus since the last comparison between the last and second to the last position will satisfy the order already"""
    for i in range(len(num)-1, 0, -1): 

list = [76, 13, 88, 26, 9, 51, 62, 22, 63, 31]
print("Unsorted list: ", list)