"""Q0 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
입력
첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)
둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.
출력
X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다. X보다 작은 수는 적어도 하나 존재한다.
예제 입력 1
10 5
1 10 4 9 2 3 8 5 7 6
예제 출력 1
1 4 2 3"""
N, X = map(int, input().split())
data = list(map(int, input().split()))
answer = []

for i in data:
    if i < X:
        answer.append(i)

for i in answer:
    print(i, end=' ')

"""Q1 (https://programmers.co.kr/learn/courses/30/lessons/77484)
로또 6/45(이하 '로또'로 표기)는 1부터 45까지의 숫자 중 6개를 찍어서 맞히는 대표적인 복권입니다. 아래는 로또의 순위를 정하는 방식입니다.
순위	당첨 내용
1	6개 번호가 모두 일치
2	5개 번호가 일치
3	4개 번호가 일치
4	3개 번호가 일치
5	2개 번호가 일치
6	(낙첨) 그 외
로또를 구매한 민우는 당첨 번호 발표일을 학수고대하고 있었습니다. 하지만, 민우의 동생이 로또에 낙서를 하여, 일부 번호를 알아볼 수 없게 되었습니다. 당첨 번호 발표 후, 민우는 자신이 구매했던 로또로 당첨이 가능했던 최고 순위와 최저 순위를 알아보고 싶어 졌습니다. 알아볼 수 없는 번호를 0으로 표기하기로 하고, 민우가 구매한 로또 번호 6개가 44, 1, 0, 0, 31 25라고 가정해보겠습니다. 당첨 번호 6개가 31, 10, 45, 1, 6, 19라면, 당첨 가능한 최고 순위와 최저 순위의 한 예는 아래와 같습니다.
당첨 번호	31 10 45 1 6 19	결과
최고 순위 번호	31 0→10 44 1 0→6 25	4개 번호 일치, 3등
최저 순위 번호	31 0→11 44 1 0→7 25	2개 번호 일치, 5등
순서와 상관없이, 구매한 로또에 당첨 번호와 일치하는 번호가 있으면 맞힌 걸로 인정됩니다.
알아볼 수 없는 두 개의 번호를 각각 10, 6이라고 가정하면 3등에 당첨될 수 있습니다.
3등을 만드는 다른 방법들도 존재합니다. 하지만, 2등 이상으로 만드는 것은 불가능합니다.
알아볼 수 없는 두 개의 번호를 각각 11, 7이라고 가정하면 5등에 당첨될 수 있습니다.
5등을 만드는 다른 방법들도 존재합니다. 하지만, 6등(낙첨)으로 만드는 것은 불가능합니다.
민우가 구매한 로또 번호를 담은 배열 lottos, 당첨 번호를 담은 배열 win_nums가 매개변수로 주어집니다. 이때, 당첨 가능한 최고 순위와 최저 순위를 차례대로 배열에 담아서 return 하도록 solution 함수를 완성해주세요.
제한사항
lottos는 길이 6인 정수 배열입니다.
lottos의 모든 원소는 0 이상 45 이하인 정수입니다.
0은 알아볼 수 없는 숫자를 의미합니다.
0을 제외한 다른 숫자들은 lottos에 2개 이상 담겨있지 않습니다.
lottos의 원소들은 정렬되어 있지 않을 수도 있습니다.
win_nums은 길이 6인 정수 배열입니다.
win_nums의 모든 원소는 1 이상 45 이하인 정수입니다.
win_nums에는 같은 숫자가 2개 이상 담겨있지 않습니다.
win_nums의 원소들은 정렬되어 있지 않을 수도 있습니다."""
def solution(lottos, win_nums):
    count = 0
    zeros = 0
    rank = [6, 6, 5, 4, 3, 2, 1]
    
    #for i in range(len(lottos)):
    #    if lottos[i] == 0:
    #        zeros += 1
    zeros = lottos.count(0)
    
    #for i in range(len(lottos)):
    #    for j in range(len(win_nums)):
    #        if win_nums[j] == lottos[i]:
    #            count += 1
    for i in lottos:
        if i in win_nums:
            count += 1
    
    answer = rank[count + zeros], rank[count]
    return answer


lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
#lottos = [0, 0, 0, 0, 0, 0]
#win_nums = [38, 19, 20, 40, 15, 25]
#lottos = [45, 4, 35, 20, 3, 9]
#win_nums = [20, 9, 3, 45, 4, 35]

answer = solution(lottos, win_nums)
print(answer)

"""Q2 (https://programmers.co.kr/learn/courses/30/lessons/86051)
0부터 9까지의 숫자 중 일부가 들어있는 배열 numbers가 매개변수로 주어집니다. numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요.
제한사항
1 ≤ numbers의 길이 ≤ 9
0 ≤ numbers의 모든 수 ≤ 9
numbers의 모든 수는 서로 다릅니다"""

def solution(numbers):
    sums = 0

    for i in range(10):       
        if i not in numbers:
            sums = sums + i
            
    return sums

#numbers = [1,2,3,4,6,7,8,0]
#numbers = [5,8,4,0,6,7,9]
#numbers = [1,2,3]
numbers = [0]
answer = solution(numbers)
print(answer)

#2번째
def solution(numbers):
    return 45 - sum(numbers)

"""Q3 (programmers)
컴퓨터 매장에는 n개의 부품이 있으며, 부품마다 정수 형태의 고유한 번호가 있다. 어느 날 손님이 m개 종류의 부품을 대량으로 구매하겠다며 부품이 재고유무를 문의하였다. 매장에 부품 재고가 있는지 확인하는 프로그램을 작성하라.
매장이 가지고 있는 부품 리스트와 고객이 확인하고자 하는 부품 리스트를 입력받는다. 고객이 요청한 부품 번호의 순서대로 부품을 확인해 부품이 있으면 yes, 없으면 no를 출력한다.
제한사항
부품 재고의 갯수는 고려하지 않으며 부품이 있는지 여부만 체크한다
부품 리스트 길이(n, m)는 1이상, 15이하입니다.
매장 보유 부품 번호는 오름차순으로 정렬된 형태로 입력한다.
부품 리스트의 원소는 100 이하인 자연수입니다."""

def bin_search(a, key):
    pl = 0
    pr = len(a)-1
    
    while True:
        pc = (pl + pr) // 2
        if a[pc] == key:
            return pc
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1
        
        if pl > pr:
            break
    
    return -1

def solution(store, customer):
    
    answer = []
    
    for i in customer:
        result = bin_search(store,i)
        if result != -1:
            answer.append('yes')
        else:
            answer.append('no')
            
    return answer

store = [2,3,7,8,9]
customer = [7,5,9]
answer = solution(store, customer)
print(answer)

"""Q4
두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다. 예를 들어 2와 7의 최소공배수는 14가 됩니다. 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다. n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.
제한 사항
arr은 길이 1이상, 15이하인 리스트입니다.
arr의 원소는 100 이하인 자연수입니다."""

def solution(arr):
    
    maximum = 0
    for i in range(len(arr)):
        if arr[i] > maximum:
            maximum = arr[i]
    
    mul = 1
    for i in range(len(arr)):
        mul = mul * arr[i]
            
    for i in range(maximum,mul+1):
        flag = 0
        for j in range(len(arr)):
            if i%arr[j] == 0:
                flag += 1
        
        if flag == len(arr):
            answer = i
            break
    
    return answer

arr = [2,6,8,14]
#arr = [1,2,3]
#arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#arr = [9, 10]
answer = solution(arr)
print(answer)

