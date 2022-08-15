import sys
from collections import defaultdict
from heapq import heappop, heappush

INF = 1e9
def dijkstra(start, end):
    dist = [INF for _ in range(N + 1)]
    dist[start] = 0

    path = [-1 for _ in range(N + 1)]

    q = []
    heappush(q, [0, start])
    while q:
        cost, current = heappop(q)
        # city는 잘 갱신돼있으니 건들 필요가 없다.
        if dist[current] < cost:
            continue
        for next_city, next_cost in graph[current]:
            current_cost = next_cost + cost
            if current_cost < dist[next_city]:
                dist[next_city] = current_cost
                path[next_city] = current
                heappush(q, [current_cost, next_city])
    return dist[end], path


N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())

graph = defaultdict(list)
for _ in range(M):
    s, e, v = map(int, sys.stdin.readline().strip().split())
    graph[s].append((e, v))

start, end = map(int, sys.stdin.readline().strip().split())

min_cost, path = dijkstra(start, end)
path_result = []
temp = end
while temp != -1:
    path_result.append(temp)
    temp = path[temp]

print(min_cost)
print(len(path_result))
path_result.reverse()
print(*path_result)