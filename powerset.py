def powerset(x):
    answers = []
    if len(x) <= 1:
        return [x, []]
    else:
        for item in powerset(x[1:]):
            answers.append([x[0]] + item) # [1] + ([2], [])
            answers.append(item) # [2], []
    return answers

arr = [1,2,3,4,5]

print(powerset(arr))