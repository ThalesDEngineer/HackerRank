
import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    count = 0
    for i in range(1, 101):
        factora = [i % x for x in a]
        factorb = [y % i for y in b]
        if sum(factora) == 0 and sum(factorb) == 0:
            count +=1
    return count

print(getTotalX([2,4], [16,32,96]))
      