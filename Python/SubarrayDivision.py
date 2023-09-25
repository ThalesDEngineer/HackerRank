import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
   count = 0
   for index, value in enumerate(s):
      if (m + index) <= len(s):
         msum = sum(s[index:m+index])
         if msum == d:
            count +=1
   return count

print(birthday([4], 4, 1))
        