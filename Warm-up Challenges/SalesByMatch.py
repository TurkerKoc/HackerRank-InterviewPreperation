#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def loop(n,sortedAr):
    for i in range(n):
        for j in range(i+1,n):
            if sortedAr[i] == sortedAr[j]:
                result = (i,j,True)
                return result
    result = (-1,-1,False)
    return result

def sockMerchant(n, ar):
    pairCount = 0
    sortedAr = sorted(ar)
    while True:        
        print(sortedAr)
        result = loop(n,sortedAr)
        print(result)               
        if not result[2]:
            break
        print("deleting element at index " + str(result[0]) + " and " + str(result[1]))      
        remove_indices = [result[0],result[1]]
        sortedAr = [i for j, i in enumerate(sortedAr) if j not in remove_indices]
        print()  
        pairCount += 1
        n -= 2
    return pairCount

    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(12)

    ar = list([10, 20, 10, 10, 30, 50, 10, 20, 20, 50, 11, 20])

    result = sockMerchant(n, ar)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
