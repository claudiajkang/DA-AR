from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

n = int(read())
m = int(read())

g = [[] for i in range(n + 1)]
con = [0] * (n + 1)

for i in range(m):
    a, b, c = map(int, read().split())
    g[b].append([a, c])
    con[a] += 1

res = [[0] * (n + 1) for i in range(n + 1)]
q = deque()
must = deque()

for i in range(1, n + 1):
    if con[i] == 0:
        res[i][i] = 1
        q.append(i)
        must.append(i)

while q:
    cur = q.popleft()

    for nxt, d in g[cur]:
        con[nxt] -= 1

        for j in must:
            res[nxt][j] += res[cur][j] * d

        if con[nxt] == 0:
            q.append(nxt)

for i in must:
    print(f"{i} {res[n][i]}")
