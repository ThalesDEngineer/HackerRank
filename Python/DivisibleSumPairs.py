import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    ar.sort()
    count = 0
    for index, value in enumerate(ar):
        if n - index != 1:
            for a in ar[index + 1:]:
                if (value + a) % k == 0:
                    count +=1
    return count

print(divisibleSumPairs(6, 5, [1,2,3,4,5,6]))
