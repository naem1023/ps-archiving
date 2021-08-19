import itertools, collections 

def deleteAll(tuple, size): 
    ans = [] 
    for i in tuple: 
        if len(i[0]) != size: 
            ans.append(i) 
    return ans 

def solution(orders, course): 
    answer = [] 
    com = [] 
    
    for i in course: 
        com.append([]) 
        for j in orders: 
            j = ''.join(sorted(list(j))) 
            com[-1] += list(map(''.join, itertools.combinations(list(j), i))) 
    temp=[] 
    for j in com: 
        temp.append(collections.Counter(j).most_common()) 
    # print(com)
    # print(temp)
    for k in temp:
        if len(k) == 0:
            continue 
        while k[0][1] != 1: 
            answer.append(''.join(sorted(k[0][0]))) 
            if len(k) == 1: 
                break 
            if k[0][1] == k[1][1]: 
                del k[0] 
                continue 
            break 
    return sorted(answer)


orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]	

print(solution(orders, course))