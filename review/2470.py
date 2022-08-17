import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

arr.sort()

start, end = 0, N - 1
answer = 2e9 + 1
answer_l = [0, 0]

while start < end:
    step_sum = arr[end] + arr[start]
    if abs(step_sum) < answer:
        answer = abs(step_sum)
        answer_l = [arr[start], arr[end]]

    if step_sum < 0:
        # 합이 음수: 0에 가까워지기 위해서 start 증가
        start += 1
    else:
        end -= 1
print(*answer_l)
        