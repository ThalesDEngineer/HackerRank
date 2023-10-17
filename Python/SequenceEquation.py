#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def permutationEquation(p):
    lst_y = []
    for i in range(1, len(p) + 1):
        first_index = p.index(i) + 1
        second_index =  p.index(first_index) + 1
        lst_y.append(second_index)
    return lst_y

print(permutationEquation([4,3,5,1,2]))