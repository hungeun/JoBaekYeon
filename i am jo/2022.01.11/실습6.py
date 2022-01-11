#함수 만들기
def hello_world(name) :
    print('hello ' + name + ' , welcom to python world')
    
hello_world('han')

#여러개의 입력 매개변수
def hello(name, loud = 1): #loud는 defaul값으로 1 가짐
    if loud == 1:
        print('hello ' + name ) #2번쨰 print(f'hello {name}') 도 가능
    else:
        print('hi ' + name) 
hello(name = 'hun', loud = 4)

#숫자들을 여러 개 받아 모두 합한 값을 반환하는 함수
def summ( *nums ): #*로 처리된 매개변수는 보통 tuple형태로 받음
    total = 0
    
    for i in nums:
        total += i
    return(total)

print(summ(1,2,3,4,5))

#출력 값은 2가지 형태로 => print() : 화면에 출력 / return : 결과 값을 output으로 내보내고 함수 종료, 결과 값을 받아서 사용하기 위해서는 반드시 return 사용
def number1( *nums):
    print(nums)
number1(1,2,3)
a1 = number1(1,2,3)
print(a1)

def number2( *nums):
    return nums
print(number2(1,2,3))
a2 = number2(1,2,3)

#나누기 함수 - a,b int인지 확인
def divide(a,b):
    if (type(a) != int) or (type(b) != int):
        print('정수가 아닙니다.')
    elif b == 0: 
        print('0이 될수 없다')
    else:
        result = a / b
        return result
divide(10,0)