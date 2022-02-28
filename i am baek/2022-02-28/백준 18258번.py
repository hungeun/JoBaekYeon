# pypy3 활용
from collections import deque
import sys

loop = int(sys.stdin.readline().rstrip())
stack = deque()

for _ in range(loop):
    tmp = list(sys.stdin.readline().rstrip().split())

    try: # -1이 출력되는 조건들 커버
        if tmp[0] == 'push':
            stack.append(tmp[1])
        elif tmp[0] == 'front':
            print(stack[0])
        elif tmp[0] == 'back':
            print(stack[-1])
        elif tmp[0] == 'empty':
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif tmp[0] == 'size':
            print(len(stack))
        elif tmp[0] == 'pop':
            print(stack.popleft())
    except IndexError:
        print(-1)
