from sys import stdin

N, B = stdin.readline().split()
N = int(N)
B = int(B)
ALPA = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

res = []
TN = N

while TN != 0:
    Q = int(TN/B)
    R = int(TN%B)
    TN = Q
    res.append(ALPA[R])

print(''.join(reversed(res)))
