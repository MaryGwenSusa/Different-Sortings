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
                # shift number in slot i right to slot i+1; then place the left index element to its right index
                # from the value stored on the variable(value) at the outer loop, replace the left index element
                list[i+1], list[i] = list[i], value 

                # this will print out the element of value (which is the current index we're comparing to) and the element on its left whenever value element is less than the element on its left
                print("Swapped: {} with {}".format(list[i+1] , list[i])) # {} is a placeholder in Python String Format

                i -= 1 # intended to continue comparisons of the left indexes
                
            else:
                break

            #this would print out sequence of every swapping of value index element
            #print(list)
        
        # this would print out sequence whenever comparion/s to the left has been interrupted 
        print(list)
        

assignedNum = [76, 13, 88, 26, 9, 51, 62, 22, 63, 31]
print("Unsorted list:", assignedNum)
insertionSort(assignedNum)
#print("In Descending Order:", end=" ")
print("In ascending order:", end=" ") # By default Python‘s print() function ends with a newline. The end parameter in the print function is used to add any string. 
# At the end of the output of the print statement in python. Passing the whitespace to the end parameter (end=‘ ‘) indicates that the end character has to be 
# identified by whitespace and not a newline.
for i in range(len(assignedNum)):
    print(assignedNum[i], end=" ")
