import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    pointshouse = list(range(s, t + 1))
    applelandingpoint = [x+a for x in apples ]
    orangelandingpoint = [x+b for x in oranges]
    applesinhouse = [x for x in applelandingpoint if x in pointshouse]
    orangeinhouse = [x for x in orangelandingpoint if x in pointshouse]
    print (len(applesinhouse))
    print (len(orangeinhouse))
    print (pointshouse)

countApplesAndOranges(7, 10, 3, 12, [1,4,10], [-2, -5, -4])

