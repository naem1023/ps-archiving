from collections import deque

graph_list = {1: set([2, 3, 4]),
              2: set([1, 5]),
              3: set([1, 6, 7]),
              4: set([1, 8]),
              5: set([2, 9]),
              6: set([3, 10]),
              7: set([3]),
              8: set([4]),
              9: set([5]),
              10: set([6]),
              }
root_node = 1

def BFS_with_adj_list(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            # 차집합 표현
            # 방문하지 않은 node들을 queue에 넣는다.
            queue += graph[n] - set(visited)
    return visited

def DFS_with_adj_list(graph, root):
    visited = []
    stack = deque([root])

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited

# print(BFS_with_adj_list(graph_list, root_node))
  
print(DFS_with_adj_list(graph_list, root_node))
