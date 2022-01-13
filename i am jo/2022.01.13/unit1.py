#Unit 1. 자료구조와 배열
a = [1,2,3]
maximum = a[0]
if a[1] > maximum: maximum = a[1]
if a[2] > maximum: maximum = a[2]  

a = [1,2,3,4]
maximum = a[0]
if a[1] > maximum: maximum = a[1]
if a[2] > maximum: maximum = a[2]
if a[3] > maximum: maximum = a[3]

def max_of(a):
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum

t = (4, 7, 5.6, 2, 3.14, 1)
s = 'string'
a = ['DTS', 'AAC', 'FLAC']

print(f'{max_of(t)}')
print(f'{max_of(s)}')
print(f'{max_of(a)}')

#미니 실습 1 -Q) 리스트 원소의 최솟값 구하기 함수 min_of( )를 작성하라
def min_of(a):
    minimum = a[0]
    for i in range(1, len(a)):
        if a[i] < minimum:
            minimum = a[i]
    return minimum

t = (4, 7, 5.6, 2, 3.14, 1)
s = 'string'
a = ['DTS', 'AAC', 'FLAC']

print(f'{min_of(t)}')
print(f'{min_of(s)}')
print(f'{min_of(a)}')

#사용자가 입력한 리스트에서 최댓값 출력하기
def max_of(a):
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum
print('리스트의 최댓값을 구합니다.')
num = int(input('원소 수를 입력하세요.: '))
x = [None] * num # 원소 수가 num인 리스트를 생성

for i in range(num):
    x[i] = int(input(f'x[{i}]값을 입력하세요.: '))
    
print(f'최댓값은 {max_of(x)}입니다.')

#사용자가 입력한 리스트에서 최댓값 출력하기 (리스트 크기 선언하지 않음)
print('리스트의 최댓값을 구합니다.')
print('주의: "End"를 입력하면 원소 입력을 종료합니다.')
i = 0
x = []

while True:
    s = input(f'x[{i}]값을 입력하세요.: ')
    if s == 'End':
        break
    x.append(int(s))
    i += 1
    
print(f'최댓값은 {max_of(x)}입니다.')

#리스트의 모든 원소를 스캔하기
    #원소 수 파악
x = ['John', 'George', 'Paul', 'Ringo']

for i in range(len(x)):
    print(f'x[{i}] = {x[i]}')
    
    # enumerate 함수로 스캔

x = ['John', 'George', 'Paul', 'Ringo']

for i, name in enumerate(x):
    print(f'x[{i}] = {name}')
    
    # 인덱스 값을 사용하지 않음

x = ['John', 'George', 'Paul', 'Ringo']

for i in x:
    print(i)
    
#미니 실습 2-Q) 리스트를 사용자로부터 입력받아서 역순으로 정렬하여 리스트의 원소를 출력하여라.
def reverse_list(a):
    n = len(a)
    for i in range(n // 2):
        a[i], a[n - i - 1] = a[n - i - 1], a[i]
print('리스트를 역순으로 출력합니다.')
num = int(input('원소 수를 입력하세요.: '))
x = [None] * num # 원소 수가 num인 리스트를 생성

for i in range(num):
    x[i] = int(input(f'x[{i}]값을 입력하세요.: '))

reverse_list(x)

print('리스트를 역순으로 출력합니다.')
for i in range(num):
    print(f'x[{i}] = {x[i]}')