/** Stress test for the implementation of the 
    maximum pairwise product solution. Test
    will generate a set of random numbers 
    and will give these as an input to two
    different implemetatios of the maximum
    pairwise product solution and then just 
    compare the result of the two. If there
    is a difference in the results then one
    of the solution is incorrect.
*/


#include <stdio.h>
#include <time.h>
#include <stdlib.h>

long long findMaxProduct_slow(int *p,int n);
long long findMaxProduct_fast(int *p,int n);

void main(){

    //size of the input array.
    //to be randomly chosen.
    int n;    
    //input array.
    int *numbers;
    //loop counter.
    int i;
    //fast solution answer.
    long long fastAns;
    //slow solution answer.
    long long slowAns;

    //This is to be executed once only.
    srand(time(NULL));
    
    while(1){
        //randomly generate size of the input array.
        n = 5 + (int)(10*((double)rand()/RAND_MAX));
        printf("%d",n);
        //allocate memory for the array.
        numbers = (int*)malloc(n*sizeof(int));
        for(i=0;i<n;i++){
            //populate the array.
            *(numbers+i)= (rand()%100000);
        }
    
        //send this array to the fast solution.
        //This is the solution that has to be 
        //stress tested.
        fastAns = findMaxProduct_fast(numbers,n);    
        //send this array to the slow/trivial
        //solution.Above solution has to be
        //tested against this.
        slowAns = findMaxProduct_slow(numbers,n);

        //now compare the results from both the
        //solutions and print out the case in 
        //which there is a difference.
        if(fastAns != slowAns){
            printf("case causing different results detected\n");
            for(i =0;i<n;i++){
                printf("%d", *(numbers+i));
                printf(",");
            }
            printf("\nfast solution answer : ");
            printf("%llu",fastAns);
            printf("\nslow solution answer : ");
            printf("%llu\n",slowAns);
            break;
        } else {
            printf("OK\n");
        }
    }
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
long long findMaxProduct_slow(int *p,int n){

    long long result=-1;
    int outerLoopCounter;
    int innerLoopCounter;
    long long currentProduct;

    for(outerLoopCounter=0;outerLoopCounter<n;outerLoopCounter++){
    
        for(innerLoopCounter=outerLoopCounter+1;innerLoopCounter<n;innerLoopCounter++){

            //find the product of the current pair.
            currentProduct = (((long long)*(p+outerLoopCounter)) * ((long long)*(p+innerLoopCounter)));
            if (result < currentProduct ){
            //largest product yet found, assign to result.
            result =  currentProduct;
            }
        }
    }
    //return the max product.
    return result;
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
long long findMaxProduct_fast(int *p,int n){

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
