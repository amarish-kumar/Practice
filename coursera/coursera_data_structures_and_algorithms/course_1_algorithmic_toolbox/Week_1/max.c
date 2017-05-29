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
    why take the pain. This implementation simply finds
    the two largest numbers in the input and returns
    their product.
*/

#include <stdio.h>
#include <stdlib.h>

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
    Given an array, finds the pair having the maximum
    product.
    @param1
    The array containing n numbers.
    @param2
    Size of the array.
    @return
    The maximum product possible from all the possible
    pairs.
 */
long long findMaxProduct(int *p,int n){

    long long result=-1;
    int loopCounter = 0;
    long long largest = -1;
    long long secondLargest = -1;
    

    //Parse the array and determine the two largest numbers.
    for( ; loopCounter < n; loopCounter++ ){

        //If number at current is largest yet encountered.
        if( p[loopCounter] > largest){
            secondLargest = largest;
            largest = p[loopCounter];
        }
        else if(p[loopCounter] > secondLargest){
            secondLargest = p[loopCounter];
        } else{
            continue;
        }
    }
    result = largest * secondLargest;
    //return the max product.
    return result;
}
