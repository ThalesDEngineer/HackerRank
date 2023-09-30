#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
   if abs(x - z) < abs(y - z):
      print("Cat A")
   elif abs(y-z) < abs(x-z):
      print("Cat B")
   else:
      print("Mouse C") 

catAndMouse(1,3,2)