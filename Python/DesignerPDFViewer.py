import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    alphabet = list(map(chr, range(97,123)))
    heightdict = dict(zip(alphabet, h))
    height = []
    for letter in word:
        height.append(heightdict[letter])
    return max(height) * len(word)

print(designerPdfViewer([1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5, 7], 'zaba'))