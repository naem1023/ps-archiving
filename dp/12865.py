import sys

N, K = list(map(int, sys.stdin.readline().strip().split()))

W = [-1]
V = [-1]
for _ in range(N):
    w, v = list(map(int, sys.stdin.readline().strip().split()))    
    W.append(w)
    V.append(v)

dp = [0 for _ in range(K + 1)]

for i in range(1, N + 1):
    for j in range(K, -1, -1):
        if j - W[i] >= 0:
            dp[j] = max(dp[j], dp[j - W[i]] + V[i])

print(dp[K])
# dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
# for i in range(1, N + 1):
#     for j in range(1, K + 1):
#         if j - W[i] >= 0:
#             dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - W[i]] + V[i])
#         else:
#             dp[i][j] = dp[i - 1][j]
# print(dp[N][K])

