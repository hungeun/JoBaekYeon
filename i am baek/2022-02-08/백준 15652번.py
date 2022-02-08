# 백준 15652번
# 라이브러리는 쓰라고 있는거다!!!!!
from itertools import *

max, cnt = map(int, input().split())

num = []

for i in range(1, max+1):
    num.append(i)

combi = list(combinations_with_replacement(num, cnt))

for i in combi:
    for j in range(len(i)):
        print(i[j], end = " ")
    print()
