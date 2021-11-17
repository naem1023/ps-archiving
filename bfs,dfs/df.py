dist_list = []

def dfs(now, end, graph, visited, dist):
    global dist_list
    if now == end:
        dist_list.append(dist)
    for node in graph[now]:
        if visited[node] == 0:
            visited[node] = 1
            dfs(node, end, visited, dist + 1)

def solution(music):
    global dist_list
    answer = 0
    from collections import defaultdict
    graph = {
        1: [2, 3],
        2: [1, 3],
        3: [1, 2, 4, 5],
        4: [3, 5],
        5: [3, 4, 6, 7],
        6: [5, 7],
        7: [5, 6, 8],
        8: [7, 9, 10],
        9: [8, 10],
        10: [8, 9, 11, 12],
        11: [10, 12],
        12: [10, 11]
    }
    
    for i in range(len(music) - 1):
        visited = [[0] * 13]
        dfs(music[i], music[i + 1], graph, visited, 0)
        answer += min(dist_list)
        dist_list.clear()
    
    return answer

solution([10, 9, 4, 5, 12])