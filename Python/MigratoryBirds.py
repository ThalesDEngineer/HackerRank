import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    arr.sort()
    distinctvalues = set(arr)
    countmax = 0
    for i in distinctvalues:
        counttype = arr.count(i)
        if counttype > countmax:
            countmax = counttype
            typemax = i
    return typemax
print(migratoryBirds([1,2,3,4,5,4,3,2,1,3,4]))