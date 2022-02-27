import sys

loop = int(input())

dict = {}

for i in range(loop):
    num = int(sys.stdin.readline())

    if num not in dict.keys():
        dict[num] = 1
    else:
        dict[num] += 1

dict = sorted(dict.items())

for i in range(len(dict)):
    for j in range(dict[i][1]):
        print(dict[i][0])
