import sys

N = int(sys.stdin.readline())

for i in range(N):
    for j in range(N-i-1):
        print(' ', end ='')
    for k in range(i+1):
        if k == i:
            print('*', end ='')

    if i == (N-1):
        for k in range(i):
            print('*', end ='')
        for k in range(N-1):
            print('*', end ='')

    else:
        m = 2*(i-1)+1
        for j in range(m):
            print(' ', end ='')
            if j == (m-1):
                print('*', end ='')

    print('')
