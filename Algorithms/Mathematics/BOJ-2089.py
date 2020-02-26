from sys import stdin
from math import ceil

N = int(stdin.readline())
res = []

if not N:
    print(0)

else:
    while N:
        R = abs(N % (-2))
        N = ceil(N / (-2))
        res.insert(0, str(R))

    print(''.join(res))
