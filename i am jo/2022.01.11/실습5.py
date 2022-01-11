#dict_a = {'v1':32,
#           'l1;:[1,2,3],
#           'd1':{'a':1,'b':2}} //가급적 문자로만 {'key' : value} 형태로 선언
dict_a = {'v1' : 32, 'l1' : [1,2,3], 'd1':{'a':1,'b':2}}
print(dict_a['v1'])
print('=' *30)
print(dict_a['l1'])
print(dict_a['l1'][:2]) #리스트 l1안에서, 처음부터 2번 인덱스 전까지 조회
print('=' * 30)
print(dict_a['d1'])
print(dict_a['d1']['a'])

#.keys() : 딕셔너리의 key만 조회하기 / .values() : 딕셔너리의 값만 조회하기 / .items() : key와 값을 쌍(tuple)으로 조회 / tuple: 리스트와 유사

dict_a = {'v1' : 32, 'l1' : [1,2,3], 'd1':{'a':1,'b':2}}
print(dict_a['l1'])
print(dict_a['d1'])
print(dict_a['d1']['b'])
print(dict_a.keys())
print(dict_a.values())
print(dict_a.items())

#여러개의 값을 한번에 할당하기
animals = ['사자', '코끼리', '하마']
a1, a2, a3 = animals
print(a1,a2,a3)

#딕셔너리의 각 값을 개별 변수로 할당하기
dict_a = {'v1' : 32, 'l1' : [1,2,3], 'd1':{'a':1,'b':2}}
i1,i2,i3 = dict_a.items() #key,value 가져옴
print(i2)
print(i3)
print(i2[0]) #key와 value 를 가져왔는데 0번이 l1이여서
print(i3[1])

#딕셔너리 수정=> 추가 : 딕셔너리['새 키'] = 새 값 / 수정 : 딕셔너리['키'] = 새 값 / 삭제 : del 딕셔너리['키']
dict_a = {'v1' : 32, 'l1' : [1,2,3], 'd1':{'a':1,'b':2}}
dict_a['v2'] = 10000000
print(dict_a)
dict_a['v2'] = 0
print(dict_a)
del dict_a['v2']
print(dict_a)

#.get() : .get('key', 0) : 'key'가 있으면 값을 불러오고, 없으면 0을 가져오기
dict_a = {'v1' : 32, 'l1' : [1,2,3], 'd1':{'a':1,'b':2}}
print(dict_a.get('v1'))
print(dict_a.get('v2',0))

#변수 두개 사용
dict_a = {'v1' : 32, 'l1' : [1,2,3], 'd1':{'a':1,'b':2}}
for key, value in dict_a.items():
    print('key: ' , key)
    print('value: ', value)
    print('#' * 40)
#연습 
dict_a = {'v1' : [1,2,3], 'v2' : [0.5,0.1,0.3], 'v3' : [21,73,35]}
print(dict_a)
for key, value in dict_a.items():
    print('key는 ',  key, '입니다!!')
    print('value는 ', value, '입니다!!')