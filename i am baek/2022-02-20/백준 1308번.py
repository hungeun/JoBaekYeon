import sys
import datetime

a, b, c = map(int, sys.stdin.readline().split())
oneday = datetime.date(a, b, c)

a, b, c = map(int, sys.stdin.readline().split())
twoday = datetime.date(a, b, c)

dday = twoday-oneday

if dday.days >= 365243:
    print('gg')
else:
    print('D-' + str(dday.days))