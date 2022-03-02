import sys
loop = int(sys.stdin.readline())
atm = list(map(int, sys.stdin.readline().split()))
lis = []
sum = 0
atm.sort()
for i in atm:
    sum += i
    lis.append(sum)
sum = 0
for i in lis:
    sum += i
print(sum)

