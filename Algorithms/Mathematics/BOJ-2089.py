import sys
from math import ceil

N = int(sys.stdin.readline())
if not N:
    sys.stdout.write('0')
    exit()
res = ''

while N:
    R = int(N % (-2))
    N = ceil(N / (-2))
    res = str(abs(R)) + res
sys.stdout.write(res)
