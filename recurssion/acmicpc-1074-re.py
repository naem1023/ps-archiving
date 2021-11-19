import sys
input = sys.stdin.readline

N, r, c = list(map(int, input().split()))

cnt = 0
def Z(y, x, size):
    global cnt

    if y == r and x == c:
        print(cnt)
        return
    
    if y <= r and r < y + size and x <= c and c < x + size:
        Z(y, x, size // 2)
        Z(y, x + size // 2, size // 2)
        Z(y + size // 2, x, size // 2)
        Z(y + size // 2, x + size // 2, size // 2)

    else:
        cnt += size ** 2

Z(0, 0, 2 ** N)