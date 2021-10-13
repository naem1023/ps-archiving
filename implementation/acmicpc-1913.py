import sys
N = int(sys.stdin.readline())
X = int(sys.stdin.readline())

arr = [ [ 0 for _ in range(N)] for _i in range(N)]
counter = 0
x = N // 2
y = N // 2
direction = {'up':0, 'down':1, 'right':2, 'left': 3}
current = direction['up']
while counter != N ** 2:
    