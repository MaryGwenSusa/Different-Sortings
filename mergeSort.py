# Print the array
def printList(lst):
    for i in range(len(lst)):
        print(lst[i], end=" ")
    print()


# Driver program
if __name__ == '__main__': #executes coroutine on the default event loop
    assignedNum = [76, 13, 88, 26, 9, 51, 62, 22, 63, 31]
    print("Unsorted List:", end=" ")
    printList(assignedNum)