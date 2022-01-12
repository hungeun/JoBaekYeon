#Q0-두 정수의 최대공약수를 구하라. 최대공약수는 두 정수를 나머지가 0이 되게 나누는 공통된 약수 중 최대값을 가진 수이다.
def solution(a, b):
    if a < b:
        min = a
    else:
        min = b
    
    answer = 0
    
    for i in range(min,1,-1):
        if a%i == 0 and b%i == 0:
            answer = i
            break
    
    return answer

a = 12
b = 16
c = solution(a,b)
print(c)

#내
a = int(input('a의 값을 입력하시오: '))
b = int(input('b의 값을 입력하시오: '))

for i in range(1, a + 1):
    if (a % i == 0) & (b % i == 0):
        c = i 
  
print("%d와 %d의 최대공약수는 %d"%(a, b, c))

#Q1-두 정수의 최소공배수를 구하라. 최소공배수는 두 정수의 배수인 수 중 최솟값을 가진 값을 수이다.
def solution(a, b):
    if a > b:
        max = a
    else:
        max = b
        
    answer = 0
    for i in range(max, a * b + 1):
        if i % a == 0 and i % b == 0:
            answer = i
            break
            
    return answer
a = 2 
b =4
c = solution(a,b)
print(c)

#내
a = int(input('a의 값을 입력하시오: '))
b = int(input('b의 값을 입력하시오: '))

a_1 = []
b_1 = []

for i in range(1, b + 1):   #1*12/2*12/3*12/ --/24*12 
    a_1.append(i * a)
for i in range(1, a + 1):   #1*24/2*24/3*24/--/12*24
    b_1.append(i * b)

for i in a_1:
    if i in b_1:
        c = i
        break
        
print("최소 공배수는: ",c)

"""Q2-0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다. 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다. 그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다. 다음 예를 보자.
26부터 시작한다. 2+6 = 8이다. 새로운 수는 68이다. 6+8 = 14이다. 새로운 수는 84이다. 8+4 = 12이다. 새로운 수는 42이다. 4+2 = 6이다. 새로운 수는 26이다.
위의 예는 4번만에 원래 수로 돌아올 수 있다. 따라서 26의 사이클의 길이는 4이다.
N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.""" #강
N = input()

j = N

count = 0

while True:
    
    if int(j) < 10:
        j = '0' + j
        
    j = int(j[0]) + int(j[1])
    j = int(j[1]) + str(i)[-1]
    j = str(j)
    
    count += 1

    if j == N:
        break
print(count)

#내
n = int(input())       #68   
num = n
cnt = 0                #사이클 수

while True:
    a = num // 10       
    b = num % 10        
    c = (a + b) % 10    
    num = (b * 10) + c  
    
    cnt = cnt + 1      
    if(num == n):       
        break
print(cnt)

"""Q3-두 정수 left와 right가 매개변수로 주어집니다. left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.
제한사항
1 ≤ left ≤ right ≤ 1,000"""
def solution(left, right):
    answer = 0
    for i in range(left,right + 1):
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
                
        if count % 2 == 0:
            answer = answer + i
        else:
            answer = answer - i
            
    return answer

left = 13
right = 17
c = solution(left, right)
print(c)

"""Q4
각 자리가 숫자(0부터 9)로만 이루어진 문자열을 사용자로 부터 입력받아, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 곱하기(x) 혹은 더하기(+) 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하세요.
단, + 보다 x 를 먼저 계산하는 일반적인 방식과 달리 모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정합니다.
입출력 예
숫자로 이루어진 문자열을 입력하세요. 02984
0 + 2 x 9 x 8 x 4 = 576"""
data = input('숫자로 이루어진 문자열을 입력하세요. ')

result = int(data[0])

print(result, end =' ')

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
        print(' + ' + str(num), end = ' ')
    else:
        result *= num
        print(' x ' + str(num), end = ' ')

print(' = ' + str(result))

"""Q5 어떤 게임의 아웃복서 캐릭터에게는 럭키 스트레이트라는 기술이 존재한다. 이 기술은 매우 강력한 대신에 항상 사용할 수는 없으며, 현재 게임 내에서 점수가 특정 조건을 만족할 때만 사용할 수 있다.
특정 조건이란 현재 캐릭터의 점수를 N이라고 할 때 점수 N을 자릿수를 기준으로 반으로 나누어 왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합을 더한 값이 동일한 상황을 의미한다. 예를 들어 현재 점수가 123,402라면 왼쪽 부분의 각 자릿수의 합은 1+2+3, 오른쪽 부분의 각 자릿수의 합은 4+0+2이므로 두 합이 6으로 동일하여 럭키 스트레이트를 사용할 수 있다.
현재 점수 N이 주어졌을 때, 럭키 스트레이트를 사용할 수 있는 상태인지 아닌지를 알려주는 프로그램을 작성하시오. 럭키 스트레이트를 사용할 수 있다면 "LUCKY"를, 사용할 수 없다면 "READY"라는 단어를 출력한다. 또한 점수 N의 자릿수는 항상 짝수 형태로만 주어진다. 예를 들어 자릿수가 5인 12,345와 같은 수는 입력으로 들어오지 않는다."""
n = input('숫자를 입력하세요. ')
length = len(n)
left = 0
right = 0

for i in range(length // 2):
    left += int(n[i])
for i in range(length // 2, length):
    right += int(n[i])
    
if left == right:
    print('LUCKY')
else:
    print('READY')
    
"""Q6-임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요"""
def solution(n):
    
    n = int(input('임의의 정수 값을 입력하세요.: '))
    
    flag = 0
    
    for i in range(1, n + 1):
        if n == i**2:
            flag = i
            break
    
    if flag == 0:
        answer = -1
    else:
        answer = (flag + 1) ** 2

    return answer

answer = solution(n)
print(answer)