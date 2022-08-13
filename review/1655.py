import sys
from heapq import heappop, heappush

input = sys.stdin.readline
N = int(input())

left_q = []
right_q = []

answers = []
for _ in range(N):
    n = int(input())
    if len(left_q) == len(right_q):
        heappush(left_q, (-n, n))
    else:
        heappush(right_q, (n, n))

    if len(right_q) and left_q[0][1] > right_q[0][1]:
        right = heappop(right_q)[1]
        left = heappop(left_q)[1]
        
        heappush(right_q, (left, left))
        heappush(left_q, (-right, right))

    answers.append(left_q[0][1])

for a in answers:
    print(a)