import re

def solution(files):
    answer = []
    files_split = [re.split(r'(\d+)', file) for file in files]
    files_split.sort(key = lambda x : (x[0].lower(), int(x[1])))
    
    for i in files_split:
        answer.append(''.join(i)) 
    
    return answer