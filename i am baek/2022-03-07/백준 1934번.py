# 유클리드 호제법 : 2개의 자연수 a, b(a > b)에 대해서 a를 b로 나눈 나머지가 r일 때, a와 b의 최대공약수는 b와 r의 최대공약수와 같다.
# a와 b의 최소공배수는 a와 b의 곱을 a와 b의 최대공약수를 나눈 것과 같다. 

loop = int(input())

for i in range(loop):
    num = list(map(int, input().split()))
    num.sort()
    a = num[0]
    b = num[1]
    while True:
        if b % a == 0:
            break
        else:
            tmp = a
            a = b % a
            b = tmp
    
    print(int(num[0] * num[1] / a))

''' # 타임오버
for i in range(loop):
    num = list(map(int, input().split()))
    num.sort()
    i = num[1]
    while True:
        if i % num[0] == 0:
            break
        i += num[1]
    print(i)
'''