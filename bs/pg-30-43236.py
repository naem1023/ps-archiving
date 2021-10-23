def solution(distance, rocks, n):
    answer = 0
    rocks.sort()

    # bs의 탐색 대상 = rock 거리 간의 최소값    
    left, right = 0, distance
    
    while left <= right:
        removeRockCnt = 0
        mid = int((left + right) / 2)
        minDistance = float('inf')

        # 현재 어느 돌데 있는지 저장
        current = 0
        
        for rock in rocks:
            diff = rock - current
            # 실제로 rocks 배열을 조작하지 않고 
            # current를 변경해주는 것으로 삭제할 돌을 선택한다.
            if diff < mid:
                # current를 저장하지 않고 건너뛰어서 마치 돌을 삭제한 효과를 기대
                removeRockCnt += 1
            else:
                current = rock
                # 삭제하지 않을 돌이기 때문에 거리의 최소값 계산
                minDistance = min(minDistance, diff)
        
        # n보다 더 많이 지웠다면 더 적게 지워야한다.
        # 즉, 돌들간의 거리의 최소값이 더 작아져야하므로 right를 감소
        if removeRockCnt > n:
            right = mid - 1
        # n보다 더 적게 지우거나 같다면 answer를 일단 저장한다. 
        # 두 경우는 문제의 답을 내포한 경우이기 때문이다.
        else:
            answer = minDistance
            # n보다 더 적거나 같게 돌을 지웠으므로
            # 거리의 최소값을 늘려서 지울 돌의 개수를 늘려야한다.
            left = mid + 1
            
    return answer