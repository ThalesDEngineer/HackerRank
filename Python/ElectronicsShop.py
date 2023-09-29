import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    spent = -1
    for i in keyboards:
        for j in drives:
            if i + j <= b:
                if i + j > spent:
                    spent = i + j
    return spent

print(getMoneySpent([4], [5], 5))