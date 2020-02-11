import sys

N = int(sys.stdin.readline())

for i in range(N):
    if i == 0:
        p = ' '*(N-i-1) + '*'

    elif i == (N-1):
        p = '*'*(2*N-1)

    else:
        p = ' '*(N-i-1) + '*' + ' '*(2*i -1) + '*'

    print(p)
