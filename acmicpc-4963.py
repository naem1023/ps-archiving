import sys
import itertools
sys.setrecursionlimit(10**5)
m = None
check = None
counts = []
path = list(itertools.product([0, -1, 1], repeat=2))
del path[path.index((0,0))]
def get_path(x, y, w, h):
    """Check range and land"""
    answer = []
    
    for i, j in path:
        if 0 <= x + i < w and 0 <= y + j < h:
            if m[y + j][x + i] == 1 and not check[y + j][x + i]:
                answer.append((i, j))
    return answer

def bfs(x, y, w, h):
    check[y][x] = True
    possible = get_path(x, y, w, h)
    for i, j in possible:
        bfs(x + i, y + j, w, h)
    
while True:
    w, h = list(map(int, sys.stdin.readline().strip().split()))
    
    if w == 0 and h == 0:
        break

    check = [[False for _ in range(w)] for _ in range(h)]
    m = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    count = 0
    for j in range(h):
        for i in range(w):
            if not check[j][i] and m[j][i] == 1:
                bfs(i, j, w, h)
                count += 1
    counts.append(count)

for count in counts:
    print(count)