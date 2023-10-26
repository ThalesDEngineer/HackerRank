#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'workbook' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#

def workbook(n, k, arr):
   page = 1
   count_special = 0
   for i in arr:
          for j in range(1, i+1):
               if j == page:
                    count_special +=1
               if j % k == 0 or j == i:
                    page +=1 
   return count_special

print(workbook(5,3,[4,2,6,1,10]))