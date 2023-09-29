#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    flipsfront = int(p/2)
    if n % 2 == 0:
        flipsback = int((n- p + 1)/2)
    else:
        flipsback = int((n-p)/2)
    return min(flipsfront, flipsback)

print(pageCount(5,4))
print(pageCount(6,2))