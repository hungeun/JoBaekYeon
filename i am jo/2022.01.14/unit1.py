# 양의 정수 n의 팩토리얼 구하기
def factorial(n):
    if n > 0:
        return n * factorial(n-1)
    else:
        return 1

n = int(input('출력할 팩토리얼 값을 입력하세요.: '))
print(f'{n}의 팩토리얼은 {factorial(n)}입니다.')

#미니 실습 1)-Q) 양의 정수 n의 팩토리얼 구하기를 재귀 알고리즘을사용하지 말고 구하시오
def factorial_simple(n):
    
    factorial = 1
    
    if n > 0:
        for i in range(1,n+1):
            factorial = factorial*i 
        return factorial
    else:
        return 1
n = int(input('출력할 팩토리얼 값을 입력하세요.: '))
print(f'{n}의 팩토리얼은 {factorial_simple(n)}입니다.')

# 유클리드 호제법

def gcd(x, y):
    
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

x = int(input('첫 번째 정숫값을 입력하세요. '))
y = int(input('두 번째 정숫값을 입력하세요. '))
print(f'두 정숫값의 최대 공약수는 {gcd(x, y)}입니다.')

#미니 실습 2)-Q) 두 정수의 최대 공약수 구하기를 재귀 알고리즘을 사용하지 말고 구현하시오.
def gcd_no_recursive(m,n):
    while n != 0:
       t = m%n
       (m,n) = (n,t)
    return m
x = int(input('첫 번째 정숫값을 입력하세요. '))
y = int(input('두 번째 정숫값을 입력하세요. '))
print(f'두 정숫값의 최대 공약수는 {gcd_no_recursive(x, y)}입니다.')

# 버블 정렬 알고리즘 구현
def bubble_sort(a):
    n = len(a)
    for i in range(n-1):
        for j in range(n-1,i,-1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                
print('버블 정렬을 수행합니다.')
num = int(input('원소 수를 입력하세요.: '))
x = [None] * num # 원소 수가 num인 리스트를 생성

for i in range(num):
    x[i] = int(input(f'x[{i}]값을 입력하세요.: '))

bubble_sort(x)

print('오름차순으로 정렬했습니다.')
print(x)

# 버블 정렬 과정 출력 (교환하는 경우 +, 교환하지 않는 경우 -)

def bubble_sort_trace(a):
    ccnt = 0 # 비교 횟수
    scnt = 0 # 교환 횟수
    n = len(a)
    for i in range(n-1):
        print(f'패스 {i+1}') # 패스 번호 출력
        for j in range(n-1,i,-1):
            for m in range(0, n-1): # 원소값과 교환 여부 출력
                print(f'{a[m]:2}' + (' ' if m != j - 1 else
                                     ' +' if a[j-1] > a[j] else ' -'),
                                     end='')
            print(f'{a[n-1]:2}')
                
            ccnt += 1
            if a[j-1] > a[j]:
                scnt += 1
                a[j-1], a[j] = a[j], a[j-1]
        
        for m in range(0, n-1):
            print(f'{a[m]:2}', end=' ')
        print(f'{a[n-1]:2}')
        
    print(f'비교를 {ccnt}번 했습니다')
    print(f'교환을 {scnt}번 했습니다')
    print('버블 정렬을 수행합니다.')
    
num = int(input('원소 수를 입력하세요.: '))
x = [None] * num # 원소 수가 num인 리스트를 생성

for i in range(num):
    x[i] = int(input(f'x[{i}]값을 입력하세요.: '))

bubble_sort_trace(x)

print('오름차순으로 정렬했습니다.')
print(x)

# 버블 정렬 개선 1

def bubble_sort(a):
    n = len(a)
    for i in range(n-1):
        exchange = 0
        for j in range(n-1,i,-1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                exchange += 1
        if exchange ==0 :
            break
        
# 버블 정렬 개선 2

def bubble_sort(a):
    n = len(a)
    k = 0
    while k < n - 1:
        last = n - 1
        for j in range(n-1, k, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                last = j
        k = last

# 단순 선택 정렬 pseudo code

for i in range(n-1):
    min    # 값이 가장 작은 원소의 인덱스
           # a[i]와 a[min]의 값을 교환

# 단순 선택 정렬

def selection_sort(a):
    n = len(a)
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]
print('단순 선택 정렬을 수행합니다.')
num = int(input('원소 수를 입력하세요.: '))
x = [None] * num # 원소 수가 num인 리스트를 생성

for i in range(num):
    x[i] = int(input(f'x[{i}]값을 입력하세요.: '))

selection_sort(x)

print('오름차순으로 정렬했습니다.')
print(x)

# 단순 삽입 정렬 pseudo code

for i in range(1, n):
    #tmp <- a[i]를 넣습니다.
    #tmp를 a[0], ... , a[i-1] 의 알맞은 위치에 삽입

# 단순 삽입 정렬 알고리즘 pseudo code

for i in range(1, n):
    j = i
    tmp = a[i]
    while j > 0 and a[j-1] > tmp:
        a[j] = a[j-1]
        j -= 1
    a[j] = tmp

# 단순 삽입 정렬
def insertion_sort(a):
    n = len(a)
    for i in range(1, n):
        j = i
        tmp = a[i]
        while j > 0 and a[j-1] > tmp:
            a[j] = a[j-1]
            j -= 1
        a[j] = tmp
print('단순 삽입 정렬을 수행합니다.')
num = int(input('원소 수를 입력하세요.: '))
x = [None] * num # 원소 수가 num인 리스트를 생성

for i in range(num):
    x[i] = int(input(f'x[{i}]값을 입력하세요.: '))

insertion_sort(x)

print('오름차순으로 정렬했습니다.')
print(x)
