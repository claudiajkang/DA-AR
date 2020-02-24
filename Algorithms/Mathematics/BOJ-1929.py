import sys

M, N = map(int, sys.stdin.readline().split())
PN = [i for i in range(N+1)]
mpow = 0

for j in range(N+1, -1, -1):
    idx = pow(j, 2)
    if idx <= N:
        mpow = idx
        break

for i in range(2, mpow+1):
    if PN[i]:
        v = N // i
        for j in range(2, v+1):
            PN[i*j] = 0

PN = sorted(PN)
idx = PN.index(2)
PN = PN[idx:]

for i in PN:
    if M <= i <= N:
        print(i)
    elif i > N:
        break
