from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

n = int(read())
m = int(read())

res = [[0] * (n + 1) for i in range(n + 1)]
con = [0] * (n + 1)
adj = [[] for i in range(n + 1)]

for i in range(m):
    x, y, k = map(int, read().split())
    con[x] += 1
    adj[y].append([x, k])

q = deque()
essential = deque()
for i in range(1, n + 1):
    if con[i] == 0:
        q.append(i)
        essential.append(i)
        res[i][i] = 1

while q:
    base = q.popleft()

    for j in adj[base]:
        mid = j[0]
        count = j[1]

        for i in essential:
            res[mid][i] += res[base][i] * count

        con[mid] -= 1

        if con[mid] == 0:
            q.append(mid)

for i in essential:
    print(f"{i} {res[n][i]}")
