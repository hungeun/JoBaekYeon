import sys
from collections import deque

loop = int(sys.stdin.readline().rstrip())

for i in range(loop):
    cnt, index = map(int, sys.stdin.readline().split())

    printer = deque(map(int, sys.stdin.readline().split()))
    ind = deque(range(0, cnt))
    count = 0
    while printer:
        important = max(printer)

        if printer[0] == important:
            count += 1
            if ind[0] == index:
                break
            else:
                printer.popleft()
                ind.popleft()
        else:
            printer.append(printer.popleft())
            ind.append(ind.popleft())
    print(count)