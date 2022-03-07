# 이항계수 : M! / (M-N)!N!

def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num

m, n = map(int, input().split())
print(int(factorial(m) / (factorial(m - n) * factorial(n))))