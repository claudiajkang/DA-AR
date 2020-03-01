from sys import stdin
from collections import deque

N = int(stdin.readline())
G = [[] for i in range(N+1)]
res = ['0' for _ in range(N+1)]
q = deque()
bfs = []

for i in range(1, N):
    A, B = list(map(int, stdin.readline().split()))
    G[A].append(B)
    G[B].append(A)

q.append(1)

while len(q):
    cur = q.popleft()
    for i in G[cur]:
        if res[i] == '0':
            res[i] = str(cur)
            q.append(i)

print('\n'.join(res[2:]))
