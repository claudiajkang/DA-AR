from sys import stdin

M, N = map(int, stdin.readline().split())
maxnum = 0
pn = [i for i in range(N + 1)]

for i in range(N):
    if pow(i, 2) > N:
        maxnum = i
        break

for i in range(2, maxnum):
    v = N // i
    for j in range(2, v + 1):
        pn[i * j] = 0

pn = sorted(pn)
idx = pn.index(2)
res = pn[idx:]

for i in res:
    if i < M:
        continue
    elif i <= N:
        print(i)
    elif i > N:
        break
