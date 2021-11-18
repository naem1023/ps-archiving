#!/bin/python3

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
def bs(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if mid >= target:
            end = mid - 1
        else:
            start = mid + 1
    return
def climbingLeaderboard(ranked, player):
    # Write your code here
    queue = sorted(set(ranked), reverse=True)
    
    idx = len(queue) - 1
    result = []
    
    for p in player:
        while queue[idx] <= p and idx >= 0:
            idx -= 1
        if idx < 0:
            result.append(1)
            continue
        result.append(idx + 2)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
