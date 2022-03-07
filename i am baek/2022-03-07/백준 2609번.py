num1, num2 = map(int, input().split())

lis = []

for i in range(num1, 0, -1):
    if num1 % i == 0 and num2 % i == 0:
        print(i)
        break


i = num1
while True:
    if i % num2 == 0:
        break
    i += num1

print(i)