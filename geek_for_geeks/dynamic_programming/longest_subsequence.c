/** Implementation of the longest subsequence problem
    from geeks for geeks(http://www.geeksforgeeks.org/
    dynamic-programming-set-3-longest-increasing-subsequence/).
  */

#define NG (-1)
#define ZERO (0)
#define ONE (1)

#include<stdio.h>
#include<stdlib.h>

/** Entry function. */
void main(){

    //Length of longest subsequence.
    int longestSubsequence = NG;
    //Number of test cases.
    int testCases = NG;
    //Size of user input.
    int userInputSize = NG;
    //User input.
    int *userInput;
    //Loop Counter.
    int loopCounter = NG;

    //Read the number of test cases.
    scanf("%d", &testCases);
    
    //Calculate longest subsequence 
    //for all the test cases.
    while(testCases-- > ZERO){

        //Read the size of the user input.
        scanf("%d", &userInputSize);
        //Allocate memory for user input.
        userInput = (int*) malloc(userInputSize * sizeof(int*));
        //Read in the user input.
        for(loopCounter = ZERO; loopCounter < userInputSize; loopCounter++){

            scanf("%d", &userInput[loopCounter]);
        }
        
        //Calculate Longest Subsequence length.
        longestSubsequence = calcLS(userInput, userInputSize);
    
        //Output the longest subsequence length.
        printf("%d\n", longestSubsequence);
    
        //Deallocate memory.
        free(userInput);
    }   
}

int calcLS(int *sequence, int sizeOfSequence){

    //Temporary array to store the subsequence length.
    int *subsequenceLength = NG;
    //Loop Counter.
    int loopCounter = NG;
    //Inner loop counter, this is used in case the previous
    //element in sequence is greater than current element.
    int innerLoopCounter = NG;

    //Allocate memory for the subsequence length array.
    subsequenceLength = (int*) malloc( sizeOfSequence * sizeof(int*));
    
    //Assign length for the base case.
    subsequenceLength[ZERO] = ONE;

    //Max length encountered upto a particular point.
    int maxLength = NG;
    
    for(loopCounter = ONE; loopCounter < sizeOfSequence; loopCounter++){

        //If previous element is smaller, increase subsequence length.
        if(sequence[loopCounter] > sequence[loopCounter - ONE]){
            subsequenceLength[loopCounter] = subsequenceLength[loopCounter - ONE] + ONE;
        }
        //Else search for last smaller number and use it's subsequence length.
        else{
            //Assign default value of 1 just in case no smaller element is found.
            subsequenceLength[loopCounter] = ONE;
            for(innerLoopCounter = loopCounter - ONE; innerLoopCounter >= ZERO; innerLoopCounter--){
                //Check if element is smaller.
                if(sequence[innerLoopCounter] < sequence[loopCounter]){
                    subsequenceLength[loopCounter] = subsequenceLength[innerLoopCounter] + 1;
                }
            }
        }
        
        //Update the max length.
        if(maxLength < subsequenceLength[loopCounter]){
            maxLength = subsequenceLength[loopCounter];
        }        
    }
    
    return maxLength;
}
