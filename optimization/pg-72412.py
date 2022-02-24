from bisect import bisect_left
from collections import defaultdict
from itertools import combinations

def solution(infos, queries):
    answers = []
    
    db = defaultdict(list):
    for user in infos:
        info = user.split()
        score = int(info[-1])
        info = info[:-1]
        
        for j in range(5):
            comb = list(combinations([0,1,2,3], j))
            for c in comb:
                tmp = info.copy()
                for idx in c:
                    tmp[idx] = '-'
                key = ''.join(tmp)
                db[key].append(score)

    for value in db.values():
        value.sort()

    for query in queries:
        query = query.split('and')
        score = int(query[-1].split()[-1])
        query[-1] = query[-1].split()[0]
        query = [q.strip() for q in query]
        query_key = ''.join(query)
        # print(query, query_key, score)
        
        num = 0
        if query_key in db:
            idx = bisect_left(db[query_key], score)
            num = len(db[query_key]) - idx 
        answers.append(num)
        
    return answers