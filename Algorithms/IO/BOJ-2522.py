import sys

N = int(sys.stdin.readline())

for i in range(N):
    for j in range(N-i-1):
        print(' ', end ='')
    for k in range(i+1):
        print('*', end ='')
    print('')

for i in range(N-1):
    for j in range(i+1):
        print(' ', end ='')
    for k in range(N-i-1):
        print('*', end ='')
    print('')
