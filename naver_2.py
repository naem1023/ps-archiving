def solution(sentence, keyword, skips):
    arrow = 0

    for index, skip in enumerate(skips):
        k = keyword[index % len(keyword)]
        for i in range(skip):
            if sentence[arrow] == k:
                arrow += 1
                break
            arrow += 1
        if arrow > len(sentence):
            break
        sentence = sentence[0:arrow] + k + sentence[arrow:]

        arrow += 1
    return sentence

print(solution("abcde fghi", "axyz", 	[3, 9, 0, 1]))