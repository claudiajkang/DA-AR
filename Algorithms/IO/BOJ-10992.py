import sys
  
N = int(sys.stdin.readline())

for i in range(N):
    for j in range(N-i-1):
        print(' ', end = '')

    print('*', end ='')
    if i != (N-1):
        c = (i-1)*2 + 1
        for j in range(c):
            print(' ', end = '')
            if j == (c-1):
                print('*', end ='')

    else:
        for i in range(i+N-1):
            print('*', end ='')
    print('')
