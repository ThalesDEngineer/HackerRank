
import math
import os
import random
import re
import sys

#
# Complete the 'angryProfessor' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY a
#

def angryProfessor(k, a):
    a.sort()
    count = 0
    for i in a:
        if i <= 0:
            count +=1
    if count < k:
        return "YES"
    else:
        return "NO"
    
print(angryProfessor(3, [-1,3,4,2]))