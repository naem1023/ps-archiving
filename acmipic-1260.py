# MAP = [list(map(itn, input().split())) for _ in range(int(input()))]

n, m, v = list(map(int, input().split()))

graph = [list(map(int, input().split(' '))) for _ in range(m)]

graph_de = {}

def graph_add(g, v1, v2):
    if v1 not in g:
        g[v1] = set([v2])
    else:
        g[v1].add(v2)

for g in graph:
    graph_add(graph_de, g[0], g[1])
    graph_add(graph_de, g[1], g[0])

# print(graph)
# print(graph_de)
from collections import deque

def dfs(g, root):
    visited = []
    stack = deque([root])

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in g:
                push = sorted(g[n] - set(visited), reverse=True)
                stack += list(push)
    return visited


def bfs(g, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in g:
                push = sorted(g[n] - set(visited))
                queue += list(push)
    return visited

dfs_list = [str(i) for i in dfs(graph_de, v)]
bfs_list = [str(i) for i in bfs(graph_de, v)]
print(' '.join(dfs_list))
print(' '.join(bfs_list))