"""Q5
자연수 2 개로 이루어진 중복 집합(multi set, 편의상 이후에는 "집합"으로 통칭) 중에 다음 두 조건을 만족하는 집합을 최고의 집합이라고 합니다.
각 원소의 합이 S가 되는 수의 집합
위 조건을 만족하면서 각 원소의 곱 이 최대가 되는 집합
예를 들어서 자연수 2개로 이루어진 집합 중 합이 9가 되는 집합은 다음과 같이 4개가 있습니다.
{ 1, 8 }, { 2, 7 }, { 3, 6 }, { 4, 5 }
그중 각 원소의 곱이 최대인 { 4, 5 }가 최고의 집합입니다.
집합의 원소의 개수 n(=2)과 모든 원소들의 합 s가 매개변수로 주어질 때, 최고의 집합을 return 하는 solution 함수를 완성해주세요.
제한사항
최고의 집합은 오름차순으로 정렬된 1차원 배열(list, vector) 로 return 해주세요.
만약 최고의 집합이 존재하지 않는 경우에 크기가 1인 1차원 배열(list, vector) 에 -1 을 채워서 return 해주세요.
자연수의 개수 n은 2 입니다.
모든 원소들의 합 s는 1 이상, 100,000,000 이하의 자연수입니다."""

def solution(n, s):
    
    list_one = []
    list_all = []
    sum_one = 0
    mul = []
    
    for i in range(1,(s//n)+1):
        list_one.append(i)
        list_one.append(s-i)
            
        list_all.append(list_one)
        list_one = []
    
    for j in range(len(list_all)):
            mul.append(list_all[j][0]*list_all[j][1])
    
    if len(mul) > 0:
        maximum = mul[0]
        
        flag = 0
        for i in range(1,len(mul)):
            if mul[i] > maximum:
                maximum = mul[i]
                flag = i
    
        answer = list_all[flag]
    else:
        answer = [-1]
        
    return answer

n = 2
s = 100000
answer = solution(n, s)
print(answer)

"""Q6 (https://programmers.co.kr/learn/courses/30/lessons/12935)
정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요. 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요. 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.
제한 조건
arr은 길이 1 이상인 배열입니다.
인덱스 i, j에 대해 i ≠ j이면 arr[i] ≠ arr[j] 입니다.
입출력 예
arr	        return
[4,3,2,1]	[4,3,2]
[10]	    [-1]
리스트에서 원소 제거 함수
a.pop(0) : 0번 인덱스의 원소가 제거됨
a.remove(10) : 10 값을 가진 원소가 제거됨, 10이라는 값이 여러개라면 맨 처음에 있는 것만 제거됨"""

def solution(arr):
        
    minimum = arr[0]
    index = 0
        
    for i in range(1, len(arr)):
        if arr[i] < minimum:
            minimum = arr[i]
            index = i
    
    arr.pop(index)
    
    return [-1] if len(arr) == 0 else arr

#arr = [4, 3, 2, 1]
arr = [10]
answer = solution(arr)
print(answer)

"""Q7 (https://programmers.co.kr/learn/courses/30/lessons/12906)
배열 arr가 주어집니다. 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다. 이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다. 단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다. 예를 들면,
arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.
arr = [4, 4, 4, 3, 3] 이면 [4, 3] 을 return 합니다.
배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성해 주세요.
제한사항
배열 arr의 크기 : 1,000,000 이하의 자연수
배열 arr의 원소의 크기 : 0보다 크거나 같고 9보다 작거나 같은 정수
입출력 예
arr	                   answer
[1,1,3,3,0,1,1] 	[1,3,0,1]
[4,4,4,3,3]	        [4,3]
"""

def solution(arr):
    answer = []
    
    prev = arr[0]
    answer.append(prev)
    
    for i in range(1,len(arr)):
        if arr[i] != prev:
            prev = arr[i]
            answer.append(prev)
    
    return answer

arr = [1,1,3,3,0,1,1]
#arr = [4,4,4,3,3]
answer = solution(arr)
print(answer)