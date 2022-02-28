import sys
from collections import deque

size, loop = map(int, sys.stdin.readline().split())

stack = deque(range(1, size+1))
num = list(map(int, sys.stdin.readline().split()))
cnt = 0

for i in range(loop):
    while True:
        if stack[0] == num[i]:
            stack.popleft()
            break
        elif stack.index(num[i]) <= len(stack) // 2:
            cnt += 1
            stack.append(stack.popleft())
        else:
            cnt += 1
            stack.insert(0, stack.pop())
print(cnt)