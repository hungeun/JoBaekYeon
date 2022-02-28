import sys
from collections import deque

card = int(sys.stdin.readline().rstrip())

que = deque(range(1, card+1))
cnt = 1
while len(que) >= 2:
    if cnt % 2 == 1:
        que.popleft()
    else:
        que.append(que.popleft())
    cnt += 1

print(que[0])