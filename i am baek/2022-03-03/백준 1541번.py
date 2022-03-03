susick = input().split('-')

sum = 0

temp = susick[0].split('+')
for j in temp:
    sum += int(j)

susick = susick[1:]

for i in susick:
    temp = i.split('+')
    for j in temp:
        sum -= int(j)
        
print(sum)

#20-40+50-40
#20 40+50 40