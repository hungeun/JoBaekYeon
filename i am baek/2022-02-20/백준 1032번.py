import sys

loop = int(sys.stdin.readline())

dic = []

for i in range(loop):
    dic.append(list(input()))
tmp = dic[0].copy()

for i in range(1, len(dic)):
    for j in range(len(dic[0])):
        if dic[0][j] != dic[i][j]:
            tmp[j] = '?'
print("".join(tmp))