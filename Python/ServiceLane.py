 #!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'serviceLane' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY cases
#

def serviceLane(width, cases):
    result = []
    for i in cases:
        result.append(min(width[min(i):max(i)+1]))
    return result

print(serviceLane([2,3,1,2,3,2,3,3], [[0, 3], [4, 6], [6, 7], [3, 5], [0, 7]]))