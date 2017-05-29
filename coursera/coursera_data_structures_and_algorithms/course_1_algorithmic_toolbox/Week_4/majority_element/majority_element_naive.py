#python3
''' A naive implementation of the majority
    element problem. Here, two nested loops
    will be used to compare an element with 
    the rest of the elemnents. An array will 
    be maintained that will show the number of
    times each element occurs in the input.
    If an element is present such that it's 
    occurence is more than half of the length
    of the input array, we've found our majority
    element.
'''

#List to store the input.
inputArray = list()
#List to store the occurence value of each element.
occurence = list()
#Value to be output.
output = 0 

#Read the number of elements in the input.
n = int(input())
#Read the input.
inputArray = input().split()

#Loop counters.
innerLoopCounter = 0;
outerLoopCounter = 0;
for i in range(n): occurence.append(0)

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
print(output)
