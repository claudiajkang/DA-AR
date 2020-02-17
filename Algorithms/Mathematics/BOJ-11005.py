from sys import stdin
  
N, B = map(int, stdin.readline().split())
alpa = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
bn = {}
res = []

for i in range(B):
    bn[i] = alpa[i]

while N != 0:
    R = int(N % B)
    N = int(N / B)
    res.append(alpa[R])

print(''.join(reversed(res)))
