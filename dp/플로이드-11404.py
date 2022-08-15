from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = defaultdict(list)

dp = [[float('inf') if i != j else 0 for j in range(n)] for i in range(n)]

for _ in range(m):
    s, e, c = map(int, input().split())
    dp[s  -1][e - 1] = min(c, dp[s  -1][e - 1])

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

for i in range(n):
    for j in range(n):
        if dp[i][j] == float('inf'):
            dp[i][j] = 0
for d in dp:
    print(*d)