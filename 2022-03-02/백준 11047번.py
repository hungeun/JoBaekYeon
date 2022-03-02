import sys
money, price = map(int, sys.stdin.readline().split())
lis = []
for i in range(money):
    lis.append(int(sys.stdin.readline()))
lis.sort(reverse=True)
cnt = 0
for i in lis:
    if price < i:
        continue
    cnt += price // i
    price = price % i

print(cnt)