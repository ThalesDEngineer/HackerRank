#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    e = 100
    idx = 0
    while True:
        idx = (idx + k) % len(c)
        
        if c[idx] == 1:
            e -= 3
        else:
            e -= 1

        if idx == 0:
            break
    return e
        

print(jumpingOnClouds([1,1,1,0,1,1,0,0,0,0], 3))