N = int(input())
A = list(map(int, input().split()))

M = int(input())
B = list(map(int, input().split()))

def bs(A, start, end, b):
    mid = (start + end) // 2
    while start <= end:
        if A[mid] > b:
            end = mid - 1
        elif A[mid] < b:
            start = mid + 1
        else:
            return True
        mid = (start + end) // 2
    return False

answer ={}
A.sort()
# print(A)
for b in B:
    if b in answer:
        print(1)
    else:
        if bs(A, 0, len(A) - 1, b):
            print(1)
            answer[b] = True
        else:
            print(0)
    