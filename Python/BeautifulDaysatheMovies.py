import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

def beautifulDays(i, j, k):
    count = 0
    for x in range(i, j+1):
        x = str(x)
        reverse_x = x[::-1]
        diff = abs(int(x)-int(reverse_x))
        if diff % k == 0:
            count +=1
    return count

print(beautifulDays(20,23,6))


