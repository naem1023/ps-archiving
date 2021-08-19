def solution(triangle):
    a = []
    
    for d in triangle:
        if len(a) == 0:
            a.append(d)
        else:
#             n-1층까지의 합을 가져온다.
            val = a[-1]
    
#           n층의 합을 구한다.
            for i in range(d):
                if i == 0:
                    d[i] += val[i]
                elif i == len(d) - 1:
                    d[i] += val[i - 1]
                else:
                    d[i] += val[i - 1] + val[i]
            a.append(d)
                    
    answer = max(a[-1])
    return answer


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))