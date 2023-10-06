#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    for x in range(n+1):
        if x == 0:
            h = 1
        elif x % 2 != 0:
            h = h * 2
        else:
            h = h + 1
    return h

print(utopianTree(4))
     