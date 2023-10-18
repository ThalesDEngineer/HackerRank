#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    letters = 0 
    for i in range(min(len(s), len(t))):
         if s[i] == t[i]:
             letters += 1
         else:
             break
 
    delt = len(s) - letters
    appd = len(t) - letters
 
    total_changes = delt + appd

    if k - total_changes >=0:
        return "Yes"
    else:
        return "No"
