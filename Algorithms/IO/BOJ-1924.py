import sys

M, D = map(int, sys.stdin.readline().split())

dates = dict()
pr = {0: 'SUN', 1: 'MON', 2: 'TUE', 3: 'WED', 4: 'THU', 5: 'FRI', 6:'SAT'}

for i in range(1, 13):
    if i in [1,3,5,7,8,10,12]:
        dates[i] = 31

    elif i == 2:
        dates[i] = 28
    
    else:
        dates[i] = 30

td = 0

for i in range(1, M):
    td += dates[i]

td += D

v = td % 7

print(pr[v])
