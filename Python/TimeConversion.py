import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

#first try, will improve it with time

def timeConversion(s):
    if ''.join(s[-2:]) == "PM":
        if s[:2] != "12":
            s = s.replace(s[:2], str(int(s[:2]) + 12), 1)
    if ''.join(s[-2:]) == "AM":
        if s[:2] == "12":
            s = s.replace(s[:2], "00")
    return s[:-2]
print(timeConversion("07:05:45PM"))
print(timeConversion("12:05:45PM"))
print(timeConversion("12:05:45AM"))
print(timeConversion("03:05:45AM"))