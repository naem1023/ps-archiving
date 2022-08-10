import sys

N, M = list(map(int, sys.stdin.readline().strip().split()))

arr = [0]
arr.extend(list(map(int, sys.stdin.readline().strip().split())))
prefix_sum = [arr[0]]
for i in range(1, N + 1):
    prefix_sum.append(prefix_sum[i - 1] + arr[i])

for _ in range(M):
    i, j = list(map(int, sys.stdin.readline().strip().split()))
    print(prefix_sum[j] - prefix_sum[i - 1])
    