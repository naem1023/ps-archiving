import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))

start = 0
end = N - 1

arr.sort()
min_val = 2e9 + 1
answer = []

while start < end:
    step_sum = arr[start] + arr[end]
    if abs(step_sum) < min_val:
        min_val = abs(step_sum)
        answer = [arr[start], arr[end]]
    
    if step_sum < 0:
        start += 1
    else:
        end -= 1

print(answer[0], answer[1])