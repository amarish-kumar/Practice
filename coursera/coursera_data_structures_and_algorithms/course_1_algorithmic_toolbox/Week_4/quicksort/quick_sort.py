''' Implementation of the quick sort algorithm. '''

globalList = list()

def partitionTheArray(inputArray,leftEnd,rightEnd):
    
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
    inputArray[lesserIndex] = inputArray[leftEnd]
    return lesserIndex


def performQuickSort(inputArray, leftEnd, rightEnd):

    globalList = inputArray
    #Anchor condition.
    if rightEnd < leftEnd:
        return #TODO
    #Perform the partition of the array.
    #This call will return an integer value
    #m such that leftEnd < m < rightEnd and
    #elements to the left of inputArray[m]
    #are smaller than it while elements to 
    #to the right of inputArray[m] are
    #greater than it.
    middleElement = partitionTheArray(inputArray, leftEnd, rightEnd)

    #Recursively quick sort the left sub-array.
    performQuickSort(inputArray, leftEnd, middleElement-1)
    #Recursively quick sort the right sub-array.
    performQuickSort(inputArray, middleElement+1, rightEnd)




