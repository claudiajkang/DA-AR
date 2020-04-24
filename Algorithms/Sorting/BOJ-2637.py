from heapq import heappush, heappop
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

q = []
res = [[0] * (n + 1) for i in range(n + 1)]
must = []

for i in range(1, n + 1):
    if con[i] == 0:
        res[i][i] = 1
        heappush(q, i)
        must.append(i)

while q:
    cur = heappop(q)

    for j, d in g[cur]:
        con[j] -= 1

        for i in must:
            res[j][i] += res[cur][i] * d

        if con[j] == 0:
            heappush(q, j)

for i in must:
    print(f"{i} {res[n][i]}")
