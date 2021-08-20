N = int(input())
cmds = [input().split() for _ in range(N)]
stack = []

for cmd in cmds:
    if len(cmd) == 2:
        if cmd[0] == 'push':
            stack.append(int(cmd[1]))
    elif cmd[0] == 'front':
        print(-1 if not stack else stack[0])
    elif cmd[0] == 'back':
        print(-1 if not stack else stack[-1])
    elif cmd[0] == 'size':
        print(len(stack))
    elif cmd[0] == 'empty':
        print(0 if stack else 1)
    elif cmd[0] == 'pop':
        if stack:
            print(stack[0])
            del stack[0]
        else:
            print(-1)