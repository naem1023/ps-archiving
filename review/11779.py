import sys
from heapq import heappush, heappop
from collections import defaultdict
input = sys.stdin.readline
INF = 1e9

N = int(input())
M = int(input())
graph = defaultdict(list)

for _ in range(M):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))
start, end = map(int, input().split())

def dijkstra(start, end):
    dist = [INF for _ in range(N + 1)]
    path = [-1 for _ in range(N + 1)]

    q = []
    dist[start] = 0
    heappush(q, (dist[start], start))
    while q:
        current_cost, current_city = heappop(q)
        
        if dist[current_city] < current_cost:
            continue
        for next_city, next_cost in graph[current_city]:
            total_cost = current_cost + next_cost
            if dist[next_city] > total_cost:
                dist[next_city] = total_cost
                path[next_city] = current_city
                heappush(q, (total_cost, next_city))

    return dist[end], path

cost, path = dijkstra(start, end)

path_result = []
temp = end
while temp != -1:
    path_result.append(temp)
    temp = path[temp]

path_result.reverse()
print(cost)
print(len(path_result))
print(*path_result)

