import sys

sys.setrecursionlimit(6000)

score = [i for i in range(10, -1, -1)]
answer = [[-1], 0]


def get_score(pan, info):
    lion = 0
    upeach = 0
    for i in range(len(pan)):
        if pan[i] == 0 and info[i] == 0:
            continue
        if pan[i] > info[i]:
            lion += score[i]
        else:
            upeach += score[i]
    if lion > upeach:
        return lion
    else:
        return -1


import copy

def is_low(target, result):
    for i in range(len(target) - 1, -1, -1):
        if target[i] < result[i]:
            return True
        else:
            return False

def bfs(n, info, result, pointer):
    if pointer >= len(info) or n == 0:
        global answer
        lion = get_score(result, info)
        if lion != -1:
            if answer[1] <= lion:
                if is_low(answer[0], result):
                    answer[0] = result
                    answer[1] = lion
        return
    # pointer에서 화살을 어피치보다 더많이 쏘는 경우
    path1 = copy.deepcopy(result)
    arrow = min(info[pointer] + 1, n)
    path1[pointer] = arrow
    bfs(n - arrow, info, path1, pointer + 1)

    # pointer에서 화살을 안 쏘는 경우
    bfs(n, info, result, pointer + 1)

def solution(n, info):
    bfs(n, info, [0 for _ in range(len(info))], 0)

    return answer[0]

print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))