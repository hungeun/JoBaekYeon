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

def bubble_sort_trace(a):
    ccnt = 0 # 비교 횟수
    scnt = 0 # 교환 횟수
    n = len(a)
    for i in range(n-1):
        print(f'패스 {i+1}') # 패스 번호 출력
        exchange = 0
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
                exchange += 1
        
        for m in range(0, n-1):
            print(f'{a[m]:2}', end=' ')
        print(f'{a[n-1]:2}')
        
        if exchange == 0:
            break
        
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

#실습 2
# 버블 정렬 개선 2

def bubble_sort_trace(a):
    ccnt = 0 # 비교 횟수
    scnt = 0 # 교환 횟수
    n = len(a)
    k = 0
    while k < n - 1:
        print(f'패스 {i+1}') # 패스 번호 출력
        last = n - 1
        for j in range(n-1,k,-1):
            for m in range(0, n-1): # 원소값과 교환 여부 출력
                print(f'{a[m]:2}' + (' ' if m != j - 1 else
                                     ' +' if a[j-1] > a[j] else ' -'),
                                     end='')
            print(f'{a[n-1]:2}')
                
            ccnt += 1
            if a[j-1] > a[j]:
                scnt += 1
                a[j-1], a[j] = a[j], a[j-1]
                last = j
        k = last
        
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

#실습 3 - 버블 정렬: 비교 21번, 교환 6번/버블 정렬 개선 1: 비교 20번, 교환 6번/버블 정렬 개선 2: 비교 12번, 교환 6번

#실습 4-Q) 단순 선택 정렬의 진행 내용을 출력하라.
# 단순 선택 정렬

def selection_sort(a):
    n = len(a)
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if a[j] < a[min]:
                min = j
                
        for m in range(0, n): 
            if m == min:
                print(' (' + f'{a[m]:1}' + ')',end='')                
            else:
                print(f'{a[m]:3}',end='')  
        print('\n')
                
        a[i], a[min] = a[min], a[i]
    
    for m in range(0, n): 
       print(f'{a[m]:3}',end='')  
    print('\n')
print('단순 선택 정렬을 수행합니다.')
num = int(input('원소 수를 입력하세요.: '))
x = [None] * num # 원소 수가 num인 리스트를 생성

for i in range(num):
    x[i] = int(input(f'x[{i}]값을 입력하세요.: '))

selection_sort(x)

print('오름차순으로 정렬했습니다.')
print(x)

#실습 5-Q) 단순 선택 정렬을 내림차순으로 정렬하게 변경하여라.
# 단순 선택 정렬

def selection_sort_desc(a):
    n = len(a)
    for i in range(n - 1):
        max = i
        for j in range(i + 1, n):
            if a[j] > a[max]:
                max = j
                
        for m in range(0, n): 
            if m == max:
                print(' (' + f'{a[m]:1}' + ')',end='')                
            else:
                print(f'{a[m]:3}',end='')  
        print('\n')
                
        a[i], a[max] = a[max], a[i]
    
    for m in range(0, n): 
       print(f'{a[m]:3}',end='')  
    print('\n')
print('단순 선택 정렬을 수행합니다.')
num = int(input('원소 수를 입력하세요.: '))
x = [None] * num # 원소 수가 num인 리스트를 생성

for i in range(num):
    x[i] = int(input(f'x[{i}]값을 입력하세요.: '))

selection_sort_desc(x)

print('내림차순으로 정렬했습니다.')
print(x)

#실습 6-Q) 단순 삽입 정렬을 내림차순으로 정렬하게 변경하라.
# 단순 삽입 정렬

def insertion_sort_desc(a):
    n = len(a)
    for i in range(1, n):
        j = i
        tmp = a[i]
        while j > 0 and a[j-1] < tmp:
            a[j] = a[j-1]
            j -= 1
        a[j] = tmp
    print('단순 삽입 정렬을 수행합니다.')
num = int(input('원소 수를 입력하세요.: '))
x = [None] * num # 원소 수가 num인 리스트를 생성

for i in range(num):
    x[i] = int(input(f'x[{i}]값을 입력하세요.: '))

insertion_sort_desc(x)

print('내림차순으로 정렬했습니다.')
print(x)