from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

n = int(read())
m = int(read())
base = [[] for i in range(n + 1)]
con = [0] * (n + 1)

for i in range(m):
    a, b, c = map(int, read().split())
    base[b].append([a, c])
    con[a] += 1

res = [[0] * n for i in range(n + 1)]

must = []
q = deque()
for i in range(1, n + 1):
    if con[i] == 0:
        res[i][i] = 1
        must.append(i)
        q.append(i)

while q:
    cur = q.popleft()

    for mid, count in base[cur]:
        con[mid] -= 1

        for i in must:
            res[mid][i] += res[cur][i] * count

        if con[mid] == 0:
            q.append(mid)

must.sort()
for i in must:
    print(f"{i} {res[n][i]}")