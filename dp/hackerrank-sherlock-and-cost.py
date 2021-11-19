#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cost' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY B as parameter.
#

def cost(B):
    # Write your code here
    S = [ [0] * 2 for _ in range(len(B))]
    
    for i in range(1, len(B)):
        # S[i] = 1
        S[i][0] = max( (S[i - 1][0] + 0), (S[i - 1][1] + abs(1 - B[i - 1])))
        
        # S[i] = B[i]
        S[i][1] = max( (S[i - 1][0] + abs(B[i] - 1)), (S[i - 1][1] + abs(B[i] - B[i - 1])))
        
    return max(max(S))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        B = list(map(int, input().rstrip().split()))

        result = cost(B)

        fptr.write(str(result) + '\n')

    fptr.close()
