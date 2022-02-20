from collections import Counter
import sys

num = list(map(int, sys.stdin.readline().split()))
cnum = Counter(num)


if cnum.most_common(n=1)[0][1] == 3:
    print(10000+num[0]*1000)
elif cnum.most_common(n=1)[0][1] == 2:
    print(1000+cnum.most_common(n=1)[0][0]*100)
else:
    print(max(num)*100)