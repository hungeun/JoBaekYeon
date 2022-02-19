from collections import deque

def bfs(field, x, y):
    save = deque()
    save.append([x, y])
    searchx = [-1, 1, 0, 0]
    searchy = [0, 0, -1 ,1]  # 0 - 왼쪽 / 1 - 오른쪽  / 2 - 아래 / 3 - 위
    field[x][y] = 0
    while save:

        x, y = save.popleft()     

        for i in range(4):
            tmpx = x + searchx[i]
            tmpy = y + searchy[i]

            if tmpx < 0 or tmpy < 0 or tmpx >= len(field) or tmpy >= a:
                continue
            if field[tmpx][tmpy] == 1:            
                field[tmpx][tmpy] = 0
                save.append([tmpx, tmpy])

loop = int(input())

for i in range(loop):
    x, y, baechu = map(int, input().split())  
    a = y
    field = [[0] * y for i in range(x)]
    cnt = 0

    for j in range(baechu):
        tmpx, tmpy = map(int, input().split())
        field[tmpx][tmpy] = 1
    for k in range(x):
        for l in range(y):
            if field[k][l] == 1:
                cnt += 1
                bfs(field, k, l)
    
    print(cnt)


