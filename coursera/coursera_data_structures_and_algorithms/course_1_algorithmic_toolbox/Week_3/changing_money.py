#python3
''' Given coins of value 10, 5 and 1 and an integer value m 
    print the minimum number of combinations of the above three
    types of coins sum of which will equal m.
'''
#read the input
m= int(input())
#list containing the available coins.
#zero at the end will act as a signal
#to stop the while loop.
coin = [10,5,1,0]
#pointer to the coin to be used
coinPointer = 0
#coin in use
currCoin = coin[coinPointer]
#final output. Denotes the number
#of coins that have been used.
number = 0
while currCoin != 0:
    #reduce m by currCoin
    m = m - currCoin
    #if m is still positive, it means the 
    #subtraction was valid.
    if m > 0:
        number = number +1
    #subtraction was not valid, need to try
    #a smaller denomination coin
    elif m < 0:
        m = m + currCoin
        coinPointer = coinPointer + 1
        currCoin = coin[coinPointer]
    #subtraction was valid and we've converted
    #entire value of m into coins.
    elif m == 0:
        number = number + 1
        break
print(number)   



