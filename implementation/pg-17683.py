import math   
def solution(m, musicinfos):
    answer = None
    m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
    musicinfos = [ musicinfo.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a").split(',') for musicinfo in musicinfos]
    
    print(musicinfos)
    for start, end, title, score in musicinfos:
        start_h, start_m = map(int, start.split(':'))
        start = start_h * 60 +start_m
        end_h, end_m = map(int, end.split(':'))
        end = end_h * 60 + end_m 
        duration = end - start
        
        # duration이 악보보다 크거나 작은 경우를 모두 커버
        score *= math.ceil(duration / len(score))
        score = score[:duration]
        
        # 쿼리 결과가 없다면
        if m not in score:
            continue
            
        # 우선순위를 파악해 정답 갱신
        if answer == None or answer[0] < duration or \
            answer[0] == duration and answer[1] > start:
            answer = (duration, start, title)
            
    if answer:
        return answer[-1]
        
    print(musicinfos)
    return "(None)"