#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    array_cities = list(range(n))
    max_total = 0
    for i in array_cities:
        max_dist = min([abs(x-i) for x in c])
        max_total = max(max_dist, max_total)
    return max_total

print(flatlandSpaceStations(5, [0,4]))