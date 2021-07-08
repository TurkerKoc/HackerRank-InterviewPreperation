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
    mult = int(n/(len(s)))
    s = s * (mult+1)
    s = s[:n]
    print(s)
    occurence = 0
    for i in range(len(s)):
        if s[i] == "a":
            occurence += 1
    return occurence

if __name__ == '__main__':

    s = "aba"

    n = 10

    result = repeatedString(s, n)
    print result
   