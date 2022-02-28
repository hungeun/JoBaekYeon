import sys
from collections import deque

loop = int(sys.stdin.readline().rstrip())

stack = deque()

for i in range(loop):
    tmp = list(sys.stdin.readline().split())
    try:
        if tmp[0] == 'push_front':
            stack.insert(0, tmp[1])
        elif tmp[0] == 'push_back':
            stack.append(tmp[1])
        elif tmp[0] == 'pop_front':
            print(stack.popleft())
        elif tmp[0] == 'pop_back':
            print(stack.pop())
        elif tmp[0] == 'size':
            print(len(stack))
        elif tmp[0] == 'empty':
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif tmp[0] == 'front':
            print(stack[0])
        elif tmp[0] == 'back':
            print(stack[-1])
    except IndexError:
        print(-1)