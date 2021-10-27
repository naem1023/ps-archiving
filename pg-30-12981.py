def solution(n, words):
    answer = [0,0]
    stack = [words[0]]
    for i in range(1, len(words)):
        # stack의 가장 윗 단어의 마지막 글자와 i번째 단어의 시작이 같고
        # i번재 단어가 스택에 없다면
        if stack[-1][-1] == words[i][0] \
            and words[i] not in stack:
            stack.append(words[i])
        # stack에 추가가 안된다면 answer 갱신
        else:
            answer[0] = (i % n) + 1
            answer[1] = i // n + 1
            break
    return answer