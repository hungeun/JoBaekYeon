import fractions

loop = int(input())

circle = list(map(int, input().split()))

big = 2 * circle[0]

for i in range(1, loop):
    a = fractions.Fraction(big, 2*circle[i])
    print(a.numerator, end = '')
    print('/', end = '')
    print(a.denominator)