#Unit 2. 반복하는 알고리즘
#1부터 n까지 정수의 합 구하기 (while)
print('1부터 n까지 정수의 합을 구합니다.')

n = int(input('n값을 입력하세요.: '))

sum = 0
i = 1

while i <= n: 
    sum += i
    i += 1

print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')

#1부터 n까지 정수의 합 구하기 (for)
print('1부터 n까지 정수의 합을 구합니다.')

n = int(input('n값을 입력하세요.: '))

sum = 0

for i in range(1, n+1):
    sum += i

print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')

#a부터 b까지 정수의 합 구하기 (for)
print('a부터 b까지 정수의 합을 구합니다.')

a = int(input('정수 a를 입력하세요.: '))
b = int(input('정수 b를 입력하세요.: '))

if a > b:
    a, b = b, a
    
sum = 0

for i in range(a, b+1):
    sum += i

print(f'{a}부터 {b}까지 정수의 합은 {sum}입니다.')

#반복과정에서 조건 판단하기 1
print('a부터 b까지 정수의 합을 구합니다.')

a = int(input('정수 a를 입력하세요.: '))
b = int(input('정수 b를 입력하세요.: '))

if a > b:
    a, b = b, a
    
sum = 0

for i in range(a, b+1):
    if i < b:
        print(f'{i} + ', end='')
    else:
        print(f'{i} = ', end='')
    sum +=i

print(sum)

#미니 실습 3)-반복 과정에서 조건 판단하기 (업그레이드)
print('a부터 b까지 정수의 합을 구합니다.')

a = int(input('정수 a를 입력하세요.: '))
b = int(input('정수 b를 입력하세요.: '))

if a > b:
    a, b = b, a
    
sum = 0

for i in range(a, b):
   print(f'{i} + ', end='')
   sum +=i
        
print(f'{b} = ', end='')
sum += b

print(sum)

#반복과정에서 조건 판단하기 2
# * 를 n 개 출력하되 w개마다 줄바꿈하기 1 

print('*를 출력합니다.')
n = int(input('몇 개를 출력할까요?: '))
w = int(input('몇 개마다 줄바꿈할까요?: '))

for i in range(n):
    print('*', end='')
    if i % w == w-1:
        print()

if n%w:
    print()
    
# * 를 n 개 출력하되 w개마다 줄바꿈하기 2 

print('*를 출력합니다.')
n = int(input('몇 개를 출력할까요?: '))
w = int(input('몇 개마다 줄바꿈할까요?: '))

for _ in range(n // w): # n//w번 반복
    print('*' * w)      # *를 w번 출력
   
rest = n % w 
if rest:                # rest 값이 있으면
    print('*' * rest)   # rest 값만큼 * 반복 출력

#무한 루프와 break
# 1부터 n까지 정수의 합 구하기 (n값은 양수만 입력받음)

print('1부터 n까지 정수의 합을 구합니다.')

while True:
    n = int(input('n값을 입력하세요.: '))
    if n > 0:
        break # n이 0보다 커질때 까지 반복
        
sum = 0
i = 1

for i in range(1, n+1):
    sum += i
    i += 1
    
print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')

#continue 와 break
# 가로, 세로 길이가 정수이고 넓이가 area인 직사각형에서 가능한 변의 길이 나열

area = int(input('직사각형의 넓이를 입력하세요.: '))

for i in range(1, area + 1):
    if i * i > area: break       
    if area % i: continue
    print(f'{i} x {area // i}')
    
#미니 실습 4
area = int(input('직사각형의 넓이를 입력하세요.: '))

for i in range(1, area + 1):     
    if area % i: continue
    print(f'{i} x {area // i}')
    
#구구단 출력
print('-' * 27)
for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i * j:3}', end='')
    print()

print('-' * 27)

