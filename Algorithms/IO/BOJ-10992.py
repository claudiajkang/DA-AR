import sys

N = int(sys.stdin.readline())

for i in range(N):
    for j in range(N-i-1):
        print(' ', end ='')

    print('*', end = '')

    if i == (N-1):
        for k in range(2*i):
            print('*', end ='')

    else:
        for j in range(i):
            print(' ', end ='')

        for j in range(i-1):
            print(' ', end = '')

        if i:
            print('*', end ='')

    print('')
