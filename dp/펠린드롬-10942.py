import sys

N = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())

dp = [[0 for _ in range(N)] for _ in range(N)]


for num_len in range(N):
    for start in range(N - num_len):
        # [start, end]로 window slicing을 하겠다는 의미
        end = start + num_len

        if start == end:
            dp[start][end] = 1
        elif nums[start] == nums[end]:
            if start + 1 == end:
                dp[start][end] = 1
            elif dp[start + 1][end - 1]:
                dp[start][end] = 1

for question in range(M):
    s, e = map(int, sys.stdin.readline().split())
    print(dp[s - 1][e - 1])