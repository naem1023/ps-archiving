import sys
input = sys.stdin.readline
N, S = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, 1

sum_arr = [arr[0]]

for i in range(1, len(arr) + 1):
    sum_arr.append(sum_arr[i - 1] + arr[i - 1])

answer = 1000001
start = 0
end = 1

while start != N:
    if sum_arr[end] - sum_arr[start] >= S:
        if end - start < answer:
            answer = end - start
        start += 1
    else:
        if end != N:
            end += 1
        else:
            start += 1

if answer != 1000001:
    print(answer)
else:
    print(0)