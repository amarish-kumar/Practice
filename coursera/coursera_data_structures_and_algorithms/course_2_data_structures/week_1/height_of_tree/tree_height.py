#python3

'''Find height of tree. Tree may or may not be binary.
   Input contains two lines. First line denotes number
   of nodes. Second line denotes the parent of that 
   particular index. For example, 
    
   5
   -1 0 4 0 3

   Here, 0 in 1st and 4th index shows that their parent is 
   the 0th element.
   You have to ouput the height of the tree.
'''

memo = dict()
def findHeight(parentIndex,nodes):


    #get child nodes.
    childNodes = [index for index,item in enumerate(nodes) if item == parentIndex]
    if len(childNodes) == 0:
        return 1
    maxHeight = -1
    #for each node recursively find height.    
    for child in childNodes:
        if child in memo:
            maxHeight = max(maxHeight, memo[child] + 1)
        else:
            maxHeight = max(maxHeight, findHeight(child,nodes)+1)
    memo[parentIndex] = maxHeight    
    return maxHeight


def main():
    
    #read user input.
    numberOfNodes = input()
    #read the nodes.
    nodes = [int(i) for i in input().split()]
    #find index of -1.
    rootIndex = nodes.index(-1) 
    #get height.
    height = findHeight(rootIndex, nodes)
    #output the answer.
    print(height)


        

if __name__ == "__main__":
    main()
