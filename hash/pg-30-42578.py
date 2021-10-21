from collections import defaultdict
def solution(clothes):
    answer = defaultdict(int)
    
    for cloth in clothes:
        answer[cloth[1]] += 1
    cnt = 1
    for key in answer:
        cnt *= answer[key] + 1
    
    return cnt - 1