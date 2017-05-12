numOfInputs = int(input())
nameRoll = dict()
for i in range(numOfInputs):
	inp = input().split()
	nameRoll[int(inp[0])] = inp[1]
numOfOutputs = int(input())
for x in range(numOfOutputs):
	roll = int(input())
	if nameRoll.has_key(roll):
		print(nameRoll.get(roll,'not found'))
