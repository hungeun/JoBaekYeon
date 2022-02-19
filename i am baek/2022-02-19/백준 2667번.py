from collections import deque

def bfs(danji, x, y):
    save = deque()
    save.append([x, y])
    searchx = [-1, 1, 0, 0]
    searchy = [0, 0, -1 ,1]  # 0 - 왼쪽 / 1 - 오른쪽  / 2 - 아래 / 3 - 위
    danji[x][y] = 0
    cnt = 1

    while save:
        x, y = save.popleft()     

        for i in range(4):
            tmpx = x + searchx[i]
            tmpy = y + searchy[i]

            if tmpx < 0 or tmpy < 0 or tmpx >= len(danji) or tmpy >= len(danji):
                continue

            if danji[tmpx][tmpy] == 1:            
                danji[tmpx][tmpy] = 0
                cnt += 1
                save.append([tmpx, tmpy])
    
    return cnt

line = int(input())

danji = []
count = []
cnt = 0

for i in range(line):
    danji.append(list(map(int, input())))

for x in range(line):
    for y in range(line):
        if danji[x][y] == 1:
            cnt += 1
            count.append(bfs(danji, x, y))

print(cnt)
count.sort()
for i in count:
    print(i)