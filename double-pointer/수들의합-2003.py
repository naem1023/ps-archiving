import sys
input = sys.stdin.readline

def solution(N, M, arr):
    start, end = 0, 0
    subsum = arr[0]
    count = 0
    while True:
        if subsum < M:
            end += 1
            if end >= N:
                break
            subsum += arr[end]
        elif subsum == M:
            count += 1
            subsum -= arr[start]
            start += 1
        else:
            subsum -= arr[start]
            start += 1
    return count

N, M = map(int, input().split())
arr = list(map(int, input().split()))

print(solution(N, M, arr))