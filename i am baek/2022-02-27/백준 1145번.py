import sys
num = list(map(int, sys.stdin.readline().split()))
cnt = 1
while True:
    cnt += 1
    count = 0
    if cnt % num[0] == 0:
        count += 1
    if cnt % num[1] == 0:
        count += 1
    if cnt % num[2] == 0:
        count += 1
    if cnt % num[3] == 0:
        count += 1
    if cnt % num[4] == 0:
        count += 1                            
    if count >= 3:
        print(cnt)
        break