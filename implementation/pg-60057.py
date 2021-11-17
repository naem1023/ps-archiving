def solution(s):
    length = []
    result = ""
    
    if len(s) == 1:
        return 1
    
    # n gram 결정
    for cut in range(1, len(s) // 2 + 1): 
        count = 1
        # 첫번째 단어 선택
        tempStr = s[:cut] 
        
        # n 단위로 끊어서 단어 확인
        for i in range(cut, len(s), cut):
            # tempStr와 같으면 counting
            if s[i : i + cut] == tempStr:
                count += 1            
            # tempStr와 다르면 counting 그만
            else:
                if count == 1:
                    count = ""
                # 최종 문자열 갱신
                result += str(count) + tempStr
                # init
                tempStr = s[i : i + cut]
                count = 1

        # 마지막 tempStr은 최종 결과에 반영 안됐으니 반영
        if count == 1:
            count = ""
            
        result += str(count) + tempStr
        length.append(len(result))
        result = ""
    
    return min(length)