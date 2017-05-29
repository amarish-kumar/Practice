/** Implementation of the dynamic programming primitive calculator program.
    A top down approach of recursion and memoization is followed in the code.
    Input to the code is a number and ouput is in two lines. First line tells
    the minimum number of steps to reach that number from 1 (by either adding 1, 
    multiplying by 2, multiplying by 3). Second line tells the actual numbers in
    the journey.
*/

/** Output Variables Declaration.*/
int minNumOfOps;
int* intermediateNumbers;


/** Main method */
void main(){

    //Declaration of input.
    int userInput;

    //Take the user input.
    scanf("%d", &userInput);

    //Make call to get output.
    primCalcEntry(userInput);
}

/** Primitive Calculator.
 * 
 * @brief : This fucntion takes in the user input and performs the required
 * computation on it. Finally, it prints the two lined output.
 *
 * @param1 : user input.
 */
void primCalcEntry(int userInput){

    int* memo;
    memo = (int *)malloc(userInput*sizeOf(int*));
    minNumOfOps = primCalc(userInput,memo); 
    printf("%d", minNumOfOps);
     



}
 


