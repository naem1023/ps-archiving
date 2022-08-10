from collections import defaultdict

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
shoot = int(input())
shoot_list = list(map(lambda x: n - int(x), input().split()))
board_copy = [[False] * m for _ in range(n)]

dxs = (0, 1, -1, 0)
dys = (1, 0, 0, -1)

def remove_mineral(i, j):
    # 바닥과 연결된 미네랄 클러스터들을 제거
    stack = [(i, j)]
    while stack:
        node = stack.pop()
        board_copy[node[0]][node[1]] = True # 빈 칸으로 표기
        for di, dj in zip(dxs, dys):
            ni, nj = node[0] + di, node[1] + dj
            if ni < 0 or ni >= n or nj < 0 or nj >= m:
                continue
            if not board_copy[ni][nj]: # 동서남북으로 있는 미네랄들을 스택에 추가
                stack.append((ni, nj))

def air_mineral():
    # remove_mineral이 실행된 후에 실행된다
    # 즉, 공중에 떠 있는 모든 미네랄의 위치를 높이별로 반환한다.
    air_dict = defaultdict(list)
    for i in range(n):
        for j in range(m):
            if not board_copy[i][j]:
                air_dict[j].append(i) # column별 row 정보 저장
    
    return air_dict

# board는 동굴의 단면도이다. 즉, 2차원의 평면이 옆으로 누워서 서 있다고 생각하면 된다.
for order in range(len(shoot_list)):
    x = shoot_list[order] # 막대를 던지는 높이
    T = 0 # 0: 미네랄이 파괴되지 않았다, 1: 미네랄이 파괴됐다.
    
    if order % 2 == 0: # 왼쪽에서 던질 순서
        for y in range(m): # 왼쪽부터 미네랄 탐색
            if board[x][y] == 'x':
                board[x][y] = '.'
                T = 1
                break
    elif order % 2 == 1:
        for y in range(m - 1, -1, -1):
            if board[x][y] == 'x':
                board[x][y] = '.'
                T = 1
                break

    if T == 1: # 미네랄이 파괴된 경우, 공중에 떠있는 클러스터를 처리
        # 모든 동굴의 단면을 True, False로 매핑
        for i in range(n):
            for j in range(m):
                if board[i][j] == '.':
                    board_copy[i][j] = True
                else:
                    board_copy[i][j] = False
        
        # board_copy 상에서 공중에 떠 있는 클러스터를 제외한, 나머지 미네랄들을 모두 제거
        for col in range(m):
            if not board_copy[-1][col]:
                remove_mineral(n - 1, col)

        air_cluster = air_mineral()

        # print(air_cluster)

        if air_cluster:
            min_v = 100

            for y in air_cluster.keys(): # column 탐색
                for x in air_cluster[y]: # 높이 탐색
                    for fx in range(x + 1, n): # 위에서부터 내려오는게 숫자가 커지는 방향이니까 range(x + 1, n)
                        if board[fx][y] == 'x' and fx not in air_cluster[y]:
                            # 미네랄이 있으면서 공중에 떠 있지 않다고 체크된 위치를 발견
                            min_v = min(min_v, fx - x - 1) # 내려가야 할 높이의 차이를 계산
                    if fx == n - 1 and board[fx][y] == '.':
                        min_v = min(min_v, fx - x)

            for y in air_cluster.keys():
                air_cluster[y].sort(reverse=True)
                for x in air_cluster[y]:
                    board[x][y] = '.'
                    # print(shoot_list[order], x, min_v, y)
                    board[x + min_v][y] = 'x'

for row in board:
    print(''.join(row))
