gear = [] # [4][8]
k, number, direction, score = 0, 0, 0, 0
isRotate = [0 for _ in range(4)] # [4]


# initializing isRotate array
def init():
    global isRotate
    isRotate = [0 for i in range(4)]

# rotating the gear 
def clock(index):
    temp = []
    for i in range(8):
        temp.append(gear[index][i])

    for i in range(1, 8):
        gear[index][i] = temp[i - 1]
    gear[index][0] = temp[7]

def unclock(index):
    temp = []
    for i in range(8):
        temp.append(gear[index][i])

    for i in range(7):
        gear[index][i] = temp[i + 1]
    gear[index][7] = temp[0]

def rotate(index, direction):
    if direction == 1:
        clock(index)
    elif direction == -1:
        unclock(index)
    else:
        return


# checking whether to rotate or not
def left_check(index, direction):
    if index <= 0:
        return
    # left sid
    if gear[index][6] != gear[index - 1][2]:
        isRotate[index - 1] = direction * (-1)
        left_check(index - 1, direction * (-1))

def right_check(index, direction):
    if index >= 3:
        return
    # right side
    if gear[index][2] != gear[index + 1][6]:
        isRotate[index + 1] = direction * (-1)
        right_check(index + 1, direction * (-1))

def check(index, direction):

    left_check(index, direction)
    right_check(index, direction)

    for i in range(4):  
        rotate(i, isRotate[i])


import sys
gear = [ list(map(int, list(sys.stdin.readline().strip()))) for _ in range(4) ]
k = int(input())

# print(gear)

for i in range(k):
    number, direction = list(map(int, sys.stdin.readline().strip().split()))
    init()
    isRotate[number - 1] = direction
    check(number - 1, direction)

temp = 1

for i in range(4):
    if gear[i][0] == 1:
        score += temp
    temp *= 2

# print(gear)
print(score)
