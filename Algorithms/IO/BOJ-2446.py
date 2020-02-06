import sys

N = int(sys.stdin.readline())

for i in range(N):
    for j in range(i):
        print(' ', end ='')
    for k in range(N-i):
        print('*', end ='')
    for k in range(N-i-1):
        print('*', end = '')
    print('')

for i in range(N-1, 0, -1):
    for j in range(i-1):
        print(' ', end ='')
    for k in range(N-i+1):
        print('*', end ='')
    for k in range(N-i):
        print('*', end ='')
    print('')
