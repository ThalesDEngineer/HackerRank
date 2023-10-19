#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#

def squares(a, b):
    # Find the integer square roots
    root_a = math.ceil(math.sqrt(a))
    root_b = math.floor(math.sqrt(b))
    
    # Calculate the count of perfect squares between a and b
    count = root_b - root_a + 1
    
    return count

print(squares(24,49))
