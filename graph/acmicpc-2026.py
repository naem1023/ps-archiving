from sys import stdin
from heapq import heappush,heappop

input = stdin.readline

k, n, f = map(int, input().split())

# 친구 목록을 저장하는 리스트
# i번째 index에는 i의 친구들이 리스트로 저장된다.
adj_list = [[] for _ in range(n+1)]

# 친구 관계가 체크되는 adjacency matrix
adj_mat = [[False]*(n+1) for _ in range(n+1)]

for _ in range(f):
    a,b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

    adj_mat[a][b] = adj_mat[b][a] = True

for idx in range(1,n+1):
    adj_list[idx].sort()

end = -1

def solv():
    for start in range(1,n+1):
        # 친구인 사람들이 순서 없이 반환
        rst = bfs(start)
        if rst:
            rst.sort()
            for num in rst:
                print(num)
            return
    print(-1)

def bfs(start):
    # 방문 여부 체크
    visited = [False] * (n + 1)

    # 모두 친구인 사람들만 저장하는 리스트
    path = [start]

    # 친구 관계를 체크할 사람들의 priority queue
    pq = [start]

    visited[start] = True
    while pq:
        now = heappop(pq)
        # now의 친구들 모두 호출
        for nxt in adj_list[now]:
            if not visited[nxt]:
                visited[nxt] = True
                flag = False
                # 모두 친구 관계인 사람들을 호출
                for target in path:
                    # nxt가 path 내의 임의의 사람과 친구가 아니라면 nxt는 path에 넣지 않는다.
                    if not adj_mat[nxt][target]:
                        flag = True
                        break

                if not flag:
                    path.append(nxt)
                    if len(path) == k:
                        return path
                    heappush(pq, nxt)
    return None

if k == 1:
    print(1)
else:
    solv()