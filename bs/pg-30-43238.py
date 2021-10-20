def bs(left, right, times, n):
    answer = -1
    while left <= right:
        cost = 0
        mid = int((left + right) / 2)
        
        for time in times:
            cost += int(mid / time)
        
        # 더 효율적인 방법을 찾았다면
        if cost >= n:
            if answer == -1:
                answer = mid
            else:
                answer = min(answer, mid)
            
            right = mid - 1    
        else:
            left = mid + 1
            
    return answer
    
def solution(n, times):
    times.sort()
    answer = bs(0, times[-1] * n, times, n)
    
    return answer