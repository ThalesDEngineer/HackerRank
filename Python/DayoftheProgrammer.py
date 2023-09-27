import math
import os
import random
import re
import sys
from datetime import date, datetime, timedelta
#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    firstdayoftheyear = datetime(year, 1, 1)
    if year < 1918 and year >= 1700 and year % 4 == 0 and year % 100 == 0:
        dayoftheprogrammer = firstdayoftheyear + timedelta(days=255-1)
    elif year == 1918:
        dayoftheprogrammer = firstdayoftheyear + timedelta(days=255+13)
    else:
        dayoftheprogrammer = firstdayoftheyear + timedelta(days=255)
    dayoftheprogrammer = dayoftheprogrammer.strftime('%d.%m.%Y')
    return dayoftheprogrammer

print(dayOfProgrammer(1916))