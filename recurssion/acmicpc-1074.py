import sys
input = sys.stdin.readline

n, r, c = list(map(int, input().split()))
ans = 0

def Z(y, x, size):
    """
    영역을 4분할하는 단위 함수.
    영역의 기준점은 해당 영역의 가장 왼쪽 위 구석.
    y: r
    x: c
    """
    global ans

    # 검색 영역이 정확하게 (r, c)와 일치한다면 반환
    if y == r and x == c:
        print(ans)
        return

    #  r, c가 현재 사분면에 존재한다면
    if r < y + size and r >= y and c < x + size and c >= x:
        # 1사분면 탐색
        Z(y, x, size // 2)
        # 2사분면 탐색
        Z(y, x + size // 2, size // 2)
        # 3사분면 탐색
        Z(y + size // 2, x, size // 2)
        # 4사분면 탐색
        Z(y + size // 2, x + size // 2, size // 2)
    # 지나왔다고 간주되는 현재 영역들을 모두 ans에 누적시킨다.
    else:
        ans += size * size

# (0, 0), size=N^2부터 시작해서 검색 영역을 좁혀간다.
Z(0, 0, (1 << n))