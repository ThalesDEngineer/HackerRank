import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    fullbill = sum(bill)
    billnoAnna = fullbill - bill[k]
    Annaowes = billnoAnna / 2
    if b - Annaowes > 0:
        print(int(b - Annaowes))
    else:
        print('Bon Appetit')

bonAppetit(k=1,bill=[3,10,2,9],b=12)