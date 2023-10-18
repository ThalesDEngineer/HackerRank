#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    count = 0
    for i in str(n):
        if int(i) == 0:
            pass
        else:
            if n % int(i) == 0:
                count +=1
    return count

print(findDigits(1012))