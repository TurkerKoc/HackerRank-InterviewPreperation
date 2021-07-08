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
    aInS = 0
    for letter in s:
        if letter == "a":
            aInS += 1
    mult = int(n/(len(s)))
    
    aInAll = aInS * mult

    leftLength = n%len(s)
    aInLeft = 0
    for i in range(leftLength):
        if s[i] == "a":
            aInLeft += 1
    aInAll += aInLeft
    return aInAll

if __name__ == '__main__':

    s = "aba"

    n = 10

    result = repeatedString(s, n)
    print result
   