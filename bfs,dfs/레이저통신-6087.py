import sys
input = sys.stdin.readline

W, H = map(int, input().split())

board = []
for _ in range(H):
    board.append(input())


dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

C = []
for i in range(H):
    for j in range(W):
        if board[i][j] == 'C':
            C.append((i, j))

(sx, sy), (ex, ey) = C

from collections import deque
visited = [[float("inf")] * W for _ in range(H)]
def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            while True:
                if not (0 <= nx < H and 0 <= ny < W):
                    break
                if board[nx][ny] == '*':
                    break
                if visited[nx][ny] < visited[x][y] + 1:
                    break
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                nx = nx + dx[i]
                ny = ny + dy[i]
            # print(visited)
bfs(sx, sy)

print(visited[ex][ey] - 1)
