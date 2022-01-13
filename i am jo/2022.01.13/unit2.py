#Unit 2. 검색 알고리즘
#선형 검색

i = 0
while True:
    if i == len(a):
        # 검색실패
        if a[i] == key:
        # 검색 성고(찾은 원소의 인덱스 i)
    
                i += 1

#While 문 선형검색
def seq_search(a, key):
    i = 0
    
    while True:
        if i == len(a):
            return -1
        if a[i] == key:
            return i
        i += 1
        a = [2, 5, 1, 3, 9, 6, 7]

index = seq_search(a, 3)

if index == -1:
    print('검색값을 갖는 원소가 존재하지 않습니다.')
else:
    print(f'검색값은 a[{index}]에 있습니다.')
    
#for 문 선형검색
def seq_search_for(a, key):
    
    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1
a = [2, 5, 1, 3, 9, 6, 7]

index = seq_search_for(a, 4)

if index == -1:
    print('검색값을 갖는 원소가 존재하지 않습니다.')
else:
    print(f'검색값은 a[{index}]에 있습니다.')
    
#보초법 (While 문)
def seq_search_sentinel(b, key):
    a = b.copy()
    a.append(key)
    
    i=0
    while True:
        if a[i] == key:
            break
        i += 1
    
    return -1 if i == len(b) else i
a = [2, 5, 1, 3, 9, 6, 7]

index = seq_search_sentinel(a, 7)

if index == -1:
    print('검색값을 갖는 원소가 존재하지 않습니다.')
else:
    print(f'검색값은 a[{index}]에 있습니다.')
    
"""미니 실습 3)-Q) 아래 리스트에서 검색값을 찾으려고 한다.
선형 검색 While 문을 사용하는 경우와 보초법을 사용하는 경우에 각각 if 조건문이 몇 번 실행되지는 수를 세어 출력하라.
a = [2, 5, 1, 3, 9, 6, 7]
검색값: 7"""
def seq_search(a, key):
    i = 0
    counter = 0
    while True:
        counter += 1
        if i == len(a):
                return -1
        counter += 1
       
        if a[i] == key:
            return counter
        i += 1
       
        def seq_search_sentinel(b, key):
            a = b.copy()
            a.append(key)
    
    i=0
    counter = 0
    
    while True:
        counter += 1
        if a[i] == key:
            break
        i += 1
    
    return -1 if i == len(b) else counter
a = [2, 5, 1, 3, 9, 6, 7]

index0 = seq_search(a, 7)
index1 = seq_search_sentinel(a, 7)

if index0 == -1:
    print('검색값을 갖는 원소가 존재하지 않습니다.')
else:
    print(f'선형검색 While 문에서 if문은 {index0}만큼 실행되었습니다.')
    print(f'선형검색 보초법에서 if문은 {index1}만큼 실행되었습니다.')
    
#이진 검색
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
a = [5, 7, 15, 28, 29, 31, 39, 58, 68, 70, 95]

index = bin_search(a, 39)

if index == -1:
    print('검색값을 갖는 원소가 존재하지 않습니다.')
else:
    print(f'검색값은 a[{index}]에 있습니다.')