/** Given a set of n integers,you have to find a
    pair the product of which is the maximum among
    the product from the rest of the pairs. The
    solution is rather easy. In any given set of 
    numbers the maximum product is of the two 
    largest numbers. So, if a set of n numbers is
    given, parse the array storing them and find 
    the two largest numbers among the set. Product
    of these two numbers is the answer. Another way
    is to sort this set and use the last two numbers
    but when the answer can be achieved without sorting
    why take the pain.
*/

#include <stdio.h>
#include <stdlib.h>

int* sortArray(int *p,int n);
long long findMaxProduct(int *p,int n);

void main(){

    //number of integers in the input set.
    int n;
    //array containing n number of integers.
    int *numbers;
    //maximum product
    unsigned long long maxProduct;
    //loop counter
    int i;
    //read the value of n.
    scanf("%d",&n);
    //allocate memory for integer array n elements long.
    numbers = (int*)malloc(n*sizeof(int));
    for(i=0;i<n;i++){
        scanf("%d",(numbers+i));
    }
    //find max product pairs
    maxProduct = findMaxProduct(numbers,n);
    //output the results.
    printf("%llu",maxProduct);
    return;
}
    
/** @brief
    performs bubble sort on the integer array passed.
    @param1
    input integer array.
    
    @return
    bubble sorted param1
 */
int* sortArray(int *p,int length){

    int outerLoopCounter;
    int innerLoopCounter;
    int innerLoopMax=-1;
    int innerLoopMaxIndex=0;
    int *firstNumToExchange;
    int *secondNumToExchange;
    //parse the array one by one
    for(outerLoopCounter=length-1;outerLoopCounter>=0;outerLoopCounter--){
        
        for(innerLoopCounter=0;innerLoopCounter<=outerLoopCounter;innerLoopCounter++){
        
            //compare the innerLoopCounter element with innerLoopMax and update 
            //innerLoopMax if neccessary.
            if(*(p+innerLoopCounter)>innerLoopMax){
                //update the max value encountered til now.
                innerLoopMax=*(p+innerLoopCounter);
                //update the index number where this max value was found.
                innerLoopMaxIndex = innerLoopCounter;
            }
        }
        //now that we know the max value and it's index position.
        //we'll replace it with the element @ outerLoopCounter.
        firstNumToExchange = (p+outerLoopCounter);
        secondNumToExchange = (p+innerLoopMaxIndex);
        *firstNumToExchange = *firstNumToExchange + *secondNumToExchange;
        *secondNumToExchange = *firstNumToExchange - *secondNumToExchange;
        *firstNumToExchange = *firstNumToExchange - *secondNumToExchange;
    }
    return p;
}

/** @brief
    Given an array, finds the pair having the maximum
    product.
    @param
    The array containing n numbers.

    @return
    The maximum product possible from all the possible
    pairs.
 */
long long findMaxProduct(int *p,int n){

    int firstLargest = -1;
    int secondLargest = -2;
    int loopCounter;

    for(loopCounter=0;loopCounter<n;loopCounter++){

        if((*(p+loopCounter) > firstLargest ) ){
        //current number largest, assign this to the largest
        //number and assign the value of the largest number
        //to the second largest number.
        secondLargest = firstLargest;
        firstLargest = *(p+loopCounter);
        } else if( (*(p+loopCounter) < firstLargest) && (*(p+loopCounter) > secondLargest) ){
        //current number in between first and second largest
        //assign it to the second largest number.
        secondLargest = *(p+loopCounter);
        }
    }
    //return the max product.
    return ((long long)firstLargest*(long long)secondLargest);
}
