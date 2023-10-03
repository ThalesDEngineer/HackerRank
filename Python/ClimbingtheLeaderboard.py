import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    rank_player = []
    unique_ranked = sorted(set(ranked), reverse=True)

    for score in player:
        # Use binary search to find the position for the player score
        lo, hi = 0, len(unique_ranked)
        while lo < hi:
            mid = (lo + hi) // 2
            if unique_ranked[mid] == score:
                lo = mid
                break
            elif unique_ranked[mid] < score:
                hi = mid
            else:
                lo = mid + 1

        # Determine the rank of the player score
        rank_player.append(lo + 1)

    return rank_player

print(climbingLeaderboard([100,100,50,40,40,20,10], [5,25,50,120]))
