#python3
''' Implemetation of the primitive calculator problem using tabulation.'''

import operator
import sys
memo = []

def getMinOps(number):
    
    #Number of Operations to get 1.
    memo.append(0)
    #Loop through all the number from 2 to number to check the number of
    #operations for each.
    for i in range(2,number + 1):
        #Check divisibility by two and three.
        if i%2==0 and i%3==0:
            memo.append(1 + min(memo[int(i/2)-1],memo[int(i/3)-1],memo[i-2]))
        #Number only divisible by two.
        elif i%2==0:
            memo.append(1 + min(memo[int(i/2)-1],memo[i-2]))
        #Number only divisible by three.
        elif i%3==0:
            memo.append(1 + min(memo[int(i/3)-1],memo[i-2]))
        #Number neither divisible by two nor three.
        else:
            memo.append(1 + memo[i-2])
    #return the no. of operations for 'number'
    return memo[-1]


def getIntermediateValues():

    #list to store the intermediate values.
    intermediateList = []
    #Memo counter.
    memoCounter = len(memo)
    intermediateList.append(memoCounter)
    while memoCounter > 1:
        counterBy2 = int(memoCounter/2)
        counterBy3 = int(memoCounter/3)
        minIndex, minValue = min(enumerate([memo[memoCounter -2],
                                            memo[counterBy2 -1] if memoCounter%2 == 0 else sys.maxsize, 
                                            memo[counterBy3 -1] if memoCounter%3 == 0 else sys.maxsize]), key = operator.itemgetter(1))
        if minIndex == 0:
            memoCounter = memoCounter -1
            intermediateList.append(memoCounter)
        if minIndex == 1:
            memoCounter = counterBy2
            intermediateList.append(counterBy2)
        if minIndex == 2:
            memoCounter = counterBy3
            intermediateList.append(counterBy3)
    return intermediateList[::-1]
    

def main():
    #read input.
    number = int(input())
    #minimum number of operations.
    minOps = getMinOps(number)
    #intermediate values from all minOps operations.
    intermediateValues = getIntermediateValues()
    #output result
    print(minOps)
    for x in intermediateValues : print(x, end=" ")


if __name__ == '__main__':
    main()
