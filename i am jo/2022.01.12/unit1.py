#문자열과 숫자 입력받기
name = input('이름을 입력하세요.: ')
print(f'안녕하세요? {name}님.')

#2
length = input('정사각형의 한 변의 길이를 입력하세요.: ')
print(f'정사각형의 넓이는 {int(length)**2}입니다.')

#세 정수를 입력받아 최댓값 구하기
print('세 정수의 최댓값을 구합니다.')
a = int(input('정수 a의 값을 입력하세요.: '))
b = int(input('정수 b의 값을 입력하세요.: '))
c = int(input('정수 c의 값을 입력하세요.: '))

maximum = a
if b > maximum:
    maximum = b
if c > maximum:
    maximum = c
    
print(f'최대값은 {maximum}입니다.')

#세 정수의 최댓값 구하기 알고리즘 확인
def max3(a, b, c):
    maximum = a
    if b > maximum:
        maximum = b
    if c > maximum:
        maximum = c
        
    return maximum # 최댓값 반환

print(f'max3(3, 2, 1) = {max3(3, 2, 1)}')
print(f'max3(3, 2, 2) = {max3(3, 2, 2)}')
print(f'max3(3, 1, 2) = {max3(3, 1, 2)}')
print(f'max3(3, 2, 3) = {max3(3, 2, 3)}')
print(f'max3(2, 1, 3) = {max3(2, 1, 3)}')
print(f'max3(3, 3, 2) = {max3(3, 3, 2)}')
print(f'max3(3, 3, 3) = {max3(3, 3, 3)}')
print(f'max3(2, 2, 3) = {max3(2, 2, 3)}')
print(f'max3(2, 3, 1) = {max3(2, 3, 1)}')
print(f'max3(2, 3, 2) = {max3(2, 3, 2)}')
print(f'max3(1, 3, 2) = {max3(1, 3, 2)}')
print(f'max3(2, 3, 3) = {max3(2, 3, 3)}')
print(f'max3(1, 2, 3) = {max3(1, 2, 3)}')

#미니 실습 1)-네 정수의 최댓값 구하기 (강)
def max4(a, b, c, d):
    maximum = a
    if b > maximum:
        maximum = b
    if c > maximum:
        maximum = c
    if d > maximum:
        maximum = d
    return maximum # 최댓값 반환

print('네 정수의 최댓값을 구합니다.')
a = int(input('정수 a의 값을 입력하세요.: '))
b = int(input('정수 b의 값을 입력하세요.: '))
c = int(input('정수 c의 값을 입력하세요.: '))
d = int(input('정수 d의 값을 입력하세요.: '))
print(f'최댓값은 {max4(a, b, c, d)}')

#내꺼
a = int(input('정수 a의 값을 입력하세요: '))
b = int(input('정수 b의 값을 입력하세요: '))
c = int(input('정수 c의 값을 입력하세요: '))
d = int(input('정수 d의 값을 입력하세요: '))

max = a 
if b > max:
    max = b
if c > max:
    max = c
if d > max:
    max = d
    
print('최대값은 ', int(max) , '입니다')

#조건문과 분기-입력받은 정수의 부호(양수, 음수, 0) 출력하기
n = int(input('정수를 입력하세요.: '))

if n > 0:
    print('이 수는 양수입니다.')
elif n < 0:
    print('이 수는 음수입니다.')
else:
    print('이 수는 0입니다.')
    
#세 정수의 중앙값 구하기
def med3(a, b, c):
    
    if a >= b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b
    
print('세 정수의 중앙값을 구합니다.')
a = int(input('정수 a의 값을 입력하세요.: '))
b = int(input('정수 b의 값을 입력하세요.: '))
c = int(input('정수 c의 값을 입력하세요.: '))

print(f'중앙값은 {med3(a, b, c)}입니다.')

#미니 실습 2)-수도 요금 계산(강)
def waterPay(company, usage):
    
    pay = 0
    
    if company == 'A':
            pay = usage*100
    else:
        if usage <= 50:
            pay = usage*150
        else:
            pay = 50*150 + (usage-50)*75
    return pay

print('수도 요금을 계산합니다.')
company = (input('수도 회사를 입력하세요.: '))
usage = int(input('수도 사용량을 입력하세요.: '))

print(f'수도요금은 {waterPay(company, usage)}입니다.')

#내
a = int(input('a의 값을 입력하세요: ' ))
b = int(input('b의 값을 입력하세요: ' ))

use_a = a * 100
print(use_a,'원')

if b > 50:
    use_b1 = b * 75
    print(use_b1,'원')
else:
    use_b2 = b * 150
    print(use_b2,'원')

