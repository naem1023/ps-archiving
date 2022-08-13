import sys
input = sys.stdin.readline

N, B = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

def mul(arr1, arr2):
    results = [[0 for _ in range(N)] for _ in range(N)]
    
    for row in range(N):
        for col in range(N):
            e = 0
            for i in range(N):
                e += arr1[row][i] * arr2[i][col]
            results[row][col] = e % 1000

    return results

one = [[1 for _ in range(N)] for _ in range(N)]
def square(cur, n):
    # if n == 0:
    #     return one
    if n == 1:
        for i in range(N):
            for j in range(N):
                cur[i][j] %= 1000
        return cur

    cache = square(cur, n // 2)
    if n % 2:
        return mul(mul(cache, cache), cur)
    else:
        return mul(cache, cache)

arr = square(arr, B)
for a in arr:
    print(*a)