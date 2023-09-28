
import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    setofsocks = set(ar)
    totalpairs = 0
    for i in setofsocks:
        countofsocks = ar.count(i)
        pairs = int(countofsocks/2)
        totalpairs += pairs
    return totalpairs

print(sockMerchant(9, [10,20,20,10,10,10,30,50,10,20]))
