import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    countmax = 0
    countmin = 0
    listminmax = [scores[0], scores[0]]
    for i in scores:
        if i < listminmax[0]:
            countmin +=1
            listminmax[0] = i
        elif i > listminmax[1]:
            countmax += 1
            listminmax[1] = i
        else:
            pass
    return countmax, countmin
print(breakingRecords([3,4,21,36,10,28,35,5,24,42]))