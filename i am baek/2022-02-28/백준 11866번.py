''' 요세푸스 순열 - 참고 : https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=attractorlim&logNo=221030930874
1. 3의 배수가 되는 순서의 사람을 죽인다.
2. 남은 사람 중 제일 낮은 순서의 사람 부터 3의 배수가 되는 순서의 사람을 죽인다.
'''

# 1 2 3 4 5 6 7 
# 1 2 4 5 7 - kill : 3, 6
# 1 4 5 - kill : 2, 7
# 1 4 - kill : 5
# kill : 1, 4
num, kill = map(int, input().split())

que = []

for i in range(1, num + 1):
    que.append(i)

killer = []
cnt = 0

# 1 2 3 4 5 6 7 
# 1 2 4 5 6 7 / 2
# 1 2 4 5 7 / 4
# 1 4 5 7 / 1

while que:
    cnt = (cnt + kill - 1) % len(que)
    killer.append(que.pop(cnt))

print('<', end = '')
for i in range(len(killer) - 1):
    print(killer[i], end = ', ')
print(killer[-1], end = '')
print('>')
