from collections import deque, defaultdict

def solution(n, edge):
    answer = 0
    
    graph = defaultdict(list)
    
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    queue = deque([1])
    
    dist_dict = {i:0 for i in range(1, n + 1)}
    dist = 1
    while queue:
        for _ in range(len(queue)):
            target = queue.popleft()
        
            # bfs이고 edge의 거리값이 없다.
            # 따라서 최초로 방문하는 node들만 거리 갱신을 해줘도 최소 거리 값이 저장된다. 
            if dist_dict[target] == 0:
                dist_dict[target] += dist
                
                for e in graph[target]:
                    queue.append(e)
        dist += 1
            
    del dist_dict[1]
    max_dist = max(dist_dict.values())
    
    for key in dist_dict:
        if dist_dict[key] == max_dist:
            answer += 1
    return answer