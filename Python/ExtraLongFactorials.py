#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    a = 1
    for i in range(n,0,-1):
        a *= i
    return a

print(extraLongFactorials(25))