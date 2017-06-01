''' Implementation of the minimum edit distance dynamic programming and 
    tablulation. Given strings A and B of length m and n, a 2-D matrix
    of length (m+1)x(n+1) is created. Each index of the matrix represent
    the minimum edit distance between the corresponding sub-strings. The
    final output is the lower right most element of the matrix.
'''

def main():
    #Read base string.
    base = list(input())
    #Read destination string.
    dest = list(input())
    #Matrix to hold output.
    matrix = [[0]*(len(base)+1) for _ in range(len(dest)+1)]   
    #Initialize the first row of the matrix.
    for i in range(len(matrix[0])):
        matrix[0][i] = i
    #Initialize the first column of the matrix.
    for i in range(len(matrix)):
        matrix[i][0] = i
    #Iterate over the matrix calculating min-edit distance of sub strings.
    for i in range(len(dest)):
        for j in range(len(base)):
            #For same corresponding letters, edit distance is same as that
            #the diagonally previous pair.
            if base[j] == dest[i]:
                matrix[i+1][j+1] = matrix[i][j]
            else:
                matrix[i+1][j+1] = 1 + min(
                                           #Element to the top
                                           matrix[i+1][j],
                                           #Diagonally top element.
                                           matrix[i][j],
                                           #Element to the left.
                                           matrix[i][j+1])
    #print outptut.
    print(matrix[len(dest)][len(base)])


if __name__ == '__main__':
    main()
