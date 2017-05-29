#python3

''' Implementation of the dynamic programming primitive calculator program.
    A top down approach of recursion and memoization is followed in the code.
    Input to the code is a number and ouput is in two lines. First line tells
    the minimum number of steps to reach that number from 1 (by either adding 1, 
    multiplying by 2, multiplying by 3). Second line tells the actual numbers in
    the journey.
'''
import operator
memo = dict()
intermediateValues = dict()
intermediateValues[1] = [1]
''' Given the type of number based on its divisibility by 2 and 3, and the index of the 
    minimum value found in primCalc. It computes the intermediate value that is used to
    reach to finalNumber.
'''
def getIntermediateValue(ifBlockType, indexOfMin, numToOperateOn):

    numToReturn = -1
    #Number is divisible by 2 and 3.
    if ifBlockType == 1:
        if indexOfMin == 0:
            numToReturn = numToOperateOn -1
        elif indexOfMin == 1:
            numToReturn = numToOperateOn/2
        else:
            numToReturn = numToOperateOn/3
    #Number is divisible by only 2.
    elif ifBlockType == 2:
        if indexOfMin == 0:
            numToReturn = numToOperateOn -1
        else:
            numToReturn = numToOperateOn/2
    else:
        if indexOfMin == 0:
            numToReturn = numToOperateOn -1
        else:
            numToReturn = numToOperateOn/3
    # Now append the appropriate intermediate values.
    if numToReturn in intermediateValues:
        tempList = [numToOperateOn]
        tempList = intermediateValues[numToReturn] + tempList
        intermediateValues[numToOperateOn] = tempList

''' Recursively calls itself and finds the minimum number of 
    steps required to reach finalNumber from 1 by +1, x2 or x3.
    Method uses memoization to save the results for later use.
'''
def primCalc(finalNumber):

    #Flags to be used to detect whether number is divisible by 2,3.
    flagTwo = False
    flagThree = False
    #Base case.
    if finalNumber == 1:
        return 0
    #Check if calculation for the input has already been done.
    if finalNumber in memo:
        return memo[finalNumber]
    #Check if number is a multiple of 2.
    if finalNumber%2 == 0:
        flagTwo = True
    #Check if number is a multiple of 3.
    if finalNumber%3 == 0:
        flagThree = True
    
    #Now according to the divisibility of the input, make calls to get
    #the output.
    if flagTwo and flagThree:
        #Get the minimum value and the index.
        numIndex, numValue  = min(enumerate([primCalc(int(finalNumber-1)),primCalc(int(finalNumber/2)),primCalc(int(finalNumber/3))]), key=operator.itemgetter(1))
        numValue  = numValue + 1
        #Based on the index of the min value and the type of arguments, find the intermediate number.
        getIntermediateValue(1,numIndex,finalNumber)
    elif flagTwo:
        numIndex, numValue  = min(enumerate([primCalc(finalNumber-1),primCalc(int(finalNumber/2))]), key=operator.itemgetter(1))
        numValue = numValue + 1
        getIntermediateValue(2,numIndex,finalNumber)
    elif flagThree:
        numIndex, numValue  = min(enumerate([primCalc(finalNumber-1),primCalc(int(finalNumber/3))]), key=operator.itemgetter(1))
        numValue = numValue + 1
        getIntermediateValue(3, numIndex,finalNumber)
    else:
        numValue = primCalc(finalNumber-1) + 1
        iv = finalNumber-1
        if iv in intermediateValues:
            tempList = [finalNumber]
            tempList = intermediateValues[iv] + tempList
            intermediateValues[finalNumber] = tempList
    memo[finalNumber] = numValue
    return numValue

def main():

    #Take user input.
    userInput = int(input())
    #Make call to method for calculation.
    output = primCalc(userInput)
    valueSet = sorted(set(intermediateValues[userInput]))
    #Print Output.
    print(output)
    for element in valueSet:
        print(element)



if __name__=='__main__':
   main()
