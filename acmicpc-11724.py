from sys import stdin
import sys
import collections
sys.setrecursionlimit(10**6)
N, M = list(map(int, stdin.readline().split()))
g = collections.defaultdict(list)

for _ in range(M):
    _input = list(map(int, stdin.readline().strip().split()))
    g[_input[0]].append(_input[1])
    g[_input[1]].append(_input[0])

check = [False] * (N + 1)
count = 0
def dfs(node):
    check[node] = True
    for v in g[node]:
        if not check[v]:
            dfs(v)

for idx in range(1, N + 1):
    if not check[idx]:
        dfs(idx)
        count += 1

print(count)