#!/bin/python3

import math
import os
import random
import re
import sys
import datetime

#
# Complete the 'libraryFine' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d1
#  2. INTEGER m1
#  3. INTEGER y1
#  4. INTEGER d2
#  5. INTEGER m2
#  6. INTEGER y2
#

def libraryFine(d1, m1, y1, d2, m2, y2):
    return_date = datetime.date(y1,m1,d1)
    due_date = datetime.date(y2,m2,d2)
    if return_date <= due_date:
        fine = 0
    elif m1 == m2 and y1 == y2:
        delta = return_date - due_date
        fine = delta.days * 15
    elif y1 == y2:
        delta = m1 - m2
        fine = delta * 500
    else:
        fine = 10000
    return fine

print(libraryFine(14,9,2017,5,9,2017))

