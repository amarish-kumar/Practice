''' Question taken from hackerearth
    https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/monk-and-power-of-time/
'''
timeToCompute = 0
def rotate_list(rotations):
	# rotate the list, 'rotations' number of times.
	i =1
	while i <= rotations:
		# increment the time to compute.
		global timeToCompute
		timeToCompute += 1
		j = 1
		# store the top element.
		top = callingOrder[0]
		# move elements up position up starting from the second element.
		while j < len(callingOrder):
			callingOrder[j] = callingOrder[j+1]
		# add the top element to the last position.
		callingOrder[len(callingOrder) -1 ] = top



print("enter num of processes") 
numOfProcesses = int(input())
#callingOrder = [int(x) for x in input().split()]
#idealOrder = [int(x) for x in input().split()]
callingOrder = [3,2,1]
idealOrder = [1,2,3]
'''match the head of the lists, and rotate callingOrder to match the 
   heads.
'''
while (len(idealOrder) == len(callingOrder)) and len(idealOrder) > 0 :
	if idealOrder[0] == callingOrder[0]:
		idealOrder.pop(0)
		callingOrder.pop(0)
		timeToCompute += 1
	else:
		''' calculate the number of rotation required and 
		    call method to rotate the list(callingOrder)
		'''
		rotate_list(callingOrder.index(idealOrder[0]))
print(timeToCompute)

