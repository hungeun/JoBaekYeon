#실습 1
def electricPay(use):
    if use < 100:
        pay = 410 + 60.7*use
    elif use <=200:
        pay = 910 + 60.7*100 + 125.9*(use-100)
    else:
        pay = 1600 + 60.7*100 + 125.9*100 + 187.9*(use-200)
    
    paysum = int(pay*1.1 + pay*0.037)
    return paysum

number = int(input('전기사용량을 입력하세요. :'))
bill = electricPay(number)
print(f'전기요금은 {bill}원 입니다.')

#실습2
# +와 -를 번갈아 출력하기

print('+와 -를 번갈아 출력합니다.')
n = int(input('몇 개를 출력할까요?: '))

for i in range(1, n+1):
    if i % 2:     #홀수인 경우 + 출력
        print('+', end='')
    else:         #짝수인 경우 + 출력
        print('-', end='')

print()

#2번방법
# +와 -를 번갈아 출력하기

print('+와 -를 번갈아 출력합니다.')
n = int(input('몇 개를 출력할까요?: '))

for _ in range(n//2):
    print('+-', end='')

if n%2:
    print('+', end='')

print()

#실습3
# 1~12까지 8을 건너뛰고 출력하기(강)

for i in range(1,13):
    if i == 8:
        continue
    print(i, end=' ')

print()

#(내)
a = []
for i in range(1,13):
    if i != 8:
        a.append(i)
print(a)

#실습4
# root ** pwr ( 1 < pwr < 6)

number = int(input('숫자를 입력하세요.: '))
flag = 0

for root in range(1, number+1):
    for pwr in range(2, 6):
        if (root ** pwr) == number:
            print(f'{root}**{pwr} = {number}입니다.')
            flag = 1

if flag == 0:
    print('해당하는 결과가 없습니다.')