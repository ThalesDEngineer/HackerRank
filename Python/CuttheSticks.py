#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    answer = []
    while len(arr) > 0:
        answer.append(len(arr))
        stick_sub = min(arr) 
        arr = [x - stick_sub for x in arr]
        arr = list(filter(lambda num: num!=0, arr))
    return answer

print(cutTheSticks([5,4,4,2,2,8]))