import sys

M, N = map(int, sys.stdin.readline().split())
mn = 0
PN = [i for i in range(N+1)]

for j in range(2, N):
    if pow(j, 2) > N:
        mn = j
        break

for i in range(2, mn+1):
    v = N // i
    for j in range(2, v+1):
        PN[i*j] = 0

PN = sorted(PN)
idx = PN.index(2)
res = PN[idx:]

for i in res:
    if M <= i <= N:
        print(i)
    elif i > N:
        break

