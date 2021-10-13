import sys, copy

# [0, 3] 순서롱 상하좌우
def move(direction):
    if direction == 0:
        # arr의 모든 column을 보기 위해서 n번 본다
        for j in range(n):
            idx = 0 
            # arr의 0번째 row를 빼고 모든 row에 대해서 봐야하므로
            for i in range(1, n):
                # arr의 요소가 0이 아니라면 == 비어있지 않다면
                if arr[i][j]:
                    # 일단 옮길 것을 저장해둔다.
                    temp = arr[i][j]
                    # 일단 옮길 것의 본래 공간을 비워둔다.
                    arr[i][j] = 0
                    # 옮겨갈 곳이 0일 때
                    if arr[idx][j] == 0:
                        # 비어있으므로 그냥 옮기면 된다.
                        arr[idx][j] = temp
                    # 옮기는 것과 옮겨갈 것이 같다면
                    elif arr[idx][j] == temp:
                        # 합친다
                        arr[idx][j] = temp * 2
                        # 다시 합치면 안되므로 idx를 더해준다.
                        idx += 1
                    # 옮기는 것과 옮겨갈 것이 다르다면
                    else:
                        idx += 1 # 막아주고
                        arr[idx][j] = temp # 복원
    elif direction == 1:
        # arr의 모든 column을 보기 위해서 n번 본다
        for j in range(n):
            idx = n - 1
            # arr의 0번째 row를 빼고 모든 row에 대해서 봐야하므로
            for i in range(n - 2,  -1, -1):
                # arr의 요소가 0이 아니라면 == 비어있지 않다면
                if arr[i][j]:
                    # 일단 옮길 것을 저장해둔다.
                    temp = arr[i][j]
                    # 일단 옮길 것의 본래 공간을 비워둔다.
                    arr[i][j] = 0
                    # 옮겨갈 곳이 0일 때
                    if arr[idx][j] == 0:
                        # 비어있으므로 그냥 옮기면 된다.
                        arr[idx][j] = temp
                    # 옮기는 것과 옮겨갈 것이 같다면
                    elif arr[idx][j] == temp:
                        # 합친다
                        arr[idx][j] = temp * 2
                        # 다시 합치면 안되므로 idx를 더해준다.
                        idx -= 1
                    # 옮기는 것과 옮겨갈 것이 다르다면
                    else:
                        idx -= 1 # 막아주고
                        arr[idx][j] = temp # 복원

    elif direction == 2:
        # arr의 모든 column을 보기 위해서 n번 본다
        for i in range(n):
            idx = 0
            # arr의 0번째 row를 빼고 모든 row에 대해서 봐야하므로
                # arr의 요소가 0이 아니라면 == 비어있지 않다면
            for j in range(1, n):
                if arr[i][j]:
                    # 일단 옮길 것을 저장해둔다.
                    temp = arr[i][j]
                    # 일단 옮길 것의 본래 공간을 비워둔다.
                    arr[i][j] = 0
                    # 옮겨갈 곳이 0일 때
                    if arr[i][idx] == 0:
                        # 비어있으므로 그냥 옮기면 된다.
                        arr[i][idx] = temp
                    # 옮기는 것과 옮겨갈 것이 같다면
                    elif arr[i][idx] == temp:
                        # 합친다
                        arr[i][idx] = temp * 2
                        # 다시 합치면 안되므로 idx를 더해준다.
                        idx += 1
                    # 옮기는 것과 옮겨갈 것이 다르다면
                    else:
                        idx += 1 # 막아주고
                        arr[i][idx] = temp # 복원

    elif direction == 3:
        # arr의 모든 column을 보기 위해서 n번 본다
        for i in range(n):
            idx = n - 1
            # arr의 0번째 row를 빼고 모든 row에 대해서 봐야하므로
            for j in range(n - 2,  -1, -1):
                # arr의 요소가 0이 아니라면 == 비어있지 않다면
                if arr[i][j]:
                    # 일단 옮길 것을 저장해둔다.
                    temp = arr[i][j]
                    # 일단 옮길 것의 본래 공간을 비워둔다.
                    arr[i][j] = 0
                    # 옮겨갈 곳이 0일 때
                    if arr[i][idx] == 0:
                        # 비어있으므로 그냥 옮기면 된다.
                        arr[i][idx]= temp
                    # 옮기는 것과 옮겨갈 것이 같다면
                    elif arr[i][idx] == temp:
                        # 합친다
                        arr[i][idx] = temp * 2
                        # 다시 합치면 안되므로 idx를 더해준다.
                        idx -= 1
                    # 옮기는 것과 옮겨갈 것이 다르다면
                    else:
                        idx -= 1 # 막아주고
                        arr[i][idx] = temp # 복원
                        
                        
                        
def dfs(cnt):
    global arr, max_val
    # 최대 시도 횟수가 5번이므로
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                max_val = max(max_val, arr[i][j])
        return

    # dfs 돌리기 전에 원본 arr 저장
    origin_arr = copy.deepcopy(arr) 
    # 4방위이므로 [0, 4) 사용
    for i in range(4):
        move(i)
        dfs(cnt + 1)
        # dfs 돌리고 나서 원본 복원해야지 다른 dfs 경로 돌릴 수 있으므로
        arr = copy.deepcopy(origin_arr)
    

n = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
max_val = 0
dfs(0)

print(max_val)