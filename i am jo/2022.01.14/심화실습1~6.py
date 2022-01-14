"""Q0 (https://www.acmicpc.net/problem/2108)
수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.
산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값 (여기서는 제외하자.)
범위 : N개의 수들 중 최댓값과 최솟값의 차이
N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

입력
-첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 단, N은 홀수이다. 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.
출력
-첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
-둘째 줄에는 중앙값을 출력한다.
-셋째 줄에는 범위를 출력한다.
"""
n = int(input())
data = []
for i in range(n):
    data.append(int(input()))

data.sort()
print(int(round(sum(data)/n,0)))
print(data[n//2])
print(data[n-1] - data[0])

# Q0 Answer with 최빈값 (시간초과)
n = int(input())
data = []
for i in range(n):
    data.append(int(input()))

data.sort()
print(int(round(sum(data)/n,0)))
print(data[n//2])

counts = []
flag = []
for i in data:
    if i not in flag:
        flag.append(i)
        counts.append([i, data.count(i)])

answer = sorted(counts, key=lambda x: x[1], reverse=True)

# sorted(list, key=criteria)
# lambda 매개변수 : 표현식

answers = [ x for x in answer if x[1] == answer[0][1]]   

if len(answers) >= 2: 
    print(answers[1][0])
else:
    print(answers[0][0])
    
print(data[n-1] - data[0])

"""Q1
피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다.
예를들어
F(2) = F(0) + F(1) = 0 + 1 = 1
F(3) = F(1) + F(2) = 1 + 1 = 2
F(4) = F(2) + F(3) = 1 + 2 = 3
F(5) = F(3) + F(4) = 2 + 3 = 5
와 같이 이어집니다.

2 이상의 n이 입력되었을 때, n번째 피보나치 수를 리턴하는 함수, solution을 완성해 주세요.

제한 사항-n은 2 이상 100 이하인 자연수입니다.
입출력 예
                                n	        return
                                3	           2
                                5	           5
"""
# recursive - but it is slow
def solution(n):
    if n == 0:
        answer = 0
    elif n == 1:
        answer = 1
    else:
        answer = solution(n-1) + solution(n-2)
    return answer

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

def fib(n):
    answer = [0, 1]
    while n > 1:
        answer.append(answer[-1] + answer[-2])
        n -= 1
    return answer[-1]

n = 5
answer = fibonacci(n)
print(answer)

"""Q2 (https://programmers.co.kr/learn/courses/30/lessons/68644)
정수 리스트 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 리스트에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.
제한사항
-numbers의 길이는 2 이상 100 이하입니다.
-numbers의 모든 수는 0 이상 100 이하입니다.
-결과값에 중복되는 값은 한번만 포함되어야 합니다.

입출력 예
numbers	            result
[2,1,3,4,1]	     [2,3,4,5,6,7]
[5,0,2,7]	      [2,5,7,9,12]
"""
def bubble_sort(a):
    n = len(a)
    for i in range(n-1):
        for j in range(n-1,i,-1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]

def solution(numbers):
    answer = []
    
    for i in range(len(numbers),0,-1):
        j = i
        while j > 1:
            sums = numbers[i-1] + numbers[i-j]
            if sums not in answer:
                answer.append(sums)
            j -= 1
        
    
    #bubble_sort(answer)
    #return answer

    return sorted(answer)
    

numbers = [2,1,3,4,1]
#numbers = [5,0,2,7]
answer = solution(numbers)
print(answer)

"""Q3
리스트의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 리스트를 반환하는 함수, solution을 작성해주세요. divisor로 나누어 떨어지는 element가 하나도 없다면 리스트에 -1을 담아 반환하세요.
제한사항
-arr은 자연수를 담은 리스트입니다.
-정수 i, j에 대해 i ≠ j 이면 arr[i] ≠ arr[j] 입니다.
-divisor는 자연수입니다.
-array는 길이 1 이상인 리스트입니다.

입출력 예
arr	                    divisor	            return
[5, 9, 7, 10]	           5	            [5, 10]
[2, 36, 1, 3]	           1	           [1, 2, 3, 36]
[3,2,6]	                   10	              [-1]
"""
def solution(arr, divisor):
    answer = []
    for i in arr:
        if i%divisor == 0:
            answer.append(i)
    
    if len(answer) == 0:
        answer.append(-1)
    
    return sorted(answer)

#arr = [5,9,7,10]
#arr = [2,36,1,3]
arr = [3,2,6]
divisor = 10
answer = solution(arr, divisor)
print(answer)

# Q3 answer (short)

def solution(arr, divisor):
    arr = [x for x in arr if x % divisor == 0]
    arr.sort()
    return arr if len(arr) != 0 else [-1]

arr = [5,9,7,10]
divisor = 5
answer = solution(arr, divisor)
print(answer)

"""Q4
동일한 갯수의 원소로 구성된 두 개의 리스트 a와 b를 입력 받는다. 리스트의 원소는 모두 자연수이다. k 를 입력받아 k의 값만큼 리스트 a에 있는 원소 하나와 리스트 b에 있는 원소 하나를 골라서 두 원소를 서로 바꾸어라. 다만, 원소 교환의 목표는 교환 후 리스트 a의 모든 원소의 합이 최대가 되도록 하는 것이다.
k, 리스트 a와 b가 주어졌을 때, 최대 k번의 바꿔치기 연산을 수행하여 만들 수 있는 리스트 a의 모든 원소의 합의 최댓값을 출력하는 프로그램을 작성하시오.

입출력 예
k	                a	                b	            answer
3	            [1,2,5,4,3]	        [5,5,6,6,5]	          26
"""
def solution(k, a, b):
    
    a.sort()   # 리스트 a 오름차순 정렬
    b.sort(reverse=True) # 리스트 b 내림차순 정렬
    
    for i in range(k):
        if a[i] < b[i]:
            a[i], b[i] = b[i], a[i]
        else:
            break
    
    return sum(a)

k = 3
a = [1,2,5,4,3]
b = [5,5,6,6,5]
answer = solution(k, a, b)
print(answer)

"""Q5 (https://www.acmicpc.net/problem/18310)
일직선 상의 마을에 여러 채의 집이 위치해 있다. 이중에서 특정 위치의 집에 특별히 한 개의 안테나를 설치하기로 결정했다. 효율성을 위해 안테나로부터 모든 집까지의 거리의 총 합이 최소가 되도록 설치하려고 한다. 이 때 안테나는 집이 위치한 곳에만 설치할 수 있고, 논리적으로 동일한 위치에 여러 개의 집이 존재하는 것이 가능하다.
집들의 위치 값이 주어질 때, 안테나를 설치할 위치를 선택하는 프로그램을 작성하시오.
예를 들어 N=4이고, 각 위치가 1, 5, 7, 9일 때를 가정하자.

이 경우 5의 위치에 설치했을 때, 안테나로부터 모든 집까지의 거리의 총 합이 (4+0+2+4)=10으로, 최소가 된다.
입력
-집의 수 N의 범위는 1≤N≤200,000이며, N채의 집에 위치가 공백을 기준으로 구분되어 1이상 100,000이하의 자연수로 주어진다.
출력
-첫째 줄에 안테나를 설치할 위치의 값을 출력한다. 단, 안테나를 설치할 수 있는 위치 값으로 여러 개의 값이 도출될 경우 가장 작은 값을 출력한다.
입출력 예
입력	        출력
[1,5,7,9]	     5
"""
# Q5 Answer

def solution(numbers):
    
    n = len(numbers)
    numbers.sort()
    
    return numbers[(n-1)//2]

#numbers = [1, 5, 7, 9]
numbers = [1, 5, 100, 200, 202, 203]
answer = solution(numbers)
print(answer)

def seq_search(a, key):
    i = 0
    
    while True:
        if i == len(a):
            return -1
        if a[i] == key:
            return i
        i += 1

def solution(numbers):
    
    n = len(numbers)
    
    numbers.sort()
    
    distance = [None]*n
    
    for i in range(n):
        
        distance[i] = 0
        
        if i == 0:
            for j in range(i+1, n):
                distance[i] = distance[i] + abs(numbers[i]-numbers[j])
        else:
            for j in range(i-1, -1, -1):
                distance[i] = distance[i] + abs(numbers[i]-numbers[j])
            for j in range(i+1, n):
                distance[i] = distance[i] + abs(numbers[i]-numbers[j])
    
    #print(numbers)
    #print(distance)
    dist = distance.copy()
    dist.sort()
    index = seq_search(distance, dist[0])
    
    return numbers[index]

#numbers = [5, 1, 9, 7]
numbers = [202, 5, 1, 200, 100, 203]
answer = solution(numbers)
print(answer)

"""Q6 (https://programmers.co.kr/learn/courses/30/lessons/42889)
슈퍼 게임 개발자 오렐리는 큰 고민에 빠졌다. 그녀가 만든 프랜즈 오천성이 대성공을 거뒀지만, 요즘 신규 사용자의 수가 급감한 것이다. 원인은 신규 사용자와 기존 사용자 사이에 스테이지 차이가 너무 큰 것이 문제였다.

이 문제를 어떻게 할까 고민 한 그녀는 동적으로 게임 시간을 늘려서 난이도를 조절하기로 했다. 역시 슈퍼 개발자라 대부분의 로직은 쉽게 구현했지만, 실패율을 구하는 부분에서 위기에 빠지고 말았다. 오렐리를 위해 실패율을 구하는 코드를 완성하라.

실패율은 다음과 같이 정의한다.
-스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때, 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하라.

제한사항
-스테이지의 개수 N은 1 이상 500 이하의 자연수이다.
-stages의 길이는 1 이상 200,000 이하이다.
-stages에는 1 이상 N + 1 이하의 자연수가 담겨있다.
-각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타낸다.
-단, N + 1 은 마지막 스테이지(N 번째 스테이지) 까지 클리어 한 사용자를 나타낸다.
-만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.
-스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.

입출력 예
N	                stages              	   result
5	        [2, 1, 2, 6, 2, 4, 3, 3]	    [3,4,2,1,5]
4	               [4,4,4,4,4]	             [4,1,2,3]

입출력 예 설명

입출력 예 #1
-1번 스테이지에는 총 8명의 사용자가 도전했으며, 이 중 1명의 사용자가 아직 클리어하지 못했다. 따라서 1번 스테이지의 실패율은 다음과 같다.
-1 번 스테이지 실패율 : 1/8
-2번 스테이지에는 총 7명의 사용자가 도전했으며, 이 중 3명의 사용자가 아직 클리어하지 못했다. 따라서 2번 스테이지의 실패율은 다음과 같다.
-2 번 스테이지 실패율 : 3/7
-마찬가지로 나머지 스테이지의 실패율은 다음과 같다.
-3 번 스테이지 실패율 : 2/4
-4번 스테이지 실패율 : 1/2
-5번 스테이지 실패율 : 0/1
-각 스테이지의 번호를 실패율의 내림차순으로 정렬하면 다음과 같다.
-[3,4,2,1,5]

입출력 예 #2
-모든 사용자가 마지막 스테이지에 있으므로 4번 스테이지의 실패율은 1이며 나머지 스테이지의 실패율은 0이다.
-[4,1,2,3]
"""
# Q6 Answer 

def solution(N, stages):
    
    total = len(stages)
    answer = []
    
    for i in range(1, N+1):
        count = 0
        for j in stages:
            if j == i:
                count += 1
        
        if total == 0:
            fail = 0
        else:
            fail = count / total
    
        total = total - count
        answer.append((i, fail))
    
    answer = sorted(answer, key=lambda x: x[1], reverse=True)
    
    # sorted(list, key=criteria)
    # lambda 매개변수 : 표현식
    
    answer = [i[0] for i in answer]
    
    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
answer = solution(N, stages)
print(answer)