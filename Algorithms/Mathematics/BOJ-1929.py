from sys import stdin

M, N = map(int, stdin.readline().split())
MAXN = 0
NUM = [i for i in range(N+1)]

for j in range(N+1, -1, -1):
    idx = pow(j, 2)
    if idx <= N:
        MAXN = idx
        break

for i in range(2, MAXN+1):
    if NUM[i]:
        v = N // i
        for j in range(2, v+1):
            NUM[i*j] = 0

NUM = sorted(NUM)
idx = NUM.index(2)
NUM = NUM[idx:]

for i in NUM:
    if M <= i <= N:
        print(i)
    elif i > N: break

