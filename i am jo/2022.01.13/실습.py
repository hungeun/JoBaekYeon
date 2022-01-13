#Q) 2부터 1000사이의 수 중에서 소수를 리스트에 입력하고 출력하여라.

prime = []

for n in range(2, 1001):
    flag = 0
    for i in range(2, n):
        if n % i == 0:
            flag = 1
            break
        
    if(flag == 0):
        prime.append(n)
    
print(prime)

#Q) 리스트를 사용자로부터 입력받아서 역순으로 정렬하여 리스트의 원소를 출력하여라. 원소 수를 미리 묻지 말고 코드가 실행될 수 있도록하라.
def reverse_list(a):
    n = len(a)
    for i in range(n // 2):
        a[i], a[n - i - 1] = a[n - i - 1], a[i]
        
print('리스트를 역순으로 정렬하여 출력합니다.')
print('주의: "End"를 입력하면 원소 입력을 종료합니다.')
i = 0
x = []

while True:
    s = input(f'x[{i}]값을 입력하세요.: ')
    if s == 'End':
        break
    x.append(int(s))
    i += 1
    
reverse_list(x)

print(x)

#Q) 리스트와 검색할 값을 사용자로부터 입력받아서 검색값이 있는 인덱스를 출력하라. 검색방안은 어떤 방안을 사용하여도 됩니다.
def seq_search(a, key):
    i = 0
    
    while True:
        if i == len(a):
            return -1
        if a[i] == key:
            return i
        i += 1
        print('리스트와 검색할 값을 입력받아 검색값이 있는 인덱스를 출력합니다.')
print('주의: "End"를 입력하면 원소 입력을 종료합니다.')
i = 0
x = []

while True:
    s = input(f'x[{i}]값을 입력하세요.: ')
    if s == 'End':
        break
    x.append(int(s))
    i += 1

key = int(input('검색할 값을 입력하세요.: '))
    
index = seq_search(x, key)

print(f'검색값 {key}는 a[{index}]에 있습니다.')

#Q) 리스트를 사용자로부터 입력받아서 최대값과 최대값이 있는 인덱스를 출력하라.
def max_of(a):
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum
def seq_search(a, key):
    i = 0
    
    while True:
        if i == len(a):
            return -1
        if a[i] == key:
            return i
        i += 1
        print('리스트를 사용자로부터 입력받아서 최대값과 최대값이 있는 인덱스를 출력합니다.')
print('주의: "End"를 입력하면 원소 입력을 종료합니다.')
i = 0
x = []

while True:
    s = input(f'x[{i}]값을 입력하세요.: ')
    if s == 'End':
        break
    x.append(int(s))
    i += 1

maximum = max_of(x)
index = seq_search(x, maximum)

print(f'최대값은 {maximum}이고 a[{index}]에 있습니다.')