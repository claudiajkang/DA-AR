import sys

N = int(sys.stdin.readline())

for i in range(N):
    for j in range(i+1):
        print('*', end ='')
    for k in range(2*(N-i-1)):
        print(' ', end ='')
    for j in range(i+1):
        print('*', end ='')
    print('')

for i in range(N-1, 0, -1):
    for j in range(i):
        print('*', end ='')
    for k in range((N-i)*2):
        print(' ', end ='')
    for l in range(i):
        print('*', end ='')
    print('')

