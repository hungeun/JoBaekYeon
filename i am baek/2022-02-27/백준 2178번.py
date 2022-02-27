import sys
from collections import deque

searchx = [-1, 1, 0, 0]
searchy = [0, 0, -1 ,1]  # 0 - 왼쪽 / 1 - 오른쪽  / 2 - 아래 / 3 - 위

x, y = map(int, sys.stdin.readline().split())
a = x
b = y
miro = []

for i in range(x):
    tmp = list(map(int, input()))
    miro.append(tmp)

route = deque()
route.append([0,0])
cnt = 1

while route:
    x, y = route.popleft()

    for i in range(4):
        tmpx = x + searchx[i]
        tmpy = y + searchy[i]
        
        if tmpx < 0 or tmpy < 0 or tmpx >= a or tmpy >= b:
            continue
        if miro[tmpx][tmpy] == 1:
            miro[tmpx][tmpy] = miro[x][y] + 1
            route.append([tmpx, tmpy])

print(miro[-1][-1])    