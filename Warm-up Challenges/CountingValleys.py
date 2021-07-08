#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    level = 0
    belowFlag = False
    valleyCount = 0
    for step in path:
        if step == "U":
            level += 1
        elif step == "D":
            level -= 1
        if not belowFlag and level < 0:
            belowFlag = True
            valleyCount += 1
        if belowFlag == True and level == 0:
            belowFlag = False            
    return valleyCount

if __name__ == '__main__':
    steps = 8
    path = "UDDDUDUU"

    result = countingValleys(steps, path)
    print(result)
