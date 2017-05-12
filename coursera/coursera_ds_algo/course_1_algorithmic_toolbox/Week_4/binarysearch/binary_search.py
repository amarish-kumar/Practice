#python3
'''Implementation of the binary search algoritm.
   Input will contain two lines. First line will
   have an integer n followed by n integers in 
   increasing order. Second line will have an 
   integer n again followed by n integers. For 
   each of the integers in the second line, you 
   have to perform binary search and output the 
   index of the integer in the set on the first
   line else output -1 if it is not there.
'''
sorted_array = list()

def binary_search(num, l, h):
    #value containing the index where num resides.
    #it will be -1 in case num is not found.
    valueToReturn = -1
    #if high end is less than the low end, end
    #search and return -1.
    if h < l :
        return valueToReturn
    #get the middle element.
    mid = int((l+h)/2)
    #if num is equal to be searched, return index
    #of middle element.
    if int(num) == int(sorted_array[mid]):
        valueToReturn = mid
    #if num is greater than the middle element,
    #implement binary search on the upper half
    #of the sorted array.
    elif int(num) > int(sorted_array[mid]):
        valueToReturn = binary_search(num,mid+1,h)
    #if num is smaller than the middle element, 
    #implement binary search on the lower half
    #of the sorted array.
    elif int(num) < int(sorted_array[mid]):
        valueToReturn = binary_search(num,l,mid-1)
    return valueToReturn
    



#read the first line
first_line = input()
#extract the number and the sorted array from 
#the first line.
num_first = first_line.split()[0]
sorted_array = first_line.split()[1:]

#read the second line.Put the numbers to be
#searched in a separate list.
second_line = input()
num_second = second_line.split()[0]
input_array = second_line.split()[1:]

#parse the second list and call binary search
#utility for each of the number in the list.
#Save the output of the binary search for each
#of the number in a separate list.
output_array = list()
for num_to_be_searched in input_array:
    #search for the index of the number.
    output_array.append(binary_search(num_to_be_searched,0,len(sorted_array)-1))

for element in output_array:
    print(element,end='')
    print(" ",end='')
