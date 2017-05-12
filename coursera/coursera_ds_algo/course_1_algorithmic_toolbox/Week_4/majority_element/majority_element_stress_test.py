#python3
'''Stress Test implementation for the 
   majority element codes. This will
   create random input and fetch output
   from two versions of the majority
   element implementation (fast and
   naive.It will then compare the results
   and bring out the case where there is 
   a mismatch.
'''
import random


def partitionTheArray(inputArray, leftEnd,rightEnd):
    
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


def performQuickSort(inputArray, leftEnd, rightEnd):

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
    middleElement = partitionTheArray(inputArray, leftEnd, rightEnd)

    #Recursively quick sort the left sub-array.
    performQuickSort(inputArray, leftEnd, middleElement-1)
    #Recursively quick sort the right sub-array.
    performQuickSort(inputArray, middleElement+1, rightEnd)





def fast(inputArray):
    #Read the user input
    #First the size of the input array.
    n = len(inputArray)
    if n ==1:
        return n
    output = 0
    #Sort the array
    performQuickSort(inputArray, 0, n-1)
    counter = 0
    #Parse the array
    while counter <= (len(inputArray)/2)-1:
        if int(inputArray[counter + int(n/2)]) == int(inputArray[counter]):
            output = 1
            break
        counter = counter + 1
    return output


def naive(inputArray):
    #List to store the occurence value of each element.
    occurence = list()
    #Value to be output.
    output = 0 

    #Loop counters.
    innerLoopCounter = 0;
    outerLoopCounter = 0;
    for i in range(len(inputArray)): occurence.append(0)

    #Loop through each element of the input array.
    while outerLoopCounter < len(inputArray):
        innerLoopCounter = 0
        #Again loop through the elements of input array.
        while innerLoopCounter < len(inputArray):
            #compare the elements in  the inner and outer loops.
            if inputArray[outerLoopCounter] == inputArray[innerLoopCounter]:
                #If a match is found, increment the occurence index for outerLoop element.
                occurence[outerLoopCounter] = occurence[outerLoopCounter]+ 1
            innerLoopCounter = innerLoopCounter + 1
        outerLoopCounter = outerLoopCounter + 1
    #Now check for a majority element.
    for element in occurence:
        if element > len(inputArray)/2:
            output = 1
            break
    return output

def main():

    while(1):
        inputArray = list()
        #First generate the random size of the input array.domain - 0 to 100000(10e5)
        size = random.randint(0,1000)
        #Now create a list containing the number of elements previously generated.
        for time in range(size):
            #For each time,generate a random number between 0 and 1000000000 (10e9)
            number = random.randint(0,1000000000)
            #Append the number to the list.
            inputArray.append(number)
    
        #Copy the list into two separate lists.
        naiveInput, fastInput = inputArray, inputArray
        #Make calls to both the fast and the naive implementations and fetch the output.
        print("**************************************************************************************************\n")
        print("get naive output\n")
        naiveOutput = naive(naiveInput)
        print("got naive output: "+ str(naiveOutput) + "\n")
        print("get fast output\n")
        fastOutput = fast(fastInput)
        print("got fast output : " + str(fastOutput) + "\n")
        #Compare the outputs, if a mismatch is found, raise an alarm.
        if naiveOutput != fastOutput:
            print("mismatch found : \n")
            print(inputArray)
            break
        else:
            print("OK\n")







if __name__=='__main__':main()
