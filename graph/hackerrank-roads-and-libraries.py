#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#

def dfs(target, visited, graph):
    visited[target] = True
    total = 0
    for node in graph[target]:
        if not visited[node]:
            total += 1
            total += dfs(node, visited, graph)
    return total
    
def roadsAndLibraries(n, c_lib, c_road, cities):
    # Build library in every city
    if c_lib < c_road:
        return c_lib * n
    
    # Write your code here
    from collections import defaultdict
    graph = defaultdict(list)
    
    for c in cities:
        graph[c[0]].append(c[1])
        graph[c[1]].append(c[0])
        
    visited = [ False for _ in range(n + 1)]
    total_path = 0
    
    for i in range(1, n + 1):
        if not visited[i]:
            total_path += dfs(i,visited, graph)
    
    return total_path * c_road + (n - total_path) * c_lib

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
