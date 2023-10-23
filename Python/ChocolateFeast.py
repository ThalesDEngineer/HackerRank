#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'chocolateFeast' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c
#  3. INTEGER m
#

def chocolateFeast(n, c, m):
   bars = wrappers = int(n/c)
   while wrappers >= m:
      bars_added = int(wrappers/m)
      wrappers = wrappers % m
      bars += bars_added
      wrappers += bars_added
   return bars

print(chocolateFeast(10,2,5))
print(chocolateFeast(12,4,4))
print(chocolateFeast(6,2,2))