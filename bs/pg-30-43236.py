def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    
    left, right = 0, distance
    
    while left <= right:
        removeRockCnt = 0
        mid = int((left + right) / 2)
        minDistance = float('inf')
        current = 0
        
        for rock in rocks:
            diff = rock - current
            if diff < mid:
                removeRockCnt += 1
            else:
                current = rock
                minDistance = min(minDistance, diff)
        
        if removeRockCnt > n:
            right = mid - 1
        else:
            answer = minDistance
            left = mid + 1
            
    return answer