# 이항계수 : M! / (M-N)!N!

def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num
loop = int(input())

for i in range(loop):
    m, n = map(int, input().split())
    if m >= n:
        print(int(factorial(m) / (factorial(m - n) * factorial(n))))
    else:
        print(int(factorial(n) / (factorial(n - m) * factorial(m))))