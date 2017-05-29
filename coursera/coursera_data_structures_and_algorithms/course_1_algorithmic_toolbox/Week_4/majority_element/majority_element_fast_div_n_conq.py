#python3
'''Implemetation of the program to calculate the
   majority element in an array. An element is 
   considered as a majority element if it occurs
   more than n/2 times. Input will be an unsorted
   array and output will be the majority element
   if one exists or 0 otherwise. To implement this
   first perform quick sort (or any other sort) on 
   the input array and then parse the array to 
   determine for each element if the element present
   at i+(n/2+1)th index is the same or not.
'''

def partitionTheArray(leftEnd,rightEnd):
    
    greaterIndex = leftEnd + 1
    lesserIndex = leftEnd
    pivotElement = inputArray[leftEnd]
    while greaterIndex <= rightEnd:
        #Compare the current element with the pivot 
        #element.
        if int(pivotElement) < int(inputArray[greaterIndex]):
            #Current value greater than pivot element,
            #move the index of the greater elements list
            #ahead by one.
            greaterIndex = greaterIndex + 1
        elif int(pivotElement) >= int(inputArray[greaterIndex]):
            #Current value lesser than or equal to the
            #pivot element. Increase the band of the
            #lesser elements by swapping elements at 
            #greaterIndex and lesserIndex +1.
            lesserIndex = lesserIndex + 1
            temp = inputArray[greaterIndex]
            inputArray[greaterIndex] = inputArray[lesserIndex]
            inputArray[lesserIndex] = temp
            greaterIndex = greaterIndex + 1
    #Finally Swap the pivot element with the element at lesserIndex.
    temp = inputArray[leftEnd]
    inputArray[leftEnd] = inputArray[lesserIndex]
    inputArray[lesserIndex] = temp
    return lesserIndex


def performQuickSort(leftEnd, rightEnd):

    #Anchor condition.
    if rightEnd < leftEnd:
        return 
    #Perform the partition of the array.
    #This call will return an integer value
    #m such that leftEnd < m < rightEnd and
    #elements to the left of inputArray[m]
    #are smaller than it while elements to 
    #to the right of inputArray[m] are
    #greater than it.
    middleElement = partitionTheArray(leftEnd, rightEnd)

    #Recursively quick sort the left sub-array.
    performQuickSort(leftEnd, middleElement-1)
    #Recursively quick sort the right sub-array.
    performQuickSort(middleElement+1, rightEnd)


inputArray = list()
output = 0

#Read the user input
#First the size of the input array.
n = int(input())
#Now the input array.
inputArray = input().split()
if n ==1 :
    print(n)
else :    
    #Sort the array
    performQuickSort(0, len(inputArray)-1)
    counter = 0
    #Parse the array
    while counter <= (len(inputArray)/2)-1:
        if int(inputArray[counter + int(n/2)]) == int(inputArray[counter]):
            output = 1
            break
        counter = counter + 1
    print(output)
