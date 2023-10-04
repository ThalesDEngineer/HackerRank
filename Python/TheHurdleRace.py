#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hurdleRace' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY height
#

def hurdleRace(k, height):
    if k < max(height):
        return max(height) - k
    else:
        return 0
    
print(hurdleRace(7, [2,5,4,5,2]))
print(hurdleRace(4, [1,6,3,5,2]))
print(hurdleRace(1, [1,2,3,3,2]))
            