#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    aInS = 0 #number of a's in s
    for letter in s: #finding number of a's in s
        if letter == "a":
            aInS += 1

    mult = int(n/(len(s))) #finding how many s string exist in n length
    
    aInAll = aInS * mult #find a in all

    leftLength = n%len(s) #finding a in last s (can be smaller than lenght of s)
    aInLeft = 0
    for i in range(leftLength):
        if s[i] == "a":
            aInLeft += 1

    aInAll += aInLeft #add a's in last s
    return aInAll

if __name__ == '__main__':

    s = "aba"

    n = 10

    result = repeatedString(s, n)
    print result
   