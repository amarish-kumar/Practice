#python3
'''Implementation of majority element problem by using python dictionaries.
   Here, the input list will be parsed onced and for each value the dict.
   will be updated. Finally the key-value pair having max value will be 
   fetched.
'''

dict = dict()
#Read input size.
n = int(input())
#Read the user input.
userInput = input().split()
#Parse the user input.
for element in userInput:
    #Check if element already in dictionary.
    #If not add to dictionary and set value to 1.
    #If already present, increment the value.
    if element in dict:
        dict[element] = dict [element] + 1
    else:
        dict[element] = 1
#Get the list of values from the dictionary.
values = dict.values()
#Check if any of the values are greater than n/2.
if max(values) >= int(n/2) +1:
    print('1')
else:
    print('0')

