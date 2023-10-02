import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    a.sort()
    maxcountarray = 1
    for index, value in enumerate(a):
        prevcountarray = maxcountarray
        countarray = 1
        if index != -1:
            for j in a[index+1:]:
                if j - value <=1:
                    countarray +=1
        maxcountarray = max(countarray, prevcountarray)
    return maxcountarray


print(pickingNumbers([66] * 100))