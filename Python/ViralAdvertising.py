#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    adv = 5
    likes_cum = 0
    for i in range(n):
       if i > 0:
           adv = likes * 3
       likes = math.floor(adv/2)
       likes_cum += likes
    return likes_cum

print(viralAdvertising(1))
print(viralAdvertising(5))
print(viralAdvertising(4))