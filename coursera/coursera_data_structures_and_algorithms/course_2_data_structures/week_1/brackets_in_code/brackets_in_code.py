#python3
''' Implementation to read in a stream of characters
    and match various pairs of brackets '()', '{}' or
    '[]'. If all the pairs match then output 'SUCCESS'
    otherwise if the unmatch is found for a closing bracket
    then output its 1 indexed location else if it is an 
    opening bracket then output its 1 indexed location.
'''

def main():

    #Read the entire input.
    charStream = input()
    #Stack for storing brackets.
    bracketStack = list()
    #Stream counter.
    streamCounter = 1
    #Flag for unmatching closing brackets case.
    unmatchFlag = False
    #List for all the open brackets.
    openBrackets = ['(','[','{']
    #List for all the closing brackets.
    closeBrackets = [')',']','}']
    #Go through each of the character in the stream.
    for char in charStream:
        if char in openBrackets:
            bracketStack.append([streamCounter,char])
            streamCounter = streamCounter + 1
            continue
        elif char in closeBrackets:
            #Check if stack is empty.
            if len(bracketStack) == 0:
                unmatchFlag = True
                break
            else:
                # Peek stack. Pop if match found else break.
                if bracketStack[-1][1] == openBrackets[closeBrackets.index(char)]:
                    del bracketStack[-1]
                    streamCounter = streamCounter + 1
                else:
                    unmatchFlag = True
                    break
        else:
            streamCounter = streamCounter + 1
            continue
    if len(bracketStack) == 0:
        if unmatchFlag == True:
            print(streamCounter)
        else:
            print("Success")
    else:
        if unmatchFlag == True:
            print(streamCounter)
        else:
            print(bracketStack[0][0])


if __name__=='__main__':
    main()
