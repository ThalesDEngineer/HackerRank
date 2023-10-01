import math
import math
import os
import random
import re
import sys

def formingMagicSquare(s):
    # All possible 3x3 magic squares
    magic_squares = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
    ]
    
    # Compute the cost to convert the given matrix to a magic square
    def compute_cost(s, magic_square):
        return sum(abs(s[i][j] - magic_square[i][j]) for i in range(3) for j in range(3))

    # Find the minimum cost among all magic squares
    min_cost = float('inf')
    for magic_square in magic_squares:
        cost = compute_cost(s, magic_square)
        min_cost = min(min_cost, cost)

    return min_cost

# Sample input
s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
print(formingMagicSquare(s))  
           