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
    position = 0
    countvalley = 0
    for i in path:
        prevposition = position
        if i == 'D':
            position -=1
        else:
            position +=1
        if prevposition == -1 and position == 0:
            countvalley +=1
    return countvalley

print(countingValleys(8, 'UDDDUDUU'))
 