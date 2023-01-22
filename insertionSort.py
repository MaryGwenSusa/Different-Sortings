def insertionSort(list):
    for index in range(1,len(list)):
        value = list[index]
        i = index - 1
        while i >= 0:
            if value < list[i]:
                list[i+1] = list[i] #shift number in slot i right to slot i+1
                list[i] = value #shift value left into slot i
                i = i - 1
            else:
                break

assignedNum = [76, 13, 88, 26, 9, 51, 62, 22, 63, 31]
insertionSort(assignedNum)
print(assignedNum)