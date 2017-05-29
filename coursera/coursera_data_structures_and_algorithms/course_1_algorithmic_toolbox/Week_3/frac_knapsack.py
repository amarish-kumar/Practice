#python2
''' Implementation of the fractional knapsack problem.
    Input consists of the first line having two values,
    n and W. n is the number of following lines whereas
    W is the max weight of the knapsack. Next n lines
    contain two space separated numbers denoting the 
    value and the weight of each item/line. Output
    is the maximum value of fractions of items that
    fit into the knapsack.
'''
from operator import itemgetter

#read the first line.
firstLine = raw_input()
#extract the number of items.
numberOfItems = int(firstLine.split()[0])
#extract max weight.
maxWeight = int(firstLine.split()[1])
#Maximum Value (this is the output).
maxValue = 0
#List having input regarding the items
#to be filled.
itemsList = list()
#now read each of the next n lines
#for the weight and values.
for i in range(numberOfItems):
    line = raw_input()
    value = float(line.split()[0])
    weight = float(line.split()[1])
    valuePerUnitWeight = value/weight
    lineList = [value,weight,valuePerUnitWeight]
    itemsList.append(lineList)
#Sort the list according to the value/weight field.
itemsList = sorted(itemsList, key=itemgetter(2), reverse = True)
#itemsList counter.
counter = 0
#Keep adding items in the knapsack until it becomes full.
while maxWeight != 0 and (counter <= len(itemsList) -1):
    #Weight and the value per unit weight of the highest
    #valued item.
    currentWeight = itemsList[counter][1]
    currentValuePerUnit = itemsList[counter][2]
    #If the current item can be fully fitted inside the knapsack.
    #In this case, reduce weight of the knapsack by the weight of 
    #the current item and update max value.
    if currentWeight < maxWeight:
        maxWeight = maxWeight - currentWeight
        maxValue = maxValue + currentWeight*currentValuePerUnit
    #It cannot be fully fitted.Only maxWeight amount of the current
    #item can be used. Update max value accordingly.
    else:
        maxValue = maxValue + maxWeight*currentValuePerUnit
        maxWeight = 0
    #Increment the counter.
    counter = counter + 1
print maxValue
