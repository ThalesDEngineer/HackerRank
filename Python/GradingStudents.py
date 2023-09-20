import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    gradesNew = []
    for i in grades:
        grade = i
        remainder = i % 10
        if remainder not in (0,5):
            if remainder < 5:
                roundlimit = (round(i/10) * 10) + 5
            else: 
                roundlimit = round(i/10) * 10
            if roundlimit - i < 3:
                grade = roundlimit
        else:
            grade = i
        if grade < 40:
            grade = i
        gradesNew.append(grade)
    return(gradesNew)

numbers = [
    57, 97, 56, 81, 38, 30, 1, 9, 23, 69, 24, 44, 69, 12, 61, 50, 84, 3, 17, 91,
    39, 26, 18, 66, 76, 31, 42, 52, 21, 55, 57, 18, 3, 97, 85, 78, 45, 94, 39, 90,
    93, 60, 73, 93, 32, 8, 57, 19, 52, 4, 97, 32, 85, 39, 75, 27, 54, 0
]

print(gradingStudents(numbers))