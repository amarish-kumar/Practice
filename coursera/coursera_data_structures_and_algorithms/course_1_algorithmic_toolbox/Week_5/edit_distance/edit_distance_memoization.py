#python3
''' Implementation of the edit distance problem solved using the dynamic
    programming approach. Additionally, memoization has been used to 
    reduce complexity.
'''

memo = dict()

def findEditDistance(stringA, stringB):

    #if a string has lenght 0, return the lenght of the other string.
    if len(stringA) == 0:
        return len(stringB)
    elif len(stringB) == 0:
        return len(stringA)

    #if both strings are have last characters same, then calculate the
    #min. edit distance for the substrings without the last characters.
    if stringA[-1] == stringB[-1]:
        return findEditDistance(stringA[:len(stringA)-1], stringB[:len(stringB)-1])
    
    #if the last characters are not the same, then its a case of deletion
    #addition or modification(renaming).So, three cases will arise here.

    #addition case.
    if stringA[:len(stringA)-1] + stringB in memo:
        additionCase = memo[stringA[:len(stringA)-1] + stringB]
    else:
        additionCase = findEditDistance(stringA[:len(stringA)-1], stringB)
    #deletion case.
    if stringA + stringB[:len(stringB)-1] in memo:
        deletionCase = memo[stringA + stringB[:len(stringB)-1]]
    else:
        deletionCase = findEditDistance(stringA, stringB[:len(stringB)-1])
    #modification/replacement
    if stringA[:len(stringA)-1] + stringB[:len(stringB)-1] in memo:
        replacementCase = memo[stringA[:len(stringA)-1] + stringB[:len(stringB)-1]]
    else:
        replacementCase = findEditDistance(stringA[:len(stringA)-1], stringB[:len(stringB)-1])

    memo[stringA + stringB] = 1 + min(additionCase, deletionCase, replacementCase)
    return memo[stringA + stringB]


def main():
    #read the input strings.
    stringA = str(input())
    stringB = str(input())

    #find out the minimum edit distace of the above strings.
    minEditDistance = findEditDistance(stringA,stringB)
    #print the output.
    print(minEditDistance)




if __name__ == '__main__':
    main()
