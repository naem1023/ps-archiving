from collections import deque

def bfs(place):
    starts = []
    
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                starts.append([i, j])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    for start in starts:
        queue = deque([start])
        visited = [ [0] * 5 for i in range(5)]
        distance = [ [0] * 5 for i in range(5)]
        # start point은 방문한걸로
        visited[start[0]][start[1]] = 1
        
        while queue:
            target = queue.popleft()
            
            for i in range(4):
                target_y = target[0] + dy[i]
                target_x = target[1] + dx[i]
                
                if visited[target_y][target_x] == 0 \
                    and 0 <= target_x < 5 and 0 <= target_y < 5:
                    if place[target_y][target_x] == 'O':
                        distance[target_y][target_x] = distance[target[0]][target[1]] + 1
                        visited[target_y][target_x] = 1
                        queue.append([target_y, target_x])

                    elif place[target_y][target_x] == 'P' \
                        and distance[target_y][target_x] <= 1:
                        return 0
                
    return 1
                
def solution(places):
    answer= []
    
    for place in places:
        answer.append(bfs(place))
    
    return answer

a = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(a))