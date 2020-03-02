from sys import stdin
from collections import deque

read = lambda : stdin.readline().strip()

N = int(read())
G = [[] for i in range(N+1)]
P = ['-1'] * (N+1)

for i in range(1, N):
    A, B = map(int, read().split())
    G[A].append(B)
    G[B].append(A)

for i in range(1, N+1):
    if P[i] == '-1':
        q = deque()
        q.append(i)

        while len(q):
            cur = q.popleft()

            for j in G[cur]:
                if P[j] == '-1':
                    P[j] = str(cur)
                    q.append(j)

print('\n'.join(P[2:]))