#for _ in 리스트 : 리스트 목록의 인덱스0 부터 마지막 인덱스까지 값을 하나씩 가져다 처리
# a = ['사자', '코끼리', '하마', '기린', '얼룩말'] =>0 1 2 3 4 
#   for animal in a:
#       print(animal)

#for 반복문으로 처리된 결과를 리스트에 담기도함
# multiple7 = []
# for n in range(1,101):
#   if n % 7 == 0:
#       multiple7.append(n) => 리스트에 값을 추가
#print(multiple7) => [7,14,21,28,35,42,49,56,63,70,77,84,91,98]

a = ['a','b','c','d','e','f']
for i in a:
    print(i)

b = []
for n in range(1,11):
    if n % 2 == 0:
        b.append(n)
print(b)